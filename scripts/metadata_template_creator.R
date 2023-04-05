# install.packages("methods")
# install.packages("xml2")
# install.packages("dplyr")
# install.packages("stringr")
# install.packages("reshape")
# install.packages("openxlsx")
# install.packages("httr")
# install.packages("rlist")
# install.packages("jsonlite")
# install.packages("dplyr")

## script to build metadata template sheets using ENA sample checklists (xml) + basic Study/Experiment/Run tsvs
library("methods")
library("xml2")
library("dplyr")
library("stringr")
library("reshape")
require("openxlsx")
library("httr")
library("rlist")
library("jsonlite")
library("dplyr")

#set working directory
setwd(getwd())
## get list of active checklists
## from https://datascienceplus.com/accessing-web-data-json-in-r-using-httr/
resp<-GET("https://www.ebi.ac.uk/ena/browser/api/summary/ERC000001-ERC999999")
# Structurised data in form of R vectors and lists
jsonRespParsed<-content(resp,as="parsed") 
modJson<-jsonRespParsed$summaries #. Access data element of whole list and ignore other vectors
checklists <- modJson%>%bind_rows%>%select(accession,name, description, statusDescription)


# Load the table with 'sample' elements not found in checklist (alias, title, etc.)
basic_sample <- read.table("bin/no_checklist/sample.tsv", sep = "\t", header = F)

# Load study, experiment and run controlled vocabulary
ser.cv <- read.csv("bin/controlled_vocabulary/controlled_vocabulary.csv", na.strings = c("NA"))

