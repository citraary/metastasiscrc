app_code = """import streamlit as st
import pickle
import numpy as np

# Load trained model
with open("model_rf.pkl", "rb") as f:
    model = pickle.load(f)

st.title("Metastasis Predictor")
st.write("Predict metastasis based on Snail1 and EMT levels")

# Input values
snail = st.selectbox("Snail1 Level", [1, 2, 3], index=0)
emt = st.selectbox("EMT Level", [1, 2, 3], index=0)

if st.button("Predict"):
    features = np.array([[snail, emt]])
    pred = model.predict(features)[0]
    result = "Yes (2)" if pred == 2 else "No (1)"
    st.success(f"Predicted Metastasis: {result}")
"""

with open("app.py", "w") as f:
    f.write(app_code)

print("Streamlit app saved to app.py")


reqs = """pandas
scikit-learn
streamlit
openpyxl
nbformat
"""

with open("requirements.txt", "w") as f:
    f.write(reqs)

print("requirements.txt written")


readme = """# Deploy Random Forest Metastasis Predictor

This project trains a Random Forest model using Snail1 and EMT levels to predict metastasis.

## Files
- `random_forest_metastasis.ipynb` - Training notebook
- `model_rf.pkl` - Trained model
- `app.py` - Streamlit app
- `requirements.txt` - Dependencies

## Run locally
```bash
pip install -r requirements.txt
streamlit run app.py