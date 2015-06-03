-- MySQL dump 10.13  Distrib 5.1.73, for redhat-linux-gnu (x86_64)
--
-- Host: localhost    Database: cmdb
-- ------------------------------------------------------
-- Server version	5.1.73

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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_5f412f9a` (`group_id`),
  KEY `auth_group_permissions_83d7f98b` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_37ef4eb4` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=73 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add server',7,'add_server'),(20,'Can change server',7,'change_server'),(21,'Can delete server',7,'delete_server'),(22,'Can add storage',8,'add_storage'),(23,'Can change storage',8,'change_storage'),(24,'Can delete storage',8,'delete_storage'),(25,'Can add vm',9,'add_vm'),(26,'Can change vm',9,'change_vm'),(27,'Can delete vm',9,'delete_vm'),(28,'Can add model',10,'add_model'),(29,'Can change model',10,'change_model'),(30,'Can delete model',10,'delete_model'),(31,'Can add vendor',11,'add_vendor'),(32,'Can change vendor',11,'change_vendor'),(33,'Can delete vendor',11,'delete_vendor'),(34,'Can add os',12,'add_os'),(35,'Can change os',12,'change_os'),(36,'Can delete os',12,'delete_os'),(37,'Can add kernel',13,'add_kernel'),(38,'Can change kernel',13,'change_kernel'),(39,'Can delete kernel',13,'delete_kernel'),(40,'Can add cpu',14,'add_cpu'),(41,'Can change cpu',14,'change_cpu'),(42,'Can delete cpu',14,'delete_cpu'),(43,'Can add memory',15,'add_memory'),(44,'Can change memory',15,'change_memory'),(45,'Can delete memory',15,'delete_memory'),(46,'Can add disk',16,'add_disk'),(47,'Can change disk',16,'change_disk'),(48,'Can delete disk',16,'delete_disk'),(49,'Can add raid',17,'add_raid'),(50,'Can change raid',17,'change_raid'),(51,'Can delete raid',17,'delete_raid'),(52,'Can add service',18,'add_service'),(53,'Can change service',18,'change_service'),(54,'Can delete service',18,'delete_service'),(55,'Can add idc',19,'add_idc'),(56,'Can change idc',19,'change_idc'),(57,'Can delete idc',19,'delete_idc'),(58,'Can add rack',20,'add_rack'),(59,'Can change rack',20,'change_rack'),(60,'Can delete rack',20,'delete_rack'),(61,'Can add zone',21,'add_zone'),(62,'Can change zone',21,'change_zone'),(63,'Can delete zone',21,'delete_zone'),(64,'Can add ip',22,'add_ip'),(65,'Can change ip',22,'change_ip'),(66,'Can delete ip',22,'delete_ip'),(67,'Can add mac',23,'add_mac'),(68,'Can change mac',23,'change_mac'),(69,'Can delete mac',23,'delete_mac'),(70,'Can add department',24,'add_department'),(71,'Can change department',24,'change_department'),(72,'Can delete department',24,'delete_department');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(75) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$12000$rWBPhfmZhIX8$u3YvhLWGMkRWHoOS64Zl/cLLxirPOjL7JGb5IsKqkOQ=','2015-05-07 10:22:11',1,'admin','','','jiaminqiangx@163.com',1,1,'2015-05-07 10:20:42');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_6340c63c` (`user_id`),
  KEY `auth_user_groups_5f412f9a` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_6340c63c` (`user_id`),
  KEY `auth_user_user_permissions_83d7f98b` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cmdb_cpu`
--

DROP TABLE IF EXISTS `cmdb_cpu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cmdb_cpu` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cpu_Type` varchar(30) NOT NULL,
  `cpu_Cores` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cmdb_cpu`
--

LOCK TABLES `cmdb_cpu` WRITE;
/*!40000 ALTER TABLE `cmdb_cpu` DISABLE KEYS */;
/*!40000 ALTER TABLE `cmdb_cpu` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cmdb_department`
--

DROP TABLE IF EXISTS `cmdb_department`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cmdb_department` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Department_Name` varchar(50) NOT NULL,
  `Department_Contact` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cmdb_department`
--

LOCK TABLES `cmdb_department` WRITE;
/*!40000 ALTER TABLE `cmdb_department` DISABLE KEYS */;
/*!40000 ALTER TABLE `cmdb_department` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cmdb_disk`
--

