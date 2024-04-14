/*
 Navicat Premium Data Transfer

 Source Server         : SELF_SQL
 Source Server Type    : MySQL
 Source Server Version : 80031
 Source Host           : localhost:3306
 Source Schema         : users

 Target Server Type    : MySQL
 Target Server Version : 80031
 File Encoding         : 65001

 Date: 22/10/2023 01:15:27
*/



SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

DROP DATABASE IF EXISTS `users`;
CREATE DATABASE users;
USE users;

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user`  (
  `username` varchar(255) NOT NULL,
  `passwd` varchar(255) NOT NULL,
  `describes` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`username`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES ('admin', '21232f297a57a5a743894a0e4a801fc3', 'welcome admin');
INSERT INTO `user` VALUES ('guest', '084e0343a0486ff05530df6c705c8bb4', 'hello~,guest');

SET FOREIGN_KEY_CHECKS = 1;
