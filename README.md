# ENA-metadata-templates

The European Nucleotide Archive has specific [metadata requirements](https://ena-docs.readthedocs.io/en/latest/submit/general-guide/metadata.html) for submitting data.

This repository contains tabular-format metadata templates required to submit data to ENA using the [ena-upload-cli](https://github.com/usegalaxy-eu/ena-upload-cli) or [Galaxy's ENA upload tool](https://toolshed.g2.bx.psu.edu/view/iuc/ena_upload/). Specifically, there are templates for all the existing [sample checklists](https://www.ebi.ac.uk/ena/browser/checklists), and one for a submission without using a sample checklist.

## Tabular metadata templates (*.tsv)
There are four *(\\*.tsv)* files, one for each metadata object (**study**, **sample**, **experiment** and **run**).

## Workbook (*.xlsx) templates
Workbook templates contain one worksheet per metadata object. Controlled vocabulary options can be selected from dropdown menus.

## Versioning

The version releases on this repository will be synchronized with the [ena-upload-cli](https://github.com/usegalaxy-eu/ena-upload-cli) release cycle, guarantying compliance between what the tool can submit, and the templates it uses.
