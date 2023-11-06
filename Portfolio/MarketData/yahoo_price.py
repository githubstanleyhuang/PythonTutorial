import yfinance as yf

# Get the data for the stock AAPL
data = yf.download(['AAPL','AMZN'],'2016-01-01','2019-08-01')

# Import the plotting library
import matplotlib.pyplot as plt
#%matplotlib inline

# Plot the close price of the AAPL
data['Adj Close'].plot()
plt.show()