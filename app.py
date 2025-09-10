import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open("model_rf.pkl", "rb") as f:
    model = pickle.load(f)

st.set_page_config(page_title="Metastasis Predictor", page_icon="🧬")

st.title("🧬 Metastasis Predictor")
st.write("Predict the likelihood of metastasis based on **Snail1** and **EMT** levels.")

# Input section
st.subheader("Input Parameters")

snail = st.selectbox("Snail1 Level", [1, 2, 3], index=0, help="1 = Low, 2 = Moderate, 3 = High")
emt = st.selectbox("EMT Level", [1, 2, 3], index=0, help="1 = Low, 2 = Moderate, 3 = High")

# Predict button
if st.button("🔮 Predict"):
    features = np.array([[snail, emt]])
    prediction = model.predict(features)[0]
    result = "Yes (2)" if prediction == 2 else "No (1)"
    st.success(f"Predicted Metastasis: **{result}**")
