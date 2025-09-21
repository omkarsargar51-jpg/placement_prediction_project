import streamlit as st

# Title
st.title("Placement Prediction System")

# Section 1: Student Details
st.header("Student Details")
name = st.text_input("Enter Student Name:")
roll_no = st.text_input("Enter Roll Number:")

# Section 2: Academic Performance
st.header("Academic Performance")
cgpa = st.slider("Enter CGPA:", 0.0, 10.0, step=0.01)
internships = st.number_input("Number of Internships:", min_value=0)
certifications = st.number_input("Number of Certifications:", min_value=0)
aptitude_score = st.slider("Aptitude Test Score:", 0, 100)
communication_skill = st.slider("Communication Skill Rating:", 0, 10)

# Predict button
if st.button("Predict Placement"):
    # Example simple logic (you can replace this with your ML model prediction)
    if cgpa >= 6.0 and aptitude_score >= 60 and communication_skill >= 6 and internships >= 2.0 and certifications >= 2.0:
        result = "Placed"
    else:
        result = "Not Placed"

    # Beautiful Success message
    if result == "Placed":
        st.success(f"Congratulations {name} (Roll No: {roll_no})! You are likely to be *{result}*!")
    else:
        st.error(f"Sorry {name} (Roll No: {roll_no}), you might be *{result}*. Keep improving!")

# Footer
st.markdown("---")
st.caption("Made with ❤ using Streamlit")