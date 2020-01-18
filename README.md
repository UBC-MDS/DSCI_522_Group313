# DSCI_522_Group313
Milestone1 Repository

## File Structure

```
.
├── README.md
├── data
│   └── README.md
├── docs
│   ├── CODE_OF_CONDUCT.md
│   ├── CONTRIBUTING.md
│   └── LICENSE
└── src
    ├── README.md
    ├── exploratory_analysis.ipynb
    └── load_data.R
```

## How to Download Data

Please refer to the README.md file on the `src` folder



## Proposal

### Data Set
[AirBnb Quebec City Dataset](http://data.insideairbnb.com/canada/qc/quebec-city/2019-11-07/data/listings.csv.gz)

This data set looks at various AirBnb listings from 2019 in Quebec City, Quebec. It has various features, including neighbourhood, room type, and price. 

### Research Question

Our main research question is a **predictive research question**: What are the most important features to predict the price per night of an AirBnb in Quebec City?
 

### Analysis Plan

We plan to train a regression model to predict the price per night of hosting airbnb on Quebec City.
Some of the models in consideration are:
- Multiple Linear Regression
- Generalized Linear Regression
- Random Forest Regression

We will try to test out models and choose the one that performs the best.


### Exploratory Data Analysis 
For our exploratory data analysis, we will first aim to become familiar with the data by exploring the data-types of each column, as well as the unique names of the categorical features (e.g. the names of neighbourhoods contained within the dataset).
Because there are over 80 columns in our dataset, selecting features is an impending matter. Using correlation plots, we will try to observe distribution of each variables and relationship between predictors and response.

### Sharing of Results
After development, we will present our model with visualized residual plots, table with coefficients and their interpretations.

Also, we will compare our results with the prediction that is made on the airbnb official website, which gives an estimation of how much you can earn as an airbnb host: https://airbnb.ca/host/homes.
