# 🤖 Machine Learning Notes
## 📖 What is Machine Learning?

Machine Learning (ML) is a branch of Artificial Intelligence (AI) that enables computers to learn patterns from data and make predictions or decisions without being explicitly programmed.

Instead of writing rules manually, ML algorithms learn from historical data.

# 📂 Types of Machine Learning
## 1️⃣ Supervised Learning

Supervised learning uses labeled data, meaning the correct output is already known during training.

Goal

Learn a mapping from inputs (X) to outputs (Y).

Examples
House Price Prediction
Email Spam Detection
Student Marks Prediction
Disease Prediction
Common Algorithms
Linear Regression
Logistic Regression
Decision Tree
Random Forest
Support Vector Machine (SVM)
K-Nearest Neighbors (KNN)
Naive Bayes
Advantages
High accuracy with quality data
Easy to evaluate
Widely used
Disadvantages
Requires labeled datasets
Collecting labels can be expensive
# 2️⃣ Unsupervised Learning

Unsupervised learning works with unlabeled data.

The algorithm finds hidden patterns or relationships without knowing the correct answers.

Goal

Discover the structure of data.

Examples
Customer Segmentation
Market Basket Analysis
Anomaly Detection
Common Algorithms
K-Means Clustering
Hierarchical Clustering
DBSCAN
Principal Component Analysis (PCA)
Advantages
No labeled data required
Finds hidden patterns
Disadvantages
Harder to evaluate
Results may be difficult to interpret
# 3️⃣ Semi-Supervised Learning

Semi-supervised learning uses both:

Small amount of labeled data
Large amount of unlabeled data
Example

Medical image classification where only a few images are labeled.

Advantages
Better performance than unsupervised learning
Requires fewer labels
Disadvantages
More complex
Depends on data quality
# 4️⃣ Reinforcement Learning

An agent learns by interacting with an environment.

The agent receives:

## Rewards ✅
## Penalties ❌

It tries to maximize the total reward.

Examples
Self-driving Cars
Robotics
Chess
Video Games
Recommendation Systems
Components
Agent
Environment
State
Action
Reward
Common Algorithms
Q-Learning
SARSA
Deep Q Networks (DQN)
PPO
Advantages
Learns from experience
Excellent for sequential decision making
Disadvantages
Requires large training time
Computationally expensive
## 📊 Machine Learning Workflow
collect Data.\
      │
      ▼
Data Cleaning.\
      │
      ▼
Feature Engineering.\
      │
      ▼
Split Dataset.\
      │
      ▼
Train Model.\
      │
      ▼
Evaluate Model.\
      │
      ▼
Improve Model.\
      │
      ▼
Deploy Model.\
# 📚 Classification vs Regression
Classification	Regression
Predicts Categories	Predicts Continuous Values
Spam or Not Spam	House Price
Disease Detection	Temperature Prediction
Pass / Fail	Sales Prediction
# 📈 Common Evaluation Metrics
Classification
Accuracy
Precision
Recall
F1 Score
ROC-AUC
Confusion Matrix
Regression
Mean Absolute Error (MAE)
Mean Squared Error (MSE)
Root Mean Squared Error (RMSE)
R² Score
# 📂 Popular Machine Learning Libraries
Library	Purpose
NumPy	Numerical Computing
Pandas	Data Analysis
Matplotlib	Visualization
Scikit-learn	Machine Learning Algorithms
TensorFlow	Deep Learning
PyTorch	Deep Learning
Seaborn	Statistical Visualization
XGBoost	Gradient Boosting
# 📁 Typical Project Structure
Machine-Learning/
│
├── datasets/
├── notebooks/
├── src/
├── models/
├── images/
├── README.md
├── requirements.txt
└── LICENSE
# 🎯 Applications of Machine Learning
Healthcare
Finance
Banking
Fraud Detection
Recommendation Systems
Autonomous Vehicles
Natural Language Processing
Image Recognition
Speech Recognition
Agriculture
Cybersecurity
Marketing
E-commerce
# 🚀 Popular Machine Learning Algorithms
Regression
Linear Regression
Ridge Regression
Lasso Regression
Elastic Net
Classification
Logistic Regression
Decision Tree
Random Forest
KNN
Naive Bayes
SVM
XGBoost
Clustering
K-Means
DBSCAN
Hierarchical Clustering
Dimensionality Reduction
PCA
t-SNE
LDA
Ensemble Learning
Random Forest
AdaBoost
Gradient Boosting
XGBoost
LightGBM
CatBoost
