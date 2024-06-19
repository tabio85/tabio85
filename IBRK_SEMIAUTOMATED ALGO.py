# Download historical data of Amazon stock from yahoo finance
import yfinance as yf

def test_yfinance():
    for symbol in ['AAPL', 'MSFT', 'VFINX', 'BTC-USD']:
        print(">>", symbol, end=' ... ')
        try:
            data = yf.download(symbol, start='2020-09-25', end='2020-10-02')
            print(data)
        except Exception as e:
            print(f"Failed to retrieve data for {symbol}: {e}")

if __name__ == "__main__":
    test_yfinance()




