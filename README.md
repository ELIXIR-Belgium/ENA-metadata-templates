# ENA-metadata-templates

The European Nucleotide Archive has specific [metadata requirements](https://ena-docs.readthedocs.io/en/latest/submit/general-guide/metadata.html) for submitting data.

This repository contains tabular-format and xlsx spreadsheet metadata templates required to submit data to ENA using the [ena-upload-cli](https://github.com/usegalaxy-eu/ena-upload-cli) or [Galaxy's ENA upload tool](https://toolshed.g2.bx.psu.edu/view/iuc/ena_upload/). Specifically, there are templates for all the existing [sample checklists](https://www.ebi.ac.uk/ena/browser/checklists). These templates are kept **automatically** up to date with ENA to guarantee the use of the latest attributes. Additionally we also provide a machine actionable JSON file for each template and a `checklist_overview.json` file in the root of this repository listing all available templates in a machine actionable way.

**Supported ENA Checklists:**

<!-- TABLE START -->
| ID       | Name       | Description |
| ---------- | ---------- | ------------ |
| [ERC000011](./templates/ERC000011) | ENA default sample checklist | Minimum information required for the sample |
| [ERC000012](./templates/ERC000012) | GSC MIxS air | Genomic Standards Consortium package extension for reporting of measurements and observations obtained from the environment where the sample was obtained. By choosing the environmental package, a selection of fields can be made from a relevant subsets of the GSC terms. |
| [ERC000013](./templates/ERC000013) | GSC MIxS host associated | Genomic Standards Consortium package extension for reporting of measurements and observations obtained from the environment where the sample was obtained. By choosing the environmental package, a selection of fields can be made from a relevant subsets of the GSC terms. |
| [ERC000014](./templates/ERC000014) | GSC MIxS human associated | Genomic Standards Consortium package extension for reporting of measurements and observations obtained from the environment where the sample was obtained. By choosing the environmental package, a selection of fields can be made from a relevant subsets of the GSC terms. |
| [ERC000015](./templates/ERC000015) | GSC MIxS human gut | Genomic Standards Consortium package extension for reporting of measurements and observations obtained from the environment where the sample was obtained. By choosing the environmental package, a selection of fields can be made from a relevant subsets of the GSC terms. |
| [ERC000016](./templates/ERC000016) | GSC MIxS human oral | Genomic Standards Consortium package extension for reporting of measurements and observations obtained from the environment where the sample was obtained. By choosing the environmental package, a selection of fields can be made from a relevant subsets of the GSC terms. |
| [ERC000017](./templates/ERC000017) | GSC MIxS human skin | Genomic Standards Consortium package extension for reporting of measurements and observations obtained from the environment where the sample was obtained. By choosing the environmental package, a selection of fields can be made from a relevant subsets of the GSC terms. |
| [ERC000018](./templates/ERC000018) | GSC MIxS human vaginal | Genomic Standards Consortium package extension for reporting of measurements and observations obtained from the environment where the sample was obtained. By choosing the environmental package, a selection of fields can be made from a relevant subsets of the GSC terms. |
| [ERC000019](./templates/ERC000019) | GSC MIxS microbial mat biolfilm | Genomic Standards Consortium package extension for reporting of measurements and observations obtained from the environment where the sample was obtained. By choosing the environmental package, a selection of fields can be made from a relevant subsets of the GSC terms. |
| [ERC000020](./templates/ERC000020) | GSC MIxS plant associated | Genomic Standards Consortium package extension for reporting of measurements and observations obtained from the environment where the sample was obtained. By choosing the environmental package, a selection of fields can be made from a relevant subsets of the GSC terms. |
| [ERC000021](./templates/ERC000021) | GSC MIxS sediment | Genomic Standards Consortium package extension for reporting of measurements and observations obtained from the environment where the sample was obtained. By choosing the environmental package, a selection of fields can be made from a relevant subsets of the GSC terms. |
| [ERC000022](./templates/ERC000022) | GSC MIxS soil | Genomic Standards Consortium package extension for reporting of measurements and observations obtained from the environment where the sample was obtained. By choosing the environmental package, a selection of fields can be made from a relevant subsets of the GSC terms. |
| [ERC000023](./templates/ERC000023) | GSC MIxS wastewater sludge | Genomic Standards Consortium package extension for reporting of measurements and observations obtained from the environment where the sample was obtained. By choosing the environmental package, a selection of fields can be made from a relevant subsets of the GSC terms. |
| [ERC000024](./templates/ERC000024) | GSC MIxS water | Genomic Standards Consortium package extension for reporting of measurements and observations obtained from the environment where the sample was obtained. By choosing the environmental package, a selection of fields can be made from a relevant subsets of the GSC terms. |
| [ERC000025](./templates/ERC000025) | GSC MIxS miscellaneous natural or artificial environment | Genomic Standards Consortium package extension for reporting of measurements and observations obtained from the environment where the sample was obtained. By choosing the environmental package, a selection of fields can be made from a relevant subsets of the GSC terms. |
| [ERC000027](./templates/ERC000027) | ENA Micro B3 | Minimum information about a Micro B3 sample. A checklist for reporting metadata of marine microbial samples associated with genomics data. NOTE: Non-genomics data, i.e. oceanographic environmental data and morphology-based biodiversity data, should be submitted to the appropriate National Oceanographic Data Centre according to established reporting practices maintained by oceanographic community experts. Major National Oceanographic Data Centres from countries bordering the North-East Atlantic, and its adjacent seas: the Mediterranean, the Black Sea, the Baltic, the North Sea and the Arctic are listed at http://www.seadatanet.org/Overview/Partners. For the Ocean Sampling Day campaign, non-genomics data shall be reported to the PANGAEA (http://www.pangaea.de/submit/). |
| [ERC000028](./templates/ERC000028) | ENA prokaryotic pathogen minimal sample checklist | Minimum information required for a prokaryotic pathogen sample |
| [ERC000029](./templates/ERC000029) | ENA Global Microbial Identifier reporting standard checklist GMI_MDM:1.1 | Minimum Data for Matching (MDM). A checklist for reporting metadata of pathogen samples for the Global Microbial Identifier (GMI) reporting system. More about GMI can be found here http://www.g-m-i.org/ |
| [ERC000030](./templates/ERC000030) | ENA Tara Oceans | Minimum information about a Tara Oceans sample. A checklist for reporting metadata of oceanic plankton samples associated with genomics data from the Tara Oceans Expedition. |
| [ERC000031](./templates/ERC000031) | GSC MIxS built environment | Genomic Standards Consortium package extension for reporting of measurements and observations obtained from the environment where the sample was obtained. By choosing the environmental package, a selection of fields can be made from a relevant subsets of the GSC terms. |
| [ERC000032](./templates/ERC000032) | ENA Influenza virus reporting standard checklist | Minimum information about an Influenza virus sample. A checklist for reporting metadata of Influenza virus samples associated with genomic data. This minimum metadata standard supports submission of avian, human and mammalian surveillance data as well as serology and viruse isolate information (where available). The ENA Influenza sample checklist is based on standards in use at the Influenza Research Database. |
| [ERC000033](./templates/ERC000033) | ENA virus pathogen reporting standard checklist | Minimum information about a virus pathogen. A checklist for reporting metadata of virus pathogen samples associated with genomic data. This minimum metadata standard was developed by the COMPARE platform for submission of virus surveillance and outbreak data (such as Ebola) as well as virus isolate information. |
| [ERC000034](./templates/ERC000034) | ENA mutagenesis by carcinogen treatment checklist | Minimum Information required for reporting samples associated with genomic data, derived from carcinogen induced animal tumours. This minimum metadata standard was developed in collaboration with Duncan Odom lab for the Mouse Liver Cancer Evolution Project. |
| [ERC000035](./templates/ERC000035) | ENA Crop Plant sample enhanced annotation checklist | The ENA Crop sample enhanced checklist has been developed in collaboration with a number of EMBL-EBI teams to capture enriched annotation of published crop plant samples that lack sufficient reported metadata and are typically associated with systematic transcriptomic realignment-based analyses. |
| [ERC000036](./templates/ERC000036) | ENA sewage checklist | Minimum information about sewage samples. A checklist for reporting of sewage surveillance samples associated with sequence data from metagenomic sequencing projects. This minimum metadata standard was developed by the COMPARE platform. |
| [ERC000037](./templates/ERC000037) | ENA Plant Sample Checklist | ENA implementation of plant specimen contextual information associated with molecular data. The checklist has been developed in collaboration with the NCBI-GenBank and iPlant data resources under the umbrella of the Genomic Standards Consortium. |
| [ERC000038](./templates/ERC000038) | ENA Shellfish Checklist | Shellfish contextual information associated with molecular data. The checklist has been developed in collaboration with EMBRIC Project partners. |
| [ERC000039](./templates/ERC000039) | ENA parasite sample checklist | Minimum information about parasite samples. A checklist for reporting metadata of parasite samples associated with molecular data. This standard was developed by the COMPARE platform and can be used for submission of sample metadata derived from protozoan parasites (e.g. Cryptosporidium) and also multicellular eukaryotic parasites (e.g. Platyhelminthes and Nematoda). |
| [ERC000040](./templates/ERC000040) | ENA UniEuk_EukBank Checklist | Minimum information required for reporting samples associated with the UniEuk EukBank initiative. This checklist aims to capture contextual metadata associated with V4 18S SSU rRNA molecular data. |
| [ERC000041](./templates/ERC000041) | ENA Global Microbial Identifier Proficiency Test (GMI PT) checklist | Minimum information to standardise metadata related to samples used in GMI PT (Global Microbial Identifier Proficiency Test). A checklist for reporting metadata of GMI PT samples associated with molecular data. This minimum metadata standard was developed by the COMPARE platform and can be used for submission of sample metadata derived from Campylobacter coli, Campylobacter jejuni, Listeria monocytogenes, Klebsiella pneumoniae, Salmonella enterica, Escherichia coli and Staphylococcus aureus. |
| [ERC000043](./templates/ERC000043) | ENA Marine Microalgae Checklist | Marine microalgae contextual information. The checklist has been developed in collaboration with EMBRIC Project partners and is suitable for reporting metadata related to environmental samples and those in culture collections. |
| [ERC000044](./templates/ERC000044) | COMPARE-ECDC-EFSA pilot human-associated reporting standard | A checklist for reporting metadata of human-associated pathogen samples for the COMPARE-ECDC-EFSA reporting system. |
| [ERC000045](./templates/ERC000045) | COMPARE-ECDC-EFSA pilot food-associated reporting standard | A checklist for reporting metadata of food-borne pathogen samples for the COMPARE-ECDC-EFSA reporting system. |
| [ERC000047](./templates/ERC000047) | GSC MIMAGS | Genomic Standards Consortium package extension for reporting of measurements and observations obtained from the environment where the sample was obtained. By choosing the environmental package, a selection of fields can be made from a relevant subsets of the GSC terms. |
| [ERC000048](./templates/ERC000048) | GSC MISAGS | Genomic Standards Consortium package extension for reporting of measurements and observations obtained from the environment where the sample was obtained. By choosing the environmental package, a selection of fields can be made from a relevant subsets of the GSC terms. |
| [ERC000049](./templates/ERC000049) | GSC MIUVIGS | Genomic Standards Consortium package extension for reporting of measurements and observations obtained from the environment where the sample was obtained. By choosing the environmental package, a selection of fields can be made from a relevant subsets of the GSC terms. |
| [ERC000050](./templates/ERC000050) | ENA binned metagenome | Minimum information to standardise metadata of binned metagenome samples. Ensures binned and MAG metagenome assembly metadata is compatible. |
| [ERC000051](./templates/ERC000051) | PDX Checklist | Minimum information required for reporting samples associated with patient-derived xenograft (PDX) models or patient samples |
| [ERC000052](./templates/ERC000052) | HoloFood Checklist | Minimum information required for reporting HoloFood samples. HoloFood is a 'hologenomic' approach that will improve the efficiency of food production systems by understanding the biomolecular and physiological processes affected by incorporating feed additives and novel sustainable feeds in farmed animals (https://www.holofood.eu/). |
| [ERC000053](./templates/ERC000053) | Tree of Life Checklist | Minimum information required for reporting samples associated with the Tree of Life Programme (https://www.sanger.ac.uk/programme/tree-of-life/). |
| [ERC000055](./templates/ERC000055) | GSC MIxS agriculture | Genomic Standards Consortium package extension for reporting of measurements and observations obtained from the environment where the sample was obtained. By choosing the environmental package, a selection of fields can be made from a relevant subsets of the GSC terms. |
| [ERC000056](./templates/ERC000056) | GSC MIxS Food and Production | Genomic Standards Consortium package extension for reporting of measurements and observations obtained from the environment where the sample was obtained. By choosing the environmental package, a selection of fields can be made from a relevant subsets of the GSC terms. This package is a combination of the four food extensions (MIxS-food-animal and animal feed, MIxS-food-farm environment, MIxS-food-food production facility, MIxS-food-human foods). |
| [ERC000057](./templates/ERC000057) | GSC MIxS Symbiont | Genomic Standards Consortium package extension for reporting of measurements and observations obtained from the environment where the sample was obtained. By choosing the environmental package, a selection of fields can be made from a relevant subsets of the GSC terms. |
| [ERC000058](./templates/ERC000058) | GSC MIxS Hydrocarbon | Genomic Standards Consortium package extension for reporting of measurements and observations obtained from the environment where the sample was obtained. By choosing the environmental package, a selection of fields can be made from a relevant subsets of the GSC terms. |
<!-- TABLE END -->

## Tabular metadata templates (*.tsv)
There are four *(\\*.tsv)* files, one for each metadata object (**study**, **sample**, **experiment** and **run**).

## Workbook (*.xlsx) templates
Workbook templates contain one worksheet per metadata object. Controlled vocabulary options can be selected from dropdown menus.


## Machine actionable JSON files
Every template folder has a machine actionable yaml file describing all attributes in a template in the following way:

```json
  {
  "name": "Attribute name",
  "cardinality": "mandatory",
  "description": "Description of the attribute",
  "units": "m/s",
  "regex": "Regular expression",
  "field_type": "TEXT_FIELD",
  "cv": [
      "Controlled vocabulary 1",
      "Controlled vocabulary 2"
    ]
  },
```


## Operational Practices

A GitHub Action is put in place to pull the [sample checklists](https://www.ebi.ac.uk/ena/browser/api/summary/ERC000001-ERC999999) and the study, sample, experiment and run [XSD specifications](https://raw.githubusercontent.com/enasequence/schema/master/src/main/resources/uk/ac/ebi/ena/sra/schema/) and update these templates and READMEs accordingly.


### Versioning
The version releases on this repository will be synchronized with the [ena-upload-cli](https://github.com/usegalaxy-eu/ena-upload-cli) release cycle, guarantying compliance between what the tool can submit, and the templates it uses.
