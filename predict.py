import pickle

# Load model and scaler
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

# Input
hours = float(input("Enter study hours: "))
attendance = float(input("Enter attendance: "))
score = float(input("Enter previous score: "))
sleep = float(input("Enter sleep hours: "))

import pandas as pd

data = pd.DataFrame([[hours, attendance, score, sleep]],
                    columns=["hours_studied", "attendance", "previous_score", "sleep_hours"])

data = scaler.transform(data)

prediction = model.predict(data)

print("Predicted Difficulty:", prediction[0])