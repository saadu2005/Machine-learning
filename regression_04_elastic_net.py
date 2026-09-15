"""Step-by-step Elastic Net Regression example."""
import numpy as np
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import ElasticNet
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Step 1: Load the dataset
X, y = load_diabetes(return_X_y=True)
# Step 2: Split features and target into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Step 3: Build preprocessing and one model
model = Pipeline([('imputer', SimpleImputer(strategy='median')), ('scaler', StandardScaler()), ('regressor', ElasticNet(alpha=0.1, l1_ratio=0.5, max_iter=10000))])
# Step 4: Train the model
model.fit(X_train, y_train)
# Step 5: Make predictions
predictions = model.predict(X_test)
# Step 6: Evaluate the model
print('MAE:', mean_absolute_error(y_test, predictions))
print('RMSE:', np.sqrt(mean_squared_error(y_test, predictions)))
print('R2:', r2_score(y_test, predictions))
