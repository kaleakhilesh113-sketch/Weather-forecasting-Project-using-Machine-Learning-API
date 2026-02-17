# AI Weather Forecast System

An end-to-end ML system that provides real-time weather and predictions
for any city or village in India.

## Features
- Live weather (Open-Meteo API)
- Temperature prediction (XGBoost)
- Rain probability (Random Forest)
- Streamlit dashboard
- RMSE / MAE evaluation

## How to Run
pip install -r requirements.txt
python extract_dataset.py
python train_model.py
python train_rain_model.py
streamlit run app.py
