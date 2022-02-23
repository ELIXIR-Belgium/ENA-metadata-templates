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
| project name | Mandatory | Name of the project within which the sequencing was organized |
| sample volume or weight for DNA extraction | Mandatory | Volume (ml) or weight (g) of sample processed for dna extraction. Units: g, ml, mg, ng |
| nucleic acid extraction | Optional | Link to a literature reference, electronic resource or a standard operating procedure (sop) |
| pcr primers | Optional | Pcr primers that were used to amplify the sequence of the targeted gene, locus or subfragment. This field should contain all the primers used for a single pcr reaction if multiple forward or reverse primers are present in a single pcr reaction. The primer sequence should be reported in uppercase letters |
| adapters | Recommended | Adapters provide priming sequences for both amplification and sequencing of the sample-library fragments. Both adapters should be reported; in uppercase letters |
| sequencing method | Mandatory | Sequencing method used; e.g. Sanger, pyrosequencing, abi-solid |
| reference host genome for decontamination | Mandatory | Reference host genome that was mapped against for host decontamination (in the form of a valid assembly accession - e.g. in the format gca_xxxxxxx.x) |
| collection date | Recommended | The date of sampling, either as an instance (single point in time) or interval. In case no exact time is available, the date/time can be right truncated i.e. all of these are valid iso8601 compliant times: 2008-01-23t19:23:10+00:00; 2008-01-23t19:23:10; 2008-01-23; 2008-01; 2008. |
| geographic location (country and/or sea) | Optional | The geographical origin of the sample as defined by the country or sea. Country or sea names should be chosen from the insdc country list (http://insdc.org/country.html). |
| geographic location (latitude) | Optional | The geographical origin of the sample as defined by latitude and longitude. The values should be reported in decimal degrees and in wgs84 system. Units: dd |
| geographic location (longitude) | Optional | The geographical origin of the sample as defined by latitude and longitude. The values should be reported in decimal degrees and in wgs84 system. Units: dd |
| geographic location (region and locality) | Optional | The geographical origin of the sample as defined by the specific region name followed by the locality name. |
| trial length | Recommended | Length of time from the beginning of the trial until the end of the trial. Units: days, hours, minutes, weeks, years |
| trial timepoint | Mandatory | Timepoint of the trial when the sample was collected - length of time after the beginning of the trial. Units: days, hours, minutes, weeks, years |
| sample storage temperature | Recommended | Temperature at which sample was stored, e.g. -80. Units: °c |
| sample storage location | Optional | Location at which sample was stored, usually name of a specific freezer/room |
| sample storage buffer | Recommended | Buffer used for sample storage (e.g. Rnalater) |
| sample storage container | Recommended | Container that sample was stored in e.g. tube type |
| host disease status | Recommended | List of diseases with which the host has been diagnosed; can include multiple diagnoses. The value of the field depends on host; for humans the terms should be chosen from do (disease ontology) at http://www.disease-ontology.org, other hosts are free text |
| host common name | Mandatory | Common name of the host, e.g. human |
| host subject id | Mandatory | A unique identifier by which each subject can be referred to, de-identified, e.g. #131 |
| host taxid | Mandatory | Ncbi taxon id of the host, e.g. 9606 |
| host body site | Mandatory | Name of body site where the sample was obtained from, such as a specific organ or tissue (tongue, lung etc...). For foundational model of anatomy ontology (fma) (v 3.1) terms, please see http://purl.bioontology.org/ontology/fma |
| host length | Optional | The length of subject. Units: cm, m, mm |
| host total mass | Recommended | Total mass of the host at collection, the unit depends on host. Units: g, kg |
| host sex | Optional | Gender or sex of the host. |
| host scientific name | Recommended | Scientific name of the natural (as opposed to laboratory) host to the organism from which sample was obtained. |
| host breed | Recommended | Breed of the host (e.g. Cobb-500) |
| host gutted mass | Optional | Total mass of the host after gutting, the unit depends on host. Units: g, kg |
| host diet | Recommended | Type of diet depending on the host, for animals omnivore, herbivore etc., for humans high-fat, mediterranean etc.; can include multiple diet types |
| host diet treatment | Mandatory | Experimental diet treatment/additive to normal host feed e.g. Probiotic (gallipro epb5) |
| host diet treatment concentration | Optional | Concentration of experimental diet treatment/additive to normal host feed as a percentage of the mass of the feed (e.g. 20%). Units: % mass |
| host storage container | Optional | Storage container that the host organism is kept in before sampling (e.g. cage, water tank, pen) including details of size and type |
| host storage container pH | Optional | Ph of the medium in which the host organism is kept before sampling (e.g. ph of water in tank) |
| host storage container temperature | Recommended | Temperature at which the host is kept before sampling. Units: °c |
