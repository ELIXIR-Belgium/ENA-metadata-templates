from lxml import etree
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import time
import xlsxwriter
import os

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
    for attribute in root.iter('FIELD'):
        output = {}
        output['name'] = ''
        output['cardinality'] = ''
        output['description'] = ''
        output['choices'] = []
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
                                output['choices'].append(choice.text)
        yield output


def main():

    mapping = { "run":["FILE"], "experiment":["LIBRARY_SELECTION", "LIBRARY_SOURCE", "LIBRARY_STRATEGY", "LOCUS"], "common":["PLATFORM"], "study":["STUDY_TYPE"]}
    template_names= ["ENA.project", "SRA.common", "SRA.experiment", "SRA.run", "SRA.sample", "SRA.study", "SRA.submission"]
    
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
                    xml_tree = query_dict['simpleType']['restriction']['enumeration']
                elif template_block == "LIBRARY_SELECTION":
                    query_dict = (list(findkeys(xsd_dict, 'typeLibrarySelection')))[0]
                    xml_tree = query_dict['restriction']['enumeration']
                elif template_block == "LIBRARY_SOURCE":
                    query_dict = (list(findkeys(xsd_dict, 'typeLibrarySource')))[0]
                    xml_tree = query_dict['restriction']['enumeration']
                elif template_block == "LOCUS":
                    query_dict = (list(findkeys(xsd_dict, 'locus_name')))[0]
                    xml_tree = query_dict['simpleType']['restriction']['enumeration']
                elif template_block == "STUDY_TYPE":
                    query_dict = (list(findkeys(xsd_dict, 'existing_study_type')))[0]
                    xml_tree = query_dict['simpleType']['restriction']['enumeration']
                elif template_block == "LIBRARY_STRATEGY":
                    query_dict = (list(findkeys(xsd_dict, 'typeLibraryStrategy')))[0]
                    xml_tree = query_dict['restriction']['enumeration']
                elif template_block == "PLATFORM":
                    platformtype_dict = (list(findkeys(xsd_dict, 'PlatformType')))[0]
                    xml_tree = {}
                    for platformtype, instrument_models in platformtype_dict['choice'].items():
                        instrument_models_dict = (list(findkeys(xsd_dict, instrument_models['complexType']['sequence']['INSTRUMENT_MODEL'].strip('com:'))))[0]
                        xml_tree[platformtype] = instrument_models_dict['restriction']['enumeration']

                else:
                    break
            print(xml_tree)

    for response_object in [{'accession':'ERC000013'}]: #fetching_checklists():
        checklist = response_object['accession']
        print(f"Parsing {checklist}")
        # Getting the xml checklist from ENA
        url = f"https://www.ebi.ac.uk/ena/browser/api/xml/{checklist}?download=true"
        response = fetch_object(url)

        # Dictionary that will contain all attributes needed
        xml_tree = {}

        # Parsing XML
        root = etree.fromstring(response.content)
        root_dir = "templates"
        folder_name = checklist
        folder_path = os.path.join(root_dir, folder_name)
        
        # Create the folder if it doesn't exist
        os.makedirs(folder_path, exist_ok=True)
        
        # Create the TSV files
        for j in ["experiment","study", "run", "sample"]:
            tsv_file_name = f"{j}.tsv"
            tsv_file_path = os.path.join(folder_path, tsv_file_name)
            
            # Create or overwrite the TSV file
            with open(tsv_file_path, 'w') as tsv_file:
                tsv_file.write("Column1\tColumn2\tColumn3\n")
                tsv_file.write("Value1\tValue2\tValue3\n")
                tsv_file.write("Value4\tValue5\tValue6\n")
        
        # Create the README.md file
        readme_file_path = os.path.join(folder_path, "README.md")
        
        # Create or overwrite the README.md file
        with open(readme_file_path, 'w') as readme_file:
            readme_file.write("# Folder Information\n")
            readme_file.write("This is a sample README file.\n")
            readme_file.write("You can add more information here.\n")
        
        # Create the XLSX
        xlsx_file_name = f"metadata_template_{checklist}.xlsx"
        xlsx_file_path = os.path.join(folder_path, xlsx_file_name)

        workbook = xlsxwriter.Workbook(xlsx_file_path)
        worksheet_names = ["cv", "study", "sample", "experiment", "run"]
        header_format = workbook.add_format({'bold': True, 'align': 'center'})
        description_format = workbook.add_format({'text_wrap': True, 'align': 'center', 'valign':'top'})

        cv_columns = ["section", "metadata_field", "permitted_value"]
        
        # Create controlled vocabulary worksheet

        for name in worksheet_names:

            worksheet = workbook.add_worksheet(name)
            
            worksheet.set_column(0, 300, 15)
            index = 0
            if name == "sample":
                for checklist in fetch_sample_attrib(root):
                    if name:
                        # Write the header
                        worksheet.write(0, index, name, header_format)
                        # Write the description row
                        worksheet.set_row(1, 100)
                        worksheet.write(1, index, f"({checklist['cardinality'].capitalize()}) {checklist['description'].capitalize()}{checklist['units']}", description_format)
                        # Add data validation
                        if checklist['choices']:
                            worksheet.data_validation(2, index, 100, index, {'validate': 'list', 'source': checklist['choices']})
                    index += 1
        workbook.close()    

if __name__ == "__main__":

    main()

