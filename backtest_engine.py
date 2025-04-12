import backtrader as bt
import pandas as pd
from datetime import datetime


# Import your strategy
from mean_reversion import MeanReversion


# Observer to track portfolio values
class PortfolioObserver(bt.Observer):
    lines = ('portfolio_value', 'returns',)
    plotinfo = dict(plot=False)

    def __init__(self):
        self.starting_cash = None

    def next(self):
        if self.starting_cash is None:
            self.starting_cash = self._owner.broker.getvalue()
        self.lines.portfolio_value[0] = self._owner.broker.getvalue()
        self.lines.returns[0] = (
            self.lines.portfolio_value[0] - self.starting_cash
        ) / self.starting_cash


def run_backtest(csv_path, strategy, cash=100000):
    # Load and clean data
    df = pd.read_csv(csv_path, index_col='Date', parse_dates=True)

    # Keep only the necessary columns and ensure they're numeric
    numeric_cols = ['Open', 'High', 'Low', 'Close', 'Volume']
    df = df[numeric_cols]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    df.dropna(inplace=True)

    # Setup backtrader engine
    cerebro = bt.Cerebro()
    data = bt.feeds.PandasData(dataname=df)
    cerebro.adddata(data)
    cerebro.addstrategy(strategy)
    cerebro.broker.set_cash(cash)
    cerebro.addanalyzer(bt.analyzers.SharpeRatio, _name='sharpe')
    cerebro.addobserver(PortfolioObserver)

    print(f"📈 Running backtest on {csv_path}...")

    results = cerebro.run()
    final_value = cerebro.broker.getvalue()
    sharpe = results[0].analyzers.sharpe.get_analysis()

    print(f"✅ Final Portfolio Value: ${final_value:.2f}")
    print(f"📊 Sharpe Ratio: {sharpe.get('sharperatio', 'N/A')}")

    # Extract portfolio values over time
    value_line = results[0].observers.portfolioobserver.lines.portfolio_value
    returns_line = results[0].observers.portfolioobserver.lines.returns

    portfolio_values = [
        {
            'Date': date,
            'PortfolioValue': value,
            'Returns': ret
        }
        for date, value, ret in zip(df.index, value_line.array, returns_line.array)
        if not pd.isna(value) and not pd.isna(ret)
    ]

    results_df = pd.DataFrame(portfolio_values)
    results_df.to_csv('backtest_results.csv', index=False)
    print("📁 Results saved to backtest_results.csv")

    # Plot
    cerebro.plot()


# Entry point
if __name__ == '__main__':
    run_backtest('AAPL.csv', MeanReversion)
