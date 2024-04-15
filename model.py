import numpy as np
import pandas as pd
import os
from sklearn.preprocessing import LabelEncoder
from sklearn.neural_network import MLPClassifier

# loading dataset
path = "D:\Third_Year\Second_Sem\Mini_Project\Project_Execution\TUANDROMD.csv"
data = pd.read_csv(path)

# preprocessing
data = data.dropna()
lb = LabelEncoder()
data['Label'] = lb.fit_transform(data['Label'])

# Removing Class Inequalities with SMOTE
from imblearn.over_sampling import SMOTE
y = data['Label']
X = data.drop(['Label'], axis=1)
smote = SMOTE()
x_smote, y_smote = smote.fit_resample(X, y)

# Training MLP Classifier
mlp_classifier = MLPClassifier(random_state=1, max_iter=300)
mlp_classifier.fit(x_smote, y_smote)

# Saving the trained model
import joblib
joblib.dump(mlp_classifier, 'mlp_classifier_model.pkl')
