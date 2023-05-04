/*
 Navicat Premium Data Transfer

 Source Server         : root
 Source Server Type    : MySQL
 Source Server Version : 80033
 Source Host           : localhost:3306
 Source Schema         : aerospace

 Target Server Type    : MySQL
 Target Server Version : 80033
 File Encoding         : 65001

 Date: 04/05/2023 20:55:58
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for zhidao
-- ----------------------------
DROP TABLE IF EXISTS `zhidao`;
CREATE TABLE `zhidao`  (
  `url` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `title` text CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL,
  `key` text CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL,
  `best_answer` text CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL,
  `other_answers` text CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL,
  `create_date` datetime(0) NULL DEFAULT NULL,
  PRIMARY KEY (`url`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
