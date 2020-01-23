##first instance of RandomForestRegressor

from sklearn.ensemble import RandomForestRegressor
from sklearn.datasets import make_regression
def model_regression(data, features, target, fraction=1): #takes (clean) data, list of features and target/list of targets if needed
    regr = RandomForestRegressor(max_depth=4, random_state=1, bootstrap=True)  #bootstramp True means samples with replacement
    regr.fit(data.loc[:, features].values, data[target].values.reshape(-1,1))
    RandomForestRegressor(max_depth=4, n_estimators=500, random_state=42)
    #print(regr.feature_importances_))
    #print(regr.predict([[0, 0, 0, 0]]))
    return regr

#returns the model, can be used for predictions for ex. with regr.predict() 