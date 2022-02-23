## Description of the metadata fields

### Study

| field name | requirement | description |
| ------- | ------- | ------- |
| alias | Mandatory | Unique identificator for a study. This is used to link experiments to the study. |
| title | Mandatory | Title of the study as would be used in a publication. |
| study_type | Mandatory | The STUDY_TYPE presents a controlled vocabulary for expressing the overall purpose of the study. |
| new_study_type | Optional if ‘study_type’ is not ‘other’ | To propose a new term, select Other and enter a new study type. |
| study_abstract | Optional | Briefly describes the goals, purpose, and scope of the Study.  This need not be listed if it can be inherited from a referenced publication. |


### Experiment

| field name | requirement | description |
| ------- | ------- | ------- |
| alias | Mandatory | Unique identificator for each experiment. This is used to link runs to experiments. |
| title | Optional | Short text that can be used to call out experiment records in searches or in displays. This element is technically optional but should be used for all new records. |
| study_alias | Mandatory | Identifies the parent study. (From study metadata) |
| sample_alias | Mandatory | (From sample metadata) |
| design_description | Optional | Goal and setup of the individual library including library was constructed. |
| library_name | Optional | The submitter's name for this library. |
| library_strategy | Mandatory | Sequencing technique intended for this library. |
| library_source | Mandatory | The LIBRARY_SOURCE specifies the type of source material that is being sequenced. |
| library_selection | Mandatory | Method used to enrich the target in the sequence library preparation |
| library_layout | Mandatory | LIBRARY_LAYOUT specifies whether to expect single, paired, or other configuration of reads. In the case of paired reads, information about the relative distance and orientation is specified. |
| insert_size | Optional | Insert size for paired reads |
| library_construction_protocol | Optional | Free form text describing the protocol by which the sequencing library was constructed. |
| platform | Mandatory | The PLATFORM record selects which sequencing platform and platform-specific runtime parameters. This will be determined by the Center. Optional if 'instrument_model' is provided. |
| instrument_model | Mandatory | Model of the sequencing instrument. |


### Run

| field name | requirement | description |
| ------- | ------- | ------- |
| alias | Mandatory | Unique identificator for each run. |
| experiment_alias | Mandatory | From_experiment_metadata |
| file_name | Mandatory | The name or relative pathname of a run data file. |
| file_format | Mandatory | The run data file model. |



### Sample (this checklist)
| field name | requirement | description |
| ------- | ------- | ------- |
| alias | Mandatory | Unique identificator for each sample. This is used to link experiments to the samples. |
| title | Mandatory | Short text that can be used to call out sample records in search results or in displays. |
| scientific_name | Mandatory | Scientific name of sample that distinguishes its taxonomy.  Please use a name or synonym that is tracked in the INSDC Taxonomy database. Also, this field can be used to confirm the TAXON_ID setting. |
| sample_description | Mandatory | Free-form text describing the sample, its origin, and its method of isolation. |
| subject exposure | Optional | Exposure of the subject to infected human or animals, such as poultry, wild bird or swine. If multiple exposures are applicable, please state them separated by semicolon. Example: poultry; wild bird |
| subject exposure duration | Optional | Duration of the exposure of the subject to an infected human or animal. If multiple exposures are applicable, please state their duration in the same order in which you reported the exposure in the field 'subject exposure'. Example: 1 day; 0.33 days |
| travel-relation | Optional | Designates the relation of the main diagnosis to the patient's travel. |
| clinical setting | Optional | The timing of the clinic visit in relation to travel. |
| country of travel | Optional | The name of the country of patient's travel. |
| collection_date | Mandatory | Date that the specimen was collected |
| collected_by | Mandatory | Name of persons or institute who collected the specimen |
| geographic location (country and/or sea) | Mandatory | The geographical origin of the sample as defined by the country or sea. Country or sea names should be chosen from the insdc country list (http://insdc.org/country.html). |
| geographic location (region and locality) | Optional | The geographical origin of the sample as defined by the specific region name followed by the locality name. |
| host disease status | Optional | List of diseases with which the host has been diagnosed; can include multiple diagnoses. The value of the field depends on host; for humans the terms should be chosen from do (disease ontology) at http://www.disease-ontology.org, other hosts are free text |
| host disease outcome | Optional | Disease outcome in the host. |
| host scientific name | Mandatory | Scientific name of the natural (as opposed to laboratory) host to the organism from which sample was obtained. |
| isolate | Mandatory | Individual isolate from which the sample was obtained |
| sub_type | Optional | Name of sub-type of organism from which sample was obtained |
| serovar | Recommended | Serological variety of a species (usually a prokaryote) characterized by its antigenic properties |
| serovar_in-silico | Recommended | Serological variety of a species characterized by its antigenic properties derived by in silico prediction |
| isolation source host-associated | Recommended | Name of host tissue or organ sampled for analysis. Example: tracheal tissue |
