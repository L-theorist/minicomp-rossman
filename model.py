##first instance of RandomForestRegressor

from sklearn.ensemble import RandomForestRegressor
from sklearn.datasets import make_regression
from sklearn.linear_model import LinearRegression

def model_RFR(X, y, m=4 fraction=1): #takes (clean) data, list of features and target/list of targets if needed
    regr = RandomForestRegressor(max_depth=m, random_state=1, bootstrap=True)  #bootstramp True means samples with replacement
    regr.fit(X.values, y.values.reshape(-1,1))
    #RandomForestRegressor(max_depth=4, n_estimators=500, random_state=42)
    #print(regr.feature_importances_))
    #print(regr.predict([[0, 0, 0, 0]]))
    return regr

#returns the model, can be used for predictions for ex. with regr.predict() 
#syntax mdl.predict(df_percent.loc[:, features].iloc[999].values.reshape(1,-1))[0]
def make_float(x):
    if isinstance(x, float):
        return x
    else:
        return x[0]
"""
def model_LinRegr(data, features, target, fraction=1):
    x = data.loc[:, features]
    y = data.loc[:, target]
    linr = LinearRegression()
    linr.fit(x, y)
    return linr
"""
def model_LinRegr(x, y, fraction=1):
    #x = data.iloc[:, :-1] features]
    #y = data.loc[:, target]
    linr = LinearRegression()
    linr.fit(x, y)
    return linr

def model_predict(X, model):
    pred = X.apply(lambda row: make_float(model.predict(row.values.reshape(1,-1))[0]), axis=1)
    return pred
def accuracy(X, y, model):
    preds = model_predict(X, model)
    actuals = y
    return(metric(preds, actuals))
#data.loc[:, feat].iloc[9217].values.reshape(1,-1))[0][0]

#def compare(model1, model2, features, target, data):
#    pred1 = data.apply(lambda row: model1.predict(row[features].values.reshape(1,-1))[0], axis=1)
#    pred2 = data.apply(lambda row: model2.predict(row[features].values.reshape(1,-1))[0], axis=1)
    
    
#   for row in data:
#        pred1 = data.apply(lambda row: model1.predict(row), axis=1)
#        pred2 =  
def metric(preds, actuals):
    preds = preds.reshape(-1)
    actuals = actuals.reshape(-1)
    assert preds.shape == actuals.shape
    return round(100 * np.linalg.norm((actuals - preds) / actuals) / np.sqrt(preds.shape[0]),3)

