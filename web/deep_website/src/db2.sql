/*
 Navicat Premium Data Transfer

 Source Server         : SELF_SQL
 Source Server Type    : MySQL
 Source Server Version : 80031
 Source Host           : localhost:3306
 Source Schema         : secret

 Target Server Type    : MySQL
 Target Server Version : 80031
 File Encoding         : 65001

 Date: 22/10/2023 01:15:16
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

DROP DATABASE IF EXISTS `secret`;
CREATE DATABASE secret;
USE secret;

-- ----------------------------
-- Table structure for path
-- ----------------------------
DROP TABLE IF EXISTS `path`;
CREATE TABLE `path`  (
  `filename` varchar(255) NOT NULL,
  `filepath` varchar(255) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of path
-- ----------------------------
INSERT INTO `path` VALUES ('flagggggg__wher_e_14_F5MSsYteUvm21W9w.txt', '/var/www/html/');
INSERT INTO `path` VALUES ('Mysql_connect_shell.php', '/var/www/html/');

SET FOREIGN_KEY_CHECKS = 1;

