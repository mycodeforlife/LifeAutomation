import json
import csv 

class dataParser:
	file_name = ""
	TestCaseDataMap = {}
	TestCaseExpectedResult = {}
	def __init__(self,filename):
		self.file_name = filename

	def constructDataSet(self):
		with open(self.file_name,'rb') as csvfile: 
			data = csv.DictReader(csvfile)
			for i in data:
				self.TestCaseDataMap[i["testcase_id"]] = json.dumps(i)
				
	def getTestCaseData(self,testcaseid):
			return self.TestCaseDataMap[testcaseid]




