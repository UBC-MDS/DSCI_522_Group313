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

# Rendering final report
docs/final_report.md: docs/final_report.Rmd docs/citations.bib results/score_plot.PNG results/score_summary.PNG eda/heatmap.PNG eda/price_linearanalysis1.PNG eda/price_linearanalysis2.PNG eda/price_linearanalysis3.PNG
	Rscript -e "library(rmarkdown);render('docs/final_report.Rmd', output_format = 'github_document')"

clean :
	rm data/raw_quebec_city_airbnb_data.csv results/*.csv results/*.png results/*.PNG eda/*.PNG