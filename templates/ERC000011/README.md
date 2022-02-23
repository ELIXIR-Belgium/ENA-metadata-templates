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
| cell_type | Optional | Cell type from which the sample was obtained |
| dev_stage | Optional | If the sample was obtained from an organism in a specific developmental stage, it is specified with this qualifier |
| germline | Optional | The sample described presented in the entry has not undergone somatic genomic rearrangement as part of an adaptive immune response; it is the unrearranged molecule that was inherited from the parental germline |
| tissue_lib | Optional | Tissue library from which sample was obtained |
| tissue_type | Optional | Tissue type from which the sample was obtained |
| collection_date | Optional | Date that the specimen was collected |
| isolation_source | Optional | Describes the physical, environmental and/or local geographical source of the biological sample from which the sample was derived |
| lat_lon | Optional | Geographical coordinates of the location where the specimen was collected |
| collected_by | Optional | Name of persons or institute who collected the specimen |
| geographic location (country and/or sea) | Optional | The geographical origin of the sample as defined by the country or sea. Country or sea names should be chosen from the insdc country list (http://insdc.org/country.html). |
| geographic location (region and locality) | Optional | The geographical origin of the sample as defined by the specific region name followed by the locality name. |
| identified_by | Optional | Name of the expert who identified the specimen taxonomically |
| environmental_sample | Optional | Identifies sequences derived by direct molecular isolation from a bulk environmental dna sample (by pcr with or without subsequent cloning of the product, dgge, or other anonymous methods) with no reliable identification of the source organism |
| mating_type | Optional | Mating type of the organism from which the sequence was obtained; mating type is used for prokaryotes, and for eukaryotes that undergo meiosis without sexually dimorphic gametes |
| sex | Optional | Sex of the organism from which the sample was obtained |
| lab_host | Optional | Scientific name of the laboratory host used to propagate the source organism from which the sample was obtained |
| host scientific name | Optional | Scientific name of the natural (as opposed to laboratory) host to the organism from which sample was obtained. |
| bio_material | Optional | Identifier for the biological material from which the sample was obtained, with optional institution code and collection code for the place where it is currently stored. |
| culture_collection | Optional | Institution code and identifier for the culture from which the sample was obtained, with optional collection code. |
| specimen_voucher | Optional | Unique identifier that references the physical specimen that remains after the sequence has been obtained and that ideally exists in a curated collection. |
| cultivar | Optional | Cultivar (cultivated variety) of plant from which sample was obtained |
| ecotype | Optional | A population within a given species displaying genetically based, phenotypic traits that reflect adaptation to a local habitat. |
| isolate | Optional | Individual isolate from which the sample was obtained |
| sub_species | Optional | Name of sub-species of organism from which sample was obtained |
| variety | Optional | Variety (= varietas, a formal linnaean rank) of organism from which sample was derived. |
| sub_strain | Optional | Name or identifier of a genetically or otherwise modified strain from which sample was obtained, derived from a parental strain (which should be annotated in the strain field; sub_strain from which sample was obtained |
| cell_line | Optional | Cell line from which the sample was obtained |
| serotype | Optional | Serological variety of a species characterized by its antigenic properties |
| serovar | Optional | Serological variety of a species (usually a prokaryote) characterized by its antigenic properties |
| strain | Optional | Name of the strain from which the sample was obtained. |
