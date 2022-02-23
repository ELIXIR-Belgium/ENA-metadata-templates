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
| geographic location (altitude) | Optional | The altitude of the sample is the vertical distance between earth's surface above sea level and the sampled position in the air.. Units: m |
| geographic location (country and/or sea) | Mandatory | The geographical origin of the sample as defined by the country or sea. Country or sea names should be chosen from the insdc country list (http://insdc.org/country.html). |
| geographic location (latitude) | Mandatory | The geographical origin of the sample as defined by latitude and longitude. The values should be reported in decimal degrees and in wgs84 system. Units: dd |
| geographic location (longitude) | Mandatory | The geographical origin of the sample as defined by latitude and longitude. The values should be reported in decimal degrees and in wgs84 system. Units: dd |
| geographic location (region and locality) | Optional | The geographical origin of the sample as defined by the specific region name followed by the locality name. |
| host-associated environmental package | Mandatory | Migs/mims/mimarks extension for reporting of measurements and observations obtained from one or more of the environments where the sample was obtained. All environmental packages listed here are further defined in separate subtables. By giving the name of the environmental package, a selection of fields can be made from the subtables and can be reported |
| geographic location (depth) | Optional | Depth is defined as the vertical distance below surface, e.g. for sediment or soil samples depth is measured from sediment or soil surface, respectivly. Depth can be reported as an interval for subsurface samples.. Units: m |
| environment (biome) | Mandatory | Biomes are defined based on factors such as plant structures, leaf types, plant spacing, and other factors like climate. Biome should be treated as the descriptor of the broad ecological context of a sample. Examples include: desert, taiga, deciduous woodland, or coral reef. Envo (v 2013-06-14) terms can be found via the link: www.environmentontology.org/browse-envo |
| environment (feature) | Mandatory | Environmental feature level includes geographic environmental features. Compared to biome, feature is a descriptor of the more local environment. Examples include: harbor, cliff, or lake. Envo (v 2013-06-14) terms can be found via the link: www.environmentontology.org/browse-envo |
| environment (material) | Mandatory | The environmental material level refers to the material that was displaced by the sample, or material in which a sample was embedded, prior to the sampling event. Environmental material terms are generally mass nouns. Examples include: air, soil, or water. Envo (v 2013-06-14) terms can be found via the link: www.environmentontology.org/browse-envo |
| geographic location (elevation) | Optional | The elevation of the sampling site as measured by the vertical distance from mean sea level.. Units: m |
| source material identifiers | Optional | A unique identifier assigned to a material sample (as defined by http://rs.tdwg.org/dwc/terms/materialsampleid, and as opposed to a particular digital record of a material sample) used for extracting nucleic acids, and subsequent sequencing. The identifier can refer either to the original material collected or to any derived sub-samples. The insdc qualifiers /specimen_voucher, /bio_material, or /culture_collection may or may not share the same value as the source_mat_id field. For instance, the /specimen_voucher qualifier and source_mat_id may both contain 'uam:herps:14' , referring to both the specimen voucher and sampled tissue with the same identifier. However, the /culture_collection qualifier may refer to a value from an initial culture (e.g. Atcc:11775) while source_mat_id would refer to an identifier from some derived culture from which the nucleic acids were extracted (e.g. xatc123 or ark:/2154/r2). |
| sample collection device or method | Optional | The method or deviced employed for collecting the sample |
| sample material processing | Optional | Any processing applied to the sample during or after retrieving the sample from environment. This field accepts obi, for a browser of obi (v 2013-10-25) terms please see http://purl.bioontology.org/ontology/obi |
| isolation and growth condition | Optional | Publication reference in the form of pubmed id (pmid), digital object identifier (doi) or url for isolation and growth condition specifications of the organism/material. Mandatory for migs and mimarks specimen. |
| propagation | Optional | This field is specific to different taxa. For plants: sexual/asexual, for phages: lytic/lysogenic, for plasmids: incompatibility group (note: there is the strong opinion to name phage propagation obligately lytic or temperate, therefore we also give this choice. Mandatory for migs of eukaryotes, plasmids and viruses. |
| amount or size of sample collected | Optional | Amount or size of sample (volume, mass or area) that was collected. Units: l, g, kg, m2, m3 |
| host body product | Optional | Substance produced by the body, e.g. stool, mucus, where the sample was obtained from. For foundational model of anatomy ontology (fma) (v 3.1) terms, please see http://purl.bioontology.org/ontology/fma |
| host dry mass | Optional | Measurement of dry mass. Units: g, kg, mg |
| oxygenation status of sample | Optional | Oxygenation status of sample |
| organism count | Optional | Total count of any organism per gram or volume of sample, should include name of organism followed by count; can include multiple organism counts |
| sample storage duration | Optional | Duration for which sample was stored. Units: days, hours, months, weeks, years |
| sample storage temperature | Optional | Temperature at which sample was stored, e.g. -80. Units: °c |
| sample storage location | Optional | Location at which sample was stored, usually name of a specific freezer/room |
| host disease status | Optional | List of diseases with which the host has been diagnosed; can include multiple diagnoses. The value of the field depends on host; for humans the terms should be chosen from do (disease ontology) at http://www.disease-ontology.org, other hosts are free text |
| host common name | Optional | Common name of the host, e.g. human |
| host subject id | Optional | A unique identifier by which each subject can be referred to, de-identified, e.g. #131 |
| host age | Optional | Age of host at the time of sampling; relevant scale depends on species and study, e.g. could be seconds for amoebae or centuries for trees. Units: centuries, days, decades, hours, minutes, months, seconds, weeks, years |
| host taxid | Optional | Ncbi taxon id of the host, e.g. 9606 |
| host body habitat | Optional | Original body habitat where the sample was obtained from |
| host body site | Optional | Name of body site where the sample was obtained from, such as a specific organ or tissue (tongue, lung etc...). For foundational model of anatomy ontology (fma) (v 3.1) terms, please see http://purl.bioontology.org/ontology/fma |
| host life stage | Optional | Description of life stage of host |
| host height | Optional | The height of subject. Units: cm, m, mm |
| host length | Optional | The length of subject. Units: cm, m, mm |
| host growth conditions | Optional | Literature reference giving growth conditions of the host |
| host substrate | Optional | The growth substrate of the host |
| host total mass | Optional | Total mass of the host at collection, the unit depends on host. Units: g, kg |
| host infra-specific name | Optional | Taxonomic information about the host below subspecies level |
| host infra-specific rank | Optional | Taxonomic rank information about the host below subspecies level, such as variety, form, rank etc. |
| host phenotype | Optional | Phenotype of host. For phenotypic quality ontology (pato) (v 2013-10-28) terms, please see http://purl.bioontology.org/ontology/pato |
| host body temperature | Optional | Core body temperature of the host when sample was collected. Units: ºc |
| host color | Optional | The color of host |
| host shape | Optional | Morphological shape of host |
| host sex | Optional | Gender or sex of the host. |
| temperature | Optional | Temperature of the sample at time of sampling. Units: ºc |
| sample salinity | Optional | Salinity of sample, i.e. measure of total salt concentration. Units: psu |
| miscellaneous parameter | Optional | Any other measurement performed or parameter collected, that is not listed here |
| host blood pressure diastolic | Optional | Resting diastolic blood pressure, measured as mm mercury. Units: mm hg |
| host blood pressure systolic | Optional | Resting systolic blood pressure, measured as mm mercury. Units: mm hg |
| host diet | Optional | Type of diet depending on the host, for animals omnivore, herbivore etc., for humans high-fat, mediterranean etc.; can include multiple diet types |
| host last meal | Optional | Content of last meal and time since feeding; can include multiple values |
| host family relationship | Optional | Relationships to other hosts in the same study; can include multiple relationships |
| host genotype | Optional | Observed genotype |
| gravidity | Optional | Whether or not the subject is gravid. If so, report date due or date post-conception and specify which of these two dates is being reported. |
| subspecific genetic lineage | Optional | This should provide further information about the genetic distinctness of this lineage by recording additional information i.e biovar, serovar, serotype, biovar, or any relevant genetic typing schemes like group i plasmid. It can also contain alternative taxonomic information |
| trophic level | Optional | Trophic levels are the feeding position in a food chain. Microbes can be a range of producers (e.g. chemolithotroph) |
| relationship to oxygen | Optional | Is this organism an aerobe, anaerobe? Please note that aerobic and anaerobic are valid descriptors for microbial environments |
| known pathogenicity | Optional | To what is the entity pathogenic, for instance plant, fungi, bacteria |
| encoded traits | Optional | Should include key traits like antibiotic resistance or xenobiotic degradation phenotypes for plasmids, converting genes for phage |
| observed biotic relationship | Optional | Is it free-living or in a host and if the latter what type of relationship is observed |
| chemical administration | Optional | List of chemical compounds administered to the host or site where sampling occurred, and when (e.g. antibiotics, n fertilizer, air filter); can include multiple compounds. For chemical entities of biological interest ontology (chebi) (v111), please see http://purl.bioontology.org/ontology/chebi |
| perturbation | Optional | Type of perturbation, e.g. chemical administration, physical disturbance, etc., coupled with time that perturbation occurred; can include multiple perturbation types |
