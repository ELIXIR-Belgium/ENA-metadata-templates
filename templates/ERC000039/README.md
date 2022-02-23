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
| dev_stage | Mandatory | If the sample was obtained from an organism in a specific developmental stage, it is specified with this qualifier |
| subject exposure | Optional | Exposure of the subject to infected human or animals, such as poultry, wild bird or swine. If multiple exposures are applicable, please state them separated by semicolon. Example: poultry; wild bird |
| subject exposure duration | Optional | Duration of the exposure of the subject to an infected human or animal. If multiple exposures are applicable, please state their duration in the same order in which you reported the exposure in the field 'subject exposure'. Example: 1 day; 0.33 days |
| travel-relation | Optional | Designates the relation of the main diagnosis to the patient's travel. |
| clinical setting | Optional | The timing of the clinic visit in relation to travel. |
| country of travel | Optional | The name of the country of patient's travel. |
| collection date | Recommended | The date of sampling, either as an instance (single point in time) or interval. In case no exact time is available, the date/time can be right truncated i.e. all of these are valid iso8601 compliant times: 2008-01-23t19:23:10+00:00; 2008-01-23t19:23:10; 2008-01-23; 2008-01; 2008. |
| geographic location (country and/or sea) | Mandatory | The geographical origin of the sample as defined by the country or sea. Country or sea names should be chosen from the insdc country list (http://insdc.org/country.html). |
| geographic location (latitude) | Recommended | The geographical origin of the sample as defined by latitude and longitude. The values should be reported in decimal degrees and in wgs84 system. Units: dd |
| geographic location (longitude) | Recommended | The geographical origin of the sample as defined by latitude and longitude. The values should be reported in decimal degrees and in wgs84 system. Units: dd |
| geographic location (region and locality) | Optional | The geographical origin of the sample as defined by the specific region name followed by the locality name. |
| genotype | Recommended | Name or code for genotype of organism |
| host disease outcome | Recommended | Disease outcome in the host. |
| host common name | Recommended | Common name of the host, e.g. human |
| host subject id | Recommended | A unique identifier by which each subject can be referred to, de-identified, e.g. #131 |
| host age | Recommended | Age of host at the time of sampling; relevant scale depends on species and study, e.g. could be seconds for amoebae or centuries for trees. Units: centuries, days, decades, hours, minutes, months, seconds, weeks, years |
| host health state | Recommended | Health status of the host at the time of sample collection. |
| host sex | Recommended | Gender or sex of the host. |
| host scientific name | Recommended | Scientific name of the natural (as opposed to laboratory) host to the organism from which sample was obtained. |
| collector name | Mandatory | Name of the person who collected the specimen. Example: john smith |
| collecting institution | Mandatory | Name of the institution to which the person collecting the specimen belongs. Format: institute name, institute address |
| sample storage conditions | Optional | Conditions at which sample was stored, usually storage temperature, duration and location |
| isolate | Mandatory | Individual isolate from which the sample was obtained |
| strain | Recommended | Name of the strain from which the sample was obtained. |
| isolation source host-associated | Recommended | Name of host tissue or organ sampled for analysis. Example: tracheal tissue |
| diagnostic method | Recommended | The method or procedure (imaging, genetic or other) performed to determine or confirm the presence of disease in an individual. Examples: microscopy, immunofluorescence, pcr, rapid tests, etc. |
| known pathogenicity | Recommended | To what is the entity pathogenic, for instance plant, fungi, bacteria |
| isolation source non-host-associated | Recommended | Describes the physical, environmental and/or local geographical source of the biological sample from which the sample was derived. Example: soil |
