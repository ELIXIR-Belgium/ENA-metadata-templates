from lxml import etree
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import time
import xlsxwriter
import os
import pandas as pd
import yaml
import re

def fetch_object(url):
    print('  GET ' + url)
    session = requests.Session()
    retry = Retry(connect=3, backoff_factor=15)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    r = session.get(url)
    # Covering internal server errors by retrying one more time
    if r.status_code == 500:
        time.sleep(5)
        r = requests.get(url, allow_redirects=True)
    elif r.status_code != 200:
        print(f"Problem with request: {str(r)}")
        raise RuntimeError("Non-200 status code")
    return r

def elem2dict(node):
    """
    Convert an lxml.etree node tree into a dict.
    """
    result = {}

    for element in node.iterchildren():
        # Remove namespace prefix
        if element.tag:
            key = element.tag.split('}')[1] if '}' in element.tag else element.tag
            if element.attrib and 'name' in element.attrib:
                key= element.attrib['name']
            # Process element as tree element if the inner XML contains non-whitespace content
            if element.attrib and 'value' in element.attrib:
                value = element.attrib['value']
            elif element.text and element.text.strip():
                value = element.text.strip().rstrip()
            elif element.attrib and 'type' in element.attrib:
                value = element.attrib['type']
            else:
                value = elem2dict(element)
            if key in result:
                if type(result[key]) is list:
                    result[key].append(value)
                else:
                    if type(result[key]) is dict:
                        tempvalue = result[key].copy
                    else:
                        tempvalue = result[key]
                    result[key] = [tempvalue, value]
            else:
                result[key] = value
    return result


def findkeys(node, query):
    if isinstance(node, list):
        for i in node:
            for x in findkeys(i, query):
               yield x
    elif isinstance(node, dict):
        if query in node:
            yield node[query]
        for j in node.values():
            for x in findkeys(j, query):
                yield x

def fetching_checklists():
    # Gathering all checklist ID's
    session = requests.Session()
    session.trust_env = False
    response = fetch_object('https://www.ebi.ac.uk/ena/browser/api/summary/ERC000001-ERC999999')
    return response.json()['summaries']

def fetch_sample_attrib(root):
    # Looping over all fields and storing their name and cardinality
    output_list = []
    for attribute in root.iter('FIELD'):
        output = {}
        output['name'] = ''
        output['cardinality'] = ''
        output['description'] = ''
        output['cv'] = []
        output['units'] = ''
        for sub_attr in attribute:
            if sub_attr.tag == 'NAME':
                output['name'] = sub_attr.text
            elif sub_attr.tag == 'MANDATORY':
                output['cardinality'] = sub_attr.text
            elif sub_attr.tag == 'DESCRIPTION':
                output['description'] = sub_attr.text
            elif sub_attr.tag == 'UNITS':
                for unit in sub_attr:
                    output['units'] = unit.text
                output['units'] = ' Units: ' + sub_attr.text
            elif sub_attr.tag == 'FIELD_TYPE':
                for options in sub_attr:
                    if options.tag == 'TEXT_CHOICE_FIELD':
                        for value in options:
                            for choice in value:
                                output['cv'].append(choice.text)
        output_list.append(output)
    return output_list

def create_attributes(ena_object_name, ena_cv, sample_attributes, xml_tree):
    for attribute in ena_cv['fields']:
        if attribute['name'] in xml_tree.keys():
            attribute['cv'] = xml_tree[attribute['name']]
        yield attribute

    if ena_object_name == "sample" and sample_attributes:
        for sample_attribute in sample_attributes:
            yield sample_attribute

def index_to_letter(index):
    """Converts a 0-based index to an Excel column letter."""
    column_letter = ""
    while index >= 0:
        remainder = index % 26
        column_letter = chr(65 + remainder) + column_letter
        index = (index - remainder) // 26 - 1

    return column_letter

def create_alphanum (attrib):
    return ''.join(char for char in attrib if char.isalnum())

