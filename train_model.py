# import pandas as pd
# import joblib
# from sklearn.model_selection import train_test_split
# from xgboost import XGBRegressor

# # Load dataset
# df = pd.read_csv("india_weather.csv")

# print("Initial rows:", len(df))

# # Required columns
# cols = ["tavg", "tmin", "tmax", "prcp", "wspd", "pres"]
# df = df[cols]

# # Convert to numeric
# for c in cols:
#     df[c] = pd.to_numeric(df[c], errors="coerce")

# # Fill missing values
# df.ffill(inplace=True)

# # Drop rows without target
# df = df.dropna(subset=["tavg"])

# print("Rows after cleaning:", len(df))

# # Lag feature
# df["tavg_lag1"] = df["tavg"].shift(1)
# df = df.dropna(subset=["tavg_lag1"])

# print("Rows after lag feature:", len(df))

# # Features & target
# features = ["tmin", "tmax", "prcp", "wspd", "pres", "tavg_lag1"]
# X = df[features]
# y = df["tavg"]

# # Split
# X_train, X_test, y_train, y_test = train_test_split(
#     X, y, test_size=0.2, random_state=42
# )

# # Train model
# model = XGBRegressor(
#     n_estimators=200,
#     learning_rate=0.05,
#     max_depth=6,
#     random_state=42
# )

# model.fit(X_train, y_train)

# # Save model
# joblib.dump(model, "weather_model.pkl")

# print("✅ MODEL TRAINED SUCCESSFULLY")
# print("📁 Saved as weather_model.pkl")
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor

df = pd.read_csv("india_weather.csv")

cols = ["tavg", "tmin", "tmax", "prcp", "wspd", "pres"]
df = df[cols]

for c in cols:
    df[c] = pd.to_numeric(df[c], errors="coerce")

df.ffill(inplace=True)
df.dropna(subset=["tavg"], inplace=True)

df["tavg_lag1"] = df["tavg"].shift(1)
df.dropna(inplace=True)

X = df[["tmin", "tmax", "prcp", "wspd", "pres", "tavg_lag1"]]
y = df["tavg"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = XGBRegressor(
    n_estimators=200,
    learning_rate=0.05,
    max_depth=6,
    random_state=42
)

model.fit(X_train, y_train)
joblib.dump(model, "weather_model.pkl")

print("✅ Temperature prediction model trained")
