import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page title
st.title("StockSense - Algorithmic Trading Dashboard")

# Load data
data = pd.read_csv("data/AAPL.csv", skiprows=2)

# Rename columns
data.columns = ['Date', 'Close', 'High', 'Low', 'Open', 'Volume']

# Convert Close to numeric
data['Close'] = pd.to_numeric(data['Close'])

# Moving averages
data['MA20'] = data['Close'].rolling(20).mean()
data['MA50'] = data['Close'].rolling(50).mean()

# Trading signals
data['Signal'] = 0

data.loc[data['MA20'] > data['MA50'], 'Signal'] = 1
data.loc[data['MA20'] < data['MA50'], 'Signal'] = -1

# Show dataframe
st.subheader("Stock Data")
st.write(data.tail())

# Create chart
fig, ax = plt.subplots(figsize=(12,6))

ax.plot(data['Close'], label='Close Price')
ax.plot(data['MA20'], label='20-Day MA')
ax.plot(data['MA50'], label='50-Day MA')

ax.set_title("AAPL Trading Analysis")

ax.legend()

# Display chart
st.pyplot(fig)

# Backtesting
initial_money = 10000

money = initial_money
shares = 0

for i in range(len(data)):

    signal = data['Signal'][i]
    price = data['Close'][i]

    if signal == 1 and money > 0:
        shares = money / price
        money = 0

    elif signal == -1 and shares > 0:
        money = shares * price
        shares = 0

final_value = money + (shares * data['Close'].iloc[-1])

profit = final_value - initial_money

# Show results
st.subheader("Backtesting Results")

st.write(f"Initial Money: ${initial_money:.2f}")
st.write(f"Final Portfolio Value: ${final_value:.2f}")
st.write(f"Profit/Loss: ${profit:.2f}")