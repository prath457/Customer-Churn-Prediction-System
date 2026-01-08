!pip install streamlit
import streamlit as st
import pandas as pd
import pickle

# Load model and columns
model = pickle.load(open("churn_model.pkl", "rb"))
columns = pickle.load(open("columns.pkl", "rb"))

st.title("📊 Customer Churn Prediction App")

st.write("Enter customer details to predict churn")

# User Inputs
tenure = st.number_input("Tenure (Months)", 0, 72)
monthly_charges = st.number_input("Monthly Charges", 0.0, 200.0)
total_charges = st.number_input("Total Charges", 0.0, 10000.0)

# Create input dataframe
input_data = pd.DataFrame([[tenure, monthly_charges, total_charges]],
                          columns=["tenure", "MonthlyCharges", "TotalCharges"])

# Add missing columns
for col in columns:
    if col not in input_data.columns:
        input_data[col] = 0

input_data = input_data[columns]

# Predict
if st.button("Predict Churn"):
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("⚠️ Customer is likely to CHURN")
    else:
        st.success("✅ Customer is likely to STAY")
