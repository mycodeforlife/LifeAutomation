# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
import requests
import json

class NewsFeedsFromSeekingAlpha:
	
	symbol = "CTL"
	base_url = "http://seekingalpha.com/api/sa/combined/"
	request_url = base_url+symbol
	news_response_json="["


	def __init__(self,Symbol):

		self.request_url = self.base_url+Symbol
		# setting User-Agent
		headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36'}
		response = requests.get(self.request_url, headers=headers)
		temp = response.content
		
		# trying to replace special character to fix the Unicode error: UnicodeEncodeError: 'ascii' codec can't encode character u'\u2019' in position 30: ordinal not in range(128)

		original_str = "<?xml version=\"1.0\"?>"
		new_str = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>"

		temp = temp.replace(original_str,new_str)
		response_data = temp.replace("&#x2019;","")
		
		root = ET.fromstring(response_data)
		
		for country in root.findall('channel'):
			for i in country.findall('item'):
				news_date = str(i.find("pubDate").text)
				news_title = str(i.find("title").text)
				news_url = str(i.find("link").text)
				self.news_response_json = self.news_response_json+"{\"title\":\""+news_title+"\",\"url\":\""+news_url+"\",\"publishedDate\":\""+news_date+"\"},"

		self.news_response_json=self.news_response_json.rstrip(",")		
		self.news_response_json=self.news_response_json+"]"

	def getNewsInJSONFormat(self):
		return json.loads(self.news_response_json)
	
