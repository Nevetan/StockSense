import yfinance as yf

data = yf.download("AAPL", start="2022-01-01")

print(data.head())

data.to_csv("data/AAPL.csv")