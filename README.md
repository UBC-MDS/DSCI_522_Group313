# DSCI_522_Group313 - AirBnb Price Predictor
Milestone1 Repository
- Authors: Suvarna Moharir, Jaekeun Lee, Chimaobi Amadi

A data analysis project for DSCI 522 (Data Science Workflows), a course as part of the Master of Data Science program at the University of British Columbia.

## File Structure

```
.
├── README.md
├── data
├── docs
│   ├── CODE_OF_CONDUCT.md
│   ├── CONTRIBUTING.md
│   └── LICENSE
├── eda
└── src
    ├── README.md
    ├── analysis.ipynb
    ├── eda_summary.py
    ├── exploratory_analysis.ipynb
    ├── load_data.R
    ├── preprocessing.ipynb
    └── preprocessing.py

R
```

## Introduction

### Research Question

For this project, our main research question is a **predictive research question**: What are the most important features to predict the price per night of an AirBnb in Quebec City? This analysis could prove useful for 2 major groups of individuals: (1) individuals who are looking to rent out one of their properties as an Airbnb, and are looking for a potential price to charge, and (2) individuals who currently rent out their properties as an Airbnb ('hosts'), and are trying to determine how best to increase the valuation of the rental property. Airbnbs are often a popular option for those who are looking for low-cost, short-term rentals, and can often be a source of secondary income for hosts. Therefore, it is important to conduct this analysis to help guide them in setting fair and realistic prices for their units.  

### Data Set
[AirBnb Quebec City Dataset](http://data.insideairbnb.com/canada/qc/quebec-city/2019-11-07/data/listings.csv.gz)

This data set includes various AirBnb listings from 2019 in Quebec City, Quebec. It has various features, including room type, included amenities, number of beds, and per-night price. There are a mix of categorical, numeric, and logical data types. The raw data set contains 106 columns and 2704 rows. 

### Analysis Plan

To answer the request question stated above, we plan to train a regression model to predict the price per night of hosting an Airbnb in Quebec City.
Some of the models in consideration are:
- Multiple Linear Regression
- Generalized Linear Regression
- Random Forest Regression

We will test out models and choose the one that performs the best. Prior to building the model, we will partition in a training (80%) and test (20%) split and will then perform an explanatory data analysis to gain further familiarity with out data as well as any potential problems we need to address, as well as predictors that we may need to omit. After selection of the final model, we will re-fit the model on the training set, and then use the test set and a confusion matrix to evaluate performance.

### Exploratory Data Analysis 
For our exploratory data analysis, we will first aim to become familiar with the data by exploring the data-types of each column, as well as the unique names of the categorical features (e.g. the names of neighbourhoods contained within the dataset). We will wrangle data to ensure that all columns have a sensible data type (e.g. `price` is currently listed as a string; we will convert it to a numeric), and will remove columns that we cannot use in our analysis (e.g. columns that are completely blank, or columns that list full reviews, which are in French.) <br/>
After cleaning, there are still over 80 columns in our dataset, so selecting features is an impending matter. Using correlation plots, we will try to observe distribution of each variables and relationship between predictors and response.  <br/>
[The exploratory analysis can be found here](https://github.com/UBC-MDS/DSCI_522_Group313/blob/master/src/exploratory_analysis.ipynb).

### Sharing of Results
After development, we will present our model with visualized residual plots, table with coefficients and their interpretations.

Also, we will compare our results with the prediction that is made on the airbnb official website, which gives an estimation of how much you can earn as an airbnb host: https://airbnb.ca/host/homes.

## How to Download Data

Please refer to the README.md file on the [src folder](https://github.com/UBC-MDS/DSCI_522_Group313/tree/master/src)

## Dependencies
- R version 3.6.1 and R packages:
    - tidyverse == 1.2.1
    - caTools == 1.17.1.2
    - GGally == 1.4.0
 
    

