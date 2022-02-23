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
| experimental factor | Optional | Experimental factors are essentially the variable aspects of an experiment design which can be used to describe an experiment, or set of experiments, in an increasingly detailed manner. This field accepts ontology terms from experimental factor ontology (efo) and/or ontology for biomedical investigations (obi). For a browser of efo (v 2.43) terms, please see http://purl.bioontology.org/ontology/efo; for a browser of obi (v 2013-10-25) terms please see http://purl.bioontology.org/ontology/obi |
| ploidy | Optional | The ploidy level of the genome (e.g. allopolyploid, haploid, diploid, triploid, tetraploid). It has implications for the downstream study of duplicated gene and regions of the genomes (and perhaps for difficulties in assembly). For terms, please select terms listed under class ploidy (pato:001374) of phenotypic quality ontology (pato), and for a browser of pato (v 2013-10-28) please refer to http://purl.bioontology.org/ontology/pato. Mandatory for migs of eukaryotes. |
| number of replicons | Optional | Reports the number of replicons in a nuclear genome of eukaryotes, in the genome of a bacterium or archaea or the number of segments in a segmented virus. Always applied to the haploid chromosome count of a eukaryote. Mandatory for migs of eukaryotes, bacteria, archaea and segmented virus. |
| extrachromosomal elements | Optional | Do plasmids exist of significant phenotypic consequence (e.g. ones that determine virulence or antibiotic resistance). Megaplasmids? Other plasmids (borrelia has 15+ plasmids). |
| estimated size | Optional | The estimated size of the genome (in bp) prior to sequencing. Of particular importance in the sequencing of (eukaryotic) genome which could remain in draft form for a long or unspecified period. Mandatory for migs of eukaryotes. |
| reference for biomaterial | Optional | Primary publication if isolated before genome publication; otherwise, primary genome report. Mandatory for migs of bacteria and archaea. |
| finishing strategy | Optional | Was the genome project intended to produce a complete or draft genome, coverage, the fold coverage of the sequencing expressed as 2x, 3x, 18x etc, and how many contigs were produced for the genome. Mandatory for migs of eukaryote, bacteria and archaea. |
| annotation source | Optional | For cases where annotation was provided by a community jamboree or model organism database rather than by a specific submitter |
| sample volume or weight for DNA extraction | Optional | Volume (ml) or weight (g) of sample processed for dna extraction. Units: g, ml, mg, ng |
| nucleic acid extraction | Optional | Link to a literature reference, electronic resource or a standard operating procedure (sop) |
| nucleic acid amplification | Optional | Link to a literature reference, electronic resource or a standard operating procedure (sop) |
| library size | Optional | Total number of clones in the library prepared for the project |
| library reads sequenced | Optional | Total number of clones sequenced from the library |
| library construction method | Optional | Library construction method used for clone libraries |
| library vector | Optional | Cloning vector type(s) used in construction of libraries |
| library screening strategy | Optional | Specific enrichment or screening methods applied before and/or after creating clone libraries in order to select a specific group of sequences |
| target gene | Optional | Targeted gene or locus name for marker gene studies |
| target subfragment | Optional | Name of subfragment of a gene or locus. Important to e.g. identify special regions on marker genes like v6 on 16s rrna |
| pcr primers | Optional | Pcr primers that were used to amplify the sequence of the targeted gene, locus or subfragment. This field should contain all the primers used for a single pcr reaction if multiple forward or reverse primers are present in a single pcr reaction. The primer sequence should be reported in uppercase letters |
| multiplex identifiers | Optional | Molecular barcodes, called multiplex identifiers (mids), that are used to specifically tag unique samples in a sequencing run. Sequence should be reported in uppercase letters |
| adapters | Optional | Adapters provide priming sequences for both amplification and sequencing of the sample-library fragments. Both adapters should be reported; in uppercase letters |
| pcr conditions | Optional | Description of reaction conditions and components for pcr in the form of 'initial denaturation:94degc_1.5min; annealing=...' |
| sequencing method | Mandatory | Sequencing method used; e.g. Sanger, pyrosequencing, abi-solid |
| sequence quality check | Optional | Indicate if the sequence has been called by automatic systems (none) or undergone a manual editing procedure (e.g. by inspecting the raw data or chromatograms). Applied only for sequences that are not submitted to sra or dra |
| chimera check | Optional | A chimeric sequence, or chimera for short, is a sequence comprised of two or more phylogenetically distinct parent sequences. Chimeras are usually pcr artifacts thought to occur when a prematurely terminated amplicon reanneals to a foreign dna strand and is copied to completion in the following pcr cycles. The point at which the chimeric sequence changes from one parent to the next is called the breakpoint or conversion point |
| relevant electronic resources | Optional | - |
| relevant standard operating procedures | Optional | Standard operating procedures used in assembly and/or annotation of genomes, metagenomes or environmental sequences |
| investigation type | Mandatory | Nucleic acid sequence report is the root element of all mixs compliant reports as standardised by genomic standards consortium |
| collection date | Mandatory | The date of sampling, either as an instance (single point in time) or interval. In case no exact time is available, the date/time can be right truncated i.e. all of these are valid iso8601 compliant times: 2008-01-23t19:23:10+00:00; 2008-01-23t19:23:10; 2008-01-23; 2008-01; 2008. |
| geographic location (country and/or sea) | Mandatory | The geographical origin of the sample as defined by the country or sea. Country or sea names should be chosen from the insdc country list (http://insdc.org/country.html). |
| geographic location (latitude) | Mandatory | The geographical origin of the sample as defined by latitude and longitude. The values should be reported in decimal degrees and in wgs84 system. Units: dd |
| geographic location (longitude) | Mandatory | The geographical origin of the sample as defined by latitude and longitude. The values should be reported in decimal degrees and in wgs84 system. Units: dd |
| geographic location (region and locality) | Optional | The geographical origin of the sample as defined by the specific region name followed by the locality name. |
| built environment environmental package | Mandatory | Migs/mims/mimarks extension for reporting of measurements and observations obtained from one or more of the environments where the sample was obtained. All environmental packages listed here are further defined in separate subtables. By giving the name of the environmental package, a selection of fields can be made from the subtables and can be reported |
| environment (biome) | Mandatory | Biomes are defined based on factors such as plant structures, leaf types, plant spacing, and other factors like climate. Biome should be treated as the descriptor of the broad ecological context of a sample. Examples include: desert, taiga, deciduous woodland, or coral reef. Envo (v 2013-06-14) terms can be found via the link: www.environmentontology.org/browse-envo |
| environment (feature) | Mandatory | Environmental feature level includes geographic environmental features. Compared to biome, feature is a descriptor of the more local environment. Examples include: harbor, cliff, or lake. Envo (v 2013-06-14) terms can be found via the link: www.environmentontology.org/browse-envo |
| environment (material) | Mandatory | The environmental material level refers to the material that was displaced by the sample, or material in which a sample was embedded, prior to the sampling event. Environmental material terms are generally mass nouns. Examples include: air, soil, or water. Envo (v 2013-06-14) terms can be found via the link: www.environmentontology.org/browse-envo |
| surface material | Optional | Surface materials at the point of sampling |
| surface air contaminant | Optional | Contaminant identified on surface |
| indoor surface | Optional | Type of indoor surface |
| indoor space | Mandatory | A distinguishable space within a structure, the purpose for which discrete areas of a building is used |
| filter type | Mandatory | A device which removes solid particulates or airborne molecular contaminants |
| heating and cooling system type | Mandatory | Methods of conditioning or heating a room or building |
| substructure type | Optional | The substructure or under building is that largely hidden section of the building which is built off the foundations to the ground floor level |
| light type | Mandatory | Application of light to achieve some practical or aesthetic effect. Lighting includes the use of both artificial light sources such as lamps and light fixtures, as well as natural illumination by capturing daylight. Can also include absence of light |
| building setting | Mandatory | A location (geography) where a building is set |
| building occupancy type | Mandatory | The primary function for which a building or discrete part of a building is intended to be used |
| space typical state | Mandatory | Customary or normal state of the space |
| typical occupant density | Mandatory | Customary or normal density of occupants |
| occupancy at sampling | Mandatory | Number of occupants present at time of sample within the given space |
| occupant density at sampling | Mandatory | Average number of occupants at time of sampling per square footage |
| ventilation type | Mandatory | The intentional movement of air from outside a building to the inside through forced or natural movement of air |
| source material identifiers | Optional | A unique identifier assigned to a material sample (as defined by http://rs.tdwg.org/dwc/terms/materialsampleid, and as opposed to a particular digital record of a material sample) used for extracting nucleic acids, and subsequent sequencing. The identifier can refer either to the original material collected or to any derived sub-samples. The insdc qualifiers /specimen_voucher, /bio_material, or /culture_collection may or may not share the same value as the source_mat_id field. For instance, the /specimen_voucher qualifier and source_mat_id may both contain 'uam:herps:14' , referring to both the specimen voucher and sampled tissue with the same identifier. However, the /culture_collection qualifier may refer to a value from an initial culture (e.g. Atcc:11775) while source_mat_id would refer to an identifier from some derived culture from which the nucleic acids were extracted (e.g. xatc123 or ark:/2154/r2). |
| sample collection device or method | Optional | The method or deviced employed for collecting the sample |
| sample material processing | Optional | Any processing applied to the sample during or after retrieving the sample from environment. This field accepts obi, for a browser of obi (v 2013-10-25) terms please see http://purl.bioontology.org/ontology/obi |
| isolation and growth condition | Optional | Publication reference in the form of pubmed id (pmid), digital object identifier (doi) or url for isolation and growth condition specifications of the organism/material. Mandatory for migs and mimarks specimen. |
| propagation | Optional | This field is specific to different taxa. For plants: sexual/asexual, for phages: lytic/lysogenic, for plasmids: incompatibility group (note: there is the strong opinion to name phage propagation obligately lytic or temperate, therefore we also give this choice. Mandatory for migs of eukaryotes, plasmids and viruses. |
| amount or size of sample collected | Optional | Amount or size of sample (volume, mass or area) that was collected. Units: l, g, kg, m2, m3 |
| sample size sorting method | Optional | Method by which samples are sorted |
| organism count | Mandatory | Total count of any organism per gram or volume of sample, should include name of organism followed by count; can include multiple organism counts |
| specific host | Optional | If there is a host involved, please provide its taxid (or environmental if not actually isolated from the dead or alive host - i.e. pathogen could be isolated from a swipe of a bench etc) and report whether it is a laboratory or natural host). From this we can calculate any number of groupings of hosts (e.g. animal vs plant, all fish hosts, etc) |
| health or disease status of specific host | Optional | Health or disease status of specific host at time of collection. This field accepts pato (v 2013-10-28) terms, for a browser please see http://purl.bioontology.org/ontology/pato |
| relative air humidity | Mandatory | Partial vapor and air pressure, density of the vapor and air, or by the actual mass of the vapor and air. Units: % |
| absolute air humidity | Mandatory | Actual mass of water vapor - mh20 - present in the air water vapor mixture. Units: kg |
| surface humidity | Optional | Surface water activity as a function of air and material moisture. Units: % |
| air temperature | Mandatory | Temperature of the air at time of sampling. Units: ºc |
| surface temperature | Optional | Temperature of the surface at time of sampling. Units: ºc |
| surface moisture | Optional | Water held on the surface. Units: g/m2, g/m3, parts/million |
| surface moisture pH | Optional | Ph measurement of surface |
| dew point | Optional | The temperature to which a given parcel of humid air must be cooled, at constant barometric pressure, for water vapor to condense into water. Units: ºc |
| carbon dioxide | Mandatory | Carbon dioxide (gas) amount or concentration at the time of sampling. Units: µmol/l |
| subspecific genetic lineage | Optional | This should provide further information about the genetic distinctness of this lineage by recording additional information i.e biovar, serovar, serotype, biovar, or any relevant genetic typing schemes like group i plasmid. It can also contain alternative taxonomic information |
| trophic level | Optional | Trophic levels are the feeding position in a food chain. Microbes can be a range of producers (e.g. chemolithotroph) |
| relationship to oxygen | Optional | Is this organism an aerobe, anaerobe? Please note that aerobic and anaerobic are valid descriptors for microbial environments |
| known pathogenicity | Optional | To what is the entity pathogenic, for instance plant, fungi, bacteria |
| encoded traits | Optional | Should include key traits like antibiotic resistance or xenobiotic degradation phenotypes for plasmids, converting genes for phage |
| observed biotic relationship | Optional | Is it free-living or in a host and if the latter what type of relationship is observed |
| perturbation | Optional | Type of perturbation, e.g. chemical administration, physical disturbance, etc., coupled with time that perturbation occurred; can include multiple perturbation types |
