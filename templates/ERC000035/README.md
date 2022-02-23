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
| organism part | Optional | The part of organism's anatomy or substance arising from an organism from which the biomaterial was derived, excludes cells. |
| ploidy | Optional | The ploidy level of the genome (e.g. allopolyploid, haploid, diploid, triploid, tetraploid). It has implications for the downstream study of duplicated gene and regions of the genomes (and perhaps for difficulties in assembly). For terms, please select terms listed under class ploidy (pato:001374) of phenotypic quality ontology (pato), and for a browser of pato (v 2013-10-28) please refer to http://purl.bioontology.org/ontology/pato. Mandatory for migs of eukaryotes. |
| infect | Optional | The name of the disease causing/contaminating organism; the value can also be ‘control’. |
| protocol | Optional | The laboratory method used to reveal the presence of the sample sequenced in the experiment. |
| sampling time point | Optional | NA |
| initial time point | Optional | The first time point measured at the start of some process. |
| growth condition | Optional | A role that a material entity can play which enables particular conditions used to grow organisms or parts of the organism. This includes isolated environments such as cultures and open environments such as field studies. |
| genotype | Recommended | Name or code for genotype of organism |
| sex | Optional | Sex of the organism from which the sample was obtained |
| age | Recommended | Age of the organism the sample was derived from. |
| genetic modification | Optional | A genetic modification of the genome of an organism which may occur naturally by spontaneous mutation, or be introduced by some experimental means. Examples of genetic modification include specification of a transgene or the gene knocked-out or details of transient transfection. |
| phenotype | Optional | Where possible, please use the experimental factor ontology (efo) to describe your phenotypes. |
| cellular component | Optional | The part of a cell or its extracellular environment in which a gene product is located. |
| individual | Optional | An individual used a specimen in an experiment, from which a material sample was derived. |
| disease staging | Optional | The stage or progression of a disease in an organism. Includes pathological staging of cancers and other disease progression. E.g. Dukes c stage describing colon cancer (efo_0000410). |
| immunoprecipitate | Optional | The precipitate antibody bound target molecules generated when precipitating an antigen out of a solution during the process of immunoprecipitation. |
| replicate | Optional | A role played by a a biological sample in the context of an experiment where the intent is that biological or technical variation is measured. |
| cultivar | Optional | Cultivar (cultivated variety) of plant from which sample was obtained |
| ecotype | Optional | A population within a given species displaying genetically based, phenotypic traits that reflect adaptation to a local habitat. |
| cell_line | Optional | Cell line from which the sample was obtained |
| strain | Optional | Name of the strain from which the sample was obtained. |
| time | Optional | The duration in which the treatment has occurred. |
| dose | Optional | The total quantity or strength of a substance administered at one time. |
| chemical compound | Optional | A drug, solvent, chemical, etc., with a property that can be measured such as concentration (http://purl.obolibrary.org/obo/chebi_37577). |
| experimental factor 1 | Optional | A variable that the experiment is based on. |
| experimental factor 2 | Optional | A variable that the experiment is based on. |
| experimental factor 3 | Optional | A variable that the experiment is based on. |
| experimental factor 4 | Optional | A variable that the experiment is based on. |
| experimental factor 5 | Optional | A variable that the experiment is based on. |
| block | Optional | A block or batch is an experimental unit arrangement into a group which is similar to one another. Typically, a blocking factor is a source of variability that is not of primary interest to the experimenter. An example of a blocking factor might be the sex of a patient; by blocking on sex, this source of variability is controlled for, thus leading to greater accuracy (efo_0005067). |
| environmental stress | Optional | Environmental stress is a treatment where some aspect of the environment is perturbed in order to stress the organism or culture, e.g. change in temperature, change in watering regime. |
| environmental history | Optional | Information concerning the envinonrment a material entity has been exposed to, such as an organism from a lake. |
