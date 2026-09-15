"""Support Vector Regression with preprocessing."""
import numpy as np
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
X,y=load_diabetes(return_X_y=True); Xt,Xv,yt,yv=train_test_split(X,y,test_size=.2,random_state=42)
m=Pipeline([('imputer',SimpleImputer(strategy='median')),('scaler',StandardScaler()),('regressor',SVR(kernel='rbf',C=100,epsilon=.1))]); m.fit(Xt,yt); p=m.predict(Xv)
print('MAE:',mean_absolute_error(yv,p)); print('RMSE:',np.sqrt(mean_squared_error(yv,p))); print('R2:',r2_score(yv,p))
