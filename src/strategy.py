import pandas as pd
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv("data/AAPL.csv", skiprows=2)

# Rename columns
data.columns = ['Date', 'Close', 'High', 'Low', 'Open', 'Volume']

# Convert Close to numeric
data['Close'] = pd.to_numeric(data['Close'])

# Moving averages
data['MA20'] = data['Close'].rolling(20).mean()
data['MA50'] = data['Close'].rolling(50).mean()

# Create signals
data['Signal'] = 0

# BUY signal
data.loc[data['MA20'] > data['MA50'], 'Signal'] = 1

# SELL signal
data.loc[data['MA20'] < data['MA50'], 'Signal'] = -1

# Print last rows
print(data[['Close', 'MA20', 'MA50', 'Signal']].tail())