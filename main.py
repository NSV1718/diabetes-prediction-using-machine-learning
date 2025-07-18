#!/usr/bin/env python3
import sys, subprocess
# Install missing dependencies
for pkg, module in [('numpy', None), ('pandas', None), ('scikit-learn', 'sklearn')]:
    try:
        __import__(module or pkg)
    except ImportError:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', pkg])

# Begin actual imports
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score
import os
import urllib.request  # for downloading dataset

print("Please enter the following information:")

pregnancies = float(input("Number of Pregnancies: "))
glucose = float(input("Glucose Level: "))
blood_pressure = float(input("Blood Pressure: "))
skin_thickness = float(input("Skin Thickness: "))
insulin = float(input("Insulin Level: "))
bmi = float(input("BMI: "))
diabetes_pedigree_function = float(input("Diabetes Pedigree Function: "))
age = float(input("Age: "))

#Data Collection and Analysis 

# locate the CSV file in the same directory as this script
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, 'diabetes.csv')
if not os.path.exists(csv_path):
    print("Dataset not found. Downloading diabetes.csv...")
    url = "https://raw.githubusercontent.com/plotly/datasets/master/diabetes.csv"
    urllib.request.urlretrieve(url, csv_path)
    print("Download complete.")
diabetes_dataset = pd.read_csv(csv_path)  # load from local file
# number of rows and colums in this dataset
diabetes_dataset.shape

# getting the statistical measures of the data
diabetes_dataset.describe()
diabetes_dataset['Outcome'].value_counts()
diabetes_dataset.groupby('Outcome').mean()
# separating the data and labels
X = diabetes_dataset.drop(columns = 'Outcome', axis=1)
Y = diabetes_dataset['Outcome']
#Data Standardization
scaler = StandardScaler()
scaler.fit(X)
standardized_data = scaler.transform(X)
#X represent the data and Y represent model
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size = 0.2, stratify=Y, random_state=2)
classifier = svm.SVC(kernel='linear')
#training the support vector Machine Classifier
classifier.fit(X_train, Y_train)
# accuracy score on the training data
X_train_prediction = classifier.predict(X_train)

training_data_accuracy = accuracy_score(X_train_prediction, Y_train)
# accuracy score on the test data
X_test_prediction = classifier.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, Y_test)
input_data = (pregnancies,glucose,blood_pressure,skin_thickness,insulin,bmi,diabetes_pedigree_function,age)

# changing the input_data to numpy array
input_data_as_numpy_array = np.asarray(input_data)

# reshape the array as we are predicting for one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

# Convert the numpy array to a pandas DataFrame with appropriate column names
input_data_df = pd.DataFrame(input_data_reshaped, columns=X.columns)

# standardize the input data
std_data = scaler.transform(input_data_df)

# Convert standardized data back to DataFrame with column names
std_data_df = pd.DataFrame(std_data, columns=X.columns)

prediction = classifier.predict(std_data_df)

if (prediction[0] == 0):
  print('Congrats,You are not diabetic')
else:
  print('The person is diabetic')