# author: Group 313
# date: 2020-01-16

"This script downloads and loads dataset given url.

Usage: load_data.R [--file_dir=<file_dir> --file_name=<file_name>]

Options:
  --file_dir=<file_dir>     Path to save your datafile [default: ../data/]
  --file_name=<file_name>    your datafile name [default: quebec_city_airbnb_data.csv]
" -> doc

library(docopt)
library(tidyverse)
library(testthat)

opt <- docopt(doc)
# print the options for checking
print(head(opt)) 


main <- function(file_dir, file_name){
  
  # Read Data from source
  file <- read_csv("http://data.insideairbnb.com/canada/qc/quebec-city/2019-11-07/data/listings.csv.gz")
  
  # Import necessary columns
  
  airbnb_df <- subset(file, select = -c(summary, space, description, scrape_id, last_scraped, 
                                        experiences_offered, thumbnail_url, medium_url, xl_picture_url, 
                                        host_acceptance_rate, name, neighbourhood, neighborhood_overview, 
                                        neighbourhood_group_cleansed, license, notes, transit, access, 
                                        interaction, house_rules, picture_url, host_about, host_thumbnail_url, 
                                        host_picture_url))
  
  
  
  # Write Data to a csv file
  if (endsWith(file_dir,"/")){
    path <- paste(file_dir,file_name, sep="")
  } else {
    path <- paste(file_dir, file_name, sep="/")
  }
  
  write_csv(airbnb_df, path)
  print("---------------------------")
  print("---------------------------")
  print("Data Successfully Downloaded.")
  print("---------------------------")
  print("---------------------------")
  
  # Test function
  test_data(data_dir=path)

}


#' Test downloaded dataset is the identical with the one used in our analysis
#'
#' @param  path path of downloaded datafile
#' @return the string that confirmss consistency of data through a dimension check.

test_data <- function(data_dir){
  data <- read_csv(data_dir)
  
  # Test 1
  test_that("Number of columns should be 82", {
    expect_equal(dim(data)[2], 82)
  })
  # Test 2
  test_that("Number of observations should be 2704", {
    expect_equal(dim(data)[1], 2704)
  })
  
  # Return a message
  print("--------------")
  print("--------------")
  print("Data confirmed.")
  print("--------------")
  print("--------------")
}

main(opt$file_dir, opt$file_name)