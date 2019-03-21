library(tidyverse)
if(!require(jsonlite)){install.packages(jsonlite)}
library(here)

glyphosate_tweets <-  fromJSON("glyphosate_tweets.json",flatten = TRUE) %>% as.tbl()
