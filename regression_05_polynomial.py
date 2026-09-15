"""Polynomial Regression with preprocessing."""
# Step 1: Import libraries
import numpy as np
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
# Step 2: Load dataset
X, y = load_diabetes(return_X_y=True)
# Step 3: Split features and target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Step 4: Create preprocessing and exactly one regression model
model = Pipeline([('imputer', SimpleImputer(strategy='median')), ('scaler', StandardScaler()), ('polynomial', PolynomialFeatures(degree=2, include_bias=False)), ('regressor', LinearRegression())])
# Step 5: Train
model.fit(X_train, y_train)
# Step 6: Predict
predictions = model.predict(X_test)
# Step 7: Evaluate
print('MAE:', mean_absolute_error(y_test, predictions))
print('RMSE:', np.sqrt(mean_squared_error(y_test, predictions)))
print('R2:', r2_score(y_test, predictions))
