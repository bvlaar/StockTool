#Get a stock quote
import ystockquote

def data_type():
	print "From the list above, enter the data type you'd like to see"
	data = raw_input("> ")
	print "What stock would you like to see data on?"
	stock = raw_input("> ")
	if data == 'price' or data == 'Price':
		print ystockquote.get_price(stock)
	elif data == 'change' or data == 'Change':
		print ystockquote.get_change(stock)
	elif data == 'Volume' or data == 'volume':
		print ystockquote.get_avg_daily_vol(stock)
	elif data == 'exchange' or data == 'Exchange':
		print ystockquote.get_stock_exchange(stock)
	elif data == 'market cap' or data == 'Market cap' or data == 'Market Cap':
		print ystockquote.get_market_cap(stock)
	elif data == 'book value' or data == 'Book value' or data == 'Book Value':
		print ystockquote.get_book_value(stock)
	elif data == 'eps' or data == 'EPS':
		print ystockquote.get_earnings_per_share(stock)
	elif data == 'short ratio' or data == 'Short Ratio':
		print ystockquote.get_short_ratio(stock)
	elif data == 'dividend yield' or data == 'Dividend Yield' or data == 'div yield':
		print ystockquote.get_dividend_yield(stock)
	elif data == 'ebitda' or data == 'EBITDA':
		print ystockquote.get_ebitda(stock)
	else:
		print 'Sorry, we don\'t have that data type'
		quit()



print """
******************************************************************
This script will allow you to pull data about a stock from the web

The following is data that you can pull about a particular firm:
Price
Change
Volume
Average Daily Volume
Exchange
Market Cap
Book Value
EPS
Short Ratio
Dividend Yield
EBITDA
******************************************************************
"""
data_type()




