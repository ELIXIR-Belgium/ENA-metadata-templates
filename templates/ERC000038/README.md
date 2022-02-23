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
| Event Date/Time | Mandatory | Date and time in utc when the sampling event started and ended, e.g. each ctd cast, net tow, or bucket collection is a distinct event. Format: yyyy-mm-ddthh:mm:ssz. Example: 2013-06-21t14:05:00z/2013-06-21t14:46:00z. |
| Latitude Start | Mandatory | Latitude of the location where the sampling event started, e.g. each ctd cast, net tow, or bucket collection is a distinct event. Format: ##.####, Decimal degrees; north= +, south= -; use wgs 84 for gps data. Example: -24.6666.. Units: dd |
| Longitude Start | Mandatory | Longitude of the location where the sampling event started, e.g. each ctd cast, net tow, or bucket collection is a distinct event. Format: ###.####, Decimal degrees; east= +, west= -; use wgs 84 for gps data. Example: -096.1012.. Units: dd |
| Depth | Mandatory | The distance below the surface of the water at which a measurement was made or a sample was collected. Format: ####.##, Positive below the sea surface. Sdn:p06:46:ulaa for m. Example: 14.71. Units: m |
| Sample Collection Device | Optional | The sampling device(s) used for the event. Example: ctd(sbe9c)/rosette with niskin bottles. |
| Protocol Label | Mandatory | Identifies the protocol used to produce the sample, e.g. filtration and preservation. Example: bact_nuc_w0.22-1.6. |
| environment (biome) | Mandatory | Biomes are defined based on factors such as plant structures, leaf types, plant spacing, and other factors like climate. Biome should be treated as the descriptor of the broad ecological context of a sample. Examples include: desert, taiga, deciduous woodland, or coral reef. Envo (v 2013-06-14) terms can be found via the link: www.environmentontology.org/browse-envo |
| environment (feature) | Mandatory | Environmental feature level includes geographic environmental features. Compared to biome, feature is a descriptor of the more local environment. Examples include: harbor, cliff, or lake. Envo (v 2013-06-14) terms can be found via the link: www.environmentontology.org/browse-envo |
| environment (material) | Mandatory | The environmental material level refers to the material that was displaced by the sample, or material in which a sample was embedded, prior to the sampling event. Environmental material terms are generally mass nouns. Examples include: air, soil, or water. Envo (v 2013-06-14) terms can be found via the link: www.environmentontology.org/browse-envo |
| Sampling Campaign | Mandatory | Refers to a finite or indefinite activity aiming at collecting data/samples, e.g. a cruise, a time series, a mesocosm experiment. Example: tara_20110401z. |
| Sampling Station | Mandatory | Refers to the site/station where data/sample collection is performed. Example: tara_100. |
| Sampling Platform | Mandatory | Refers to the unique stage from which the sampling device has been deployed. Includes platform category from sdn:l06, http://seadatanet.maris2.nl/v_bodc_vocab_v2/search.asp?Lib=l06, and platform name. Example: research vessel tara. |
| storage conditions (fresh/frozen/other) | Optional | Explain how and for how long the soil sample was stored before dna extraction. |
| sample health state | Optional | Health status of the subject at the time of sample collection |
| sample disease status | Optional | List of diseases with which the subject has been diagnosed at the time of sample collection; can include multiple diagnoses; the value of the field depends on subject; e.g. Charcoal rot (macrophomina phaseolina), late wilt (cephalosporium maydis) |
| Marine Region | Recommended | The geographical origin of the sample as defined by the marine region name chosen from the marine regions vocabulary at http://www.marineregions.org/. Example: aegean sea. |
| seabed habitat | Mandatory | Classification of the seabed where the organism has been found; for european seabed habitats please use terms from http://eunis.eea.europa.eu/habitats-code-browser.jsp; example: b3.4 : soft sea-cliffs, often vegetated |
| age | Mandatory | Age of the organism the sample was derived from. |
| aquaculture origin | Mandatory | Origin of stock and raised conditions |
| shellfish total weight | Mandatory | Total weight of shellfish including shell at the time of sampling. Epifauna and epiphytes to be removed.. Units: g |
| shellfish soft tissue weight | Mandatory | Total weight of all soft tissue, i.e. weight of entire organism without shell, at the time of sampling. Units: g |
| shell length | Mandatory | Length of shell (perpendicular to the hinge). Units: g |
| shell width | Mandatory | Width of shell (perpendicular angle to length). Units: g |
| adductor weight | Recommended | Total weight of striated muscle and smooth muscle. Units: g |
| gonad weight | Recommended | Total weight of entire gonad tissue. Units: g |
| shell markings | Recommended | Visible markings on outer shell. Units: g |
| toxin burden | Recommended | Concentration of toxins in the organism at the time of sampling. Units: g, kg, mg |
| treatment agent | Optional | The name of the treatment agent used. |
| chemical compound | Optional | A drug, solvent, chemical, etc., with a property that can be measured such as concentration (http://purl.obolibrary.org/obo/chebi_37577). |