#h <- checklists$accession[38]
#loop over all sample checklists XML in ENA
for (h in checklists$accession){
  #Load study, experiment and run tables
  stu.df <- read.csv("bin/no_checklist/study.tsv", sep = "\t", header = F)
  exp.df <- read.csv("bin/no_checklist/experiment.tsv", sep = "\t", header = F)
  run.df <- read.csv("bin/no_checklist/run.tsv", sep = "\t", header = F)
  
  dir.create(paste("templates",h, sep = "/")) ##create dir
  #write basic metadata tables in directory
  write.table(stu.df, paste("templates", h, "study.tsv", sep = "/" ), sep = "\t", row.names=F, col.names = F, qmethod = "double")
  write.table(exp.df, paste("templates", h, "experiment.tsv", sep = "/" ), sep = "\t", row.names=F, col.names = F, qmethod = "double")
  write.table(run.df, paste("templates", h, "run.tsv", sep = "/" ), sep = "\t", row.names=F, col.names = F, qmethod = "double")
  
  all.cv <- NULL
  raw <- NULL
  df <- NULL
  raw.df <- NULL
  template <- NULL
  tmpurl <- NULL
  units <- NULL
  tmpunitmat <- NULL
  ##
  
  tmpurl <- paste("https://www.ebi.ac.uk/ena/browser/api/xml/", h, sep="")  ## create URL
  raw <- read_xml(x = tmpurl) ## read XML
  raw.df <- xml_find_all(raw, "//FIELD")  ## subset to FIELD nodes
  
  ##### extract controlled vocabulary, link to FIELDS = parse the 'FIELD_TYPE'
  labels <- xml_text(xml_find_all(raw.df, ".//LABEL")) ## extract LABELS of each FIELD names to link
  #
  ftypes <- xml_find_all(raw.df, ".//FIELD_TYPE")  ## FIELD_TYPE nodes
  
  ##make list of all existing FIELDS for dataframe
  fields <- xml_name(xml_children(raw.df[[which(xml_length(raw.df) == max(xml_length(raw.df)))[1]]]))
  pfields <- paste(".//", fields, sep="")  ## paste to create vector of xml_find_first() arguments 
  ##
  field.df <- matrix(ncol = length(pfields), nrow = length(raw.df))  ## empty matrix to fill with metadata fields
  
  ## loop over each FIELD and populate matrix
  for (i in 1:length(pfields)){
    field.df[,i] <- xml_text(xml_find_first(raw.df, pfields[i]))
  }
  field.df <- as.data.frame(field.df)  ## make data frame
  names(field.df) <- fields  ## add column names
  names(field.df)[names(field.df) == "FIELD_TYPE"] <- "FIELD_RESTRICTION"
  field.df$FIELD_RESTRICTION <- as.character(field.df$FIELD_RESTRICTION) ### maybe fix quotation issue here
  #
  field.df$FIELD_RESTRICTION[which(xml_length(xml_children(ftypes)) == 0)] <- "free_text"
  field.df$FIELD_RESTRICTION[which(xml_length(xml_children(ftypes)) == 1)] <- "regular_expression"
  field.df$FIELD_RESTRICTION[which(xml_length(xml_children(ftypes)) > 1)] <- "controlled_vocabulary"
  ### remove idi0osyncracies
  #stupid open/close double quotes
  field.df$DESCRIPTION <- sapply(X = field.df$DESCRIPTION, FUN = str_replace_all, pattern = "[”“]", replacement = '"')
  
  #REMOVE SYNONYM
  if("SYNONYM" %in% names(field.df)){
    field.df <- field.df[,-which(names(field.df) == "SYNONYM")]
  } else {}
  
  #add missing units for uniformity
  if(!"UNITS" %in% names(field.df)){
    UNITS <- rep(NA, nrow(field.df))
    field.df <- cbind(field.df[,1:3], UNITS, field.df[,4:6])
  } else {}
  
  
  #write.csv(field.df,paste(h, paste("checklist_metadata_",h,".csv", sep = ""), sep = "/" ), row.names = F)  ## write to file
  ################## UNITS
  units <- xml_find_first(raw.df, ".//UNITS")
  tmpunitmat <- data.frame(FIELD = NULL, UNITS = NULL)
  
  for (i in which(!is.na(units))){
    tmpunits <- xml_find_all(raw.df[[i]], ".//UNIT")
    tmpunitmat <- rbind(tmpunitmat, cbind(rep(xml_text(xml_find_all(raw.df[[i]], ".//LABEL")), length(xml_text(tmpunits))),xml_text(tmpunits)))
  }
  if(nrow(tmpunitmat)>0){
    names(tmpunitmat) <- c("FIELD", "UNITS")
    write.csv(tmpunitmat, "bin/units.csv")
  } else {}
  
  unitvec = NULL
  for(k in unique(tmpunitmat$FIELD)){
    unitvec <-  c(unitvec, paste("Units:", paste(tmpunitmat$UNITS[tmpunitmat$FIELD == k], collapse = ", "), sep= " "))
  }
  unit.df <- as.data.frame(cbind(as.character(unique(tmpunitmat$FIELD)), unitvec))
  colnames(unit.df) <- c("FIELD", "UNITS")
  rm(units,tmpunits, tmpunitmat, unitvec)
  
  ## make metadata template with field names and descriptions
  field.df$DESCRIPTION <- as.character(field.df$DESCRIPTION)
  unitindex <- which(field.df$LABEL %in% unit.df$FIELD)
  field.df$DESCRIPTION[unitindex] <- paste(field.df$DESCRIPTION[unitindex], unit.df$UNITS, sep = ". ")
  template <- as.data.frame(rbind(as.character(field.df$LABEL), paste(str_to_sentence(field.df$MANDATORY),str_to_sentence(field.df$DESCRIPTION), sep = ". ")))
  template <- cbind(basic_sample, template)
  write.table(template, paste("templates", h, paste("sample_",h,".tsv", sep = ""), sep = "/" ), sep = "\t", row.names=F, col.names = F, qmethod = "double")
  #
  rm(fields, pfields, unitindex)

############################################################################################3  
  ## make controlled vocabulary by linking FIELDSto the values inside FIELD_TYPE
  sam.cv <- data.frame(field_name = NULL, field_type = NULL, permitted_values = NULL)  ## make empty data frame
  loopind <- which(xml_length(xml_children(ftypes)) > 0)
  
  for (i in loopind){
    if (!xml_length(xml_children(ftypes[i])) > 1){
      tmp_values <- xml_text(xml_find_all(ftypes[[i]],paste(".//", xml_name(xml_children(ftypes[[i]])), sep="")))
    } else {
      tmp_values <- xml_text(xml_find_all(ftypes[[i]],paste(".//", xml_name(xml_child(xml_child(ftypes[[i]]))), sep="")))
      
    }
    tmptype <- rep(xml_name(xml_child(ftypes[[i]])),times = length(tmp_values))
    tmplabel <- rep(labels[i], times = length(tmp_values))
    
    tmp.df <- cbind(tmplabel, tmptype, tmp_values)
    sam.cv <- rbind(sam.cv, tmp.df)
  }
  #
  if(nrow(sam.cv)>0){
    colnames(sam.cv)<- c("field_name", "field_type", "permitted_values")
    sam.cv <- sam.cv[!sam.cv$field_type=='TEXT_FIELD',]
    sam.cv <- droplevels(sam.cv)
    #write.csv(x = sam.cv, paste(h,"controlled_vocabulary.csv", sep = "/" ), row.names = F)
  } else {}
  
  
  test.df <- data.frame(section = rep("sample", nrow(sam.cv)), metadata_field = sam.cv$field_name, 
                        permitted_value = sam.cv$permitted_values, 
                        description = field.df$DESCRIPTION[match(x = sam.cv$field_name,table =  field.df$LABEL)])
  all.cv <- rbind(test.df, ser.cv)
  
   rm(loopind, tmp_values, tmp.df, tmplabel, tmptype, labels, test.df)

  ### Add cell references to sample template
  form.vec = NULL
  for (l in 1:ncol(template)){
    
    if(template[1,l] %in% all.cv$metadata_field){
      form = NULL
      tmpmin <- min(which(all.cv$metadata_field == template[1,l]))+1
      tmpmax <- max(which(all.cv$metadata_field == template[1,l]))+1
      form <- as.character(paste("'=sheet1!$C$", tmpmin, ":$C$", tmpmax, sep = ""))
      form.vec <- c(form.vec,form)
    } else {
      form.vec <- c(form.vec,"")
    }
  }
  template <- rbind(form.vec, template)
  
  ### Add cell references to study template
  form.vec = NULL
  for (l in 1:ncol(stu.df)){
    
    if(stu.df[1,l] %in% all.cv$metadata_field){
      form = NULL
      tmpmin <- min(which(all.cv$metadata_field == stu.df[1,l]))+1
      tmpmax <- max(which(all.cv$metadata_field == stu.df[1,l]))+1
      form <- as.character(paste("'=sheet1!$C$", tmpmin, ":$C$", tmpmax, sep = ""))
      form.vec <- c(form.vec,form)
    } else {
      form.vec <- c(form.vec,"")
    }
  } 
  stu.df <- rbind(form.vec, stu.df)
  
  ### Add cell references to experiment template
  form.vec = NULL
  for (l in 1:ncol(exp.df)){
    
    if(exp.df[1,l] %in% all.cv$metadata_field){
      form = NULL
      tmpmin <- min(which(all.cv$metadata_field == exp.df[1,l]))+1
      tmpmax <- max(which(all.cv$metadata_field == exp.df[1,l]))+1
      form <- as.character(paste("'=sheet1!$C$", tmpmin, ":$C$", tmpmax, sep = ""))
      form.vec <- c(form.vec,form)
    } else {
      form.vec <- c(form.vec,"")
    }
  }
  exp.df <- rbind(form.vec, exp.df)
  
  ### Add cell references to run template
  form.vec = NULL
  for (l in 1:ncol(run.df)){
    
    if(run.df[1,l] %in% all.cv$metadata_field){
      form = NULL
      tmpmin <- min(which(all.cv$metadata_field == run.df[1,l]))+1
      tmpmax <- max(which(all.cv$metadata_field == run.df[1,l]))+1
      form <- as.character(paste("'=sheet1!$C$", tmpmin, ":$C$", tmpmax, sep = ""))
      form.vec <- c(form.vec,form)
    } else {
      form.vec <- c(form.vec,"")
    }
  }
  run.df <- rbind(form.vec, run.df)
  rm(form.vec, form, tmpmin, tmpmax, l)
  ##########################################################################################################################################
  # write to excel
  
  all.cv <- rbind(colnames(all.cv),all.cv)

  list_of_datasets <- list("study" = stu.df,  "sample" = template, "experiment" = exp.df, "run" = run.df, "controlled_vocabulary" = all.cv)
  write.xlsx(x = list_of_datasets, colNames = F,  
             file = paste('templates', h,paste("metadata_template_",h,".xlsx", sep = ""), sep = "/" ), 
             overwrite = T)
}
rm(stu.df, template, exp.df, run.df, all.cv,  resp, field.df, ftypes, list_of_datasets, raw, raw.df, sam.cv, unit.df, df, h, i, k, UNITS )
#help(write.xlsx)
