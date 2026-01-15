import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(111)

data = {
    'Age': np.random.randint(29, 77, 300),
    'Cholesterol': np.random.randint(150, 300, 300),
    'RestingBP': np.random.randint(90, 180, 300),
    'MaxHeartRate': np.random.randint(70, 190, 300),
    'ChestPainType': np.random.choice(['Typical', 'Atypical', 'Non-Anginal', 'Asymptomatic'], 300),
    'Disease': np.random.choice([0, 1], 300, p=[0.45, 0.55])
}

df = pd.DataFrame(data)

df['RiskScore'] = (df['Cholesterol'] * 0.5) + (df['RestingBP'] * 0.3) + (df['MaxHeartRate'] * 0.2)

print("Average Cholesterol:", df['Cholesterol'].mean())
print("Average Resting BP:", df['RestingBP'].mean())
print("Average Heart Rate:", df['MaxHeartRate'].mean())

df['AgeGroup'] = pd.cut(df['Age'], bins=[29, 40, 55, 80], labels=['Young', 'Middle', 'Old'])

print("\nPatients per Age Group:")
print(df['AgeGroup'].value_counts())

plt.figure(figsize=(6,4))
plt.hist(df['Age'], bins=10)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()

plt.figure(figsize=(6,4))
df['ChestPainType'].value_counts().plot(kind='bar')
plt.title("Chest Pain Type Frequency")
plt.xlabel("Type")
plt.ylabel("Count")
plt.show()

plt.figure(figsize=(6,4))
df['Disease'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title("Disease Ratio")
plt.ylabel("")
plt.show()

print("\nTop 5 High Risk Patients:")
print(df[['Age', 'Cholesterol', 'RestingBP', 'MaxHeartRate', 'RiskScore']].sort_values('RiskScore', ascending=False).head())