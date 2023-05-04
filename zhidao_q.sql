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

 Date: 04/05/2023 20:56:05
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for zhidao_q
-- ----------------------------
DROP TABLE IF EXISTS `zhidao_q`;
CREATE TABLE `zhidao_q`  (
  `url` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `key` text CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL,
  `title` text CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL,
  `question` text CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL,
  `answer` text CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL,
  `date` datetime(0) NULL DEFAULT NULL,
  `count` int(0) NULL DEFAULT NULL,
  `agree` int(0) NULL DEFAULT NULL,
  `answerer` text CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL,
  `create_date` datetime(0) NULL DEFAULT NULL,
  `has_crawl` int(0) NULL DEFAULT 0,
  PRIMARY KEY (`url`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
