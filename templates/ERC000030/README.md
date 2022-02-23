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
| Event Label | Recommended | An event corresponds to the deployment of a sampling device. It is bound in space and time. The event label is a unique identifier composed of the project prefix "tara", sampling date/time "yyyymmddthh:mm:ssz", station number "000" and a short label to indicate the sampling device used, e.g. "Event_cast", "event_net", "event_pump". Example: tara_20110416t1508z_100_event_cast. |
| Event Date/Time Start | Mandatory | Date and time in utc when the sampling event started, e.g. each ctd cast, net tow, or bucket collection is a distinct event. Format: yyyy-mm-ddthh:mm:ssz. Example: 2011-04-16t15:05:30z. |
| Event Date/Time End | Recommended | Date and time in utc when the sampling event ended, e.g. each ctd cast, net tow, or bucket collection is a distinct event. Format: yyyy-mm-ddthh:mm:ssz. Example: 2011-04-16t15:38:00z. |
| Latitude Start | Mandatory | Latitude of the location where the sampling event started, e.g. each ctd cast, net tow, or bucket collection is a distinct event. Format: ##.####, Decimal degrees; north= +, south= -; use wgs 84 for gps data. Example: -24.6666.. Units: dd |
| Longitude Start | Mandatory | Longitude of the location where the sampling event started, e.g. each ctd cast, net tow, or bucket collection is a distinct event. Format: ###.####, Decimal degrees; east= +, west= -; use wgs 84 for gps data. Example: -096.1012.. Units: dd |
| Latitude End | Recommended | Latitude of the location where the sampling event ended, e.g. each ctd cast, net tow, or bucket collection is a distinct event. Format: ##.####, Decimal degrees; north= +, south= -; use wgs 84 for gps data. Example: -24.6643.. Units: dd |
| Longitude End | Recommended | Longitude of the location where the sampling event ended, e.g. each ctd cast, net tow, or bucket collection is a distinct event. Format: ###.####, Decimal degrees; east= +, west= -; use wgs 84 for gps data. Example: -096.1171.. Units: dd |
| Depth | Mandatory | The distance below the surface of the water at which a measurement was made or a sample was collected. Format: ####.##, Positive below the sea surface. Sdn:p06:46:ulaa for m. Example: 14.71. Units: m |
| Sample Collection Device | Recommended | The sampling device(s) used for the event. Example: ctd(sbe9c)/rosette with niskin bottles. |
| Protocol Label | Mandatory | Identifies the protocol used to produce the sample, e.g. filtration and preservation. Example: bact_nuc_w0.22-1.6. |
| Size Fraction Lower Threshold | Recommended | Sample_protocol_size-fraction_lower-threshold_(µm) indicates the lower size threshold. Materials smaller than the size threshold are excluded from the sample. Example: 0.22 µm |
| Size Fraction Upper Threshold | Recommended | Sample_protocol_size-fraction_upper-threshold_(µm) indicates the upper size threshold. Materials larger than the size threshold are excluded from the sample.example: 1.6 µm |
| Sample Status | Recommended | Refers to the completness of sample metadata validation. Example: preliminary but can be used to provide data discovery services. |
| Last Update Date | Recommended | Date of the last update of this sample in the samples registry. Example: 2014-03-01z. |
| project name | Mandatory | Name of the project within which the sequencing was organized |
| environmental package | Mandatory | Migs/mims/mimarks extension for reporting of measurements and observations obtained from one or more of the environments where the sample was obtained. All environmental packages listed here are further defined in separate subtables. By giving the name of the environmental package, a selection of fields can be made from the subtables and can be reported |
| environment (biome) | Mandatory | Biomes are defined based on factors such as plant structures, leaf types, plant spacing, and other factors like climate. Biome should be treated as the descriptor of the broad ecological context of a sample. Examples include: desert, taiga, deciduous woodland, or coral reef. Envo (v 2013-06-14) terms can be found via the link: www.environmentontology.org/browse-envo |
| environment (feature) | Mandatory | Environmental feature level includes geographic environmental features. Compared to biome, feature is a descriptor of the more local environment. Examples include: harbor, cliff, or lake. Envo (v 2013-06-14) terms can be found via the link: www.environmentontology.org/browse-envo |
| environment (material) | Mandatory | The environmental material level refers to the material that was displaced by the sample, or material in which a sample was embedded, prior to the sampling event. Environmental material terms are generally mass nouns. Examples include: air, soil, or water. Envo (v 2013-06-14) terms can be found via the link: www.environmentontology.org/browse-envo |
| Sampling Campaign | Mandatory | Refers to a finite or indefinite activity aiming at collecting data/samples, e.g. a cruise, a time series, a mesocosm experiment. Example: tara_20110401z. |
| Sampling Station | Mandatory | Refers to the site/station where data/sample collection is performed. Example: tara_100. |
| Sampling Platform | Mandatory | Refers to the unique stage from which the sampling device has been deployed. Includes platform category from sdn:l06, http://seadatanet.maris2.nl/v_bodc_vocab_v2/search.asp?Lib=l06, and platform name. Example: research vessel tara. |
| Marine Region | Mandatory | The geographical origin of the sample as defined by the marine region name chosen from the marine regions vocabulary at http://www.marineregions.org/. Example: aegean sea. |
| Salinity Sensor | Mandatory | Salinity of water at the time of taking the sample. Format: ##.####, Sdn:p02:75:psal, sdn:p06:46:ugkg for psu. Example: 39.2268.. Units: psu |
| Oxygen Sensor | Recommended | Oxygen concentration parameters in the water column measured in volts and converted to micromoles per kilogrammes. Format: ###.####, Sdn:p02:75:doxy, sdn:p06:46:kgum for µmol/kg. Example: 217.7895.. Units: µmol/kg |
| Nitrate Sensor | Recommended | Nitrate concentration parameters in the water column measured in volts and converted to micromoles per litres. Format: ##.####, Sdn:p02:75:ntra, sdn:p06:46:upox for µmol/l. Example: 0.2259.. Units: µmol/l |
| Temperature | Mandatory | Temperature of water at the time of taking the sample. Format: ##.####, Sdn:p02:75:temp, sdn:p06:46:upaa for °c. Example: 17.7122.. Units: ºc |
| Chlorophyll Sensor | Recommended | Fluorescence of the water measured in volts and converted to milligrammes of chlorophyll per cubic metre. Format: ##.####, Sdn:p02:75:cpwc, sdn:p06:46:ummc for mg chl/m3. Example: 0.066.. Units: mg chl/m3 |
| Citation | Recommended | Citation of the sample registry (html version) at the pangaea. Example: doi.pangaea.de/10.1594/pangaea.76752. |
| Further Details | Recommended | Reference details related to a sample in form of an uri. |
