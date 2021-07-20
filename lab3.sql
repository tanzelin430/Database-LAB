-- MySQL dump 10.13  Distrib 8.0.23, for Win64 (x86_64)
--
-- Host: localhost    Database: banksys
-- ------------------------------------------------------
-- Server version	8.0.23

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `account`
--

DROP TABLE IF EXISTS `account`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `account` (
  `account_num` char(18) NOT NULL,
  `bank_name` varchar(20) DEFAULT NULL,
  `money` double DEFAULT NULL,
  `account_date` datetime DEFAULT NULL,
  `account_type` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`account_num`),
  KEY `FK_FK_ac_bank` (`bank_name`),
  CONSTRAINT `FK_FK_ac_bank` FOREIGN KEY (`bank_name`) REFERENCES `bank` (`bank_name`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='账户';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account`
--

LOCK TABLES `account` WRITE;
/*!40000 ALTER TABLE `account` DISABLE KEYS */;
INSERT INTO `account` VALUES ('000001','hf_bank',5000,'2020-06-12 00:00:00','储蓄账户'),('000002','hf_bank',1500,'2020-05-30 00:00:00','支票账户'),('000003','hf_bank',2000,'2021-06-29 14:48:04','支票账户'),('100001','zz_bank',10000,'2021-03-12 00:00:00','储蓄账户'),('100002','zz_bank',2500,'2020-07-12 00:00:00','支票账户'),('200001','sh_bank',7550,'2021-01-31 00:00:00','储蓄账户'),('200002','sh_bank',3000,'2020-12-24 00:00:00','支票账户');
/*!40000 ALTER TABLE `account` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bank`
--

DROP TABLE IF EXISTS `bank`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bank` (
  `bank_name` varchar(20) NOT NULL,
  `bank_addr` varchar(20) DEFAULT NULL,
  `bank_money` float DEFAULT NULL,
  PRIMARY KEY (`bank_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='支行';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bank`
--

LOCK TABLES `bank` WRITE;
/*!40000 ALTER TABLE `bank` DISABLE KEYS */;
INSERT INTO `bank` VALUES ('hf_bank','hf',NULL),('sh_bank','sh',NULL),('zz_bank','zz',NULL);
/*!40000 ALTER TABLE `bank` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bank_member`
--

DROP TABLE IF EXISTS `bank_member`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bank_member` (
  `ID` char(18) NOT NULL,
  `bank_name` varchar(20) DEFAULT NULL,
  `section_num` char(10) DEFAULT NULL,
  `mname` varchar(15) DEFAULT NULL,
  `telephone` char(11) DEFAULT NULL,
  `address` varchar(20) DEFAULT NULL,
  `start_time` date DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `FK_FK_MemberInSection` (`bank_name`,`section_num`),
  CONSTRAINT `FK_FK_MemberInSection` FOREIGN KEY (`bank_name`, `section_num`) REFERENCES `bank_section` (`bank_name`, `section_num`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='银行员工';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bank_member`
--

LOCK TABLES `bank_member` WRITE;
/*!40000 ALTER TABLE `bank_member` DISABLE KEYS */;
INSERT INTO `bank_member` VALUES ('200000000000000000','zz_bank','0001','员工一','1234141','zz','2000-01-04','123@126.com');
/*!40000 ALTER TABLE `bank_member` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bank_section`
--

DROP TABLE IF EXISTS `bank_section`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bank_section` (
  `bank_name` varchar(20) NOT NULL,
  `section_num` char(10) NOT NULL,
  `section_name` varchar(10) DEFAULT NULL,
  `section_type` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`bank_name`,`section_num`),
  CONSTRAINT `FK_FK_SectionInBank` FOREIGN KEY (`bank_name`) REFERENCES `bank` (`bank_name`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='部门';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bank_section`
--

LOCK TABLES `bank_section` WRITE;
/*!40000 ALTER TABLE `bank_section` DISABLE KEYS */;
INSERT INTO `bank_section` VALUES ('zz_bank','0001','业务部',NULL);
/*!40000 ALTER TABLE `bank_section` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `check_ac`
--

DROP TABLE IF EXISTS `check_ac`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `check_ac` (
  `account_num` char(18) NOT NULL,
  `ban_bank_name` varchar(20) DEFAULT NULL,
  `money` double DEFAULT NULL,
  `account_date` datetime DEFAULT NULL,
  `credit_line` double DEFAULT NULL,
  PRIMARY KEY (`account_num`),
  KEY `FK_check_ac_bankname_idx` (`ban_bank_name`),
  CONSTRAINT `FK_check_ac_bankname` FOREIGN KEY (`ban_bank_name`) REFERENCES `bank` (`bank_name`),
  CONSTRAINT `FK_Inheritance_check` FOREIGN KEY (`account_num`) REFERENCES `account` (`account_num`) ON DELETE CASCADE ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='支票账号';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `check_ac`
--

LOCK TABLES `check_ac` WRITE;
/*!40000 ALTER TABLE `check_ac` DISABLE KEYS */;
INSERT INTO `check_ac` VALUES ('000002','hf_bank',1500,'2020-05-30 00:00:00',1000),('000003','hf_bank',2000,'2021-06-29 14:48:04',2000),('100002','zz_bank',2500,'2020-07-12 00:00:00',1500),('200002','sh_bank',3000,'2020-12-24 00:00:00',500);
/*!40000 ALTER TABLE `check_ac` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `check_bank_client`
--

DROP TABLE IF EXISTS `check_bank_client`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `check_bank_client` (
  `ID` char(18) NOT NULL,
  `bank_name` varchar(20) NOT NULL,
  PRIMARY KEY (`ID`,`bank_name`),
  KEY `FK_check_bc_bankname_idx` (`bank_name`),
  CONSTRAINT `FK_check_bc_bankname` FOREIGN KEY (`bank_name`) REFERENCES `bank` (`bank_name`),
  CONSTRAINT `FK_check_bc_client` FOREIGN KEY (`ID`) REFERENCES `customer` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `check_bank_client`
--

LOCK TABLES `check_bank_client` WRITE;
/*!40000 ALTER TABLE `check_bank_client` DISABLE KEYS */;
INSERT INTO `check_bank_client` VALUES ('100000000000000002','hf_bank'),('100000000000000006','sh_bank'),('100000000000000003','zz_bank');
/*!40000 ALTER TABLE `check_bank_client` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer` (
  `ID` char(18) NOT NULL,
  `cname` varchar(15) DEFAULT NULL,
  `telephone` char(11) DEFAULT NULL,
  `address` varchar(20) DEFAULT NULL,
  `link_name` varchar(15) DEFAULT NULL,
  `link_telephone` char(11) DEFAULT NULL,
  `link_Email` varchar(50) DEFAULT NULL,
  `relationship` varchar(5) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='客户';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` VALUES ('100000000000000000','赵一','13783754892','hf','员工一','1234141','123@126.com','账户负责人'),('100000000000000001','钱二','13965192275','bj',NULL,NULL,NULL,NULL),('100000000000000002','孙三','19276891511','sh','员工一','1234141','123@126.com','贷款负责人'),('100000000000000003','李四','18418946719','sz',NULL,NULL,NULL,NULL),('100000000000000004','周五','13774252526','zj',NULL,NULL,NULL,NULL),('100000000000000005','吴六','17527805720','sz',NULL,NULL,NULL,NULL),('100000000000000006','郑七','15637082127','zz',NULL,NULL,NULL,NULL),('100000000000000007','王八','11678741451','xy',NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fk_customer_check_ac`
--

DROP TABLE IF EXISTS `fk_customer_check_ac`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `fk_customer_check_ac` (
  `ID` char(18) NOT NULL,
  `account_num` char(18) NOT NULL,
  `least_use` datetime DEFAULT NULL,
  PRIMARY KEY (`ID`,`account_num`),
  KEY `FK_customer_check_ac` (`account_num`),
  CONSTRAINT `FK_customer_check_ac` FOREIGN KEY (`account_num`) REFERENCES `check_ac` (`account_num`) ON DELETE CASCADE ON UPDATE RESTRICT,
  CONSTRAINT `FK_customer_check_ac_ID` FOREIGN KEY (`ID`) REFERENCES `customer` (`ID`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='FK_客户支票账户';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fk_customer_check_ac`
--

LOCK TABLES `fk_customer_check_ac` WRITE;
/*!40000 ALTER TABLE `fk_customer_check_ac` DISABLE KEYS */;
INSERT INTO `fk_customer_check_ac` VALUES ('100000000000000002','000002',NULL),('100000000000000003','100002',NULL),('100000000000000006','200002',NULL);
/*!40000 ALTER TABLE `fk_customer_check_ac` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fk_customer_savings_ac`
--

DROP TABLE IF EXISTS `fk_customer_savings_ac`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `fk_customer_savings_ac` (
  `ID` char(18) NOT NULL,
  `account_num` char(18) NOT NULL,
  `least_use` datetime DEFAULT NULL,
  PRIMARY KEY (`ID`,`account_num`),
  KEY `FK_customer_savings_ac` (`account_num`),
  CONSTRAINT `FFK_customer_savings_ac_ID` FOREIGN KEY (`ID`) REFERENCES `customer` (`ID`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `FK_customer_savings_ac` FOREIGN KEY (`account_num`) REFERENCES `savings_ac` (`account_num`) ON DELETE CASCADE ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='FK_客户储蓄账户';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fk_customer_savings_ac`
--

LOCK TABLES `fk_customer_savings_ac` WRITE;
/*!40000 ALTER TABLE `fk_customer_savings_ac` DISABLE KEYS */;
INSERT INTO `fk_customer_savings_ac` VALUES ('100000000000000000','000001',NULL),('100000000000000001','100001',NULL),('100000000000000005','000001',NULL),('100000000000000007','200001',NULL);
/*!40000 ALTER TABLE `fk_customer_savings_ac` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `linkman`
--

DROP TABLE IF EXISTS `linkman`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `linkman` (
  `ID` char(18) NOT NULL,
  `ban_ID` char(18) NOT NULL,
  `link_type` varchar(15) DEFAULT '0',
  PRIMARY KEY (`ID`,`ban_ID`),
  KEY `FK_FK_员工联系人` (`ban_ID`),
  CONSTRAINT `FK_FK_员工联系人` FOREIGN KEY (`ban_ID`) REFERENCES `bank_member` (`ID`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `FK_FK_客户联系人` FOREIGN KEY (`ID`) REFERENCES `customer` (`ID`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='联系人';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `linkman`
--

LOCK TABLES `linkman` WRITE;
/*!40000 ALTER TABLE `linkman` DISABLE KEYS */;
INSERT INTO `linkman` VALUES ('100000000000000000','200000000000000000','账户负责人');
/*!40000 ALTER TABLE `linkman` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `loan`
--

DROP TABLE IF EXISTS `loan`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `loan` (
  `loan_ID` char(18) NOT NULL,
  `bank_name` varchar(20) DEFAULT NULL,
  `loan_amount` double DEFAULT NULL,
  `times` int DEFAULT NULL,
  `status` varchar(20) DEFAULT '未开始发放',
  PRIMARY KEY (`loan_ID`),
  KEY `FK_FK_bank_loan` (`bank_name`),
  CONSTRAINT `FK_FK_bank_loan` FOREIGN KEY (`bank_name`) REFERENCES `bank` (`bank_name`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='贷款';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `loan`
--

LOCK TABLES `loan` WRITE;
/*!40000 ALTER TABLE `loan` DISABLE KEYS */;
INSERT INTO `loan` VALUES ('000001','hf_bank',10000,1,'未开始发放'),('000002','zz_bank',2000,2,'已全部发放'),('000003','hf_bank',3000,2,'发放中'),('000004','zz_bank',5000,3,'发放中'),('000005','sh_bank',7000,1,'未开始发放'),('000006','sh_bank',12000,2,'已全部发放');
/*!40000 ALTER TABLE `loan` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `loan_condition`
--

DROP TABLE IF EXISTS `loan_condition`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `loan_condition` (
  `loan_ID` char(18) NOT NULL,
  `loan_date` datetime NOT NULL,
  `loan_money` double NOT NULL,
  PRIMARY KEY (`loan_ID`,`loan_date`),
  CONSTRAINT `FK_FK_loan_condition` FOREIGN KEY (`loan_ID`) REFERENCES `loan` (`loan_ID`) ON DELETE CASCADE ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='放款情况';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `loan_condition`
--

LOCK TABLES `loan_condition` WRITE;
/*!40000 ALTER TABLE `loan_condition` DISABLE KEYS */;
INSERT INTO `loan_condition` VALUES ('000002','2020-06-29 00:00:00',500),('000002','2020-09-27 00:00:00',1500),('000003','2020-12-05 00:00:00',1000),('000004','2021-01-23 00:00:00',1000),('000004','2021-02-23 00:00:00',2000),('000006','2020-02-26 00:00:00',6000),('000006','2020-04-26 00:00:00',6000);
/*!40000 ALTER TABLE `loan_condition` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `loan_customer`
--

DROP TABLE IF EXISTS `loan_customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `loan_customer` (
  `loan_ID` char(18) NOT NULL,
  `ID` char(18) NOT NULL,
  PRIMARY KEY (`loan_ID`,`ID`),
  KEY `FK_FK_贷款人_贷款` (`ID`),
  CONSTRAINT `FK_FK_贷款人_客户` FOREIGN KEY (`loan_ID`) REFERENCES `loan` (`loan_ID`) ON DELETE CASCADE ON UPDATE RESTRICT,
  CONSTRAINT `FK_FK_贷款人_贷款` FOREIGN KEY (`ID`) REFERENCES `customer` (`ID`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='贷款人';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `loan_customer`
--

LOCK TABLES `loan_customer` WRITE;
/*!40000 ALTER TABLE `loan_customer` DISABLE KEYS */;
INSERT INTO `loan_customer` VALUES ('000001','100000000000000000'),('000002','100000000000000001'),('000003','100000000000000002'),('000004','100000000000000003'),('000005','100000000000000004'),('000006','100000000000000005'),('000001','100000000000000006'),('000003','100000000000000006'),('000001','100000000000000007');
/*!40000 ALTER TABLE `loan_customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `savings_ac`
--

DROP TABLE IF EXISTS `savings_ac`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `savings_ac` (
  `account_num` char(18) NOT NULL,
  `ban_bank_name` varchar(20) DEFAULT NULL,
  `money` double DEFAULT NULL,
  `account_date` datetime DEFAULT NULL,
  `interest_rate` double DEFAULT NULL,
  `money_type` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`account_num`),
  KEY `FK_bank_savings_ac_idx` (`ban_bank_name`),
  CONSTRAINT `FK_bank_savings_ac` FOREIGN KEY (`ban_bank_name`) REFERENCES `bank` (`bank_name`),
  CONSTRAINT `FK_Inheritance_savings` FOREIGN KEY (`account_num`) REFERENCES `account` (`account_num`) ON DELETE CASCADE ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='储蓄账号';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `savings_ac`
--

LOCK TABLES `savings_ac` WRITE;
/*!40000 ALTER TABLE `savings_ac` DISABLE KEYS */;
INSERT INTO `savings_ac` VALUES ('000001','hf_bank',5000,'2020-06-12 00:00:00',0.0315,'人民币'),('100001','zz_bank',10000,'2021-03-12 00:00:00',0.0328,'人民币'),('200001','sh_bank',7550,'2021-01-31 00:00:00',0.0402,'人民币');
/*!40000 ALTER TABLE `savings_ac` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `savings_bank_client`
--

DROP TABLE IF EXISTS `savings_bank_client`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `savings_bank_client` (
  `ID` char(18) NOT NULL,
  `bank_name` varchar(20) NOT NULL,
  PRIMARY KEY (`ID`,`bank_name`),
  KEY `FK_bc_bank_name_idx` (`bank_name`),
  CONSTRAINT `FK_bc_bank_name` FOREIGN KEY (`bank_name`) REFERENCES `bank` (`bank_name`),
  CONSTRAINT `FK_bc_client` FOREIGN KEY (`ID`) REFERENCES `customer` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `savings_bank_client`
--

LOCK TABLES `savings_bank_client` WRITE;
/*!40000 ALTER TABLE `savings_bank_client` DISABLE KEYS */;
INSERT INTO `savings_bank_client` VALUES ('100000000000000000','hf_bank'),('100000000000000005','hf_bank'),('100000000000000007','sh_bank'),('100000000000000001','zz_bank');
/*!40000 ALTER TABLE `savings_bank_client` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `section_manager`
--

DROP TABLE IF EXISTS `section_manager`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `section_manager` (
  `ID` char(18) NOT NULL,
  `bank_name` varchar(20) DEFAULT NULL,
  `section_num` char(10) DEFAULT NULL,
  `ban_section_num` char(10) DEFAULT NULL,
  `mname` varchar(15) DEFAULT NULL,
  `telephone` char(11) DEFAULT NULL,
  `address` varchar(20) DEFAULT NULL,
  `start_time` date DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `FK_FK_section_manager` (`bank_name`,`section_num`),
  CONSTRAINT `FK_FK_section_manager` FOREIGN KEY (`bank_name`, `section_num`) REFERENCES `bank_section` (`bank_name`, `section_num`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `FK_Inheritance_ID` FOREIGN KEY (`ID`) REFERENCES `bank_member` (`ID`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='部门经理';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `section_manager`
--

LOCK TABLES `section_manager` WRITE;
/*!40000 ALTER TABLE `section_manager` DISABLE KEYS */;
/*!40000 ALTER TABLE `section_manager` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'lab3_bankmanagesys'
--

--
-- Dumping routines for database 'lab3_bankmanagesys'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-07-05 21:53:34
