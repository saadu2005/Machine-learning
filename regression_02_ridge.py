"""Step-by-step Ridge Regression example."""
import numpy as np
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Step 1: Load the dataset
X, y = load_diabetes(return_X_y=True)
# Step 2: Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Step 3: Preprocess data and create exactly one model
model = Pipeline([('imputer', SimpleImputer(strategy='median')), ('scaler', StandardScaler()), ('regressor', Ridge(alpha=1.0))])
# Step 4: Train
model.fit(X_train, y_train)
# Step 5: Predict
predictions = model.predict(X_test)
# Step 6: Evaluate
print('MAE:', mean_absolute_error(y_test, predictions))
print('RMSE:', np.sqrt(mean_squared_error(y_test, predictions)))
print('R2:', r2_score(y_test, predictions))
