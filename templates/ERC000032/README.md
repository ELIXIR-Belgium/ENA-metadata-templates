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
| number of inoculated individuals | Optional | Number of host individuals inoculated for the experiment. |
| inoculation route | Optional | Brief description of the protocol inoculation route. |
| inoculation dose | Optional | Dose used for the inoculoation experiment. |
| inoculation stock availability | Optional | Is the virus stock used for the inoculation available? |
| subject exposure | Optional | Exposure of the subject to infected human or animals, such as poultry, wild bird or swine. If multiple exposures are applicable, please state them separated by semicolon. Example: poultry; wild bird |
| subject exposure duration | Optional | Duration of the exposure of the subject to an infected human or animal. If multiple exposures are applicable, please state their duration in the same order in which you reported the exposure in the field 'subject exposure'. Example: 1 day; 0.33 days |
| type exposure | Optional | Setting within which the subject is exposed to animals, such as farm, slaughterhouse, food preparation. If multiple exposures are applicable, please state their type in the same order in which you reported the exposure in the field 'subject exposure'. Example: backyard flock; confined animal feeding operation |
| personal protective equipment | Optional | Use of personal protective equipment, such as gloves, gowns, during any type of exposure. Example: mask |
| hospitalisation | Optional | Was the subject confined to a hospital as a result of virus infection or problems occurring secondary to virus infection? |
| antiviral treatment | Optional | Antiviral treatment used for this subject, such as zanamavir oseltamivir, amantadine. Example: rimantadine |
| antiviral treatment initiation | Optional | Initiation of antiviral treatment after onset of clinical symptoms in days. Example: 2.5 |
| antiviral treatment dosage | Optional | Dosage of the treatment taken by the subject. Example: 0.05 mg |
| antiviral treatment duration | Optional | Duration of antiviral treatment after onset of clinical symptoms in days.example: 5 |
| influenza vaccination type | Optional | Influenza vaccinations that have been administered to the subject over the last year. Example: 2009 h1n1 flumist |
| influenza vaccination date | Optional | Date that the influenza vaccination was administered to the subject over the past year. Format: yyyy-mm-dd. Example: 2007-05-12 |
| source of vaccination information | Optional | Designation of information related to vaccination history as self reported or documented. |
| vaccine lot number | Optional | Lot number of the vaccine. |
| vaccine manufacturer | Optional | Manufacturer of the vaccine. |
| vaccine dosage | Optional | Dosage of the vaccine taken by the subject. Example: 0.05 ml |
| influenza-like illness at the time of sample collection | Optional | Is the subject at the time of sample collection considered to have influenza like illness? |
| illness onset date | Optional | Date the subject showed an onset of symptoms. Format: yyyy-mm-dd. Example: 2011-10-20 |
| illness duration | Optional | The number of days the illness lasted. Example: 4 |
| illness symptoms | Optional | The symptoms that have been reported in relation to the illness, such as cough, diarrhea, fever, headache, malaise, myalgia, nausea, runny_nose, shortness_of_breath, sore_throat. If multiple exposures are applicable, please state them separated by semicolon. |
| collection date | Recommended | The date of sampling, either as an instance (single point in time) or interval. In case no exact time is available, the date/time can be right truncated i.e. all of these are valid iso8601 compliant times: 2008-01-23t19:23:10+00:00; 2008-01-23t19:23:10; 2008-01-23; 2008-01; 2008. |
| geographic location (country and/or sea) | Mandatory | The geographical origin of the sample as defined by the country or sea. Country or sea names should be chosen from the insdc country list (http://insdc.org/country.html). |
| geographic location (latitude) | Recommended | The geographical origin of the sample as defined by latitude and longitude. The values should be reported in decimal degrees and in wgs84 system. Units: dd |
| geographic location (longitude) | Recommended | The geographical origin of the sample as defined by latitude and longitude. The values should be reported in decimal degrees and in wgs84 system. Units: dd |
| geographic location (region and locality) | Recommended | The geographical origin of the sample as defined by the specific region name followed by the locality name. |
| sample capture status | Recommended | Reason for the sample collection. |
| host disease outcome | Recommended | Disease outcome in the host. |
| host common name | Mandatory | Common name of the host, e.g. human |
| host subject id | Mandatory | A unique identifier by which each subject can be referred to, de-identified, e.g. #131 |
| host age | Recommended | Age of host at the time of sampling; relevant scale depends on species and study, e.g. could be seconds for amoebae or centuries for trees. Units: centuries, days, decades, hours, minutes, months, seconds, weeks, years |
| host health state | Mandatory | Health status of the host at the time of sample collection. |
| host sex | Mandatory | Gender or sex of the host. |
| host scientific name | Mandatory | Scientific name of the natural (as opposed to laboratory) host to the organism from which sample was obtained. |
| influenza test method | Mandatory | Method by which the current assessment of a sample as flu positive/negative is made. If multiple test were performed, please state them separated by semicolon. Example: rt-pcr; antigen elisa |
| influenza test result | Mandatory | Classification of a sample as flu positive or negative based on the test performed and reported. If multiple tests were performed, please state the results in the same order in which you reported the tests in the field 'influenza test method'. Format: p(ositive)/n(egative). Example: p; p |
| other pathogens tested | Mandatory | Classification of pathogenic organisms other than influenza virus tested in the current assessment of a sample. If multiple tests were performed, please state them separated by semicolon. If no other pathogens test was performed, please state 'none'. Example: newcastle |
| other pathogens test result | Mandatory | Classification of a sample as positive or negative based on the test performed and reported. If tests for multiple pathogenic organisms were performed, please state the results in the same order in which you reported the tests in the field 'other pathogens tested'. Format: p(ositive)/n(egative)/not applicable. Example: n |
| influenza virus type | Recommended | One of the three influenza virus classification types. |
| virus identifier | Recommended | Unique laboratory identifier assigned to the virus by the investigator. Strain name is not sufficient since it might not be unique due to various passsages of the same virus. Format: up to 50 alphanumeric characters |
| influenza strain unique number | Optional | Unique number of the strain which is reported as a part of the influenza strain name, such as a/chicken/fujian/411/2002(hxn1). Format: integer number, example: 411 |
| WHO/OIE/FAO clade (required for HPAI H5N1 viruses) | Optional | Who/oie/fao clade should be included for highly pathogenic h5n1 viruses. Example: 2.2 |
| lineage:swl (required for H1N1 viruses) | Optional | Does the h1n1 influenza virus originate from a swine-like outbreak (as opposed to a seasonal flu)? |
| collector name | Mandatory | Name of the person who collected the specimen. Example: john smith |
| collecting institution | Mandatory | Name of the institution to which the person collecting the specimen belongs. Format: institute name, institute address |
| receipt date | Recommended | Date on which the sample was received. Format:yyyy-mm-dd. Please provide the highest precision possible. If the sample was received by the institution and not collected, the 'receipt date' must be provided instead. Either the 'collection date' or 'receipt date' must be provided. If available, provide both dates. |
| sample storage conditions | Optional | Conditions at which sample was stored, usually storage temperature, duration and location |
| definition for seropositive sample | Recommended | The cut off value used by an investigatior in determining that a sample was seropositive. |
| meaning of cut off value | Optional | Description helping to explain what the cut off value means. |
| serotype (required for a seropositive sample) | Recommended | Serological variety of a species characterised by its antigenic properties. For influenza, ha subtype should be the letter h followed by a number between 1-16 unless novel subtype is identified and the na subtype should be the letter n followed by a number between 1-9 unless novel subtype is identified. If only one of the subtypes have been tested then use the format h5nx or hxn1. Example: h1n1 |
| strain | Optional | Name of the strain from which the sample was obtained. |
| host habitat | Recommended | Natural habitat of the avian or mammalian host. |
| isolation source host-associated | Recommended | Name of host tissue or organ sampled for analysis. Example: tracheal tissue |
| host description | Optional | Other descriptive information relating to the host. |
| gravidity | Optional | Whether or not the subject is gravid. If so, report date due or date post-conception and specify which of these two dates is being reported. |
| host behaviour | Recommended | Natural behaviour of the host. |
| isolation source non-host-associated | Recommended | Describes the physical, environmental and/or local geographical source of the biological sample from which the sample was derived. Example: soil |
