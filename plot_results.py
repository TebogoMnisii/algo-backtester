import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Example performance log
df = pd.read_csv("backtest_results.csv")

plt.figure(figsize=(12,6))
sns.lineplot(data=df, x='Date', y='PortfolioValue')
plt.title("Portfolio Performance Over Time")
plt.grid(True)
plt.show()
