# # Download historical data of Amazon stock from yahoo finance
# import yfinance as yf

# def test_yfinance():
#     for symbol in ['AAPL']:
#         print(">>", symbol, end=' ... ')
#         try:
#             data = yf.download(symbol, start='2020-09-25', end='2020-10-02')
#             print(data)
#         except Exception as e:
#             print(f"Failed to retrieve data for {symbol}: {e}")

# if __name__ == "__main__":
#     test_yfinance()

# # Save the data into a csv file
# data.to_csv('AAPL.csv')


# OPTION 2 
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# def test_yfinance():
#     data = None  # Define data outside the loop
#     for symbol in ['AAPL']:
#         print(">>", symbol, end=' ... ')
#         try:
#             data = yf.download(symbol, start='2024-01-01', end='2024-06-19')
#             print(data)
#         except Exception as e:
#             print(f"Failed to retrieve data for {symbol}: {e}")
#     return data

# if __name__ == "__main__":
#     data = test_yfinance()
    
#     # Save the data into a csv file
#     if data is not None:
#         data.to_csv('AAPL.csv')
#     else:
#         print("No data to save.")

# # # Load the data from the csv file and plot it
# # data = pd.read_csv('AAPL.csv', index_col='Date', parse_dates=True)
# # data['Close'].plot(title='AAPL Stock Price')
# # plt.xlabel('Date')
# # plt.ylabel('Close Price')
# # plt.show()

# # Calculate Stochastic Oscillator using 20 periods with Upper Band 80 and Lower Band 20
# def Stochastic_Oscillator(data, periods=20):
#     data['L14'] = data['Low'].rolling(window=14).min()
#     data['H14'] = data['High'].rolling(window=14).max()
#     data['%K'] = (data['Close'] - data['L14'])*100/(data['H14'] - data['L14'])
#     data['%D'] = data['%K'].rolling(window=3).mean()
#     return data

# data = Stochastic_Oscillator(data)
# data[['%K', '%D']].plot(title='AAPL Stock Stochastic Oscillator')
# plt.xlabel('Date')
# plt.ylabel('Stochastic Oscillator')
# plt.show()

# # Plot both stock price and Stochastic Oscillator using plotly
# import plotly.graph_objects as go


# fig, ax1 = plt.subplots()
# ax1.set_xlabel('Date')
# ax1.set_ylabel('Price')
# ax1.plot(data['Close'], 'b-')
# ax2 = ax1.twinx()
# ax2.set_ylabel('Stochastic Oscillator')
# ax2.plot(data['%K'], 'r--') # Plot %K in red dash line
# ax2.plot(data['%D'], 'g-') # Plot %D in green solid line
# plt.title('AAPL Stock Price and Stochastic Oscillator')
# plt.show()


# OPTION 3 USING PLOTLY

import yfinance as yf
import pandas as pd
import plotly.graph_objects as go

def test_yfinance():
    data = None  # Define data outside the loop
    for symbol in ['AAPL']:
        print(">>", symbol, end=' ... ')
        try:
            data = yf.download(symbol, start='2024-01-01', end='2024-06-19')
            print(data)
        except Exception as e:
            print(f"Failed to retrieve data for {symbol}: {e}")
    return data

def Stochastic_Oscillator(data, periods=20):
    data['L14'] = data['Low'].rolling(window=14).min()
    data['H14'] = data['High'].rolling(window=14).max()
    data['%K'] = (data['Close'] - data['L14']) * 100 / (data['H14'] - data['L14'])
    data['%D'] = data['%K'].rolling(window=3).mean()
    return data

if __name__ == "__main__":
    data = test_yfinance()
    
    # Save the data into a csv file
    if data is not None:
        data.to_csv('AAPL.csv')
    else:
        print("No data to save.")
        
    # Apply Stochastic Oscillator
    if data is not None:
        data = Stochastic_Oscillator(data)

    # Plot the data using Plotly
    fig = go.Figure()

    # Add trace for closing prices
    fig.add_trace(go.Scatter(x=data.index, y=data['Close'], mode='lines', name='Close Price'))

    # Add traces for Stochastic Oscillator
    fig.add_trace(go.Scatter(x=data.index, y=data['%K'], mode='lines', name='%K'))
    fig.add_trace(go.Scatter(x=data.index, y=data['%D'], mode='lines', name='%D'))

    # Update layout
    fig.update_layout(
        title='AAPL Stock Price and Stochastic Oscillator',
        xaxis_title='Date',
        yaxis_title='Price / %K / %D',
        template='plotly_dark'
    )

    # Show the figure
    fig.show()












