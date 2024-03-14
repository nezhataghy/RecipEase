-- MySQL dump 10.13  Distrib 8.0.36, for Linux (x86_64)
--
-- Host: localhost    Database: RecipEase
-- ------------------------------------------------------
-- Server version	8.0.36-0ubuntu0.22.04.1

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
-- Table structure for table `Food`
--

DROP TABLE IF EXISTS `Food`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Food` (
  `name` varchar(200) NOT NULL,
  `category` varchar(200) NOT NULL,
  `image` varchar(200) DEFAULT NULL,
  `__id` varchar(200) NOT NULL,
  `__created_at` datetime NOT NULL,
  `__updated_at` datetime NOT NULL,
  PRIMARY KEY (`__id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Food`
--

LOCK TABLES `Food` WRITE;
/*!40000 ALTER TABLE `Food` DISABLE KEYS */;
INSERT INTO `Food` VALUES ('Chicken Panet','lunch','No image','1281f4e5-0a3a-4b0e-97ea-11d2d2d97f97','2024-03-08 13:13:01','2024-03-08 13:48:38'),('Cheesy Croissant','Breakfast','/root/RecipEase/images/580caa35-4a7a-4238-a941-50d1dbbfea82.jpg','580caa35-4a7a-4238-a941-50d1dbbfea82','2024-03-08 13:14:59','2024-03-12 19:53:43'),('Negresco','lunch','No image','59142e97-d1e4-404c-b381-0de5e8307486','2024-03-08 13:12:46','2024-03-08 13:12:46'),('Rizo Rice','lunch','No image','61e0a37d-7b71-4fd6-b9d5-0daa38e68f42','2024-03-08 13:12:09','2024-03-08 13:12:09'),('Chicken with Rice','lunch','No image','6f845f39-b2e9-4794-84c4-bc6c7fbc9359','2024-03-08 13:12:38','2024-03-08 13:12:38'),('Greek yogurt parfait','breakfast','No image','75a88b25-e0a0-4980-9ad0-7415ca387498','2024-03-08 13:34:28','2024-03-08 13:34:28'),('Turkey and cheese sandwich','lunch','No image','819f00e0-89b2-47e2-aaf2-daf3db31582a','2024-03-08 13:18:56','2024-03-08 13:18:56'),('Spaghetti with marinara sauce and meatballs','dinner','No image','9448689e-0ca5-4363-9dba-c70fef970798','2024-03-08 13:16:19','2024-03-08 13:16:19'),('Fool and Falafel','Breakfast','No image','ade806d8-d72d-4f97-933a-23cd77cdabd9','2024-03-08 13:13:22','2024-03-08 13:13:22'),('Alfredo','lunch','No image','bece0d59-5c94-4230-b731-f0fcbab0cd11','2024-03-08 13:12:19','2024-03-08 13:12:19'),('Avocado toast with poached eggs and cherry tomatoes','breakfast','No image','c3378142-e70a-4e7f-874f-0c0be7beafc7','2024-03-08 13:18:01','2024-03-08 13:18:01'),('Beef tacos with lettuce, cheese, and salsa','dinner','No image','d3b26a82-bf0c-4f0d-b8fd-00e5ededcec9','2024-03-08 13:17:17','2024-03-08 13:17:17'),('Grilled chicken with roasted vegetables','dinner','No image','dad4a5ae-d003-4f6d-a877-77d3176c7fa8','2024-03-08 13:16:08','2024-03-08 13:16:08'),('Pizza with Eggs','Breakfast','No image','e05586ad-e627-4fa2-b8da-2459099f59c9','2024-03-08 13:14:00','2024-03-08 13:14:00'),('Alfredo Spaghetti','cat2','No image','e7f45d69-8c70-4d68-95c4-a0dca5a22945','2024-03-02 19:27:30','2024-03-11 01:35:18'),('Stir-fried tofu with vegetables and rice','dinner','No image','e894a430-6626-47db-bf5a-7dc343e1a8b6','2024-03-08 13:16:52','2024-03-08 13:16:52'),('Margherita pizza with a side salad','dinner','No image','ee82565e-d026-48fd-bf45-a85c26690845','2024-03-08 13:17:32','2024-03-08 13:17:32'),('Kebda','lunch','No image','efa0efad-fa7a-4c39-8516-e6509a4b28a5','2024-03-08 13:12:28','2024-03-08 13:12:28'),('Baked salmon with steamed asparagus','dinner','No image','fd7e3480-3167-4e08-8878-4aba614aa630','2024-03-08 13:17:07','2024-03-08 13:17:07');
/*!40000 ALTER TABLE `Food` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Food_Ingredients`
--

