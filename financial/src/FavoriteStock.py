from MyStockDB import *

class FavoriteStock:
	
	mystockdb = MyStockDB("localhost","root","admin","mystockdb")
	
	def __init__(self):
		# TBD: db configuration will be pulled from confi file
		self.mystockdb = MyStockDB("localhost","root","admin","mystockdb")

	def addFavoriteStock(self,symbol,market):
		self.mystockdb.store_fav_stock(symbol,market)
		self.mystockdb.close_db_connection()

	def removeFavoriteStock(self,symbol):
		pass

	def getFavoriteStockList(self):
		return self.mystockdb.get_fav_stock_list()



