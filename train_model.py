import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# Step 1: Load your data
data = pd.read_csv('placement_data.csv')

# Step 2: Prepare features and labels
X = data[['cgpa', 'internships', 'certifications', 'aptitude', 'communication']]
y = data['placement']  # Make sure your CSV has a 'placement' column

# Step 3: Train a model
model = RandomForestClassifier()
model.fit(X, y)

# Step 4: Save the model
joblib.dump(model, 'placement_model.pkl')

print("Model trained and saved successfully!")