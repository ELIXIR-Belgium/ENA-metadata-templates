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
| reference for biomaterial | Optional | Primary publication if isolated before genome publication; otherwise, primary genome report. Mandatory for migs of bacteria and archaea. |
| annotation source | Optional | For cases where annotation was provided by a community jamboree or model organism database rather than by a specific submitter |
| nucleic acid extraction | Optional | Link to a literature reference, electronic resource or a standard operating procedure (sop) |
| nucleic acid amplification | Optional | Link to a literature reference, electronic resource or a standard operating procedure (sop) |
| library size | Optional | Total number of clones in the library prepared for the project |
| library reads sequenced | Optional | Total number of clones sequenced from the library |
| library vector | Optional | Cloning vector type(s) used in construction of libraries |
| library screening strategy | Optional | Specific enrichment or screening methods applied before and/or after creating clone libraries in order to select a specific group of sequences |
| multiplex identifiers | Optional | Molecular barcodes, called multiplex identifiers (mids), that are used to specifically tag unique samples in a sequencing run. Sequence should be reported in uppercase letters |
| adapters | Optional | Adapters provide priming sequences for both amplification and sequencing of the sample-library fragments. Both adapters should be reported; in uppercase letters |
| sequencing method | Mandatory | Sequencing method used; e.g. Sanger, pyrosequencing, abi-solid |
| relevant electronic resources | Optional | - |
| relevant standard operating procedures | Optional | Standard operating procedures used in assembly and/or annotation of genomes, metagenomes or environmental sequences |
| number of standard tRNAs extracted | Optional | The total number of trnas identified from the bin, sag or mag |
| assembly software | Mandatory | Tool(s) used for assembly, including version number and parameters in the format {software};{version};{parameters} e.g. metaspades;3.11.0;kmer set 21,33,55,77,99,121, default parameters otherwise |
| feature prediction | Optional | Method used to predict uvigs features such as orfs, integration site, etc. Add names and versions of software(s), parameters used |
| reference database(s) | Optional | List of database(s) used for orf annotation, along with version number and reference to website or publication |
| similarity search method | Optional | Tool used to compare orfs with database, along with version and cutoffs used. Add names and versions of software(s), parameters used |
| 16S recovered | Optional | Can a 16s gene be recovered from the submitted bin, sag or mag? |
| 16S recovery software | Optional | Tools used for 16s rrna gene extraction. Add names and versions of software(s), parameters used |
| tRNA extraction software | Optional | Tools used for trna identification. Add names and versions of software(s), parameters used |
| completeness score | Mandatory | Completeness score is typically based on either the fraction of markers found as compared to a database or the percent of a genome found as compared to a closely related reference genome. Completeness score is one of 3 attributes which in combination reflect the standard quality of a mag, see here for more information: https://ena-docs.readthedocs.io/en/latest/faq_metagenomes.html.. Units: % |
| completeness software | Mandatory | Tools used for completion estimate, i.e. checkm, anvi'o, busco |
| completeness approach | Optional | The approach used to determine the completeness of a given bin, sag or mag, which would typically make use of a set of conserved marker genes or a closely related reference genome. For uvig completeness, include reference genome or group used, and contig feature suggesting a complete genome |
| contamination score | Mandatory | The contamination score is based on the fraction of single-copy genes that are observed more than once in a query genome. Contamination score is one of 3 attributes which in combination reflect the standard quality of a mag, see here for more information: https://ena-docs.readthedocs.io/en/latest/faq_metagenomes.html. If contamination ≥ 10% then please submit as a binned assembly.. Units: % |
| contamination screening input | Optional | The type of sequence data used as input |
| contamination screening parameters | Optional | Specific parameters used in the decontamination sofware, such as reference database, coverage, and kmers. Combinations of these parameters may also be used, i.e. kmer and coverage, or reference database and kmer |
| decontamination software | Optional | Tool(s) used in contamination screening |
| binning software | Mandatory | Tool(s) used for the extraction of genomes from metagenomic datasets e.g. concoct and maxbin |
| reassembly post binning | Optional | Has an assembly been performed on a genome bin extracted from a metagenomic assembly?. Units: no, yes |
| MAG coverage software | Optional | Tool(s) used to determine the genome coverage if coverage is used as a binning parameter in the extraction of genomes from metagenomic datasets e.g. bwa, bbmap, bowtie, other |
| assembly quality | Mandatory | Assembly quality is one of 3 attributes which in combination reflect the standard quality of a mag, see here for more information: https://ena-docs.readthedocs.io/en/latest/faq_metagenomes.html. Assembly statistics include, but are not limited to total assembly size, number of contigs, contig n50/l50, and maximum contig length. |
| investigation type | Mandatory | Nucleic acid sequence report is the root element of all mixs compliant reports as standardised by genomic standards consortium |
| binning parameters | Mandatory | The parameters that have been applied during the extraction of genomes from metagenomic datasets e.g. coverage and kmer |
| taxonomic identity marker | Mandatory | The phylogenetic marker(s) used to assign an organism name to the bin, sag or mag. Examples are 16s gene, multi-marker approach or other e.g. rpob gene |
| taxonomic classification | Optional | Method used for taxonomic classification, along with reference database used, classification rank, and thresholds used to classify new genomes. Expected values are: classification method, database name, and other parameters e.g. vcontact vcontact2 (references from ncbi refseq v83, genus rank classification, default parameters) |
| isolation_source | Mandatory | Describes the physical, environmental and/or local geographical source of the biological sample from which the sample was derived |
| collection date | Mandatory | The date of sampling, either as an instance (single point in time) or interval. In case no exact time is available, the date/time can be right truncated i.e. all of these are valid iso8601 compliant times: 2008-01-23t19:23:10+00:00; 2008-01-23t19:23:10; 2008-01-23; 2008-01; 2008. |
| geographic location (altitude) | Optional | The altitude of the sample is the vertical distance between earth's surface above sea level and the sampled position in the air.. Units: m |
| geographic location (country and/or sea) | Mandatory | The geographical origin of the sample as defined by the country or sea. Country or sea names should be chosen from the insdc country list (http://insdc.org/country.html). |
| geographic location (latitude) | Mandatory | The geographical origin of the sample as defined by latitude and longitude. The values should be reported in decimal degrees and in wgs84 system. Units: dd |
| geographic location (longitude) | Mandatory | The geographical origin of the sample as defined by latitude and longitude. The values should be reported in decimal degrees and in wgs84 system. Units: dd |
| geographic location (region and locality) | Optional | The geographical origin of the sample as defined by the specific region name followed by the locality name. |
| geographic location (depth) | Optional | Depth is defined as the vertical distance below surface, e.g. for sediment or soil samples depth is measured from sediment or soil surface, respectivly. Depth can be reported as an interval for subsurface samples.. Units: m |
| environment (biome) | Mandatory | Biomes are defined based on factors such as plant structures, leaf types, plant spacing, and other factors like climate. Biome should be treated as the descriptor of the broad ecological context of a sample. Examples include: desert, taiga, deciduous woodland, or coral reef. Envo (v 2013-06-14) terms can be found via the link: www.environmentontology.org/browse-envo |
| environment (feature) | Mandatory | Environmental feature level includes geographic environmental features. Compared to biome, feature is a descriptor of the more local environment. Examples include: harbor, cliff, or lake. Envo (v 2013-06-14) terms can be found via the link: www.environmentontology.org/browse-envo |
| environment (material) | Mandatory | The environmental material level refers to the material that was displaced by the sample, or material in which a sample was embedded, prior to the sampling event. Environmental material terms are generally mass nouns. Examples include: air, soil, or water. Envo (v 2013-06-14) terms can be found via the link: www.environmentontology.org/browse-envo |
| geographic location (elevation) | Optional | The elevation of the sampling site as measured by the vertical distance from mean sea level.. Units: m |
| source material identifiers | Optional | A unique identifier assigned to a material sample (as defined by http://rs.tdwg.org/dwc/terms/materialsampleid, and as opposed to a particular digital record of a material sample) used for extracting nucleic acids, and subsequent sequencing. The identifier can refer either to the original material collected or to any derived sub-samples. The insdc qualifiers /specimen_voucher, /bio_material, or /culture_collection may or may not share the same value as the source_mat_id field. For instance, the /specimen_voucher qualifier and source_mat_id may both contain 'uam:herps:14' , referring to both the specimen voucher and sampled tissue with the same identifier. However, the /culture_collection qualifier may refer to a value from an initial culture (e.g. Atcc:11775) while source_mat_id would refer to an identifier from some derived culture from which the nucleic acids were extracted (e.g. xatc123 or ark:/2154/r2). |
| sample collection device or method | Optional | The method or deviced employed for collecting the sample |
| sample material processing | Optional | Any processing applied to the sample during or after retrieving the sample from environment. This field accepts obi, for a browser of obi (v 2013-10-25) terms please see http://purl.bioontology.org/ontology/obi |
| amount or size of sample collected | Optional | Amount or size of sample (volume, mass or area) that was collected. Units: l, g, kg, m2, m3 |
| size fraction selected | Optional | Filtering pore size used in sample preparation e.g. 0-0.22 micrometer |
| sample derived from | Mandatory | Reference to parental sample(s) or original run(s) that the assembly is derived from. The referenced samples or runs should already be registered in insdc. This should be formatted as one of the following. A single sample/run e.g. Ersxxxxxx or a comma separated list e.g. Ersxxxxxx,ersxxxxxx or a range e.g. Ersxxxxxx-ersxxxxxx |
| metagenomic source | Mandatory | The metagenomic source of the sample. This value should contain "metagenome" and be in the taxonomy database e.g. wastewater metagenome or human gut metagenome. Please note "metagenome" alone will not be accepted. Check here for more details on metagenome taxonomy: https://ena-docs.readthedocs.io/en/latest/faq_taxonomy.html#environmental-taxonomic-classifications |
| relationship to oxygen | Optional | Is this organism an aerobe, anaerobe? Please note that aerobic and anaerobic are valid descriptors for microbial environments |
