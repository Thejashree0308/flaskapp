import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import pickle

# Load the CSV
df = pd.read_csv("D:\\flask\\Student_Performance.csv")

# Convert categorical to numbers
df['Extracurricular Activities'] = LabelEncoder().fit_transform(df['Extracurricular Activities'])

# Prepare X and y
X = df.drop("Performance Index", axis=1)
y = df["Performance Index"]

# Train model
model = LinearRegression()
model.fit(X, y)

# Save model to a file
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)
