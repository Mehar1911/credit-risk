import streamlit as st
import pandas as pd
import joblib

model = joblib.load("extra_trees_credit_model.pkl")

# Manual string → integer maps (verify against your debug output)
sex_map = {"male": 1, "female": 0}
housing_map = {"free": 0, "own": 1, "rent": 2}
saving_map = {"little": 0, "moderate": 1, "quite rich": 2, "rich": 3}
checking_map = {"little": 0, "moderate": 1, "rich": 2, "quite rich": 3}

st.title("Credit Risk Prediction App")
st.write("Enter applicant information to predict credit risk")

age = st.number_input("Age", min_value=18, max_value=80, value=30)
sex = st.selectbox("Sex", list(sex_map.keys()))
job = st.number_input("Job (0-3)", min_value=0, max_value=3, value=1)
housing = st.selectbox("Housing", list(housing_map.keys()))
saving_accounts = st.selectbox("Saving Accounts", list(saving_map.keys()))
checking_accounts = st.selectbox("Checking Accounts", list(checking_map.keys()))
credit_amount = st.number_input("Credit Amount", min_value=0, value=1000)
duration = st.number_input("Duration (months)", min_value=1, value=12)

input_df = pd.DataFrame({
    "Age": [age],
    "Sex": [sex_map[sex]],
    "Job": [job],
    "Housing": [housing_map[housing]],
    "Saving accounts": [saving_map[saving_accounts]],
    "Checking account": [checking_map[checking_accounts]],
    "Credit amount": [credit_amount],
    "Duration": [duration]
})

if st.button("Predict Risk"):
    pred = model.predict(input_df)[0]
    if pred == 1:
        st.success("The predicted credit risk is: **GOOD**")
    else:
        st.error("The predicted credit risk is: **BAD**")