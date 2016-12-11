from MyStockDB import *


class StockExchanges:
	mystockdb = MyStockDB("localhost","root","admin","mystockdb")
	
	def __init__(self):
		self.mystockdb = MyStockDB("localhost","root","admin","mystockdb")

	def getListOfExchanges(self):
		return self.mystockdb.get_stock_exchange()

	def getExchangeSymbol(self,Name):
		pass
	def getExchangeName(self,Symbol):
		pass
