import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv("india_weather.csv")

cols = ["prcp", "tmin", "tmax", "wspd", "pres"]
df = df[cols]

for c in cols:
    df[c] = pd.to_numeric(df[c], errors="coerce")

df.ffill(inplace=True)

# ✅ FIX: real rain threshold
df["rain"] = (df["prcp"] >= 2.0).astype(int)

X = df[["tmin", "tmax", "wspd", "pres"]]
y = df["rain"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier(
    n_estimators=150,
    max_depth=10,
    random_state=42
)

model.fit(X_train, y_train)

acc = accuracy_score(y_test, model.predict(X_test))
joblib.dump(model, "rain_model.pkl")

print(f"🌧 Rain model accuracy: {acc*100:.2f}%")