DROP TABLE IF EXISTS `Food_Ingredients`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Food_Ingredients` (
  `food_id` varchar(200) NOT NULL,
  `ingredients_id` varchar(200) NOT NULL,
  `quantity` varchar(15) NOT NULL,
  PRIMARY KEY (`food_id`,`ingredients_id`),
  KEY `ingredients_id` (`ingredients_id`),
  CONSTRAINT `Food_Ingredients_ibfk_1` FOREIGN KEY (`food_id`) REFERENCES `Food` (`__id`),
  CONSTRAINT `Food_Ingredients_ibfk_2` FOREIGN KEY (`ingredients_id`) REFERENCES `Ingredients` (`__id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Food_Ingredients`
--

LOCK TABLES `Food_Ingredients` WRITE;
/*!40000 ALTER TABLE `Food_Ingredients` DISABLE KEYS */;
INSERT INTO `Food_Ingredients` VALUES ('1281f4e5-0a3a-4b0e-97ea-11d2d2d97f97','20e8041a-2a1f-410d-a781-29d422fa221e','0.250kg'),('1281f4e5-0a3a-4b0e-97ea-11d2d2d97f97','2e6c488a-3ebf-44fd-b767-4cf5630fa5f6','2 pcs'),('1281f4e5-0a3a-4b0e-97ea-11d2d2d97f97','53da066d-5e06-482a-a3f1-c96cdbb92f47','2 pcs'),('580caa35-4a7a-4238-a941-50d1dbbfea82','6cf71ef3-82c3-48eb-89d3-4ec0f67d5712','2 pcs'),('580caa35-4a7a-4238-a941-50d1dbbfea82','70072b14-30ff-4213-b5ae-2ed80ac1baac','2 pcs');
/*!40000 ALTER TABLE `Food_Ingredients` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Ingredients`
--

DROP TABLE IF EXISTS `Ingredients`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Ingredients` (
  `name` varchar(200) NOT NULL,
  `__id` varchar(200) NOT NULL,
  `__created_at` datetime NOT NULL,
  `__updated_at` datetime NOT NULL,
  PRIMARY KEY (`__id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Ingredients`
--

LOCK TABLES `Ingredients` WRITE;
/*!40000 ALTER TABLE `Ingredients` DISABLE KEYS */;
INSERT INTO `Ingredients` VALUES ('Chicken','20e8041a-2a1f-410d-a781-29d422fa221e','2024-03-08 13:42:11','2024-03-08 13:42:11'),('Green Chilli Pepper','2d985402-1744-453d-a246-9ef39ce6ee4b','2024-03-08 13:41:56','2024-03-08 13:41:56'),('Tomato','2e6c488a-3ebf-44fd-b767-4cf5630fa5f6','2024-03-08 13:41:23','2024-03-08 13:41:23'),('Lemon','53da066d-5e06-482a-a3f1-c96cdbb92f47','2024-03-08 13:41:40','2024-03-08 13:41:40'),('Flour','6a23bf30-ec01-4a5b-b0ae-1d7040776329','2024-03-08 13:41:17','2024-03-08 13:41:17'),('Egg','6cf71ef3-82c3-48eb-89d3-4ec0f67d5712','2024-03-08 13:42:05','2024-03-08 13:42:05'),('Cheese','70072b14-30ff-4213-b5ae-2ed80ac1baac','2024-03-08 13:42:43','2024-03-08 13:42:43'),('Fish','c4163d57-c82f-4e02-9197-50f4a7cb9027','2024-03-08 13:42:18','2024-03-08 13:42:18'),('Onion','d4dd4eeb-dc22-41da-82c2-83b818ada1e9','2024-03-08 13:41:35','2024-03-08 13:41:35'),('Pepper','e560fa53-97a5-42ad-bb57-7773942cc990','2024-03-08 13:41:48','2024-03-08 13:41:48'),('Meat','fc86af27-bd81-433b-9607-0798c4aa2d0d','2024-03-08 13:42:15','2024-03-08 13:42:15');
/*!40000 ALTER TABLE `Ingredients` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Recipes`
--

DROP TABLE IF EXISTS `Recipes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Recipes` (
  `content` varchar(700) NOT NULL,
  `food_id` varchar(200) NOT NULL,
  `__id` varchar(200) NOT NULL,
  `__created_at` datetime NOT NULL,
  `__updated_at` datetime NOT NULL,
  PRIMARY KEY (`__id`),
  UNIQUE KEY `content` (`content`),
  UNIQUE KEY `food_id` (`food_id`),
  CONSTRAINT `Recipes_ibfk_1` FOREIGN KEY (`food_id`) REFERENCES `Food` (`__id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Recipes`
--

LOCK TABLES `Recipes` WRITE;
/*!40000 ALTER TABLE `Recipes` DISABLE KEYS */;
INSERT INTO `Recipes` VALUES ('Cook the spaghetti according to the package instructions in a large pot of salted boiling water until al dente. Drain and set aside__In a large skillet or frying pan, heat the olive oil over medium heat. Add the chopped onion and minced garlic, and cook for 2-3 minutes until softened.__Add the minced beef to the skillet, breaking it up with a spoon, and cook until browned and cooked through.','e7f45d69-8c70-4d68-95c4-a0dca5a22945','73eda38b-a82d-4969-9d2b-e598d3dfe77b','2024-03-04 16:26:09','2024-03-10 14:37:52');
/*!40000 ALTER TABLE `Recipes` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-03-13 19:04:44
