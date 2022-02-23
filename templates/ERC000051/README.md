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
| sample origin | Mandatory | Sample origin from which data deposited was generated, e.g. Engrafted tumor |
| sample taxon name | Mandatory | This field indicates if a sample is derived from a patient or xenograft. The following two options are available: homo sapiens/mus musculus xenograft (sample is from a xenograft derived tumor/cell culture) or homo sapiens (sample is from a patient tumor/cell culture). Please ensure the selected value here is identical to the value in the 'scientific name' column/field. |
| sample material | Mandatory | Sample material from which data deposited was generated, e.g. tissue fragment. If unknown please select "not provided". |
| engrafted tumor sample passage | Mandatory | If engrafted tumor sample, please indicate the passage from which the engrafted tumor sample was harvested (passage 0 must be the first engraftment in the mouse). Please ensure you add a non-negative number greater than 0. If the sample origin is "patient tumor" please enter "not applicable". If passage number is unknown please enter "not provided". |
| engrafted tumor collection site | Recommended | If the sample origin is "engrafted tumor", please indicate the collection site from which the engrafted tumor sample was extracted (e.g. Liver). Please use terminology from ncit ontology: https://www.ebi.ac.uk/ols/ontologies/ncit. If unknown please select ncit term: "not available" ( http://purl.obolibrary.org/obo/ncit_c126101)". If the sample origin is "patient tumor" please do not use this attribute. |
| patient tumor site of collection | Mandatory | Site of collection of the patient tissue sample which was extracted (can be different to primary site if it is a metastatic sample). Please use ncit ontology, e.g. Liver (http://purl.obolibrary.org/obo/ncit_c12392). If unknown please select ncit term: "not available" (http://purl.obolibrary.org/obo/ncit_c126101) |
| patient tumor type | Mandatory | For a primary sample (a tumor at the original site of origin), please select "primary neoplasm" . For a metastatic sample (a tumor that has spread from its original (primary) site of growth to another site, close to or distant from the primary site), please select "metastatic neoplasm" . For a recurring neoplasm sample (neoplasm returning after a period of remission at the same location), please select "recurrent neoplasm" . If unknown tumor type, please select "not provided". |
| sample unique ID | Mandatory | Unique identifier of the pdx or tumor sample, e.g. Crc00003 |
| engraftment host strain name | Recommended | If the sample origin is "engrafted tumor", please indicate the host mouse strain name from which the engrafted tumor sample was extracted (e.g. Nod.cg-prkdcscid il2rgtm1wjl/szj). Please use the following guidelines for the correct nomenclature format: http://www.informatics.jax.org/mgihome/nomen/strains.shtml#mice. If the sample origin is "patient tumor" please add "not applicable" and if unknown please add "not provided". |
| patient age at collection of tumor | Mandatory | Age in years of the patient when the tumor was extracted. Please note this must be a whole number, e.g. 45 |
| patient tumor diagnosis at time of collection | Mandatory | Patient tumor diagnosis at time of collection for engraftment in pdx model or organoid/cell derivation. Please use terminology from ncit ontology: https://www.ebi.ac.uk/ols/ontologies/ncit - please note in ncit ontology, usually the "cancer" concept is represented with "malignant neoplasm"example: "lung cancer" is "malignant lung neoplasm" (http://purl.obolibrary.org/obo/ncit_c7377). If precise diagnosis is unknown, please use "neoplasm" (http://purl.obolibrary.org/obo/ncit_c3262) |
| patient tumor primary site | Mandatory | Site of the primary tumor where cancer originates (may not correspond to the site of the collected tissue sample). Please use ncit ontology, e.g. Colon (http://purl.obolibrary.org/obo/ncit_c12382). If unknown please select ncit term: "not available" ( http://purl.obolibrary.org/obo/ncit_c126101) |
| Was the PDX model humanised? | Recommended | If the sample origin is "engrafted tumor", please indicate if the host strain, from which the sample was extracted, has undergone human immune system reconstitution, using "yes" (model humanised) or "no" (model not humanised). If the sample origin is "patient tumor" please select "not applicable". |
| patient sex | Mandatory | Sex of the patient from which the tumor was extracted. If sex is unknown please select "not available" |
