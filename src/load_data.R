# author: Group 313
# date: 2020-01-16

"This script downloads and loads dataset given url.

Usage: load_data.R [--file_path=<file_path> --data_url=<data_url>]

Options:
  --file_path=<file_path>     Path to save your datafile [default: data/raw_quebec_city_airbnb_data.csv]
  --data_url=<data_url>    your datafile name [default: http://data.insideairbnb.com/canada/qc/quebec-city/2019-11-07/data/listings.csv.gz]

" -> doc

library(docopt)
library(tidyverse)
library(testthat)

opt <- docopt(doc)
# print the options for checking
print(head(opt)) 


main <- function(file_path, data_url){
  

  
  # Read Data from source
  file <- read_csv(data_url)
  raw_df <- subset(file)

  print("---------------------------")
  print("---------------------------")
  print("Data Successfully Read from the url.")
  print(paste("Downloaded Raw Data File saved in: ", file_path, sep=" "))
  print("---------------------------")
  
  
  # Write Raw Data to a csv file
  write_csv(file, file_path)
  print("---------------------------")
  print("---------------------------")
  print("Raw Data Successfully Downloaded.")
  print(paste("Downloaded Raw Data File saved in: ", file_path, sep=" "))
  print("---------------------------")
    

  # Test functions
  test_raw_data(data_dir=file_path)
  
  
  print("-------------------------------------------")
  print("-------------Process complete--------------")
  print("-------------------------------------------")
}



#' Test downloaded RAW dataset is the identical with the original one
#'
#' @param  path path of downloaded datafile
#' @return the string that confirmss consistency of data through a dimension check.

test_raw_data <- function(data_dir){
  data <- read_csv(data_dir)
  
  # Test 1
  test_that("Summary, Space, other columns should be still included in the dataset", {
    expect_equal(dim(data)[2], 106)
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


main(opt$file_path, opt$data_url)
