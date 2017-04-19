CREATE DATABASE  IF NOT EXISTS `user_dashboard` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `user_dashboard`;
-- MySQL dump 10.13  Distrib 5.6.17, for osx10.6 (i386)
--
-- Host: 127.0.0.1    Database: user_dashboard
-- ------------------------------------------------------
-- Server version	5.6.33

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
-- Table structure for table `blocked`
--

DROP TABLE IF EXISTS `blocked`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `blocked` (
  `id` int(11) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  `blocked_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_blocked_users1_idx` (`user_id`),
  KEY `fk_blocked_users2_idx` (`blocked_id`),
  CONSTRAINT `fk_blocked_users1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_blocked_users2` FOREIGN KEY (`blocked_id`) REFERENCES `users` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blocked`
--

LOCK TABLES `blocked` WRITE;
/*!40000 ALTER TABLE `blocked` DISABLE KEYS */;
/*!40000 ALTER TABLE `blocked` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `chatrooms`
--

DROP TABLE IF EXISTS `chatrooms`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `chatrooms` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `alias` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `users_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_chatrooms_users1_idx` (`users_id`),
  CONSTRAINT `fk_chatrooms_users1` FOREIGN KEY (`users_id`) REFERENCES `users` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chatrooms`
--

LOCK TABLES `chatrooms` WRITE;
/*!40000 ALTER TABLE `chatrooms` DISABLE KEYS */;
/*!40000 ALTER TABLE `chatrooms` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `comments`
--

DROP TABLE IF EXISTS `comments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `comments` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `comment` text,
  `message_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_comments_messages1_idx` (`message_id`),
  KEY `fk_comments_users1_idx` (`user_id`),
  CONSTRAINT `fk_comments_messages1` FOREIGN KEY (`message_id`) REFERENCES `messages` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_comments_users1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comments`
--

LOCK TABLES `comments` WRITE;
/*!40000 ALTER TABLE `comments` DISABLE KEYS */;
INSERT INTO `comments` VALUES (1,'First comment?',8,3,'2017-02-07 21:37:37','2017-02-07 21:37:37'),(2,'asdfdsff!!!',8,2,'2017-02-07 22:24:38','2017-02-08 20:31:42'),(3,'wreeellllll?',4,2,'2017-02-07 22:26:02','2017-02-07 22:26:02'),(6,'No you are not, you are a rat...',7,2,'2017-02-08 19:22:29','2017-02-08 19:22:29'),(7,'I made a change? Did I?!!',15,2,'2017-02-08 20:20:41','2017-02-08 20:31:55'),(8,'hghg',16,3,'2017-02-12 16:32:59','2017-02-12 16:33:04');
/*!40000 ALTER TABLE `comments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `friends`
--

DROP TABLE IF EXISTS `friends`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `friends` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `friend_id` int(11) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_friends_users_idx` (`user_id`),
  KEY `fk_friends_users1_idx` (`friend_id`),
  CONSTRAINT `fk_friends_users` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_friends_users1` FOREIGN KEY (`friend_id`) REFERENCES `users` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=76 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `friends`
--

LOCK TABLES `friends` WRITE;
/*!40000 ALTER TABLE `friends` DISABLE KEYS */;
INSERT INTO `friends` VALUES (4,3,1,'2017-02-07 18:09:33','2017-02-07 18:09:33'),(72,2,3,'2017-02-08 23:45:21','2017-02-08 23:45:21'),(73,1,3,'2017-02-08 23:47:10','2017-02-08 23:47:10'),(74,1,2,'2017-02-08 23:50:18','2017-02-08 23:50:18'),(75,2,1,'2017-02-08 23:50:25','2017-02-08 23:50:25');
/*!40000 ALTER TABLE `friends` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `messages`
--

DROP TABLE IF EXISTS `messages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `messages` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `message` text,
  `user_id` int(11) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_messages_users1_idx` (`user_id`),
  CONSTRAINT `fk_messages_users1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `messages`
--

LOCK TABLES `messages` WRITE;
/*!40000 ALTER TABLE `messages` DISABLE KEYS */;
INSERT INTO `messages` VALUES (3,'Hiya!',2,'2017-02-07 18:21:42','2017-02-07 18:21:42'),(4,'This is pretty cool right?',3,'2017-02-07 18:22:28','2017-02-07 18:22:28'),(5,'I am working!',3,'2017-02-07 18:29:12','2017-02-07 18:29:12'),(7,'Am I cool????',3,'2017-02-07 19:19:28','2017-02-07 19:19:28'),(8,'dfdf',3,'2017-02-07 21:25:46','2017-02-07 21:25:46'),(15,'dfdsfadsaf!!!',2,'2017-02-08 17:22:11','2017-02-08 20:20:31'),(16,'hgffh',3,'2017-02-12 16:32:56','2017-02-12 16:32:56');
/*!40000 ALTER TABLE `messages` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `private_messages`
--

DROP TABLE IF EXISTS `private_messages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `private_messages` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `message` text,
  `user_id` int(11) NOT NULL,
  `friend_id` int(11) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_private_messages_users1_idx` (`user_id`),
  KEY `fk_private_messages_users2_idx` (`friend_id`),
  CONSTRAINT `fk_private_messages_users1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_private_messages_users2` FOREIGN KEY (`friend_id`) REFERENCES `users` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=58 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `private_messages`
--

LOCK TABLES `private_messages` WRITE;
/*!40000 ALTER TABLE `private_messages` DISABLE KEYS */;
INSERT INTO `private_messages` VALUES (1,'hi',2,1,'2017-02-07 18:08:45','2017-02-07 18:08:45'),(2,'Mella!',2,1,'2017-02-07 18:11:32','2017-02-07 18:11:32'),(3,'Hey!',3,2,'2017-02-07 23:02:22','2017-02-07 23:02:22'),(4,'does this work?',2,3,'2017-02-07 23:02:47','2017-02-07 23:02:47'),(5,'Seems to....',3,2,'2017-02-07 23:02:58','2017-02-07 23:02:58'),(6,'Hello',1,3,'2017-02-09 00:04:35','2017-02-09 00:04:35'),(7,'Why are not not talking to me?',2,1,'2017-02-09 00:05:18','2017-02-09 00:05:18'),(8,'Hello',1,3,'2017-02-09 00:05:26','2017-02-09 00:05:26'),(9,'23',2,1,'2017-02-09 00:40:42','2017-02-09 00:40:42'),(10,'ds',2,1,'2017-02-09 00:43:23','2017-02-09 00:43:23'),(11,'sdf',2,1,'2017-02-09 00:48:36','2017-02-09 00:48:36'),(12,'s',2,1,'2017-02-09 00:48:38','2017-02-09 00:48:38'),(13,'s',2,1,'2017-02-09 01:01:06','2017-02-09 01:01:06'),(14,'a',2,1,'2017-02-09 01:01:24','2017-02-09 01:01:24'),(15,'ad',2,1,'2017-02-09 01:03:31','2017-02-09 01:03:31'),(16,'mela',2,1,'2017-02-09 01:05:57','2017-02-09 01:05:57'),(17,'dsfdsfdsfsd',2,1,'2017-02-09 01:07:09','2017-02-09 01:07:09'),(18,'sdf',2,1,'2017-02-09 01:07:46','2017-02-09 01:07:46'),(19,'dsad',2,1,'2017-02-09 01:07:53','2017-02-09 01:07:53'),(20,'dsfdsfdsf',2,1,'2017-02-09 01:08:41','2017-02-09 01:08:41'),(21,'dsf',2,1,'2017-02-09 01:09:35','2017-02-09 01:09:35'),(22,'sdsf',2,1,'2017-02-09 01:10:12','2017-02-09 01:10:12'),(23,'dsfds',2,1,'2017-02-09 01:10:14','2017-02-09 01:10:14'),(24,'dfsdfd',2,1,'2017-02-09 01:10:49','2017-02-09 01:10:49'),(25,'dsfsdf',2,1,'2017-02-09 01:11:25','2017-02-09 01:11:25'),(26,'hlg',2,1,'2017-02-09 01:12:08','2017-02-09 01:12:08'),(27,'sdf',2,1,'2017-02-09 01:13:17','2017-02-09 01:13:17'),(28,'sdf',2,1,'2017-02-09 01:15:00','2017-02-09 01:15:00'),(29,'hella!',2,1,'2017-02-09 01:15:04','2017-02-09 01:15:04'),(30,'Harvey doesn\'t know this!',1,3,'2017-02-09 01:15:28','2017-02-09 01:15:28'),(31,'Matt doesn\'t know this!!',2,3,'2017-02-09 01:15:40','2017-02-09 01:15:40'),(32,'Stop spamming me!',1,2,'2017-02-09 01:15:55','2017-02-09 01:15:55'),(33,'Yeah?',2,3,'2017-02-09 01:16:03','2017-02-09 01:16:03'),(34,'Too much stuff!',1,2,'2017-02-09 01:16:16','2017-02-09 01:16:16'),(35,'moo?',2,1,'2017-02-09 01:16:25','2017-02-09 01:16:25'),(36,'Hiya',2,1,'2017-02-09 01:17:46','2017-02-09 01:17:46'),(37,'fdfdf',2,1,'2017-02-09 01:18:44','2017-02-09 01:18:44'),(38,'sfdf',2,1,'2017-02-09 01:19:16','2017-02-09 01:19:16'),(39,'ads',2,1,'2017-02-09 01:20:14','2017-02-09 01:20:14'),(40,'dsfsd',2,1,'2017-02-09 01:21:19','2017-02-09 01:21:19'),(41,'sfd',2,1,'2017-02-09 01:22:57','2017-02-09 01:22:57'),(42,'dfs',2,1,'2017-02-09 01:23:40','2017-02-09 01:23:40'),(43,'Hiya!',2,1,'2017-02-09 01:24:28','2017-02-09 01:24:28'),(44,'yellow',1,2,'2017-02-09 01:24:42','2017-02-09 01:24:42'),(45,'brown',1,2,'2017-02-09 01:24:58','2017-02-09 01:24:58'),(46,'purple',2,1,'2017-02-09 01:25:04','2017-02-09 01:25:04'),(47,'sadsa',2,1,'2017-02-09 01:25:39','2017-02-09 01:25:39'),(48,'purple',1,2,'2017-02-09 01:26:17','2017-02-09 01:26:17'),(49,'brown',2,1,'2017-02-09 01:26:25','2017-02-09 01:26:25'),(50,'sdfsd',2,1,'2017-02-09 01:27:34','2017-02-09 01:27:34'),(51,'Yeah it\'s working!',1,2,'2017-02-09 01:27:53','2017-02-09 01:27:53'),(52,'Matt is clueless right?',2,3,'2017-02-09 01:28:10','2017-02-09 01:28:10'),(53,'Comeback!',1,2,'2017-02-09 01:28:21','2017-02-09 01:28:21'),(54,'I am talking to you!',1,2,'2017-02-09 01:37:17','2017-02-09 01:37:17'),(55,'I am still talking to you!',1,2,'2017-02-09 01:37:38','2017-02-09 01:37:38'),(56,'fvgv',1,2,'2017-02-11 12:19:12','2017-02-11 12:19:12'),(57,'gfhgg',3,1,'2017-02-12 16:33:44','2017-02-12 16:33:44');
/*!40000 ALTER TABLE `private_messages` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(255) DEFAULT NULL,
  `first_name` varchar(255) DEFAULT NULL,
  `last_name` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `num_friends` int(11) DEFAULT NULL,
  `description` text,
  `level` int(11) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'matt@matt.com','matt','matt','$2b$12$NH4fYkyDS1buXI/PZE9OOexU/Yx/kAp1NuOo8kj7OIfdSTgcv7MZK',2,NULL,9,'2016-12-22 19:49:46','2016-12-22 19:49:46'),(2,'harveychui@berkeley.edu','Harvey','Chui','$2b$12$kcaKADk7pybUw5YkaHw/Y.QXlYi/PoWwfW4G8c7RJP8N9TGf6ZFVK',1,'I am Harvey Chui, nice to meet you.  I am passionated about anything that is related to technology.  However, I am especially passionate about coding, computer hardware, machine learning, and video games.  I also immensely love reading!',1,'2016-12-22 19:50:12','2016-12-22 19:50:12'),(3,'rat@rat.com','Rat','Rat','$2b$12$O1pBmTWO.s7aPUcJ7.fjFuAS80QG7z6qHn0aNLu.m51op6Q7aUhSa',1,NULL,1,'2017-02-07 18:09:28','2017-02-07 18:09:28');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-04-19 14:27:57
