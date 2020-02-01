## How to Download Data:

#### load_data.R
Open your terminal:

1. Go to the project root directory using command prompt:

>  cd YOUR_PATH/DSCI_522_Group313


2. Execute the script using R (We have set the default values)

> Rscript src/load_data.R


3. You will be able to see the downloaded file on the "data" folder in the root project directory

**If you want to download data file in other directories or different file name use the arguments**

> Rscript load_data.R --data_url="URL to the data file"  --full_path="Path to download your raw data"

ex) 
> Rscript load_data.R --data_url="https://www.data.com/data.csv" --full_path="~/Desktop/raw_data.csv"

<br>

## How to Preprocess Data:

This script will create 5 datafiles:
- Processed datafile
- Training Set (features) of processed datafile: `X_train_` as prefix
- Training Set (labels) of processed datafile: `y_train_` as prefix
- Testing Set (features) of processed datafile: `X_test_` as prefix
- Testing Set (labels) of processed datafile: `y_test_` as prefix


#### preprocessing.py
Open your terminal:

1. Go to the project directory using command prompt

>  cd YOUR_PATH/DSCI_522_Group313

2. Execute the script using Python (We have set the default values)

> python src/preprocessing.py


** If you want to process data to a different folder as a different name use the arguments
ex)
> python src/preprocessing.py --store_path="~/Desktop/my_file_name.csv"

** The `X_train_...`, `y_train...`, `X_test...`, `y_test...` data files are stored in the same directory 
as the processed data file. The directory is derived from the `store_path` by splitting it** 
 
<br>

## How to generate EDA summary plots & tables

This script will create 3 types of files
- .html file that contains visualized information about pairwise variables
- .csv file that contains descriptive statistics information about variables
- .csv file that contains correlation coefficient information about pairwise variables.

#### eda_summary.py
Open your terminal

1. Go to the project directory using command prompt

> cd YOUR_PATH/DSCI_522_Group313

2. Execute the script using Python (we have set the default values)

> python src/eda_summary.py

or

> python src/eda_summary.py --data_dir="DIRECTORY_TO_PROCCESSED_DATA_FROM_SCRIPT_2" --file_dir="DIRECTORY_TO_SAVE_GENERATED_FILES"

<br>

## How to run the prediction model

This script will create 4 files and store in the specified folder
- .png file that contains bar plot the test accuracy scores of each model.
- .csv file that contains summary of the feature important features for Random Forest Regressor model.
- .csv file that contains summary of the feature important features for XGBoost Regressor model.
- .csv file that contains summary of the test accuracy scores.

#### model.py
Open your terminal

1. Go to the project directory using command prompt

> cd YOUR_PATH/DSCI_522_Group313

2. Execute the script using Python (we have set the default values)

> python src/model.py

OR

> python model.py --source_file_location="data" --target_location="results"


<br>