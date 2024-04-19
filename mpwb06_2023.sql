/*
SQLyog Community v8.71 
MySQL - 5.5.30 : Database - mpwb06_2023
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`mpwb06_2023` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `mpwb06_2023`;

/*Table structure for table `booktable` */

DROP TABLE IF EXISTS `booktable`;

CREATE TABLE `booktable` (
  `resid` varchar(255) NOT NULL,
  `resname` varchar(255) NOT NULL,
  `resloc` varchar(255) NOT NULL,
  `userid` varchar(255) NOT NULL,
  `fid` varchar(255) NOT NULL,
  `food` varchar(255) NOT NULL,
  `table` varchar(255) NOT NULL,
  `dateandtime` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `booktable` */

insert  into `booktable`(`resid`,`resname`,`resloc`,`userid`,`fid`,`food`,`table`,`dateandtime`) values ('2','UniqueFood','Banajara Hills, Hyderabad','user1@gmail.com','4','Chicken Biryani','T2','2023-11-26 00:00:00');

/*Table structure for table `foods` */

DROP TABLE IF EXISTS `foods`;

CREATE TABLE `foods` (
  `fid` int(255) NOT NULL AUTO_INCREMENT,
  `resid` int(255) NOT NULL,
  `resname` varchar(255) NOT NULL,
  `resloc` varchar(255) NOT NULL,
  `fimage` varchar(255) NOT NULL,
  `fname` varchar(255) NOT NULL,
  `fdesc` longblob NOT NULL,
  `T1` varchar(255) NOT NULL DEFAULT 'Available',
  `T2` varchar(255) NOT NULL DEFAULT 'Available',
  `T3` varchar(255) NOT NULL DEFAULT 'Available',
  PRIMARY KEY (`fid`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `foods` */

insert  into `foods`(`fid`,`resid`,`resname`,`resloc`,`fimage`,`fname`,`fdesc`,`T1`,`T2`,`T3`) values (1,1,'FoodZone','Panjagutta, Hyderabad','static/uploads/pizza.png','Pizza','pizza, dish of Italian origin consisting of a flattened disk of bread dough topped with some combination of olive oil, oregano, tomato, olives, mozzarella or other cheese, and many other ingredients, baked quickly—usually, in a commercial setting, using a wood-fired oven heated to a very high temperature—and served hot ','Available','Available','Available'),(2,1,'FoodZone','Panjagutta, Hyderabad','static/uploads/burger.jpg','Burger','A burger is a patty of ground beef grilled and placed between two halves of a bun. Slices of raw onion, lettuce, bacon, mayonnaise, and other ingredients add flavor.','Available','Available','Available'),(3,1,'FoodZone','Panjagutta, Hyderabad','static/uploads/Sandwich.png','Sandwich','A sandwich is a food typically consisting of vegetables, sliced cheese or meat, placed on or between slices of bread, or more generally any dish wherein bread serves as a container or wrapper for another food type.','Available','Available','Available'),(4,2,'UniqueFood','Banajara Hills, Hyderabad','static/uploads/Biryani.png','Chicken Biryani','It is made with basmati rice, spices and goat meat. Popular variations use chicken instead of goat meat. There are various forms of Hyderabadi biryani, such as kachay gosht ki biryani or dum biryani, where goat meat is marinated and cooked along with the rice.','Available','T2','Available');

/*Table structure for table `seller` */

DROP TABLE IF EXISTS `seller`;

CREATE TABLE `seller` (
  `rid` int(255) NOT NULL AUTO_INCREMENT,
  `usedname` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `dob` varchar(255) NOT NULL,
  `mobile` varchar(255) NOT NULL,
  `resid` varchar(255) DEFAULT NULL,
  `resname` varchar(255) DEFAULT NULL,
  `resloc` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`rid`,`email`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `seller` */

insert  into `seller`(`rid`,`usedname`,`email`,`password`,`dob`,`mobile`,`resid`,`resname`,`resloc`) values (1,'seller1','seller1@gmail.com','Seller1@12','1999-01-02','1234567890','1','FoodZone','Panjagutta, Hyderabad'),(2,'seller2','seller2@gmail.com','Seller2@12','1996-04-02','0147258369','2','UniqueFood','Banajara Hills, Hyderabad');

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `rid` int(255) NOT NULL AUTO_INCREMENT,
  `usedname` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `dob` varchar(255) NOT NULL,
  `mobile` varchar(255) NOT NULL,
  PRIMARY KEY (`rid`,`email`),
  UNIQUE KEY `rid` (`rid`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `user` */

insert  into `user`(`rid`,`usedname`,`email`,`password`,`dob`,`mobile`) values (1,'user1','user1@gmail.com','User1@123','1999-02-01','7894561230');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
