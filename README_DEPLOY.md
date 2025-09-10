# Deploy Random Forest Metastasis Predictor

This project predicts metastasis based on Snail1 and EMT levels using a Random Forest model.

## Files
- `app.py` - Streamlit app interface
- `requirements.txt` - Python dependencies
- `model_rf.pkl` - Trained machine learning model

## Run locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy on Streamlit Cloud
1. Push these files (`app.py`, `requirements.txt`, `model_rf.pkl`) to a GitHub repo.
2. Go to https://share.streamlit.io/
3. Point the deployment to `app.py` in your repo.
4. Done 🎉
