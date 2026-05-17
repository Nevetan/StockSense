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

# Plot
plt.figure(figsize=(12,6))

plt.plot(data['Close'], label='Close Price')
plt.plot(data['MA20'], label='20-Day MA')
plt.plot(data['MA50'], label='50-Day MA')

plt.title("AAPL Trading Analysis")

plt.xlabel("Days")
plt.ylabel("Price")

plt.legend()

plt.show()