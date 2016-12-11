import pytest 
import sys 

sys.path.append("../lib/")
sys.path.append("../sys/")

from RESTClient import *
from dataParser import *


class TestGetStockDetailsAPI:
	dp = dataParser("../inputs/stock_api.csv")
	dp.constructDataSet()
	rest_client = RESTClient("http","127.0.0.1","8081")
	
	def test_getStockQuoteAPIValidInputs(self):
		testdata = json.loads(self.dp.getTestCaseData("1"))
		test_url = testdata['base_url']+testdata['symbol']
		response_data = self.rest_client.makeGETRequest(test_url,"",None)
		assert response_data.status_code == 200
