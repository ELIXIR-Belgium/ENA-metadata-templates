# ENA-metadata-templates

The European Nucleotide Archive has specific [metadata requirements](https://ena-docs.readthedocs.io/en/latest/submit/general-guide/metadata.html) for submitting data.

This repository contains tabular-format and xlsx spreadsheet metadata templates required to submit data to ENA using the [ena-upload-cli](https://github.com/usegalaxy-eu/ena-upload-cli) or [Galaxy's ENA upload tool](https://toolshed.g2.bx.psu.edu/view/iuc/ena_upload/). Specifically, there are templates for all the existing [sample checklists](https://www.ebi.ac.uk/ena/browser/checklists). These templates are kept **automatically** up to date with ENA to guarantee the use of the latest attributes. Additionally we also provide a machine actionable YAML file for each template and an `checklist_overview.yml` file in the root of this repository listing all available templates in a machine actionable way.


## Tabular metadata templates (*.tsv)
There are four *(\\*.tsv)* files, one for each metadata object (**study**, **sample**, **experiment** and **run**).

## Workbook (*.xlsx) templates
Workbook templates contain one worksheet per metadata object. Controlled vocabulary options can be selected from dropdown menus.


## Machine actionable YAML files
Every template folder has a machine actionable yaml file describing all attributes in a template in the following way:

```yml
  - cardinality: mandatory
    cv:
    - Controlled vocabulary 1
    - Controlled vocabulary 1
    description: Description of the attribute
    name: Attribute name
    units: 'm/s'
```


## Operational Practices

A GitHub Action is put in place to pull the [sample checklists](https://www.ebi.ac.uk/ena/browser/api/summary/ERC000001-ERC999999) and the study, sample, experiment and run [XSD specifications](https://raw.githubusercontent.com/enasequence/schema/master/src/main/resources/uk/ac/ebi/ena/sra/schema/) and update these templates and READMEs accordingly.


### Versioning
The version releases on this repository will be synchronized with the [ena-upload-cli](https://github.com/usegalaxy-eu/ena-upload-cli) release cycle, guarantying compliance between what the tool can submit, and the templates it uses.
