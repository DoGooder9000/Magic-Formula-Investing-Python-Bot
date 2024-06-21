import yfinance
import pandas
from datetime import date, timedelta
from matplotlib import pyplot as plt

start_date = date.today()- timedelta(365)
end_date = date.today()

start_date.strftime('%Y-%m-%d')
end_date.strftime('%Y-%m-%d')

def closing_price(ticker: str):
	Asset = pandas.DataFrame(yfinance.download(ticker, start=start_date, end=end_date)['Adj Close'])
	print(Asset)
	return Asset

def show(ticker: str):
	price = closing_price(ticker)

	plt.plot(price)

	plt.title(ticker)

	plt.show()

show(input())

'''
with open("stocks.txt") as file:
	for stock in file:
		try:
			price = closing_price(stock)

			plt.plot(price)

			plt.title(stock)

			plt.show()
		
		except:
			pass
'''