def main():

    mapping = { "run":["FILE"], "experiment":["LIBRARY_SELECTION", "LIBRARY_SOURCE", "LIBRARY_STRATEGY", "LOCUS"], "common":["PLATFORM"], "study":["STUDY_TYPE"]}
    template_names= ["ENA.project", "SRA.common", "SRA.experiment", "SRA.run", "SRA.sample", "SRA.study", "SRA.submission"]
    yaml_file_path = "/home/bedro/Documents/ENA-metadata-templates/scripts/controlled_vocabulary/fixed_fields.yml"
    try:
        with open(yaml_file_path, 'r') as yaml_file:
            fixed_fields = yaml.safe_load(yaml_file)
    except FileNotFoundError:
        print(f"File '{yaml_file_path}' not found.")
    except yaml.YAMLError as e:
        print("Error reading YAML:", e)

    xml_tree = {}
    for template_name in template_names:
        template_name_sm = template_name.split(".")[1]
        print(f"Downloading {template_name_sm} template")
        # Getting the xml checklist from ENA
        url = f"https://raw.githubusercontent.com/enasequence/schema/master/src/main/resources/uk/ac/ebi/ena/sra/schema/{template_name}.xsd"
        response = fetch_object(url)
        
        if template_name_sm in mapping.keys():
            for template_block in mapping[template_name_sm]:
                # Parsing XSD
                parser = etree.XMLParser(recover=True, encoding='utf-8',remove_comments=True, remove_blank_text=True)
                root = etree.fromstring(response.content, parser)
                incl = etree.XInclude()
                incl(root)
                xsd_dict = elem2dict(root)
                
                if template_block == "FILE":
                    query_dict = (list(findkeys(xsd_dict, 'filetype')))[0]
                    xml_tree['file_format'] = query_dict['simpleType']['restriction']['enumeration']
                elif template_block == "LIBRARY_SELECTION":
                    query_dict = (list(findkeys(xsd_dict, 'typeLibrarySelection')))[0]
                    xml_tree['library_selection'] = query_dict['restriction']['enumeration']
                elif template_block == "LIBRARY_SOURCE":
                    query_dict = (list(findkeys(xsd_dict, 'typeLibrarySource')))[0]
                    xml_tree['library_source'] = query_dict['restriction']['enumeration']
                elif template_block == "LOCUS":
                    query_dict = (list(findkeys(xsd_dict, 'locus_name')))[0]
                    xml_tree['locus'] = query_dict['simpleType']['restriction']['enumeration']
                elif template_block == "STUDY_TYPE":
                    query_dict = (list(findkeys(xsd_dict, 'existing_study_type')))[0]
                    xml_tree['study_type'] = query_dict['simpleType']['restriction']['enumeration']
                elif template_block == "LIBRARY_STRATEGY":
                    query_dict = (list(findkeys(xsd_dict, 'typeLibraryStrategy')))[0]
                    xml_tree['library_strategy'] = query_dict['restriction']['enumeration']
                elif template_block == "PLATFORM":
                    platformtype_dict = (list(findkeys(xsd_dict, 'PlatformType')))[0]
                    xml_tree['platform'] = []
                    xml_tree['instrument_model'] = []
                    for platformtype, instrument_models in platformtype_dict['choice'].items():
                        xml_tree['platform'].append(platformtype)
                        instrument_models_dict = (list(findkeys(xsd_dict, instrument_models['complexType']['sequence']['INSTRUMENT_MODEL'].strip('com:'))))[0]
                        xml_tree['instrument_model'].extend(instrument_models_dict['restriction']['enumeration'])
                    xml_tree['instrument_model'] = sorted(list(set(xml_tree['instrument_model'])))


                else:
                    break

    for response_object in fetching_checklists(): #[{'accession':'ERC000013'}]: 
        checklist = response_object['accession']
        print(f"Parsing {checklist}")
        # Getting the xml checklist from ENA
        url = f"https://www.ebi.ac.uk/ena/browser/api/xml/{checklist}?download=true"
        response = fetch_object(url)

        # Parsing XML
        root = etree.fromstring(response.content)
        root_dir = "/home/bedro/Documents/ENA-metadata-templates/templates"
        folder_name = checklist
        folder_path = os.path.join(root_dir, folder_name)
        sample_attributes = fetch_sample_attrib(root)
        
        # Create the folder if it doesn't exist
        os.makedirs(folder_path, exist_ok=True)
        
        # Create the TSV files
        for ena_object_name, ena_cv in fixed_fields.items():
            tsv_file_name = f"{ena_object_name}.tsv"
            tsv_file_path = os.path.join(folder_path, tsv_file_name)
            header_list = []
            for attrib in create_attributes(ena_object_name, ena_cv, sample_attributes, xml_tree):
                header_list.append(f"\"{attrib['name']}\"")
            
            header_string = '\t'.join(header_list) + '\n'    
            # Create or overwrite the TSV file
            with open(tsv_file_path, 'w') as tsv_file:
                tsv_file.write(header_string)
        
        # Create or overwrite the README.md file
        readme_file_path = os.path.join(folder_path, "README.md")
        readme_file = open(readme_file_path, 'w')
        readme_file.write("# Description of the metadata fields\n\n")
        
        # Create the XLSX
        xlsx_file_name = f"metadata_template_{checklist}.xlsx"
        xlsx_file_path = os.path.join(folder_path, xlsx_file_name)

        workbook = xlsxwriter.Workbook(xlsx_file_path)
        
        header_format = workbook.add_format({'bold': True, 'align': 'center'})
        description_format = workbook.add_format({'text_wrap': True, 'align': 'center', 'valign':'top'})

        for ena_object_name, ena_cv in fixed_fields.items():

            # Initiate table to README
            readme_file.write(f"## {ena_object_name.title()}\n\n")
            readme_file.write( ena_cv['description'] + "\n\n")

            df = pd.DataFrame(columns=["Field name", "Cardinality", "Description", "CV"])

            # Create worksheet
            worksheet = workbook.add_worksheet(ena_object_name)
            worksheet.set_column(0, 300, 15)
            col_index = 0

            # Create worksheet for the controlled vocabulary
            cv_worksheet = workbook.add_worksheet(f"cv_{ena_object_name}")
            cv_worksheet.hide()
            
            for i, attrib in enumerate(create_attributes(ena_object_name, ena_cv, sample_attributes, xml_tree)):
                # Populate pandas dataframe with attributes
                header = [attrib['name'], attrib['cardinality'], f"{attrib['description'].capitalize()}{attrib['units']}"]
                if 'cv' in attrib and attrib['cv']:
                    header.append(", ".join(attrib['cv']))
                else:
                    header.append("")
                df.loc[i] = header

                # Populate the CV worksheet with values
                if 'cv' in attrib and attrib['cv']:
                    for row_index, value in enumerate(attrib['cv']):
                        cv_worksheet.write(row_index, col_index, str(value))
                    # Define a named range for the valid values.
                    range = f"'cv_{ena_object_name}'!${index_to_letter(col_index)}$1:${index_to_letter(col_index)}${len(attrib['cv'])}"
                    name = create_alphanum(attrib['name'])
                    workbook.define_name(name, range)

                # Write the header
                worksheet.write(0, col_index, attrib['name'], header_format)
                # Write the description row
                worksheet.set_row(1, 150)
                worksheet.write(1, col_index, f"({attrib['cardinality'].capitalize()}) {attrib['description'].capitalize()}{attrib['units']}", description_format)
                # Add data validation
                if 'cv' in attrib and attrib['cv']:
                    name = create_alphanum(attrib['name'])
                    worksheet.data_validation(2, col_index, 100, col_index, {'validate': 'list', 'source': f'={name}'})
                col_index += 1
            # write data table to README
            readme_file.write(df.to_markdown(index=False, tablefmt='pipe'))
            readme_file.write("\n\n")
        
        readme_file.close()
        workbook.close()    

if __name__ == "__main__":

    main()

