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

def test_yfinance():
    data = None  # Define data outside the loop
    for symbol in ['AAPL']:
        print(">>", symbol, end=' ... ')
        try:
            data = yf.download(symbol, start='2000-09-25', end='2024-06-19')
            print(data)
        except Exception as e:
            print(f"Failed to retrieve data for {symbol}: {e}")
    return data

if __name__ == "__main__":
    data = test_yfinance()
    
    # Save the data into a csv file
    if data is not None:
        data.to_csv('AAPL.csv')
    else:
        print("No data to save.")

# Load the data from the csv file and plot it
data = pd.read_csv('AAPL.csv', index_col='Date', parse_dates=True)
data['Close'].plot(title='AAPL Stock Price')
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.show()







