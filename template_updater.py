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

def fetching_checklists():
    # Gathering all checklist ID's
    session = requests.Session()
    session.trust_env = False
    response = fetch_object('https://www.ebi.ac.uk/ena/browser/api/summary/ERC000001-ERC999999')
    return response.json()['summaries']


def main():
    for response_object in fetching_checklists():
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
        
        # Create the XLSX file using pandas
        xlsx_file_name = f"metadata_template_{checklist}.xlsx"
        xlsx_file_path = os.path.join(folder_path, xlsx_file_name)
        workbook = xlsxwriter.Workbook(xlsx_file_path)
        worksheet_names = ["experiment", "run", "study", "sample"]
        
        for name in worksheet_names:
            worksheet = workbook.add_worksheet(name)
            header_format = workbook.add_format({'bold': True, 'align': 'center'})
            cell_format = workbook.add_format({'align': 'center'})
            
            if name == "sample":
                # Looping over all fields and storing their name and cardinality
                for attribute in root.iter('FIELD'):
                    name = ''
                    cardinality = ''
                    description = ''
                    choices = []
                    units = ''
                    for i, sub_attr in enumerate(attribute):
                        if sub_attr.tag == 'NAME':
                            name = sub_attr.text
                        elif sub_attr.tag == 'MANDATORY':
                            cardinality = sub_attr.text
                        elif sub_attr.tag == 'DESCRIPTION':
                            description = sub_attr.text
                        elif sub_attr.tag == 'UNITS':
                            for unit in sub_attr:
                                units = unit.text
                            units = sub_attr.text + ' '
                        elif sub_attr.tag == 'FIELD_TYPE':
                            for options in sub_attr:
                                if options.tag == 'TEXT_CHOICE_FIELD':
                                    for value in options:
                                        for choice in value:
                                            choices.append(choice.text)
                    # Write the header
                    worksheet.write(0, i, name, header_format)
                    # Write the description row
                    worksheet.write(1, i, f"{cardinality}. {units}{description}", header_format)
                    # Write 100 cells with "ok"
                    for row in range(1, 101):
                        worksheet.write(row, i, "ok", cell_format)
        workbook.close()    

if __name__ == "__main__":

    main()

