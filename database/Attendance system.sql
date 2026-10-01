-- MySQL dump 10.13  Distrib 8.0.45, for Win64 (x86_64)
--
-- Host: localhost    Database: attendancesystem
-- ------------------------------------------------------
-- Server version	8.0.45

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
-- Table structure for table `student`
--

DROP TABLE IF EXISTS `student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student` (
  `DEPARTMENT` varchar(45) DEFAULT NULL,
  `COURCE` varchar(45) DEFAULT NULL,
  `YEAR` varchar(45) DEFAULT NULL,
  `SEMESTER` varchar(45) DEFAULT NULL,
  `STUDENT_ID` int NOT NULL,
  `NAME` varchar(45) DEFAULT NULL,
  `DIVISION` varchar(45) DEFAULT NULL,
  `ROLL` varchar(45) DEFAULT NULL,
  `GENDER` varchar(45) DEFAULT NULL,
  `DOB` varchar(45) DEFAULT NULL,
  `EMAIL` varchar(100) DEFAULT NULL,
  `PHONE` varchar(45) DEFAULT NULL,
  `ADDRESS` varchar(100) DEFAULT NULL,
  `TEACHER` varchar(45) DEFAULT NULL,
  `PHOTO_SAMPLE` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`STUDENT_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student`
--

LOCK TABLES `student` WRITE;
/*!40000 ALTER TABLE `student` DISABLE KEYS */;
INSERT INTO `student` VALUES ('B.Tech','CSE','2023','7',1005,'Abhi','A','23303006','Male','14.02.2005','ghvdvjhfu','20.16002315602','pathankot','','1'),('B.Tech','CSE','2023','6',10051,'jainandan','B','23303131','Male','24.09.2004','jainandan2409@gmail.com','+91 7740044761','dinanagar','','0'),('B.Tech','CSE','2023','6',10052,'GaganDeep','B','23303096','Male','12/01/2005','gagan@gmail.com','+91 7814873869','pathankot','','0'),('B.Tech','CSE','2023','6',100053,'GaganDeep Singh','B','23303097','Male','8.10.2004','gagandeepsingh@gmail.com','+91 85580 97415','Pathankot','','0');
/*!40000 ALTER TABLE `student` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-10-01 20:18:40
