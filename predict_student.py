import joblib
import pandas as pd

# Load model
model = joblib.load('placement_model.pkl')

# Example student data
student_data = {
    'CGPA': [8.2],
    'Internships': [2],
    'Certifications': [3],
    'Aptitude_Score': [85],
    'Communication': [80]
}

# Convert to DataFrame
student = pd.DataFrame(student_data)

# Predict
prediction = model.predict(student)

if prediction[0] == 1:
    print("Placed")
else:
    print("Not Placed")