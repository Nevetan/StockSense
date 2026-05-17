import pandas as pd

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

# Starting money
initial_money = 10000

money = initial_money
shares = 0

# Simulate trading
for i in range(len(data)):

    signal = data['Signal'][i]
    price = data['Close'][i]

    # BUY
    if signal == 1 and money > 0:
        shares = money / price
        money = 0

    # SELL
    elif signal == -1 and shares > 0:
        money = shares * price
        shares = 0

# Final portfolio value
final_value = money + (shares * data['Close'].iloc[-1])

profit = final_value - initial_money

print(f"Initial Money: ${initial_money:.2f}")
print(f"Final Portfolio Value: ${final_value:.2f}")
print(f"Profit/Loss: ${profit:.2f}")