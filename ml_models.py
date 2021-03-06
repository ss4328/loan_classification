"""
Created on Tue Mar 15 19:20:48 2022

@author: shivanshsuhane
"""

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier as random_forest
from sklearn.preprocessing import MinMaxScaler, RobustScaler, MinMaxScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_validate
from sklearn import metrics
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from statsmodels.stats.outliers_influence import variance_inflation_factor
from sklearn.metrics import confusion_matrix

def print_cross_validation_scores(model_name,cv_scores):
    
    print('=====',model_name,' Cross Validation=====')
    for i,score in enumerate(cv_scores):
        print('trial {}: score {}'.format(i,score))
    print('\n')

def print_metrics(model_name, y_test, y_pred, mean_absolute_error, pipeline_score):
    
    #printing scores
    for i in range(5):
        print()
    print('=====',model_name,'=====')
    print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
    print("Precision:",metrics.precision_score(y_test, y_pred))
    print("Recall:",metrics.recall_score(y_test, y_pred))
    print('')
    print("mean_absolute_error: ", mean_absolute_error)
    print("pipeline_score: ", pipeline_score)
    for i in range(5):
        print()

if __name__ == "__main__":
    
    #1) read in data
    df = pd.read_csv ('data.csv')
    df = df.drop('JOB', 1)
    
    #2) Data exploration
    df.info()
    df.describe()
    df.corr()
    
    #VIF
    df = df[~df.isin([np.nan, np.inf, -np.inf]).any(1)]
    cols=["LOAN", "MORTDUE","VALUE","YOJ","DEROG", "DELINQ", "CLAGE", "NINQ","CLNO", "DEBTINC"]
    cols_y=['BAD']
    X_variables = df[cols]
    vif_data = pd.DataFrame()
    vif_data["feature"] = X_variables.columns
    vif_data["VIF"] = [variance_inflation_factor(X_variables.values, i) for i in range(len(X_variables.columns))]
    
    
    #3) Preprocessing
    numeric_pipeline = Pipeline(steps=[
        ('impute', SimpleImputer(strategy='mean')),
        ('scale', MinMaxScaler())
    ])

    categorical_pipeline = Pipeline(steps=[
        ('impute', SimpleImputer(strategy='most_frequent')),
        ('one-hot', OneHotEncoder(handle_unknown='ignore', sparse=False))
    ])
    
    #4) Shuffling data
    data = df.to_numpy()
    np.random.shuffle(data)
    
    #5) split to test and train datasets
    X = df.drop('BAD', axis=1)
    y = df.BAD
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.25, 
                                                    random_state=1121218)
    #Weights = linReg(trainMat, yTrain)
    
    #6) Model/Pipeline creation
    numerical_features = X_train.select_dtypes(include='number').columns.tolist()
    categorical_features = X_train.select_dtypes(exclude='number').columns.tolist()
    numeric_pipeline.fit_transform(X_train.select_dtypes(include='number'))
    
    full_processor = ColumnTransformer(transformers=[
        ('number', numeric_pipeline, numerical_features),
        ('category', categorical_pipeline, categorical_features)
    ])
    
    #define models
    logistic = LogisticRegression(max_iter=20000, tol=0.1)
    
    random_forest = random_forest()
    random_forest_pipeline = Pipeline(steps=[
        ('preprocess', full_processor),
        ('model', random_forest)
    ])
    
    
    #7) Run ML models
    logistic_reg_pipeline = Pipeline(steps=[
        ('preprocess', full_processor),
        ("logistic", logistic)
    ])
    logistic_reg_pipeline.fit(X_train, y_train)
    log_preds = logistic_reg_pipeline.predict(X_test)
    log_mae = mean_absolute_error(y_test, log_preds)
    log_pipeline_score = logistic_reg_pipeline.score(X_train, y_train)
    print_metrics('Logistic regression', y_test, log_preds, log_mae, log_pipeline_score)
    
    random_forest_pipeline.fit(X_train, y_train)
    random_forest_preds = random_forest_pipeline.predict(X_test)
    random_forest_mae = mean_absolute_error(y_test, random_forest_preds)
    random_forest_pipeline_score = random_forest_pipeline.score(X_train, y_train)
    print_metrics('Random Forest Classifier', y_test, random_forest_preds, random_forest_mae, random_forest_pipeline_score)
    
    
    #8) cross Validation
    log_reg_c_v_scores = cross_validate(logistic_reg_pipeline, X_train, y_train)['test_score']
    random_forest_c_v_scores = cross_validate(random_forest_pipeline, X_train, y_train)['test_score']
    print_cross_validation_scores('Logistic regression', log_reg_c_v_scores)
    print_cross_validation_scores('Random Forest Classifier',random_forest_c_v_scores)
    
    #9 Confusion Matrix
    cf_matrix_random_forest = confusion_matrix(y_test, random_forest_preds)
    cf_log_reg = confusion_matrix(y_test, log_preds)
      
    
    