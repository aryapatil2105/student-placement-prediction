import streamlit as st
import joblib

# -----------------------------
# Load Models
# -----------------------------
placement_model = joblib.load("placement_model.pkl")
salary_model = joblib.load("salary_model.pkl")

classification_scaler = joblib.load("classification_scaler.pkl")
regression_scaler = joblib.load("regression_scaler.pkl")

branch_encoder = joblib.load("branch_encoder.pkl")
tier_encoder = joblib.load("tier_encoder.pkl")

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Student Placement Prediction",
    page_icon="🎓",
    layout="wide"
)

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("🎓 Student Placement")

st.sidebar.markdown("---")

st.sidebar.write("### Developed By")
st.sidebar.write("Arya Anand Patil")

st.sidebar.write("### Course")
st.sidebar.write("B.Sc. Data Science & Business Analysis")

st.sidebar.write("### University")
st.sidebar.write("IT Vedant")

st.sidebar.markdown("---")

st.sidebar.write("### Models Used")
st.sidebar.write("✅ Logistic Regression")
st.sidebar.write("✅ Linear Regression")

# -----------------------------
# Main Heading
# -----------------------------
st.title("🎓 Student Placement Prediction System")

st.write(
    "Predict whether a student is likely to be placed and estimate the expected salary package."
)

# =============================
# Academic Information
# =============================

st.markdown("---")
st.subheader("📚 Academic Information")

col1, col2 = st.columns(2)

with col1:
    branch = st.selectbox(
        "Branch",
        branch_encoder.classes_
    )

with col2:
    college_tier = st.selectbox(
        "College Tier",
        tier_encoder.classes_
    )

col1, col2 = st.columns(2)

with col1:
    cgpa = st.number_input(
        "CGPA",
        min_value=0.0,
        max_value=10.0,
        value=7.5
    )

with col2:
    backlogs = st.number_input(
        "Backlogs",
        min_value=0,
        max_value=10,
        value=0
    )

# =============================
# Technical Skills
# =============================

st.markdown("---")
st.subheader("💻 Technical Skills")

col1, col2 = st.columns(2)

with col1:
    coding_skills = st.slider(
        "Coding Skills",
        0,
        100,
        70
    )

with col2:
    dsa_score = st.slider(
        "DSA Score",
        0,
        100,
        70
    )

col1, col2 = st.columns(2)

with col1:
    aptitude_score = st.slider(
        "Aptitude Score",
        0,
        100,
        70
    )

with col2:
    communication_skills = st.slider(
        "Communication Skills",
        0,
        100,
        70
    )

col1, col2 = st.columns(2)

with col1:
    ml_knowledge = st.slider(
        "ML Knowledge",
        0,
        100,
        50
    )

with col2:
    system_design = st.slider(
        "System Design",
        0,
        100,
        50
    )

# =============================
# Experience
# =============================

st.markdown("---")
st.subheader("🏆 Experience")

col1, col2 = st.columns(2)

with col1:
    internships = st.number_input(
        "Internships",
        0,
        10,
        1
    )

with col2:
    projects_count = st.number_input(
        "Projects",
        0,
        20,
        2
    )

col1, col2 = st.columns(2)

with col1:
    certifications = st.number_input(
        "Certifications",
        0,
        20,
        2
    )

with col2:
    hackathons = st.number_input(
        "Hackathons",
        0,
        20,
        1
    )

col1, col2 = st.columns(2)

with col1:
    open_source_contributions = st.number_input(
        "Open Source Contributions",
        0,
        20,
        0
    )

with col2:
    extracurriculars = st.number_input(
        "Extracurricular Activities",
        0,
        20,
        2
    )

st.markdown("---")

predict = st.button(
    "🚀 Predict Placement",
    use_container_width=True
)
if predict:

    # Encode Categorical Values
    branch_encoded = branch_encoder.transform([branch])[0]
    tier_encoded = tier_encoder.transform([college_tier])[0]

    # Create Input Data
    input_data = [[
        branch_encoded,
        tier_encoded,
        cgpa,
        backlogs,
        coding_skills,
        dsa_score,
        aptitude_score,
        communication_skills,
        ml_knowledge,
        system_design,
        internships,
        projects_count,
        certifications,
        hackathons,
        open_source_contributions,
        extracurriculars
    ]]

    # Scale Data
    input_scaled = classification_scaler.transform(input_data)

    # Prediction
    prediction = placement_model.predict(input_scaled)[0]

    st.markdown("---")
    st.subheader("📊 Prediction Result")

    if prediction == 1:

     st.success("✅ Congratulations! The student is likely to be Placed.")

    # ----------------------------
    # Salary Prediction
    # ----------------------------

     salary_input = [[
        branch_encoded,
        tier_encoded,
        cgpa,
        backlogs,
        coding_skills,
        dsa_score,
        aptitude_score,
        communication_skills,
        ml_knowledge,
        system_design,
        internships,
        projects_count,
        certifications,
        hackathons,
        open_source_contributions,
        extracurriculars
    ]]

     salary_input_scaled = regression_scaler.transform(salary_input)

     predicted_salary = salary_model.predict(salary_input_scaled)[0]

     st.markdown("---")

     st.subheader("💰 Estimated Salary Package")

     st.success(f"₹ {predicted_salary:.2f} LPA")

    else:

     st.error("❌ The student is unlikely to be Placed.")    