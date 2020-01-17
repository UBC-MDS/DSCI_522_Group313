# author: Group 313
# date: 2020-01-16

"This script downloads and loads dataset given url.

Usage: load_data.R <arg1>

Options:
<arg>             Takes any path type containing dataframe (this is a required positional argument)
" -> doc

library(docopt)
library(tidyverse)

opt <- docopt(doc)

print(head(opt))
#file <- read_csv(opt)
file <- read_csv("http://data.insideairbnb.com/canada/qc/quebec-city/2019-11-07/data/listings.csv.gz")

airbnb_df <- subset(file, select = -c(summary, space, description, scrape_id, last_scraped, 
                                      experiences_offered, thumbnail_url, medium_url, xl_picture_url, 
                                      host_acceptance_rate, name, neighbourhood, neighborhood_overview, 
                                      neighbourhood_group_cleansed, license, notes, transit, access, 
                                      interaction, house_rules, picture_url, host_about, host_thumbnail_url, 
                                      host_picture_url))
head(airbnb_df)

