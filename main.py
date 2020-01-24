# Load train and data from csv files
#train = pd.read_csv('./data/train.csv')
#store = pd.read_csv('./data/store.csv')

import pandas as pd
from cleaning import df_clean
from features import df_add_features
from model import accuracy

def predict_test(df,model,features):
    df = df_clean(df)
    df = df_add_features(df)
    X=df[features]  # Features
    y=df['Sales']  # Labels
    return accuracy(X,y,model)