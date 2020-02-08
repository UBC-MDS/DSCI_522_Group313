# author: Suvarna Moharir, Jaekeun Lee, Chimaobi Amadi
# date: 2020-01-24
'''
Usage: src/model.py [--source_file_location=<source_file_location>] [--target_location=<target_location>]

Options:
-s --source_file_location=<source_file_location>   [default: data]
-t --target_location=<target_location>             [default: results]

'''
#Import Libraries
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import make_pipeline
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from xgboost import XGBRegressor
from matplotlib import pyplot
import altair as alt
import pandas as pd
from selenium import webdriver
from docopt import docopt

def check_files(input_dir, output):
    assert len(pd.read_csv(input_dir + "/X_train.csv")) == 1755, "Wrong X_train file is loaded"
    assert len(pd.read_csv(input_dir + "/X_test.csv")) == 439, "Wrong X_test file is loaded"
    assert pd.read_csv(input_dir + "/X_test.csv").shape[1] == 75, "The number of columns for X_test is wrong"
    
def main(input_dir, output):
   
    #Load X_train, X_test
    
    X_train = pd.read_csv(input_dir + "/X_train.csv")
    X_test = pd.read_csv(input_dir + "/X_test.csv")
    y_train = pd.read_csv(input_dir + "/y_train.csv")
    y_test = pd.read_csv(input_dir + "/y_test.csv")
   
    
    #Modelling using GridSearchCV
    ##SVR
    print("Running Support Vector Regressor")
    param_grid = {'kernel':['rbf', 'poly'],
                'C':[0.1, 1, 10, 100],
                'gamma': ['auto', 'scale']}
    
    svr = SVR()
    
    clf = GridSearchCV(svr, param_grid, cv = 4)
    clf.fit(X_train, y_train.to_numpy().ravel())
    #clf.fit(X_train, y_train)
    
    print(f"Train score for Support Vector Regressor: {clf.score(X_train, y_train):.2f}")
    print(f"Test score for Support Vector Regressor: {clf.score(X_test, y_test):.2f}")
    print(clf.best_params_)
    
    print("SVR completed")
    
    #RandomForestRegressor
    print("Running Random Forest Regressor")
    
    estimator = RandomForestRegressor()
    param_grid2 = { 
                "n_estimators"      : [100, 200, 300],
                "max_features"      : ["auto", "sqrt", "log2"],
                "min_samples_split" : [2,3,4]
                }
    
    grid = GridSearchCV(estimator, param_grid2, cv=4)
    
    grid.fit(X_train, y_train.to_numpy().ravel())
    
    print(f"Train score for Random Forest Regressor: {grid.score(X_train, y_train):.2f}")
    print(f"Test score for Random Forest Regressor: {grid.score(X_test, y_test):.2f}")
    
    print(grid.best_params_)
    
    feature_importance_rfr = pd.DataFrame({'feature': X_train.columns, 'scores': grid.best_estimator_.feature_importances_}).sort_values(by=['scores'], ascending = False)
    feature_importance_rfr.to_csv(output + "/feature_importance_rfr.csv", index=False)
    
    print("Random Forest Regressor Completed")
    
    #XGBRegressor
    print("Running XGBRegressor")
    xgb = XGBRegressor(booster='gbtree',gamma=0,
                       learning_rate=0.1,colsample_bytree=0.8,subsample=0.7,min_child_weight=2,
                       max_depth=2,n_estimators=70,n_jobs=-1,reg_alpha=1,silent=True)
    
    xgb.fit(X_train, y_train)
    
    print(f"Train score for XGBRegressor :{xgb.score(X_train, y_train):.2f}")
    print(f"Test score for XGBRegressor :{xgb.score(X_test, y_test):.2f}")
    
    feature_importance_xgb = pd.DataFrame({'feature': X_train.columns, 'scores': xgb.feature_importances_}).sort_values(by=['scores'], ascending = False)
    feature_importance_xgb.to_csv(output + "/feature_importance_xgb.csv", index=False)
    
    print("Completed XGBRegressor")
    
    #SummaryTable
    summary_df = pd.DataFrame({'model': ['RFG', 'SVR', 'XGB'], 'train_scores': [grid.score(X_train, y_train), clf.score(X_train, y_train), xgb.score(X_train, y_train)], 
                  'test_scores'  : [grid.score(X_test, y_test), clf.score(X_test, y_test), xgb.score(X_test, y_test)]
                 })
    summary_df.to_csv(output + "/summary_df.csv", index=False)


    #Plot
    score_plot = alt.Chart(summary_df).mark_bar().encode(
        x=alt.X('test_scores:Q'),
        y=alt.Y('model:N', sort=alt.EncodingSortField(field="test_scores", order='descending')),

        color='model:N')
    
    best_features = feature_importance_rfr.iloc[:10,:]
    feature_summary = alt.Chart(best_features).mark_bar().encode(
        x=alt.X('scores:Q', title="importance score"),
        y=alt.Y('feature:N', sort=alt.EncodingSortField(field="scores", order='descending')),
        color=alt.Color('feature:N', legend=None)
    )

    with alt.data_transformers.enable('default'):
            score_plot.save(
                output + "/score_plot.png"
            )

            feature_summary.save(
                output + "/score_summary.png"
            )
    print("=============================")
    print("Model successfully completed!")  
    print("=============================")

#check_files()

opt = docopt(__doc__)

check_files(opt['--source_file_location'], opt['--target_location'])

main(opt['--source_file_location'], opt['--target_location'])
