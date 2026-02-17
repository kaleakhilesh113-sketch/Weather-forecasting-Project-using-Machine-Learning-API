import pandas as pd
import joblib
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

df = pd.read_csv("india_weather.csv")

cols = ["tavg", "tmin", "tmax", "prcp", "wspd", "pres"]
df = df[cols]

for c in cols:
    df[c] = pd.to_numeric(df[c], errors="coerce")

df.ffill(inplace=True)
df["tavg_lag1"] = df["tavg"].shift(1)
df.dropna(inplace=True)

X = df[["tmin", "tmax", "prcp", "wspd", "pres", "tavg_lag1"]]
y = df["tavg"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = joblib.load("weather_model.pkl")
preds = model.predict(X_test)

rmse = np.sqrt(mean_squared_error(y_test, preds))
print(f"📊 RMSE: {rmse:.2f} °C")
