import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load your dataset
# Assuming the file is in your current working directory or provide the full path
try:
  df = pd.read_csv(r'uploads/energy_consumption_dataset.csv')
except FileNotFoundError:
  print("Error: 'energy_consumption_dataset.csv' not found. Please upload the file or provide the correct path.")
  # You might want to exit or handle the error differently here
  exit()


# Features and Target
X = df[['Wind Energy (GWh)'] ]# Use double brackets for a DataFrame
y = df['Renewable (GWh)']
x=np.array(X).reshape(-1,1)
y=np.array(y).reshape(-1,1)
# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict([[900]])
import pickle
f=open('p.dat','wb')
pickle.dump(y_pred,f)
f.close()