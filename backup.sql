-- MySQL dump 10.13  Distrib 8.0.34, for Linux (x86_64)
--
-- Host: localhost    Database: hirem
-- ------------------------------------------------------
-- Server version	8.0.34-0ubuntu0.20.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `employee_details`
--

DROP TABLE IF EXISTS `employee_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employee_details` (
  `e_name` varchar(30) DEFAULT NULL,
  `e_exp` int DEFAULT NULL,
  `e_gender` varchar(30) DEFAULT NULL,
  `e_id` int NOT NULL,
  `e_skill_set_1` varchar(30) DEFAULT NULL,
  `e_skill_set_2` varchar(30) DEFAULT NULL,
  `e_skill_set_3` varchar(30) DEFAULT NULL,
  `e_skill_set_4` varchar(30) DEFAULT NULL,
  `e_skill_set_5` varchar(30) DEFAULT NULL,
  `communication_skills` int DEFAULT NULL,
  `time_management_skills` int DEFAULT NULL,
  `no_of_projects` int DEFAULT NULL,
  `exp_years` int DEFAULT NULL,
  PRIMARY KEY (`e_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee_details`
--

LOCK TABLES `employee_details` WRITE;
/*!40000 ALTER TABLE `employee_details` DISABLE KEYS */;
INSERT INTO `employee_details` VALUES ('mark',5,'male',1,'backend_development','data_analysis','databases','aws','react',8,4,3,7),('lary',5,'male',2,'backend_development','blockchain','mongo_db','aws','deep_learning',8,4,3,7),('sergery_brin',10,'male',3,'front_end','algorithms','git','linux','deep_learning',8,4,3,7),('sergery_brin',10,'male',4,'front_end','algorithms','git','linux','deep_learning',8,4,3,7),('sergery_brin',10,'male',5,'backend','data_structures','docker','linux','deep_learning',8,4,3,7),('Michael Brown',7,'Male',10,'Java','SQL','Teamwork','Problem Solving','Communication',8,4,3,7),('Sophia Clark',5,'Female',11,'Python','JavaScript','Project Management','Creativity','Adaptability',8,4,3,7),('David White',6,'Male',12,'C++','Data Analysis','Leadership','Innovation','Data Visualization',8,4,3,7),('Olivia Thomas',3,'Female',13,'Java','SQL','Teamwork','Problem Solving','Communication',8,4,3,7),('Ethan Turner',9,'Male',14,'Python','JavaScript','Project Management','Creativity','Adaptability',8,4,3,7),('Ava Mitchell',8,'Female',15,'C++','Data Analysis','Leadership','Innovation','Data Visualization',8,4,3,7),('Noah Hall',4,'Male',16,'Java','SQL','Teamwork','Problem Solving','Communication',8,4,3,7),('Mia Anderson',5,'Female',17,'Python','JavaScript','Project Management','Creativity','Adaptability',8,4,3,7),('William Baker',6,'Male',18,'C++','Data Analysis','Leadership','Innovation','Data Visualization',8,4,3,7),('Isabella Turner',7,'Female',19,'Java','SQL','Teamwork','Problem Solving','Communication',8,4,3,7),('James Harris',5,'Male',20,'Python','JavaScript','Project Management','Creativity','Adaptability',8,4,3,7);
/*!40000 ALTER TABLE `employee_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employee_score`
--

DROP TABLE IF EXISTS `employee_score`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employee_score` (
  `employee_id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(50) DEFAULT NULL,
  `last_name` varchar(50) DEFAULT NULL,
  `role` varchar(50) DEFAULT NULL,
  `hours_worked` decimal(10,2) DEFAULT NULL,
  `communication_skills` int DEFAULT NULL,
  `time_management_skills` int DEFAULT NULL,
  PRIMARY KEY (`employee_id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee_score`
--

LOCK TABLES `employee_score` WRITE;
/*!40000 ALTER TABLE `employee_score` DISABLE KEYS */;
INSERT INTO `employee_score` VALUES (4,'Mark','','backend_development',5.00,1,2),(5,'Larry','','backend_development',5.00,2,3),(6,'Sergey Brin','','front_end',5.00,3,4),(7,'Sergey Brin','','front_end',5.00,4,5),(8,'Sergey Brin','','backend',5.00,5,1),(9,'Michael Brown','','Java',10.00,5,6),(10,'Sophia Clark','','Python',11.00,6,7),(11,'David White','','C++',12.00,7,8),(12,'Olivia Thomas','','Java',13.00,8,9),(13,'Ethan Turner','','Python',14.00,9,1),(14,'Ava Mitchell','','C++',15.00,2,2),(15,'Noah Hall','','Java',16.00,3,3),(16,'Mia Anderson','','Python',17.00,4,4),(17,'William Baker','','C++',18.00,5,5),(18,'Isabella Turner','','Java',19.00,6,6),(19,'James Harris','','Python',20.00,7,7);
/*!40000 ALTER TABLE `employee_score` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-10-18 17:28:35
