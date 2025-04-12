# 📊 Algo Backtester with Machine Learning

A Python-based algorithmic trading backtesting engine that uses **Backtrader** to test **mean-reversion and momentum strategies** on 10+ years of historical stock data. Enhances signal generation using a **Random Forest Classifier** and evaluates risk-adjusted performance via **Sharpe Ratio**. Ideal for learning how to blend classical quant methods with machine learning in finance.

---

## 🚀 Features

- ⏳ Backtests on 10+ years of OHLC data (via Yahoo Finance)
- 📈 Implements a mean-reversion strategy using SMA and Standard Deviation bands
- 🧠 Trains a Random Forest model to classify next-day price direction
- 📉 Tracks Sharpe Ratio and final portfolio value
- 📊 Visualizes portfolio performance over time
- 🗂️ Modular architecture for easy strategy/model expansion

---

## 🗂️ Project Structure


---

## 🧠 Strategy Logic

### 📉 Mean Reversion
- Uses 20-day Simple Moving Average (SMA)
- Buys when price drops below SMA − 1.5 × standard deviation
- Sells when price rises above SMA + 1.5 × standard deviation
- Closes trades when price reverts to SMA

### 🧠 Machine Learning (Random Forest)
- **Features**: 20-day SMA, 20-day rolling volatility
- **Label**: 1 if price goes up the next day, else 0
- **Model**: Random Forest Classifier with 100 estimators
- **Usage**: Can be used to filter strategy signals (future integration idea)

---

## 📦 Installation

Install required packages:

bash
pip install backtrader yfinance pandas scikit-learn matplotlib seaborn

Sample Output
Final Portfolio Value: $99,868.41

Sharpe Ratio: -77.72

Results Saved To: backtest_results.csv
Note: This result shows the base strategy with no ML filter. Future improvements can raise Sharpe ratio significantly.
📚 Skills Demonstrated
Quantitative strategy design

Time series data analysis

Backtesting using Backtrader

Machine Learning with scikit-learn

Performance evaluation with Sharpe Ratio

Python OOP, modular scripting,

Built by Tebogo Mnisi, a Statistics & Data Science student passionate about quantitative finance, algorithmic trading, and machine learning.

🧠 “The goal wasn’t perfection — it was to learn, experiment, and iterate.”
