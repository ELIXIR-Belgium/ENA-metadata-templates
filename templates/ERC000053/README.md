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
| organism part | Mandatory | The part of organism's anatomy or substance arising from an organism from which the biomaterial was derived, excludes cells. |
| lifestage | Mandatory | The age class or life stage of the organism at the time of collection. |
| project name | Mandatory | Name of the project within which the sequencing was organized |
| tolid | Optional | A tolid (tree of life id) is a unique and easy to communicate sample identifier that provides species recognition, differentiates between specimen of the same species and adds taxonomic context. Tolids are endorsed by the earthbiogenome project (ebp) and should be assigned to any sample with association to the ebp. More information at id.tol.sanger.ac.uk. |
| barcoding center | Optional | Center where dna barcoding was/will be performed. |
| collected_by | Mandatory | Name of persons or institute who collected the specimen |
| collection date | Mandatory | The date of sampling, either as an instance (single point in time) or interval. In case no exact time is available, the date/time can be right truncated i.e. all of these are valid iso8601 compliant times: 2008-01-23t19:23:10+00:00; 2008-01-23t19:23:10; 2008-01-23; 2008-01; 2008. |
| geographic location (country and/or sea) | Mandatory | The geographical origin of the sample as defined by the country or sea. Country or sea names should be chosen from the insdc country list (http://insdc.org/country.html). |
| geographic location (latitude) | Mandatory | The geographical origin of the sample as defined by latitude and longitude. The values should be reported in decimal degrees and in wgs84 system. Units: dd |
| geographic location (longitude) | Mandatory | The geographical origin of the sample as defined by latitude and longitude. The values should be reported in decimal degrees and in wgs84 system. Units: dd |
| geographic location (region and locality) | Mandatory | The geographical origin of the sample as defined by the specific region name followed by the locality name. |
| identified_by | Optional | Name of the expert who identified the specimen taxonomically |
| geographic location (depth) | Optional | Depth is defined as the vertical distance below surface, e.g. for sediment or soil samples depth is measured from sediment or soil surface, respectivly. Depth can be reported as an interval for subsurface samples.. Units: m |
| geographic location (elevation) | Optional | The elevation of the sampling site as measured by the vertical distance from mean sea level.. Units: m |
| habitat | Mandatory | Description of the location of the sample material. please use envo terms where possible: https://www.ebi.ac.uk/ols/ontologies/envo |
| identifier_affiliation | Optional | The university, institution, or society responsible for identifying the specimen. |
| original collection date | Optional | For use if the specimen is from a zoo, botanic garden, culture collection etc. and has a known original date of collection. In case no exact time is available, the date/time can be right truncated i.e. all of these are valid iso8601 compliant times: 2008-01-23t19:23:10+00:00; 2008-01-23t19:23:10; 2008-01-23; 2008-01; 2008. |
| original geographic location | Optional | For use if the specimen is from a zoo, botanic garden or culture collection etc. and has a known origin elsewhere. Please record the general description of the original collection location. This should be formatted as a country and optionally include more specific locations ranging from least to most specific separated by a | character, e.g. "United kingdom | east anglia | norfolk | norwich | university of east anglia | uea broad". |
| sample derived from | Optional | Reference to parental sample(s) or original run(s) that the assembly is derived from. The referenced samples or runs should already be registered in insdc. This should be formatted as one of the following. A single sample/run e.g. Ersxxxxxx or a comma separated list e.g. Ersxxxxxx,ersxxxxxx or a range e.g. Ersxxxxxx-ersxxxxxx |
| sample same as | Optional | Reference to sample(s) that are equivalent. The referenced sample(s) should already be registered in insdc. This should be formatted as one of the following. A single sample e.g. Ersxxxxxx or a comma separated list e.g. Ersxxxxxx,ersxxxxxx |
| sample symbiont of | Optional | Reference to host sample from symbiont. The referenced sample should already be registered in insdc. E.g. Ersxxxxxx |
| sample coordinator | Optional | NA |
| sample coordinator affiliation | Optional | NA |
| sex | Mandatory | Sex of the organism from which the sample was obtained |
| relationship | Optional | Indicates if the specimen has a known parental, child, or sibling relationship to any other specimens. |
| symbiont | Optional | Used to separate host and symbiont metadata within a symbiont system where the host species are indicated as 'n' and symbionts are indicated as 'y' |
| collecting institution | Mandatory | Name of the institution to which the person collecting the specimen belongs. Format: institute name, institute address |
| GAL | Optional | The name (or acronym) of the genome acquisition lab responsible for the sample. |
| specimen_voucher | Recommended | Unique identifier that references the physical specimen that remains after the sequence has been obtained and that ideally exists in a curated collection. |
| specimen_id | Optional | Unique identifier used to link all data for the recorded specimen. |
| GAL_sample_id | Optional | Unique name assigned to the sample by the genome acquisition lab. |
| culture_or_strain_id | Optional | Living, culturable, named laboratory strain that sequenced material is derived from. |
