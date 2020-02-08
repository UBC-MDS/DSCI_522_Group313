## Authors: Jaekeun Lee, Suvarna Moharir  Chimaobi Amadi
## Date: 2020-01-28
## Summary: This script downloads and processes data, generate plots automatically, perform analysis and final report

.PHONY : all
all: data/X_train.csv eda/corr_table.csv results/score_plot.png

# Raw Data Download
data/raw_quebec_city_airbnb_data.csv : src/load_data.R
	Rscript src/load_data.R

# Cleaned Dataset
data/cleaned_data.csv : src/preprocessing.py data/raw_quebec_city_airbnb_data.csv
	python src/preprocessing.py

# Training & Testing Dataset 
data/X_train.csv data/y_train.csv data/X_test.csv data/y_test.csv : src/preprocessing.py data/cleaned_data.csv
	python src/preprocessing.py

# EDA summary
eda/descriptive_statistics.csv eda/corr_table.csv heatmap.png price_linearanalysis1.png price_linearanalysis2.png price_linearanalysis3.png : src/eda_summary.py data/cleaned_data.csv
	python src/eda_summary.py

# Model
results/feature_importance_rfr.csv results/feature_importance_xgb.csv results/summary_df results/score_plot.png results/score_summary.png : data/X_train.csv data/X_test.csv data/y_train.csv data/y_test.csv
	python src/model.py 
clean :
	rm data/raw_quebec_city_airbnb_data.csv results/*.csv results/*.png