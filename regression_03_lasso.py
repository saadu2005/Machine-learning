"""Lasso Regression with preprocessing."""
# Step 1: Import libraries
import numpy as np
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Lasso
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Step 2: Load the dataset
X, y = load_diabetes(return_X_y=True)

# Step 3: Split features and target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Create preprocessing and exactly one regression model
model = Pipeline([('imputer', SimpleImputer(strategy='median')), ('scaler', StandardScaler()), ('regressor', Lasso(alpha=0.1, max_iter=10000))])

# Step 5: Train the model
model.fit(X_train, y_train)

# Step 6: Make predictions
predictions = model.predict(X_test)

# Step 7: Evaluate the model
print('MAE:', mean_absolute_error(y_test, predictions))
print('RMSE:', np.sqrt(mean_squared_error(y_test, predictions)))
print('R2:', r2_score(y_test, predictions))
