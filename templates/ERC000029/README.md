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
| collected_by | Mandatory | Name of persons or institute who collected the specimen |
| collection date | Mandatory | The date of sampling, either as an instance (single point in time) or interval. In case no exact time is available, the date/time can be right truncated i.e. all of these are valid iso8601 compliant times: 2008-01-23t19:23:10+00:00; 2008-01-23t19:23:10; 2008-01-23; 2008-01; 2008. |
| geographic location (altitude) | Optional | The altitude of the sample is the vertical distance between earth's surface above sea level and the sampled position in the air.. Units: m |
| geographic location (country and/or sea) | Mandatory | The geographical origin of the sample as defined by the country or sea. Country or sea names should be chosen from the insdc country list (http://insdc.org/country.html). |
| geographic location (latitude) | Mandatory | The geographical origin of the sample as defined by latitude and longitude. The values should be reported in decimal degrees and in wgs84 system. Units: dd |
| geographic location (longitude) | Mandatory | The geographical origin of the sample as defined by latitude and longitude. The values should be reported in decimal degrees and in wgs84 system. Units: dd |
| geographic location (region and locality) | Optional | The geographical origin of the sample as defined by the specific region name followed by the locality name. |
| identified_by | Optional | Name of the expert who identified the specimen taxonomically |
| geographic location (depth) | Optional | Depth is defined as the vertical distance below surface, e.g. for sediment or soil samples depth is measured from sediment or soil surface, respectivly. Depth can be reported as an interval for subsurface samples.. Units: m |
| amount or size of sample collected | Optional | Amount or size of sample (volume, mass or area) that was collected. Units: l, g, kg, m2, m3 |
| environmental_sample | Mandatory | Identifies sequences derived by direct molecular isolation from a bulk environmental dna sample (by pcr with or without subsequent cloning of the product, dgge, or other anonymous methods) with no reliable identification of the source organism |
| mating_type | Optional | Mating type of the organism from which the sequence was obtained; mating type is used for prokaryotes, and for eukaryotes that undergo meiosis without sexually dimorphic gametes |
| genotype | Optional | Name or code for genotype of organism |
| pathotype | Optional | Name or code for pathotype of organism |
| host disease status | Optional | List of diseases with which the host has been diagnosed; can include multiple diagnoses. The value of the field depends on host; for humans the terms should be chosen from do (disease ontology) at http://www.disease-ontology.org, other hosts are free text |
| host disease outcome | Optional | Disease outcome in the host. |
| host subject id | Optional | A unique identifier by which each subject can be referred to, de-identified, e.g. #131 |
| host age | Optional | Age of host at the time of sampling; relevant scale depends on species and study, e.g. could be seconds for amoebae or centuries for trees. Units: centuries, days, decades, hours, minutes, months, seconds, weeks, years |
| host taxid | Optional | Ncbi taxon id of the host, e.g. 9606 |
| host life stage | Optional | Description of life stage of host |
| host health state | Mandatory | Health status of the host at the time of sample collection. |
| host sex | Optional | Gender or sex of the host. |
| lab_host | Optional | Scientific name of the laboratory host used to propagate the source organism from which the sample was obtained |
| host scientific name | Mandatory | Scientific name of the natural (as opposed to laboratory) host to the organism from which sample was obtained. |
| passage_history | Optional | Details of passage of culture between time of isolation and sequencing |
| sample storage conditions | Optional | Conditions at which sample was stored, usually storage temperature, duration and location |
| Is the sequenced pathogen host associated? | Mandatory | Is the sequenced pathogen host associated? ('Yes' or 'no') |
| bio_material | Optional | Identifier for the biological material from which the sample was obtained, with optional institution code and collection code for the place where it is currently stored. |
| culture_collection | Optional | Institution code and identifier for the culture from which the sample was obtained, with optional collection code. |
| specimen_voucher | Optional | Unique identifier that references the physical specimen that remains after the sequence has been obtained and that ideally exists in a curated collection. |
| isolate | Mandatory | Individual isolate from which the sample was obtained |
| sub_species | Optional | Name of sub-species of organism from which sample was obtained |
| sub_strain | Optional | Name or identifier of a genetically or otherwise modified strain from which sample was obtained, derived from a parental strain (which should be annotated in the strain field; sub_strain from which sample was obtained |
| sub_group | Optional | Name of sub-group of organism from which sample was obtained |
| sub_type | Optional | Name of sub-type of organism from which sample was obtained |
| serovar | Recommended | Serological variety of a species (usually a prokaryote) characterized by its antigenic properties |
| strain | Recommended | Name of the strain from which the sample was obtained. |
| host disease stage | Optional | Disease stage of host |
| isolation source host-associated | Recommended | Name of host tissue or organ sampled for analysis. Example: tracheal tissue |
| host description | Optional | Other descriptive information relating to the host. |
| isolation source non-host-associated | Recommended | Describes the physical, environmental and/or local geographical source of the biological sample from which the sample was derived. Example: soil |
