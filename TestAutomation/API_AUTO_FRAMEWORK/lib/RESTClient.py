import requests
import json

'''
In this class we need to maintain the same session for authentication as well as rest of the request. 
For this reason we are creaging request session and maintaing that per instance. 
'''

class RESTClient:
		url = ""
		content_headers = {"Content-type":"application/json"}
		s = requests.Session()
		
		def __init__(self,protocol,ip,port):
			self.url = protocol+"://"+ip+":"+port+"/"
			self.s = requests.Session()
			
		def makePOSTRequest(self,url,testdata,auth_token=None):
			req_url = self.url+url
			self.s.headers.update(self.content_headers)
			print "Request URL: "+req_url
			print "Method: POST"
			print "Request Header: "+str(self.content_headers)
			print "POST Request BODY: "+str(testdata)
			if auth_token is None:
				pass
			else:
				self.content_headers = {'accept':'application/json','Content-type':'application/json'}
				self.content_headers['fpc-sid'] = str(auth_token)
				self.s.headers.update(self.content_headers)
				print "Updated request header with Authentication token"
				print self.s.headers
			print testdata
			response_json = self.s.post(req_url,data=testdata,verify=False)
			return response_json 
		

		def makeGETRequest(self,url,data,auth_token):
			req_url = self.url+url
			self.content_headers = {'accept':'application/json','Content-type':'application/json'}
			self.content_headers['fpc-sid'] = str(auth_token)
			print "Request URL: "+req_url
			print "Method: GET"
			print "Request Header: "+str(self.content_headers)
			self.s.headers.update(self.content_headers)
			response_json = self.s.get(req_url,verify=False)
			return response_json


