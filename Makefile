results/feature_importance_rfr.dat : data/X_train.csv data/X_test.csv data/y_train.csv data/y_test.csv src/model.py
	python src/model.py data/X_train.csv data/X_test.csv data/y_train.csv data/y_test.csv

results/feature_importance_rfr.csv : results/feature_importance_rfr.dat src/model.py
	python src/model.py data/X_train.csv data/X_test.csv data/y_train.csv data/y_test.csv
	
	
results/figure/isles.png : results/isles.dat src/plotcount.py
	python src/plotcount.py results/isles.dat results/figure/isles.png	

results/feature_importance_xgb.dat : data/X_train.csv data/X_test.csv data/y_train.csv data/y_test.csv src/model.py
	python src/model.py data/X_train.csv data/X_test.csv data/y_train.csv data/y_test.csv
	
results/score_plot.dat : data/X_train.csv data/X_test.csv data/y_train.csv data/y_test.csv src/model.py
	python src/model.py data/X_train.csv data/X_test.csv data/y_train.csv data/y_test.csv
	
results/summary_df.dat : data/X_train.csv data/X_test.csv data/y_train.csv data/y_test.csv src/model.py
	python src/model.py data/X_train.csv data/X_test.csv data/y_train.csv data/y_test.csv