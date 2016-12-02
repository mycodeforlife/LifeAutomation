import MySQLdb

class MyStockDB:
	db =  MySQLdb.connect(host="localhost",user="root",passwd="admin",db="mystockdb")

	def __init__(self,host_ip,user_name,password,db_name):
		self.db=MySQLdb.connect(host=host_ip,user=user_name,passwd=password,db=db_name)

	def store_fav_stock(self,symbol,MarketSymbol):
		cur = self.db.cursor()
		save_fav_stock_query = "insert into mystockdb.fav_stock (Symbol,Market,AddedDate) values (\""+symbol+"\",\""+MarketSymbol+"\",CURDATE())"
		cur.execute(save_fav_stock_query)
		self.db.commit()

	def get_fav_stock_list(self):
		cur = self.db.cursor()
		cur.execute("SELECT Symbol FROM mystockdb.fav_stock")
		tmp = cur.fetchall()
		fav_stock_list = []
		for i in tmp:
			fav_stock_list.append(i[0])
		return fav_stock_list

	def close_db_connection(self):
		self.db.close()


