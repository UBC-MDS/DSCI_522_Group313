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
eda/descriptive_statistics.csv eda/corr_table.csv eda/response_categorical_correlation_plot.html eda/response_numerical_correlation_plot1.html eda/response_numerical_correlation_plot2.html eda/response_numerical_correlation_plot3.html eda/response_numerical_correlation_plot4.html eda/response_numerical_correlation_plot5.html : src/eda_summary.py data/cleaned_data.csv
	python src/eda_summary.py

# Model
results/feature_importance_rfr.csv results/feature_importance_xgb.csv results/summary_df results/score_plot.png : data/X_train.csv data/X_test.csv data/y_train.csv data/y_test.csv
	python src/model.py 
clean :
	rm data/raw_quebec_city_airbnb_data.csv results/*.csv results/*.png 	