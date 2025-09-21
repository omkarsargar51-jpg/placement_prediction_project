import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# Step 1: Load your data
data = pd.read_csv('placement_data.csv')

# Step 2: Prepare features and labels
X = data[['CGPA', 'Internships', 'Certifications', 'Aptitude_Score', 'Communication']]
y = data['Placed']

# Step 3: Train a model
model = RandomForestClassifier()
model.fit(X, y)

# Step 4: Save the model
joblib.dump(model, 'placement_model.pkl')

print("Model trained and saved successfully!")
print(data.columns)
import streamlit as st
import joblib
import pandas as pd

# Load the model
model = joblib.load('placement_model.pkl')

st.title("Student Placement Predictor")

# Input fields
cgpa = st.number_input("CGPA", min_value=0.0, max_value=10.0, step=0.1)
internships = st.number_input("Number of Internships", min_value=0, step=1)
certifications = st.number_input("Number of Certifications", min_value=0, step=1)
aptitude_score = st.number_input("Aptitude Score", min_value=0, max_value=100, step=1)
communication = st.number_input("Communication Score", min_value=0, max_value=100, step=1)

if st.button("Predict Placement"):
    student = pd.DataFrame({
        'CGPA': [cgpa],
        'Internships': [internships],
        'Certifications': [certifications],
        'Aptitude_Score': [aptitude_score],
        'Communication': [communication]
    })

    prediction = model.predict(student)

    if prediction[0] == 1:
        st.success("Congratulations! Student will be placed.")
    else:
        st.error("Unfortunately, the student might not be placed.")