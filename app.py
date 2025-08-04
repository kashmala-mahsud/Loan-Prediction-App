import streamlit as st
import pandas as pd
import joblib

# Load model and preprocessing artifacts
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")
expected_columns = joblib.load("columns.pkl")

st.title("🏦 Loan Approval Prediction App")
st.markdown("Enter applicant details to predict if the loan will be approved.")

# --- INPUT FORM ---
gender = st.selectbox("Gender", ["Male", "Female"])
married = st.selectbox("Married", ["Yes", "No"])
dependents = st.selectbox("Number of Dependents", ["0", "1", "2", "3+"])
education = st.selectbox("Education", ["Graduate", "Not Graduate"])
self_employed = st.selectbox("Self Employed", ["Yes", "No"])
applicant_income = st.number_input("Applicant Income", min_value=0.0, step=500.0)
coapplicant_income = st.number_input("Coapplicant Income", min_value=0.0, step=500.0)
loan_amount = st.number_input("Loan Amount (in thousands)", min_value=0.0, step=10.0)
loan_amount_term = st.selectbox("Loan Amount Term (in months)", [360.0, 120.0, 180.0, 240.0, 300.0])
credit_history = st.selectbox("Credit History (1 = Good, 0 = Bad)", [1.0, 0.0])
property_area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])

# --- ENCODE USER INPUT ---
input_dict = {
    'Gender_Male': 1 if gender == "Male" else 0,
    'Married_Yes': 1 if married == "Yes" else 0,
    'Dependents': 3 if dependents == "3+" else int(dependents),
    'Education_Not Graduate': 1 if education == "Not Graduate" else 0,
    'Self_Employed_Yes': 1 if self_employed == "Yes" else 0,
    'ApplicantIncome': applicant_income,
    'CoapplicantIncome': coapplicant_income,
    'LoanAmount': loan_amount,
    'Loan_Amount_Term': loan_amount_term,
    'Credit_History': credit_history,
    'Property_Area_Semiurban': 1 if property_area == "Semiurban" else 0,
    'Property_Area_Urban': 1 if property_area == "Urban" else 0
}

# Prepare input DataFrame
input_df = pd.DataFrame([input_dict])

# Fill missing expected columns with 0
for col in expected_columns:
    if col not in input_df.columns:
        input_df[col] = 0
input_df = input_df[expected_columns]  # ensure correct column order

# --- PREDICT ---
if st.button("Predict Loan Status"):
    try:
        scaled_input = scaler.transform(input_df)
        prediction = model.predict(scaled_input)[0]
        if prediction == 1:
            st.success("✅ Loan Approved")
        else:
            st.error("❌ Loan Rejected: Consider improving Credit History, Income, or Collateral.")
    except Exception as e:
        st.error(f"⚠️ Error during prediction: {e}")
