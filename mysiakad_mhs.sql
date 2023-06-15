-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: localhost    Database: mysiakad
-- ------------------------------------------------------
-- Server version	8.0.33

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
-- Table structure for table `mhs`
--

DROP TABLE IF EXISTS `mhs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mhs` (
  `NIM` text,
  `NAMA` text,
  `TGL LAHIR` text,
  `ALAMAT` text
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mhs`
--

LOCK TABLES `mhs` WRITE;
/*!40000 ALTER TABLE `mhs` DISABLE KEYS */;
INSERT INTO `mhs` VALUES ('M001','Agus','01/09/1979','Solo'),('M002','Budi','02/11/1980','Solo '),('M003','Candra','03/10/1979','Semarang'),('M004','Deni','04/10/1979','Jakarta'),('M005','Eko','05/09/1979','Bandung'),('M006','Fifi','06/09/1980','Bandung '),('M007','Gani','07/09/1981','Jakarta'),('M008','Hengky','08/09/1979','Solo'),('M009','Iwan','09/09/1979','Semarang'),('M010','Januar','10/09/1979','Bogor'),('M001','Agus','01/09/1979','Solo'),('M002','Budi','02/11/1980','Solo '),('M003','Candra','03/10/1979','Semarang'),('M004','Deni','04/10/1979','Jakarta'),('M005','Eko','05/09/1979','Bandung'),('M006','Fifi','06/09/1980','Bandung '),('M007','Gani','07/09/1981','Jakarta'),('M008','Hengky','08/09/1979','Solo'),('M009','Iwan','09/09/1979','Semarang'),('M010','Januar','10/09/1979','Bogor');
/*!40000 ALTER TABLE `mhs` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-06-15 11:13:02
