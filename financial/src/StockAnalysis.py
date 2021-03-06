#! /usr/bin/python 

from yahoo_finance import Share

class StockAnalysis:

	stock_symbol = 'YHOO'	
	stock_company_name = "Yahoo Inc,"
	quote = Share(stock_symbol)
	name = quote.get_name()
	stock_company_name = name.split(". ")

	def __init__(self,symbol):
		self.stock_symbol = symbol
		self.quote = Share(self.stock_symbol)
		self.name = self.quote.get_name()
		self.stock_company_name = self.name.split(". ")
		
		
	def getStockSymbol(self):
		return self.stock_symbol 

	def getStockPriceInfo(self,symbol):
		stock_price = self.quote.get_price()
		currency = self.quote.get_currency()
		#name = self.quote.get_name()
		#stock_company_name = name.split(". ")
		price_info = {'Symbol':symbol,'Price':stock_price,'Currency':currency,'Name':self.stock_company_name[0]}
		return price_info

	def getDividendYieldInfo(self,symbol):
		dividend_yield = self.quote.get_dividend_yield()
		dividend_info = {'Symbol':symbol,'DividendYield':dividend_yield,'Unit':'%'}
		return dividend_info

	def getPayOurRatio(self,symbol):
		dividend_per_share = self.quote.get_dividend_share()
		EPS_current_year = self.quote.get_EPS_estimate_current_year()
		pay_out_ratio = (float(dividend_per_share) / float(EPS_current_year))*100
		pay_out_ratio =  float("{0:.2f}".format(pay_out_ratio))
		pay_out_info = {'Symbol':symbol,'PayOut Ratio':pay_out_ratio, "Unit":"%",'Name':self.stock_company_name[0]}
		return pay_out_info

	def getDeividendDetails(self,symbol):
		dividend_per_share = self.quote.get_dividend_share()
		EPS_current_year = self.quote.get_EPS_estimate_current_year()
		dividend_yield = self.quote.get_dividend_yield()
		hold_date = self.quote.get_ex_dividend_date()
		payout_date = self.quote.get_dividend_pay_date()

		if dividend_per_share is None:
			dividend_per_share = "0"
			dividend_yield = "0%"
			payout_date = "None"
			hold_date = "None"
		pay_out_ratio = (float(dividend_per_share) / float(EPS_current_year))*100
		pay_out_ratio =  str(float("{0:.2f}".format(pay_out_ratio)))+"%"
		
		dividend_info = {'Symbol':symbol, 'DividedPerShare':dividend_per_share, 'EPSCurrentYearEstimation': EPS_current_year, 'PayOutRatio':pay_out_ratio,'ExDividedDate':hold_date,'LastPayoutDate':payout_date,'DividendYield':dividend_yield,'Name':self.stock_company_name[0]}
		return dividend_info
	
	def getExDividedDate(self,symbol):
		hold_date = self.quote.get_ex_dividend_date()
		payout_date = self.quote.get_dividend_pay_date()
		data = {'Symbol':symbol,'ExDividedDate':hold_date,'LastPayoutDate':payout_date,'Name':self.stock_company_name[0]}
		return data
		
	def isDividedRateHealthy(self):
		pass

	def getDividendDateDetails(self):
		pass
	def getNumberOfOutStandingShares(self,symbol):
		total_market_cap = self.quote.get_market_cap()
		current_price = self.quote.get_prev_close()
		if "B" in total_market_cap:
			total_market_cap = total_market_cap.rstrip("B")
			total_market_cap = float(total_market_cap)*1000000000
		elif "M" in total_market_cap:
			total_market_cap = total_market_cap.rstrip("M")
			total_market_cap = float(total_market_cap)*100000000
		out_standing_shares = (total_market_cap/float(current_price))/1000000
		out_standing_shares = round(out_standing_shares,2)
		data = {'Symbol':symbol,'OutStandingShares':out_standing_shares,'Name':self.stock_company_name[0]}
		return data

	def get200DaysLowPrice(self,symbol):
		pass
	def get200DaysHighPrice(self,symbol):
		pass
	
	def get50DaysLowPrice(self,symbol):
		pass
	def get50DaysHighPrice(self,symbol):
		pass
	def getPERation(self):
		pass
	
