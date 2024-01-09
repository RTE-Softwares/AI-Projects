-- MySQL dump 10.13  Distrib 5.7.42, for Linux (x86_64)
--
-- Host: localhost    Database: emp
-- ------------------------------------------------------
-- Server version	5.7.42-0ubuntu0.18.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `agents`
--

DROP TABLE IF EXISTS `agents`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `agents` (
  `AGENT_CODE` varchar(6) NOT NULL DEFAULT '',
  `AGENT_NAME` varchar(40) DEFAULT NULL,
  `WORKING_AREA` varchar(35) DEFAULT NULL,
  `COMMISSION` decimal(10,2) DEFAULT NULL,
  `PHONE_NO` varchar(15) DEFAULT NULL,
  `COUNTRY` varchar(25) DEFAULT NULL,
  PRIMARY KEY (`AGENT_CODE`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `agents`
--

LOCK TABLES `agents` WRITE;
/*!40000 ALTER TABLE `agents` DISABLE KEYS */;
INSERT INTO `agents` VALUES ('A007  ','Ramasundar                              ','Bangalore                          ',0.15,'077-25814763   ','\r'),('A003  ','Alex                                    ','London                             ',0.13,'075-12458969   ','\r'),('A008  ','Alford                                  ','New York                           ',0.12,'044-25874365   ','\r'),('A011  ','Ravi Kumar                              ','Bangalore                          ',0.15,'077-45625874   ','\r'),('A010  ','Santakumar                              ','Chennai                            ',0.14,'007-22388644   ','\r'),('A012  ','Lucida                                  ','San Jose                           ',0.12,'044-52981425   ','\r'),('A005  ','Anderson                                ','Brisban                            ',0.13,'045-21447739   ','\r'),('A001  ','Subbarao                                ','Bangalore                          ',0.14,'077-12346674   ','\r'),('A002  ','Mukesh                                  ','Mumbai                             ',0.11,'029-12358964   ','\r'),('A006  ','McDen                                   ','London                             ',0.15,'078-22255588   ','\r'),('A004  ','Ivan                                    ','Torento                            ',0.15,'008-22544166   ','\r'),('A009  ','Benjamin                                ','Hampshair                          ',0.11,'008-22536178   ','\r');
/*!40000 ALTER TABLE `agents` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `customer` (
  `CUST_CODE` varchar(6) NOT NULL,
  `CUST_NAME` varchar(40) NOT NULL,
  `CUST_CITY` varchar(35) DEFAULT NULL,
  `WORKING_AREA` varchar(35) NOT NULL,
  `CUST_COUNTRY` varchar(20) NOT NULL,
  `GRADE` decimal(10,0) DEFAULT NULL,
  `OPENING_AMT` decimal(12,2) NOT NULL,
  `RECEIVE_AMT` decimal(12,2) NOT NULL,
  `PAYMENT_AMT` decimal(12,2) NOT NULL,
  `OUTSTANDING_AMT` decimal(12,2) NOT NULL,
  `PHONE_NO` varchar(17) NOT NULL,
  `AGENT_CODE` varchar(6) DEFAULT NULL,
  KEY `CUSTCITY` (`CUST_CITY`),
  KEY `CUSTCITY_COUNTRY` (`CUST_CITY`,`CUST_COUNTRY`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` VALUES ('C00013','Holmes','London                             ','London','UK',2,6000.00,5000.00,7000.00,4000.00,'BBBBBBB','A003  '),('C00001','Micheal','New York                           ','New York','USA',2,3000.00,5000.00,2000.00,6000.00,'CCCCCCC','A008  '),('C00020','Albert','New York                           ','New York','USA',3,5000.00,7000.00,6000.00,6000.00,'BBBBSBB','A008  '),('C00025','Ravindran','Bangalore                          ','Bangalore','India',2,5000.00,7000.00,4000.00,8000.00,'AVAVAVA','A011  '),('C00024','Cook','London                             ','London','UK',2,4000.00,9000.00,7000.00,6000.00,'FSDDSDF','A006  '),('C00015','Stuart','London                             ','London','UK',1,6000.00,8000.00,3000.00,11000.00,'GFSGERS','A003  '),('C00002','Bolt','New York                           ','New York','USA',3,5000.00,7000.00,9000.00,3000.00,'DDNRDRH','A008  '),('C00018','Fleming','Brisban                            ','Brisban','Australia',2,7000.00,7000.00,9000.00,5000.00,'NHBGVFC','A005  '),('C00021','Jacks','Brisban                            ','Brisban','Australia',1,7000.00,7000.00,7000.00,7000.00,'WERTGDF','A005  '),('C00019','Yearannaidu','Chennai                            ','Chennai','India',1,8000.00,7000.00,7000.00,8000.00,'ZZZZBFV','A010  '),('C00005','Sasikant','Mumbai                             ','Mumbai','India',1,7000.00,11000.00,7000.00,11000.00,'147-25896312','A002  '),('C00007','Ramanathan','Chennai                            ','Chennai','India',1,7000.00,11000.00,9000.00,9000.00,'GHRDWSD','A010  '),('C00022','Avinash','Mumbai                             ','Mumbai','India',2,7000.00,11000.00,9000.00,9000.00,'113-12345678','A002  '),('C00004','Winston','Brisban                            ','Brisban','Australia',1,5000.00,8000.00,7000.00,6000.00,'AAAAAAA','A005  '),('C00023','Karl','London                             ','London','UK',0,4000.00,6000.00,7000.00,3000.00,'AAAABAA','A006  '),('C00006','Shilton','Torento                            ','Torento','Canada',1,10000.00,7000.00,6000.00,11000.00,'DDDDDDD','A004  '),('C00010','Charles','Hampshair                          ','Hampshair','UK',3,6000.00,4000.00,5000.00,5000.00,'MMMMMMM','A009  '),('C00017','Srinivas','Bangalore                          ','Bangalore','India',2,8000.00,4000.00,3000.00,9000.00,'AAAAAAB','A007  '),('C00012','Steven','San Jose                           ','San Jose','USA',1,5000.00,7000.00,9000.00,3000.00,'KRFYGJK','A012  '),('C00008','Karolina','Torento                            ','Torento','Canada',1,7000.00,7000.00,9000.00,5000.00,'HJKORED','A004  '),('C00003','Martin','Torento                            ','Torento','Canada',2,8000.00,7000.00,7000.00,8000.00,'MJYURFD','A004  '),('C00009','Ramesh','Mumbai                             ','Mumbai','India',3,8000.00,7000.00,3000.00,12000.00,'Phone No','A002  '),('C00014','Rangarappa','Bangalore                          ','Bangalore','India',2,8000.00,11000.00,7000.00,12000.00,'AAAATGF','A001  '),('C00016','Venkatpati','Bangalore                          ','Bangalore','India',2,8000.00,11000.00,7000.00,12000.00,'JRTVFDD','A007  '),('C00011','Sundariya','Chennai                            ','Chennai','India',3,7000.00,11000.00,7000.00,11000.00,'PPHGRTS','A010  ');
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orders`
--

DROP TABLE IF EXISTS `orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `orders` (
  `ORD_NUM` decimal(6,0) NOT NULL,
  `ORD_AMOUNT` decimal(12,2) NOT NULL,
  `ADVANCE_AMOUNT` decimal(12,2) NOT NULL,
  `ORD_DATE` date NOT NULL,
  `CUST_CODE` varchar(6) NOT NULL,
  `AGENT_CODE` varchar(6) NOT NULL,
  `ORD_DESCRIPTION` varchar(60) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders`
--

LOCK TABLES `orders` WRITE;
/*!40000 ALTER TABLE `orders` DISABLE KEYS */;
INSERT INTO `orders` VALUES (200100,1000.00,600.00,'2008-01-08','C00015','A003  ','SOD\r'),(200110,3000.00,500.00,'2008-04-15','C00019','A010  ','SOD\r'),(200107,4500.00,900.00,'2008-08-30','C00007','A010  ','SOD\r'),(200112,2000.00,400.00,'2008-05-30','C00016','A007  ','SOD\r'),(200113,4000.00,600.00,'2008-06-10','C00022','A002  ','SOD\r'),(200102,2000.00,300.00,'2008-05-25','C00012','A012  ','SOD\r'),(200114,3500.00,2000.00,'2008-08-15','C00002','A008  ','SOD\r'),(200122,2500.00,400.00,'2008-09-16','C00003','A004  ','SOD\r'),(200118,500.00,100.00,'2008-07-20','C00023','A006  ','SOD\r'),(200119,4000.00,700.00,'2008-09-16','C00007','A010  ','SOD\r'),(200121,1500.00,600.00,'2008-09-23','C00008','A004  ','SOD\r'),(200130,2500.00,400.00,'2008-07-30','C00025','A011  ','SOD\r'),(200134,4200.00,1800.00,'2008-09-25','C00004','A005  ','SOD\r'),(200115,2000.00,1200.00,'2008-02-08','C00013','A013  ','SOD\r'),(200108,4000.00,600.00,'2008-02-15','C00008','A004  ','SOD\r'),(200103,1500.00,700.00,'2008-05-15','C00021','A005  ','SOD\r'),(200105,2500.00,500.00,'2008-07-18','C00025','A011  ','SOD\r'),(200109,3500.00,800.00,'2008-07-30','C00011','A010  ','SOD\r'),(200101,3000.00,1000.00,'2008-07-15','C00001','A008  ','SOD\r'),(200111,1000.00,300.00,'2008-07-10','C00020','A008  ','SOD\r'),(200104,1500.00,500.00,'2008-03-13','C00006','A004  ','SOD\r'),(200106,2500.00,700.00,'2008-04-20','C00005','A002  ','SOD\r'),(200125,2000.00,600.00,'2008-10-10','C00018','A005  ','SOD\r'),(200117,800.00,200.00,'2008-10-20','C00014','A001  ','SOD\r'),(200123,500.00,100.00,'2008-09-16','C00022','A002  ','SOD\r'),(200120,500.00,100.00,'2008-07-20','C00009','A002  ','SOD\r'),(200116,500.00,100.00,'2008-07-13','C00010','A009  ','SOD\r'),(200124,500.00,100.00,'2008-06-20','C00017','A007  ','SOD\r'),(200126,500.00,100.00,'2008-06-24','C00022','A002  ','SOD\r'),(200129,2500.00,500.00,'2008-07-20','C00024','A006  ','SOD\r'),(200127,2500.00,400.00,'2008-07-20','C00015','A003  ','SOD\r'),(200128,3500.00,1500.00,'2008-07-20','C00009','A002  ','SOD\r'),(200135,2000.00,800.00,'2008-09-16','C00007','A010  ','SOD\r'),(200131,900.00,150.00,'2008-08-26','C00012','A012  ','SOD\r'),(200133,1200.00,400.00,'2008-06-29','C00009','A002  ','SOD\r'),(200132,4000.00,2000.00,'2008-08-15','C00013','A013  ','SOD\r');
/*!40000 ALTER TABLE `orders` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-01-08 17:41:03
