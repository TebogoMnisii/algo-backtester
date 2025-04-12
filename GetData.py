import yfinance as yf

ticker = 'AAPL'  # or 'TSLA', 'MSFT', etc.
data = yf.download(ticker, start='2013-01-01', end='2023-12-31')
data.reset_index().to_csv('AAPL.csv', index=False)
