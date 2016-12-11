create database mystockdb;
use mystockdb;
create table fav_stock (id MEDIUMINT NOT NULL AUTO_INCREMENT,Symbol VARCHAR(20),Market VARCHAR(20),AddedDate DATE,primary key(id));


CREATE TABLE ExchangeSymbol (ID MEDIUMINT NOT NULL AUTO_INCREMENT, ExchangeName VARCHAR(100) NOT NULL,ExchangeSymbol VARCHAR(25), UpdatedDate DATE, PRIMARY KEY (ID));

INSERT INTO ExchangeSymbol (ExchangeSymbol,ExchangeName) VALUES ("AMEX","American Stock Exchange");
INSERT INTO ExchangeSymbol (ExchangeSymbol,ExchangeName) VALUES ("AMS","Euronext Amsterdam");
INSERT INTO ExchangeSymbol (ExchangeSymbol,ExchangeName) VALUES ("ASX","Australian Securities Exchange");
INSERT INTO ExchangeSymbol (ExchangeSymbol,ExchangeName) VALUES ("BRU","Euronext Brussels");
INSERT INTO ExchangeSymbol (ExchangeSymbol,ExchangeName) VALUES ("CBOT","Chicago Board of Trade");
INSERT INTO ExchangeSymbol (ExchangeSymbol,ExchangeName) VALUES ("CFE","Chicago Futures Exchange");
INSERT INTO ExchangeSymbol (ExchangeSymbol,ExchangeName) VALUES ("CME","Chicago Merchantile Exchange");
INSERT INTO ExchangeSymbol (ExchangeSymbol,ExchangeName) VALUES ("COMEX","New York Commodity Exchange");
INSERT INTO ExchangeSymbol (ExchangeSymbol,ExchangeName) VALUES ("EUREX","EUREX Futures Exchange");
INSERT INTO ExchangeSymbol (ExchangeSymbol,ExchangeName) VALUES ("FOREX","Foreign Exchange");
INSERT INTO ExchangeSymbol (ExchangeSymbol,ExchangeName) VALUES ("HKEX","Hong Kong Stock Exchange");
INSERT INTO ExchangeSymbol (ExchangeSymbol,ExchangeName) VALUES ("INDEX","Global Indices");
INSERT INTO ExchangeSymbol (ExchangeSymbol,ExchangeName) VALUES ("KCBT","Kansas City Board of Trade");
INSERT INTO ExchangeSymbol (ExchangeSymbol,ExchangeName) VALUES ("LIFFE","LIFFE Futures and Options");
INSERT INTO ExchangeSymbol (ExchangeSymbol,ExchangeName) VALUES ("LIS","Euronext Lisbon");
INSERT INTO ExchangeSymbol (ExchangeSymbol,ExchangeName) VALUES ("LSE","London Stock Exchange");
INSERT INTO ExchangeSymbol (ExchangeSymbol,ExchangeName) VALUES ("MGEX","Minneapolis Grain Exchange");
INSERT INTO ExchangeSymbol (ExchangeSymbol,ExchangeName) VALUES ("MLSE","Milan Stock Exchange");
INSERT INTO ExchangeSymbol (ExchangeSymbol,ExchangeName) VALUES ("MSE","Madrid Stock Exchange");
INSERT INTO ExchangeSymbol (ExchangeSymbol,ExchangeName) VALUES ("NASDAQ","NASDAQ Stock Exchange");
INSERT INTO ExchangeSymbol (ExchangeSymbol,ExchangeName) VALUES ("NYBOT","New York Board of Trade");
INSERT INTO ExchangeSymbol (ExchangeSymbol,ExchangeName) VALUES ("NYMEX","New York Merchantile Exchange");
INSERT INTO ExchangeSymbol (ExchangeSymbol,ExchangeName) VALUES ("NYSE","New York Stock Exchange");
INSERT INTO ExchangeSymbol (ExchangeSymbol,ExchangeName) VALUES ("NZX","New Zealand Exchange");
INSERT INTO ExchangeSymbol (ExchangeSymbol,ExchangeName) VALUES ("OTCBB","OTC Bulletin Board");
INSERT INTO ExchangeSymbol (ExchangeSymbol,ExchangeName) VALUES ("PAR","Euronext Paris");
INSERT INTO ExchangeSymbol (ExchangeSymbol,ExchangeName) VALUES ("SGX","Singapore Stock Exchange");
INSERT INTO ExchangeSymbol (ExchangeSymbol,ExchangeName) VALUES ("TSX","Toronto Stock Exchange");
INSERT INTO ExchangeSymbol (ExchangeSymbol,ExchangeName) VALUES ("TSXV","Toronto Venture Exchange");
INSERT INTO ExchangeSymbol (ExchangeSymbol,ExchangeName) VALUES ("USMF","Mutual Funds");
INSERT INTO ExchangeSymbol (ExchangeSymbol,ExchangeName) VALUES ("WCE","Winnipeg Commodity Exchange");

