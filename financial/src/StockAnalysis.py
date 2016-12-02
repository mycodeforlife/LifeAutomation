#! /usr/bin/python 

from yahoo_finance import Share

class StockAnalysis:

	stock_symbol = 'YHOO'	

	def __init__(self,symbol):
		self.stock_symbol = symbol
	
	def getStockSymbol(self):
		return self.stock_symbol 

	def getStockPriceInfo(self,symbol):
		quote = Share(symbol)
		stock_price = quote.get_price()
		currency = quote.get_currency()
		price_info = {'Symbol':symbol,'Price':stock_price,'Currency':currency}
		return price_info

	def getDividendYieldInfo(self,symbol):
		quote = Share(symbol)
		dividend_yield = quote.get_dividend_yield()
		dividend_info = {'Symbol':symbol,'DividendYield':dividend_yield,'Unit':'%'}
		return dividend_info


	def getExDividedDate(self,symbol):
		quote = Share(symbol)
		hold_date = quote.get_ex_dividend_date()
		payout_date = quote.get_dividend_pay_date()
		data = {'Symbol':symbol,'ExDividedDate':hold_date,'LastPayoutDate':payout_date}
		return data
		
	def isDividedRateHealthy(self):
		pass
	def getDividendDateDetails(self):
		pass
	def getNumberOfOutStandingShares(self,symbol):
		quote = Share(symbol)
		total_market_cap = quote.get_market_cap()
		current_price = quote.get_prev_close()
		if "B" in total_market_cap:
			total_market_cap = total_market_cap.rstrip("B")
			total_market_cap = float(total_market_cap)*1000000000
		elif "M" in total_market_cap:
			total_market_cap = total_market_cap.rstrip("M")
			total_market_cap = float(total_market_cap)*100000000
		out_standing_shares = (total_market_cap/float(current_price))/1000000
		out_standing_shares = round(out_standing_shares,2)
		data = {'Symbol':symbol,'OutStandingShares':out_standing_shares}
		return data

	def getPERation(self):
		pass
	
