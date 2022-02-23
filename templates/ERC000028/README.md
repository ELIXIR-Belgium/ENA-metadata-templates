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
| isolation_source | Mandatory | Describes the physical, environmental and/or local geographical source of the biological sample from which the sample was derived |
| lat_lon | Recommended | Geographical coordinates of the location where the specimen was collected |
| collected_by | Optional | Name of persons or institute who collected the specimen |
| collection date | Mandatory | The date of sampling, either as an instance (single point in time) or interval. In case no exact time is available, the date/time can be right truncated i.e. all of these are valid iso8601 compliant times: 2008-01-23t19:23:10+00:00; 2008-01-23t19:23:10; 2008-01-23; 2008-01; 2008. |
| geographic location (country and/or sea) | Mandatory | The geographical origin of the sample as defined by the country or sea. Country or sea names should be chosen from the insdc country list (http://insdc.org/country.html). |
| geographic location (region and locality) | Optional | The geographical origin of the sample as defined by the specific region name followed by the locality name. |
| identified_by | Optional | Name of the expert who identified the specimen taxonomically |
| environmental_sample | Optional | Identifies sequences derived by direct molecular isolation from a bulk environmental dna sample (by pcr with or without subsequent cloning of the product, dgge, or other anonymous methods) with no reliable identification of the source organism |
| mating_type | Optional | Mating type of the organism from which the sequence was obtained; mating type is used for prokaryotes, and for eukaryotes that undergo meiosis without sexually dimorphic gametes |
| host health state | Mandatory | Health status of the host at the time of sample collection. |
| lab_host | Optional | Scientific name of the laboratory host used to propagate the source organism from which the sample was obtained |
| host scientific name | Mandatory | Scientific name of the natural (as opposed to laboratory) host to the organism from which sample was obtained. |
| bio_material | Optional | Identifier for the biological material from which the sample was obtained, with optional institution code and collection code for the place where it is currently stored. |
| culture_collection | Optional | Institution code and identifier for the culture from which the sample was obtained, with optional collection code. |
| specimen_voucher | Optional | Unique identifier that references the physical specimen that remains after the sequence has been obtained and that ideally exists in a curated collection. |
| isolate | Mandatory | Individual isolate from which the sample was obtained |
| sub_species | Optional | Name of sub-species of organism from which sample was obtained |
| sub_strain | Optional | Name or identifier of a genetically or otherwise modified strain from which sample was obtained, derived from a parental strain (which should be annotated in the strain field; sub_strain from which sample was obtained |
| serovar | Recommended | Serological variety of a species (usually a prokaryote) characterized by its antigenic properties |
| strain | Recommended | Name of the strain from which the sample was obtained. |
