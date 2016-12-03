#! /usr/bin/python

from flask import Flask, jsonify, json
from yahoo_finance import Share
from StockAnalysis import * 
from FavoriteStock import *
from flask import request
#from flask_httpauth import HTTPBasicAuth


app = Flask(__name__)
quote = Share('YHOO') 


'''
auth = HTTPBasicAuth()
@auth.get_password
def get_password(username):
    if username == 'miguel':
        return 'python'
    return None

@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)
'''

@app.route('/')
def index():
    return "Welcome to financial automation !"

@app.route('/stockautomation/api/v1.0/getquote/<stockcode>',methods=['GET'])
# @auth.login_required
def get_quote(stockcode):
	myStockAnalysis = StockAnalysis(stockcode)
	data = myStockAnalysis.getStockPriceInfo(stockcode)
	return jsonify(data)
	

@app.route('/stockautomation/api/v1.0/getnumoutstandingshares/<stockcode>',methods=['GET'])
def get_historic_low(stockcode):
	myStockAnalysis = StockAnalysis(stockcode)
	data = myStockAnalysis.getNumberOfOutStandingShares(stockcode)
	return jsonify(data)

@app.route('/stockautomation/api/v1.0/getdividenddates/<stockcode>',methods=['GET'])
def get_dividend_details(stockcode):
	myStockAnalysis = StockAnalysis(stockcode)
	data = myStockAnalysis.getExDividedDate(stockcode)
	return jsonify(data)

@app.route('/stockautomation/api/v1.0/getdividendyield/<stockcode>',methods=['GET'])	
def get_dividend_yield_info(stockcode):
	myStockAnalysis = StockAnalysis(stockcode)
	data = myStockAnalysis.getDividendYieldInfo(stockcode)
	return jsonify(data)

@app.route('/stockautomation/api/v1.0/favorite/',methods=['POST'])
def add_to_favorite_stock():
	if not 'Symbol' in request.json:
		return "symbol not there in post body"
	else:
		stockcode = request.json["Symbol"]
		favStock = FavoriteStock();
		favStock.addFavoriteStock(stockcode,"NYSE")
	return stockcode,201
 

@app.route('/stockautomation/api/v1.0/getfavstock/',methods=['GET'])
def get_fav_stock():
        myFavStock = FavoriteStock()
        data = myFavStock.getFavoriteStockList()
	fav_list = []
	for i in data: 
		tmp={}
		tmp["Symbol"]=i
		fav_list.append(tmp)

	return jsonify(fav_list)


if __name__ == '__main__':
    app.run(port=8081, debug=True)

