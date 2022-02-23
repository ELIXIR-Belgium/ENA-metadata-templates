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
| ploidy | Recommended | The ploidy level of the genome (e.g. allopolyploid, haploid, diploid, triploid, tetraploid). It has implications for the downstream study of duplicated gene and regions of the genomes (and perhaps for difficulties in assembly). For terms, please select terms listed under class ploidy (pato:001374) of phenotypic quality ontology (pato), and for a browser of pato (v 2013-10-28) please refer to http://purl.bioontology.org/ontology/pato. Mandatory for migs of eukaryotes. |
| number of replicons | Recommended | Reports the number of replicons in a nuclear genome of eukaryotes, in the genome of a bacterium or archaea or the number of segments in a segmented virus. Always applied to the haploid chromosome count of a eukaryote. Mandatory for migs of eukaryotes, bacteria, archaea and segmented virus. |
| extrachromosomal elements | Optional | Do plasmids exist of significant phenotypic consequence (e.g. ones that determine virulence or antibiotic resistance). Megaplasmids? Other plasmids (borrelia has 15+ plasmids). |
| estimated size | Recommended | The estimated size of the genome (in bp) prior to sequencing. Of particular importance in the sequencing of (eukaryotic) genome which could remain in draft form for a long or unspecified period. Mandatory for migs of eukaryotes. |
| sample volume or weight for DNA extraction | Optional | Volume (ml) or weight (g) of sample processed for dna extraction. Units: g, ml, mg, ng |
| collected_by | Optional | Name of persons or institute who collected the specimen |
| collection date | Mandatory | The date of sampling, either as an instance (single point in time) or interval. In case no exact time is available, the date/time can be right truncated i.e. all of these are valid iso8601 compliant times: 2008-01-23t19:23:10+00:00; 2008-01-23t19:23:10; 2008-01-23; 2008-01; 2008. |
| geographic location (altitude) | Optional | The altitude of the sample is the vertical distance between earth's surface above sea level and the sampled position in the air.. Units: m |
| geographic location (country and/or sea) | Mandatory | The geographical origin of the sample as defined by the country or sea. Country or sea names should be chosen from the insdc country list (http://insdc.org/country.html). |
| geographic location (latitude) | Mandatory | The geographical origin of the sample as defined by latitude and longitude. The values should be reported in decimal degrees and in wgs84 system. Units: dd |
| geographic location (longitude) | Mandatory | The geographical origin of the sample as defined by latitude and longitude. The values should be reported in decimal degrees and in wgs84 system. Units: dd |
| geographic location (region and locality) | Optional | The geographical origin of the sample as defined by the specific region name followed by the locality name. |
| identified_by | Optional | Name of the expert who identified the specimen taxonomically |
| geographic location (depth) | Optional | Depth is defined as the vertical distance below surface, e.g. for sediment or soil samples depth is measured from sediment or soil surface, respectivly. Depth can be reported as an interval for subsurface samples.. Units: m |
| environment (biome) | Optional | Biomes are defined based on factors such as plant structures, leaf types, plant spacing, and other factors like climate. Biome should be treated as the descriptor of the broad ecological context of a sample. Examples include: desert, taiga, deciduous woodland, or coral reef. Envo (v 2013-06-14) terms can be found via the link: www.environmentontology.org/browse-envo |
| environment (feature) | Optional | Environmental feature level includes geographic environmental features. Compared to biome, feature is a descriptor of the more local environment. Examples include: harbor, cliff, or lake. Envo (v 2013-06-14) terms can be found via the link: www.environmentontology.org/browse-envo |
| geographic location (elevation) | Optional | The elevation of the sampling site as measured by the vertical distance from mean sea level.. Units: m |
| source material identifiers | Recommended | A unique identifier assigned to a material sample (as defined by http://rs.tdwg.org/dwc/terms/materialsampleid, and as opposed to a particular digital record of a material sample) used for extracting nucleic acids, and subsequent sequencing. The identifier can refer either to the original material collected or to any derived sub-samples. The insdc qualifiers /specimen_voucher, /bio_material, or /culture_collection may or may not share the same value as the source_mat_id field. For instance, the /specimen_voucher qualifier and source_mat_id may both contain 'uam:herps:14' , referring to both the specimen voucher and sampled tissue with the same identifier. However, the /culture_collection qualifier may refer to a value from an initial culture (e.g. Atcc:11775) while source_mat_id would refer to an identifier from some derived culture from which the nucleic acids were extracted (e.g. xatc123 or ark:/2154/r2). |
| sample collection device or method | Optional | The method or deviced employed for collecting the sample |
| sample material processing | Optional | Any processing applied to the sample during or after retrieving the sample from environment. This field accepts obi, for a browser of obi (v 2013-10-25) terms please see http://purl.bioontology.org/ontology/obi |
| isolation and growth condition | Mandatory | Publication reference in the form of pubmed id (pmid), digital object identifier (doi) or url for isolation and growth condition specifications of the organism/material. Mandatory for migs and mimarks specimen. |
| propagation | Recommended | This field is specific to different taxa. For plants: sexual/asexual, for phages: lytic/lysogenic, for plasmids: incompatibility group (note: there is the strong opinion to name phage propagation obligately lytic or temperate, therefore we also give this choice. Mandatory for migs of eukaryotes, plasmids and viruses. |
| amount or size of sample collected | Optional | Amount or size of sample (volume, mass or area) that was collected. Units: l, g, kg, m2, m3 |
| sample storage duration | Optional | Duration for which sample was stored. Units: days, hours, months, weeks, years |
| sample storage temperature | Optional | Temperature at which sample was stored, e.g. -80. Units: °c |
| sample storage location | Optional | Location at which sample was stored, usually name of a specific freezer/room |
| sampling time point | Optional | NA |
| plant structure | Mandatory | Name of plant structure that the sample was obtained from; for plant ontology (po) terms see http://purl.bioontology.org/ontology/po, e.g. petiole epidermis (po_0000051); if an individual flower is sampled the sex of it can be recorded here |
| plant developmental stage | Mandatory | Developmental stage at the time of sample collection; for plant ontology (po) (v 20) terms, see http://purl.bioontology.org/ontology/po, e.g. hypocotyl emergence stage (po_0007043) |
| sampled age | Optional | Age of subject at the time of sample collection; relevant scale depends on species and study; e.g. 2 weeks old |
| sample phenotype | Optional | Phenotype of the plant from which the sample was obtained, such as colour of corolla, fruit diameter, circular leaf shape; plant trait ontology (to), phenotypic quality ontology (pato), or other ontology is recommended; e.g. stem epidermis colour (to:1000018) |
| sample health state | Recommended | Health status of the subject at the time of sample collection |
| sample disease status | Recommended | List of diseases with which the subject has been diagnosed at the time of sample collection; can include multiple diagnoses; the value of the field depends on subject; e.g. Charcoal rot (macrophomina phaseolina), late wilt (cephalosporium maydis) |
| sample disease stage | Optional | Stage of the disease at the time of sample collection, e.g. inoculation, penetration, infection, growth and reproduction, dissemination of pathogen |
| sample wet mass | Optional | Measurement of wet mass at the time of sample collection; e.g. 0.23 g |
| sample dry mass | Optional | Measurement of dry mass at the time of sample collection; e.g. 0.05g |
| sample height | Optional | Height of subject at the time of sampling, if different from the length; e.g. 0.75m |
| sample length | Optional | Length of subject at the time of sampling, if different from the height; e.g. 2m |
| growth facility | Recommended | Type of facility where the sampled plant was grown |
| sample capture status | Optional | Reason for the sample collection. |
| genotype | Optional | Name or code for genotype of organism |
| genetic modification | Optional | A genetic modification of the genome of an organism which may occur naturally by spontaneous mutation, or be introduced by some experimental means. Examples of genetic modification include specification of a transgene or the gene knocked-out or details of transient transfection. |
| organism common name | Recommended | Common name of the subject organism, e.g. maize |
| subspecific genetic lineage rank | Recommended | Further information about the genetic distinctness of this lineage by recording additional information i.e. variety, cultivar, ecotype, inbred line,; it can also contain alternative taxonomic information |
| subspecific genetic lineage name | Recommended | Name of the infraspecific rank, e.g ecotype col-0 |
| biological status | Optional | The level of genome modification; controlled vocabulary: wild, natural, semi-natural, inbred line, breeder's line, hybrid, clonal selection, mutant |
| organism phenotype | Optional | Most relevant phenotypic traits of the subject; for phenotypic quality ontology (pato) (v 2013-10-28) terms, please see http://purl.bioontology.org/ontology/pato, e.g. bifurcated (pato_0001784); terms from trait ontology (to), plant ontology (po) or crop ontology (co) are also accepted; include name/method/scale for each trait; can include multiple traits |
| ancestral data | Optional | Information about either pedigree or other description of ancestral information (e.g. parental variety in case of mutant or selection), e.g. A/3*b (meaning [(a x b) x b] x b) |
| source material description | Optional | Further information to clarify the nature of the specimen or population used that is not collected elsewhere, e.g. if source was derived from accessioned stock, describe how it links to the original material |
| biotic relationship | Optional | Free text description of relationship(s) between the subject organism and other organism(s) it is associate with, e.g., parasite on species x; mutualist with species y, the target organism is the subject of the relationship, and the other organism(s) is the object |
| growth habit | Optional | Characteristic shape, appearance or growth form of a plant species |
| plant sex | Optional | Sex of the reproductive parts on the whole plant, e.g. pistilate, staminate, monoecieous, hermaphrodite |
| climate environment | Optional | Treatment involving an exposure to a particular climate; can include multiple climates |
| gaseous environment | Optional | Use of conditions with differing gaseous environments; should include the name of gaseous compound, amount administered, treatment duration, interval and total experimental duration; can include multiple gaseous environment regimens |
| seasonal environment | Optional | Treatment involving an exposure to a particular season (e.g. winter, summer, rabi, rainy etc.) |
| soil_taxonomic/FAO classification | Recommended | Soil classification from the fao world reference database for soil resources |
| soil_taxonomic/local classification | Optional | Soil classification based on local soil classification system |
| soil_taxonomic/local classification method | Optional | Reference or method used in determining the local soil classification |
| soil type | Optional | Soil series name or other lower-level classification |
| soil type method | Optional | Reference or method used in determining soil series name or other lower-level classification |
| drainage classification | Optional | Drainage classification from a standard system such as the usda system |
| texture | Optional | The relative proportion of different grain sizes of mineral particles in a soil, as described using a standard system; express as % sand (50 um to 2 mm), silt (2 um to 50 um), and clay (<2 um) with textural name (e.g., silty clay loam) optional.. Units: % sand/silt/clay |
| texture method | Optional | Reference or method used in determining soil texture |
| soil water content | Optional | Water content measurement; e.g. 13.6% |
| soil pH | Recommended | Ph measurement of the soil; e.g. 6.2 |
| plant growth medium | Mandatory | Specification of the media for growing the plants or tissue cultured samples, e.g. soil, aeroponic, hydroponic, in vitro solid culture medium, in vitro liquid culture medium, recommended value is a specific value from eo:plant growth medium or other controlled vocabulary |
| rooting conditions | Recommended | Relevant rooting conditions, such as field plot size, sowing density, container dimensions, number of plants per container |
| culture rooting medium | Recommended | Name or reference for the hydroponic or in vitro culture rooting medium, can be a name of a commonly used medium or reference to a specific medium; e.g. Murashige and skoog medium, if the medium has not been formally published, use the rooting medium descriptors |
| rooting medium macronutrients | Recommended | Measurement of the culture rooting medium macronutrients (n,p, k, ca, mg, s); e.g. Kh2po4 (170mg/l) |
| rooting medium micronutrients | Recommended | Measurement of the culture rooting medium micronutrients (fe, mn, zn, b, cu, mo); e.g. H3bo3 (6.2mg/l) |
| rooting medium organic supplements | Recommended | Organic supplements of the culture rooting medium, such as vitaimins, amino acids, organic acids, antibiotics activated charcoal; e.g. Nicotinic acid (0.5mg/l) |
| rooting medium carbon | Recommended | Source of organic carbon in the culture rooting medium; e.g. sucrose |
| rooting medium regulators | Recommended | Growth regulators in the culture rooting medium, such as cytokinins, auxins, gybberellins, abscisic acid; e.g. 0.5mg/l naa |
| rooting medium solidifier | Recommended | Specification of the solidifying agent in the culture rooting medium; e.g. agar |
| rooting medium pH | Recommended | Ph measurement of the culture rooting medium; e.g. 5.5 |
| air temperature regimen | Recommended | Information about treatment involving an exposure to varying temperatures; should include the temperature, treatment duration, interval and total experimental duration; can include different temperature regimens |
| antibiotic regimen | Optional | Information about treatment involving antibiotic administration; should include the name of antibiotic, amount administered, treatment duration, interval and total experimental duration; can include multiple antibiotic regimens |
| chemical mutagen | Optional | Treatment involving use of mutagens; should include the name of mutagen, amount administered, treatment duration, interval and total experimental duration; can include multiple mutagen regimens |
| fertilizer regimen | Optional | Information about treatment involving the use of fertilizers; should include the name fertilizer, amount administered, treatment duration, interval and total experimental duration; can include multiple fertilizer regimens |
| fungicide regimen | Optional | Information about treatment involving use of fungicides; should include the name of fungicide, amount administered, treatment duration, interval and total experimental duration; can include multiple fungicide regimens |
| gravity | Optional | Information about treatment involving use of gravity factor to study various types of responses in presence, absence or modified levels of gravity; can include multiple treatments |
| growth hormone regimen | Optional | Information about treatment involving use of growth hormones; should include the name of growth hormone, amount administered, treatment duration, interval and total experimental duration; can include multiple growth hormone regimens |
| herbicide regimen | Optional | Information about treatment involving use of herbicides; information about treatment involving use of growth hormones; should include the name of herbicide, amount administered, treatment duration, interval and total experimental duration; can include multiple regimens |
| humidity regimen | Optional | Information about treatment involving an exposure to varying degree of humidity; information about treatment involving use of growth hormones; should include amount of humidity administered, treatment duration, interval and total experimental duration; can include multiple regimens |
| mineral nutrient regimen | Recommended | Information about treatment involving the use of mineral supplements; should include the name of mineral nutrient, amount administered, treatment duration, interval and total experimental duration; can include multiple mineral nutrient regimens |
| non-mineral nutrient regimen | Optional | Information about treatment involving the exposure of plant to non-mineral nutrient such as oxygen, hydrogen or carbon; should include the name of non-mineral nutrient, amount administered, treatment duration, interval and total experimental duration; can include multiple non-mineral nutrient regimens |
| pesticide regimen | Optional | Information about treatment involving use of insecticides; should include the name of pesticide, amount administered, treatment duration, interval and total experimental duration; can include multiple pesticide regimens |
| pH regimen | Optional | Information about treatment involving exposure of plants to varying levels of ph of the growth media; can include multiple regimen |
| radiation regimen | Optional | Information about treatment involving exposure of plant or a plant part to a particular radiation regimen; should include the radiation type, amount or intensity administered, treatment duration, interval and total experimental duration; can include multiple radiation regimens |
| rainfall regimen | Optional | Information about treatment involving an exposure to a given amount of rainfall; can include multiple regimens |
| salt regimen | Optional | Information about treatment involving use of salts as supplement to liquid and soil growth media; should include the name of salt, amount administered, treatment duration, interval and total experimental duration; can include multiple salt regimens |
| standing water regimen | Optional | Treatment involving an exposure to standing water during a plant's life span, types can be flood water or standing water; can include multiple regimens |
| watering regimen | Recommended | Information about treatment involving an exposure to watering frequencies; can include multiple regimens |
| water temperature regimen | Optional | Information about treatment involving an exposure to water with varying degree of temperature; can include multiple regimens |
| plant treatment | Recommended | Ontology term(s) that describes the plant treatment or relevant environmental conditions, recommend use of plant environment ontology (eo) or other ontology, such as xeml environment ontology (xeo) or crop ontology (co), more specific fields in the treatment section can be used in addition to or in place of this field |
| light regimen | Recommended | Information about treatment involving an exposure to light, this includes both light intensity and quality |
| biotic regimen | Optional | Information about treatment involving use of biotic factors, such as bacteria, viruses or fungi |
| mechanical damage | Optional | Information about any mechanical damage exerted on the plant; can include multiple damages and sites |
| chemical administration | Optional | List of chemical compounds administered to the host or site where sampling occurred, and when (e.g. antibiotics, n fertilizer, air filter); can include multiple compounds. For chemical entities of biological interest ontology (chebi) (v111), please see http://purl.bioontology.org/ontology/chebi |
| perturbation | Optional | Type of perturbation, e.g. chemical administration, physical disturbance, etc., coupled with time that perturbation occurred; can include multiple perturbation types |