DROP TABLE IF EXISTS `cmdb_disk`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cmdb_disk` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Disk_Vendor` varchar(30) NOT NULL,
  `Disk_Capacity` varchar(30) NOT NULL,
  `Disk_Type` varchar(30) NOT NULL,
  `Disk_Size` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cmdb_disk`
--

LOCK TABLES `cmdb_disk` WRITE;
/*!40000 ALTER TABLE `cmdb_disk` DISABLE KEYS */;
/*!40000 ALTER TABLE `cmdb_disk` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cmdb_idc`
--

DROP TABLE IF EXISTS `cmdb_idc`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cmdb_idc` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `IDC_Name` varchar(50) NOT NULL,
  `IDC_Location` varchar(100) NOT NULL,
  `IDC_Contact` varchar(100) NOT NULL,
  `IDC_Phone` varchar(20) NOT NULL,
  `IDC_Email` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cmdb_idc`
--

LOCK TABLES `cmdb_idc` WRITE;
/*!40000 ALTER TABLE `cmdb_idc` DISABLE KEYS */;
/*!40000 ALTER TABLE `cmdb_idc` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cmdb_ip`
--

DROP TABLE IF EXISTS `cmdb_ip`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cmdb_ip` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `IP` char(15) NOT NULL,
  `IP_Type` int(11) NOT NULL,
  `Device_id` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cmdb_ip`
--

LOCK TABLES `cmdb_ip` WRITE;
/*!40000 ALTER TABLE `cmdb_ip` DISABLE KEYS */;
/*!40000 ALTER TABLE `cmdb_ip` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cmdb_kernel`
--

DROP TABLE IF EXISTS `cmdb_kernel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cmdb_kernel` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Kernel` varchar(30) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cmdb_kernel`
--

LOCK TABLES `cmdb_kernel` WRITE;
/*!40000 ALTER TABLE `cmdb_kernel` DISABLE KEYS */;
/*!40000 ALTER TABLE `cmdb_kernel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cmdb_mac`
--

DROP TABLE IF EXISTS `cmdb_mac`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cmdb_mac` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `MAC` varchar(50) NOT NULL,
  `MAC_Type` int(11) NOT NULL,
  `Device_id` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cmdb_mac`
--

LOCK TABLES `cmdb_mac` WRITE;
/*!40000 ALTER TABLE `cmdb_mac` DISABLE KEYS */;
/*!40000 ALTER TABLE `cmdb_mac` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cmdb_memory`
--

DROP TABLE IF EXISTS `cmdb_memory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cmdb_memory` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Memory_Vendor` varchar(30) NOT NULL,
  `Memory_Type` varchar(30) NOT NULL,
  `Memory_Size` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cmdb_memory`
--

LOCK TABLES `cmdb_memory` WRITE;
/*!40000 ALTER TABLE `cmdb_memory` DISABLE KEYS */;
/*!40000 ALTER TABLE `cmdb_memory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cmdb_model`
--

DROP TABLE IF EXISTS `cmdb_model`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cmdb_model` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Model_Name` varchar(30) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cmdb_model`
--

LOCK TABLES `cmdb_model` WRITE;
/*!40000 ALTER TABLE `cmdb_model` DISABLE KEYS */;
/*!40000 ALTER TABLE `cmdb_model` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cmdb_os`
--

DROP TABLE IF EXISTS `cmdb_os`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cmdb_os` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `OS_Name` varchar(30) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cmdb_os`
--

LOCK TABLES `cmdb_os` WRITE;
/*!40000 ALTER TABLE `cmdb_os` DISABLE KEYS */;
/*!40000 ALTER TABLE `cmdb_os` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cmdb_rack`
--

DROP TABLE IF EXISTS `cmdb_rack`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cmdb_rack` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Rack_Name` varchar(30) NOT NULL,
  `IDC_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `cmdb_rack_35751f8d` (`IDC_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cmdb_rack`
--

LOCK TABLES `cmdb_rack` WRITE;
/*!40000 ALTER TABLE `cmdb_rack` DISABLE KEYS */;
/*!40000 ALTER TABLE `cmdb_rack` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cmdb_raid`
--

DROP TABLE IF EXISTS `cmdb_raid`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cmdb_raid` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Raid_Type` varchar(30) NOT NULL,
  `Raid_Cache` int(11) NOT NULL,
  `Raid_Battery` varchar(30) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cmdb_raid`
--

LOCK TABLES `cmdb_raid` WRITE;
/*!40000 ALTER TABLE `cmdb_raid` DISABLE KEYS */;
/*!40000 ALTER TABLE `cmdb_raid` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cmdb_server`
--

DROP TABLE IF EXISTS `cmdb_server`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cmdb_server` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Server_SN` varchar(30) NOT NULL,
  `Asset_id` int(11) NOT NULL,
  `Vendor_id` int(11) NOT NULL,
  `Modle_id` int(11) NOT NULL,
  `OS_id` int(11) NOT NULL,
  `Kernel_id` int(11) NOT NULL,
  `HostName` varchar(50) DEFAULT NULL,
  `Service_id` int(11) NOT NULL,
  `Service_Module` varchar(50) NOT NULL,
  `Department_id` int(11) NOT NULL,
  `IDC_id` int(11) NOT NULL,
  `Rack_id` int(11) NOT NULL,
  `CPU_id` int(11) NOT NULL,
  `CPU_Number` int(11) NOT NULL,
  `Memory_id` int(11) NOT NULL,
  `Memory_Size` int(11) NOT NULL,
  `Disk_id` int(11) NOT NULL,
  `Disk_Solt_Number` int(11) NOT NULL,
  `Disk__Number` int(11) NOT NULL,
  `RAID_id` int(11) NOT NULL,
  `RAID_Level` int(11) NOT NULL,
  `WAN_IP` int(11) DEFAULT NULL,
  `LAN_IP` int(11) DEFAULT NULL,
  `RAC_IP` int(11) DEFAULT NULL,
  `WAN_mac` int(11) DEFAULT NULL,
  `LAN_mac` int(11) DEFAULT NULL,
  `RAC_mac` int(11) DEFAULT NULL,
  `Purchasing_Time` time DEFAULT NULL,
  `Guarantee_Time` time DEFAULT NULL,
  `Change_Time` time DEFAULT NULL,
  `Change_Info` varchar(100) DEFAULT NULL,
  `Owner` varchar(30) DEFAULT NULL,
  `Up__Time` time DEFAULT NULL,
  `State` int(11) DEFAULT NULL,
  `Remarks` varchar(100) DEFAULT NULL,
  `Zone_id` int(11) DEFAULT NULL,
  `VM_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cmdb_server`
--

LOCK TABLES `cmdb_server` WRITE;
/*!40000 ALTER TABLE `cmdb_server` DISABLE KEYS */;
/*!40000 ALTER TABLE `cmdb_server` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cmdb_service`
--

DROP TABLE IF EXISTS `cmdb_service`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cmdb_service` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Service_name` varchar(30) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cmdb_service`
--

LOCK TABLES `cmdb_service` WRITE;
/*!40000 ALTER TABLE `cmdb_service` DISABLE KEYS */;
/*!40000 ALTER TABLE `cmdb_service` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cmdb_storage`
--

DROP TABLE IF EXISTS `cmdb_storage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cmdb_storage` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Storage_SN` varchar(30) NOT NULL,
  `Asset_id` int(11) NOT NULL,
  `Vendor_id` int(11) NOT NULL,
  `Modle_id` int(11) NOT NULL,
  `HostName` varchar(50) DEFAULT NULL,
  `Service_id` int(11) NOT NULL,
  `Service_Module` varchar(50) NOT NULL,
  `IDC_id` int(11) NOT NULL,
  `Rack_id` int(11) NOT NULL,
  `WAN_IP` int(11) DEFAULT NULL,
  `LAN_IP` int(11) DEFAULT NULL,
  `RAC_IP` int(11) DEFAULT NULL,
  `WAN_mac` int(11) DEFAULT NULL,
  `LAN_mac` int(11) DEFAULT NULL,
  `RAC_mac` int(11) DEFAULT NULL,
  `Purchasing_Time` time DEFAULT NULL,
  `Guarantee_Time` time DEFAULT NULL,
  `Change_Time` time DEFAULT NULL,
  `Change_Info` varchar(100) DEFAULT NULL,
  `Owner` varchar(30) DEFAULT NULL,
  `Up__Time` time DEFAULT NULL,
  `State` int(11) DEFAULT NULL,
  `Remarks` varchar(100) DEFAULT NULL,
  `Zone_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cmdb_storage`
--

LOCK TABLES `cmdb_storage` WRITE;
/*!40000 ALTER TABLE `cmdb_storage` DISABLE KEYS */;
/*!40000 ALTER TABLE `cmdb_storage` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cmdb_vendor`
--

DROP TABLE IF EXISTS `cmdb_vendor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cmdb_vendor` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Vendor__Name` varchar(30) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cmdb_vendor`
--

LOCK TABLES `cmdb_vendor` WRITE;
/*!40000 ALTER TABLE `cmdb_vendor` DISABLE KEYS */;
/*!40000 ALTER TABLE `cmdb_vendor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cmdb_vm`
--

DROP TABLE IF EXISTS `cmdb_vm`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cmdb_vm` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `OS_id` int(11) NOT NULL,
  `Kernel_id` int(11) NOT NULL,
  `HostName` varchar(50) DEFAULT NULL,
  `Service_id` int(11) NOT NULL,
  `Service_Module` varchar(50) NOT NULL,
  `Department_id` int(11) NOT NULL,
  `Server_id` int(11) NOT NULL,
  `CPU_Number` int(11) NOT NULL,
  `Memory_Size` int(11) NOT NULL,
  `Disk__Size` int(11) NOT NULL,
  `WAN_IP` int(11) DEFAULT NULL,
  `LAN_IP` int(11) DEFAULT NULL,
  `WAN_mac` int(11) DEFAULT NULL,
  `LAN_mac` int(11) DEFAULT NULL,
  `Purchasing_Time` time DEFAULT NULL,
  `Guarantee_Time` time DEFAULT NULL,
  `Change_Time` time DEFAULT NULL,
  `Change_Info` varchar(100) DEFAULT NULL,
  `Owner` varchar(30) DEFAULT NULL,
  `Up__Time` time DEFAULT NULL,
  `State` int(11) DEFAULT NULL,
  `Remarks` varchar(100) DEFAULT NULL,
  `Zone_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cmdb_vm`
--

LOCK TABLES `cmdb_vm` WRITE;
/*!40000 ALTER TABLE `cmdb_vm` DISABLE KEYS */;
/*!40000 ALTER TABLE `cmdb_vm` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cmdb_zone`
--

DROP TABLE IF EXISTS `cmdb_zone`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cmdb_zone` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Zone_Name` varchar(50) NOT NULL,
  `Zone_Info` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cmdb_zone`
--

LOCK TABLES `cmdb_zone` WRITE;
/*!40000 ALTER TABLE `cmdb_zone` DISABLE KEYS */;
/*!40000 ALTER TABLE `cmdb_zone` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `user_id` int(11) NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_6340c63c` (`user_id`),
  KEY `django_admin_log_37ef4eb4` (`content_type_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app_label` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=25 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'log entry','admin','logentry'),(2,'permission','auth','permission'),(3,'group','auth','group'),(4,'user','auth','user'),(5,'content type','contenttypes','contenttype'),(6,'session','sessions','session'),(7,'server','cmdb','server'),(8,'storage','cmdb','storage'),(9,'vm','cmdb','vm'),(10,'model','cmdb','model'),(11,'vendor','cmdb','vendor'),(12,'os','cmdb','os'),(13,'kernel','cmdb','kernel'),(14,'cpu','cmdb','cpu'),(15,'memory','cmdb','memory'),(16,'disk','cmdb','disk'),(17,'raid','cmdb','raid'),(18,'service','cmdb','service'),(19,'idc','cmdb','idc'),(20,'rack','cmdb','rack'),(21,'zone','cmdb','zone'),(22,'ip','cmdb','ip'),(23,'mac','cmdb','mac'),(24,'department','cmdb','department');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_b7b81f0c` (`expire_date`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('fuxor3udgcreu8tm5h7nu7b2f8krmfsw','YWJmZDQ0ODFiZmQ5MzhkY2YyNTE2ZTk0MTU1YWE1ZTZmMjgwMmFjYjp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6MX0=','2015-05-21 10:22:11');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-05-12 17:32:57
