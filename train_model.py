import pandas as pd
import numpy as np
import pickle
from sklearn.ensemble import RandomForestClassifier
import os

# 1. Load data
df = pd.read_csv("AAPL.csv", index_col=0)
df.index = pd.to_datetime(df.index)

# 2. Convert only columns that exist
numeric_cols = ['Open', 'High', 'Low', 'Close', 'Volume']
for col in numeric_cols:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')

# 3. Drop rows with missing values (from conversion or rolling NaNs)
df.dropna(inplace=True)

# 4. Create return column (target for modeling)
df['Return'] = df['Close'].pct_change()

# 5. Feature engineering
df['SMA20'] = df['Close'].rolling(20).mean()
df['Volatility'] = df['Return'].rolling(20).std()
df.dropna(inplace=True)  # Drop again due to rolling

# 6. Target variable: 1 if price goes up next day, else 0
df['Target'] = np.where(df['Close'].shift(-1) > df['Close'], 1, 0)

# 7. Features & labels
X = df[['SMA20', 'Volatility']]
y = df['Target']

# 8. Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# 9. Save model
os.makedirs("models", exist_ok=True)
with open("models/random_forest_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Random Forest model trained and saved successfully.")
