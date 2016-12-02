# LifeAutomation
Life Automation is my dream project where I wanted to automate things what I do on daily basis.


----------------------------------------------------------------------------
	Requirement: 
----------------------------------------------------------------------------
python version: 2.7.12
pip version: pip-9.0.1
yahoo-finance: yahoo-finance-1.4.0 
mysql: 5.7.6 or up

----------------------------------------------------------------------------
			Installation Steps 
----------------------------------------------------------------------------

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
			installation of flask 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
>> If you are using python 2.7.X verison then following steps works for you to setup Flask 

$ sudo python -m virtualenv flask
$ source flask/bin/activate
$ sudo pip install flask
$ deactivate

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 
	Installing yahoo finance module to get the information about stocks 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 
$ sudo pip install yahoo-finance 

How to check if you have right version of yahoo-finance module? 

---------------------------------
#! /usr/bin/pyhon 

import yahoo_finance
print yahoo_finance.__version__
---------------------------------

execute above  program, output should show version number as 1.4.0 
if not then run the following steps, that should get you to latest version of yahoo finance module. 

git clone git://github.com/lukaszbanasiak/yahoo-finance.git
cd yahoo-finance
python setup.py install

----------------------------------------------------------------------------------
After instalation make sure you create default schema and table for this code to work
sql queries are available in ./financial/db/initial_schema.sql


----------------------------------------------------------------------------------
----------------------------------------------------------------------------------
REST API Docs
Version: 1.0 
Edited Date: Dec 1st 2016
----------------------------------------------------------------------------------
----------------------------------------------------------------------------------

Get most recnent stock price: 
http://<localhost:5000>/stockautomation/api/v1.0/getquote/<Stock Symbol> 
METHOD: GET 
PRAMETERS: Stock Symbol

Example: 
http://localhost:5000/stockautomation/api/v1.0/getquote/CTL

JSON RESPONSE: 
{
  "Currency": "USD", 
  "Price": "23.52", 
  "Symbol": "CTL"
}

----------------------------------------------------------------------------------

Get dividend dates: 
http://<localhost:5000>/stockautomation/api/v1.0/getdividenddates/<Stock Symbole>
METHOD: GET
PARAMETERS: Stock symbol

Example: 
http://localhost:5000/stockautomation/api/v1.0/getdividenddates/CTL

JSON RESPONSE

{
  "ExDividedDate": "11/23/2016", 
  "LastPayoutDate": "9/16/2016", 
  "Symbol": "CTL"
}

----------------------------------------------------------------------------------

Get dividend yield details: 
http://<localhost:5000>/stockautomation/api/v1.0/getdividendyield/<Stock Symbole>
METHOD: GET
PARAMETERS: Stock symbol

Example: 
http://localhost:5000/stockautomation/api/v1.0/getdividendyield/CTL

JSON RESPONSE: 

{
  "DividendYield": "8.77", 
  "Symbol": "CTL", 
  "Unit": "%"
}


##########################################################################################################
