**IMPORTANT** The templates in this repo are still working, but are not up to date. We are looking into automatically updating these templates based on changes made on the ENA side.

# ENA-metadata-templates

The European Nucleotide Archive has specific [metadata requirements](https://ena-docs.readthedocs.io/en/latest/submit/general-guide/metadata.html) for submitting data.

This repository contains tabular-format metadata templates required to submit data to ENA using the [ena-upload-cli](https://github.com/usegalaxy-eu/ena-upload-cli) or [Galaxy's](https://usegalaxy.eu/) ENA upload tool. Specifically, there are templates for all the existing [sample checklists](https://www.ebi.ac.uk/ena/browser/checklists), and one for a submission without using a sample checklist.

## Tabular metadata templates (*.tsv)
There are four *(\\*.tsv)* files, one for each metadata object (**study**, **sample**, **experiment** and **run**). These can be used for submissions using the [ena-upload-cli](https://github.com/usegalaxy-eu/ena-upload-cli).

## Workbook (*.xlsx) templates
Workbook templates contain one worksheet per metadata object. Controlled vocabulary options can be selected from dropdown menus.
Workbook templates can be used for submissions using the [ena-upload-cli](https://github.com/usegalaxy-eu/ena-upload-cli) or [Galaxy's](https://usegalaxy.eu/) ENA upload tool.


## Scripts

- R script to create the folder structure and skeletons of the templates
- Excel Macro that creates the drop downs in the Excelsheet

### Dependencies
#### Linux

- libxml2
- libxml2-dev
- r-base-core
- libssl-dev
- libcurl4-openssl-dev

#### R packages

- methods
- xml2
- dplyr
- stringr
- reshape
- openxlsx
- httr
- rlist
- jsonlite
- dplyr


