-------------------------------------
| Installation of required softare: |
-------------------------------------

install python2.7.X
install pip using following command: 
easy_install pip 
install pytest using following command: 
pip install pytest


------------------------------------
|    Perperation of config file    |
------------------------------------
Step1: 
From root directory 
cd ./config
vi ./config.json

{ 
        "protocol":"http",                                       
        "serverip":"127.0.0.1",
        "port":"8081",
}   

In case if REST API is using https we need to change the portocol to http
need to update server ip address or domain 
update the port information example: 8080 or 443 

------------------------------------
| Preperation of input file as csv |
------------------------------------
 
sample input data should in saved in .csv file: 

Example: stock_api.csv

testcase_id,base_url,symbol,response_code
1,stockautomation/api/v1.0/getquote/,CTL,200

dataParser class will help you to parse this data file and gives you back the test data 

---------------------------------------
| Preperation of test automation file |
---------------------------------------

Example test automation file is available at test_get_stock_details_api.py
For now get method call is available without authentication 


