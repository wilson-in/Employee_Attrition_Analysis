import streamlit as st
import pandas as pd
import joblib

# Load your trained pipeline
model = joblib.load("Project_3-Employee_Attrition_Analysis_and_Prediction\models\svc_pipeline_ADASYN.pkl")

# --- Page Config ---
st.set_page_config(page_title="Employee Attrition Prediction",page_icon="🧑‍💻")


# --- Main Heading ---
st.markdown(
    "<h2 style='text-align: center; color: #FF5733;'>👨🏻‍💻 Employee Attrition Prediction Dashboard</h2>",
    unsafe_allow_html=True
)


# --- Space before form ---
st.markdown("<hr>", unsafe_allow_html=True)


# --- Features groups ---
median_features = {
    'Age': 30,
    'DistanceFromHome': 5,
    'MonthlyIncome': 30000,
    'NumCompaniesWorked': 1,
    'PercentSalaryHike': 10,
    'TotalWorkingYears': 5,
    'TrainingTimesLastYear': 2,
    'YearsAtCompany': 5,
    'YearsInCurrentRole': 2,
    'YearsSinceLastPromotion': 1,
    'YearsWithCurrManager': 3
}

mode_features = {
    'Education': 3,
    'EnvironmentSatisfaction': 3,
    'JobInvolvement': 3,
    'JobLevel': 2,
    'JobSatisfaction': 3,
    'RelationshipSatisfaction': 3,
    'WorkLifeBalance': 3,
    'PerformanceRating': 3,
    'BusinessTravel': 'Travel_Rarely',
    'Department': 'Sales',
    'Gender': 'Male',
    'MaritalStatus': 'Single',
    'OverTime': 'No',
    'EducationField': 'Life Sciences',
    'JobRole': 'Sales Executive'
}

# --- User Inputs (only selected subset) ---

st.subheader("📝 Enter Employee Details")

user_input = {
    'Age': st.number_input("Age",18), 

    'Education': {
        "Below College": 1,
        "College": 2,
        "Bachelor’s": 3,
        "Master’s": 4,
        "Doctorate(PhD)": 5
        }[st.radio("Education qualification", ["Below College", "College", "Bachelor’s", "Master’s", "Doctorate(PhD)"], horizontal=True)],

    'EnvironmentSatisfaction' : st.radio(
        "Environment Satisfaction", 
        options=[1, 2, 3, 4, 5],
        format_func=lambda x: "⭐" * x,   # shows stars instead of numbers
        horizontal=True),

    'JobLevel': {
        "Junior": 1,
        "Senior": 2,
        "Lead": 3,
        "Team Lead": 4,
        "PC": 5
    }[st.radio("Job Level", ["Junior", "Senior", "Lead", "Team Lead", "PC"], horizontal=True)],

    'JobSatisfaction': st.radio(
        "Job Satisfaction", 
        options=[1, 2, 3, 4, 5],
        format_func=lambda x: "⭐" * x,   # shows stars instead of numbers
        horizontal=True),

    'MonthlyIncome': st.number_input("Monthly Income", 1000, 200000, 10000),

    'PercentSalaryHike': st.number_input("Percent Salary Hike", 0),

    'PerformanceRating': st.radio(
        "Performance Rating", 
        options=[1, 2, 3, 4, 5],
        format_func=lambda x: "⭐" * x,   # shows stars instead of numbers
        horizontal=True),

    'TotalWorkingYears': st.number_input("Total Working Years", 1),

    'WorkLifeBalance': st.radio(
        "WorkLife Balance", 
        options=[1, 2, 3, 4, 5],
        format_func=lambda x: "⭐" * x,   # shows stars instead of numbers
        horizontal=True),

    'YearsAtCompany': st.number_input("Years At Company", 0),

    'YearsSinceLastPromotion': st.number_input("Years Since Last Promotion", 0),

    'YearsWithCurrManager': st.number_input("Years With Current Manager", 0),

    'Department': st.radio(
        "Department", 
        ['Sales', 'Research & Development', 'Human Resources'],horizontal=True,
        ),

    'Gender': st.radio("Gender", ['Male', 'Female'],horizontal=True),

    'JobRole': st.selectbox("Job Role", ['Sales Executive', 'Research Scientist', 'Laboratory Technician',
                                         'Manufacturing Director', 'Healthcare Representative',
                                         'Manager', 'Sales Representative', 'Human Resources']),

    'MaritalStatus': st.radio("Marital Status", ['Single', 'Married', 'Divorced'],horizontal=True),

    'OverTime': st.radio("OverTime", ['Yes', 'No'],horizontal=True)
}

# --- Fill missing features with defaults ---
full_input = {**median_features, **mode_features, **user_input}

# Convert to DataFrame
input_df = pd.DataFrame([full_input])

# Ensure column order matches model training
expected_features = list(median_features.keys()) + list(mode_features.keys())
input_df = input_df[expected_features]


# --- Prediction Button ---
if st.button("🔍 Predict"):

    # Prediction
    pred_class = model.predict(input_df)[0]
    pred_proba = model.predict_proba(input_df)[0]

    # Map probability with labels
    class_labels = model.classes_
    probability_dict = {class_labels[i]: round(pred_proba[i], 3) for i in range(len(class_labels))}


    st.markdown("""---""")


    # --- Display Results ---
    st.subheader("🎯Prediction Result")
    st.write(f"**Predicted Attrition:** {pred_class}")

    if pred_class == "Yes":
        st.error("⚠️ Employee is likely to leave.")
    else:
        st.success("✅ Employee is likely to stay.")


    st.subheader("⚖️Prediction Probabilities")

    no_prob = pred_proba[class_labels.tolist().index("No")]
    yes_prob = pred_proba[class_labels.tolist().index("Yes")]

    no_prob = pred_proba[class_labels.tolist().index("No")]
    yes_prob = pred_proba[class_labels.tolist().index("Yes")]

    progress_html = f"""
    <div style="display: flex; width: 100%; height: 20px; border-radius: 10px; overflow: hidden; font-weight: bold; color: white;">
        <!-- No Probability -->
        <div style="width: {no_prob*100}%; background-color: #2ECC40; display: flex; align-items: center; justify-content: center; font-size: 12px;">
            {no_prob*100:.0f}%
        </div>
        <!-- Yes Probability -->
        <div style="width: {yes_prob*100}%; background-color: #FF4136; display: flex; align-items: center; justify-content: center; font-size: 12px;">
            {yes_prob*100:.0f}%
        </div>
    </div>
    """

    st.markdown(progress_html, unsafe_allow_html=True)
