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
| nucleic acid extraction | Optional | Link to a literature reference, electronic resource or a standard operating procedure (sop) |
| library construction method | Optional | Library construction method used for clone libraries |
| protocol | Recommended | The laboratory method used to reveal the presence of the sample sequenced in the experiment. |
| instrument for DNA concentration measurement | Optional | Name/type of instrument used to measure the dna concentration (ng/µl) prior to library preparation |
| read quality filter | Optional | Programme used to filter reads quality before conducting the analysis |
| DNA concentration | Optional | Dna concentration used for sequencing in ng/µl. Units: ng/µl |
| collection_date | Optional | Date that the specimen was collected |
| isolation_source | Optional | Describes the physical, environmental and/or local geographical source of the biological sample from which the sample was derived |
| geographic location (country and/or sea) | Recommended | The geographical origin of the sample as defined by the country or sea. Country or sea names should be chosen from the insdc country list (http://insdc.org/country.html). |
| geographic location (region and locality) | Recommended | The geographical origin of the sample as defined by the specific region name followed by the locality name. |
| amount or size of sample collected | Optional | Amount or size of sample (volume, mass or area) that was collected. Units: l, g, kg, m2, m3 |
| sample storage duration | Optional | Duration for which sample was stored. Units: days, hours, months, weeks, years |
| sample storage temperature | Optional | Temperature at which sample was stored, e.g. -80. Units: °c |
| sample storage location | Optional | Location at which sample was stored, usually name of a specific freezer/room |
| sampling time point | Optional | NA |
| sample transportation temperature | Optional | Transportation temperature from sample site to storage. Units: °c |
| sample transportation date | Optional | Transportation/shipping date of the sample. Format:yyyy-mm-dd |
| sample transportation time | Optional | Transportation time from sample site to storage |
| receipt date | Recommended | Date on which the sample was received. Format:yyyy-mm-dd. Please provide the highest precision possible. If the sample was received by the institution and not collected, the 'receipt date' must be provided instead. Either the 'collection date' or 'receipt date' must be provided. If available, provide both dates. |
| links to additional analysis | Recommended | Link to additional analysis results performed on the sample |
| isolate | Mandatory | Individual isolate from which the sample was obtained |
| sub_species | Recommended | Name of sub-species of organism from which sample was obtained |
| Further Details | Recommended | Reference details related to a sample in form of an uri. |
