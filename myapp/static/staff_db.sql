/*
 Navicat Premium Data Transfer

 Source Server         : MySQL
 Source Server Type    : MySQL
 Source Server Version : 80029
 Source Host           : localhost:3306
 Source Schema         : staff_db

 Target Server Type    : MySQL
 Target Server Version : 80029
 File Encoding         : 65001

 Date: 28/07/2022 10:54:34
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `name`(`name` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of auth_group
-- ----------------------------

-- ----------------------------
-- Table structure for auth_group_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_group_permissions_group_id_permission_id_0cd325b0_uniq`(`group_id` ASC, `permission_id` ASC) USING BTREE,
  INDEX `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm`(`permission_id` ASC) USING BTREE,
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of auth_group_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for auth_permission
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_permission_content_type_id_codename_01ab375a_uniq`(`content_type_id` ASC, `codename` ASC) USING BTREE,
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 49 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES (1, 'Can add log entry', 1, 'add_logentry');
INSERT INTO `auth_permission` VALUES (2, 'Can change log entry', 1, 'change_logentry');
INSERT INTO `auth_permission` VALUES (3, 'Can delete log entry', 1, 'delete_logentry');
INSERT INTO `auth_permission` VALUES (4, 'Can view log entry', 1, 'view_logentry');
INSERT INTO `auth_permission` VALUES (5, 'Can add permission', 2, 'add_permission');
INSERT INTO `auth_permission` VALUES (6, 'Can change permission', 2, 'change_permission');
INSERT INTO `auth_permission` VALUES (7, 'Can delete permission', 2, 'delete_permission');
INSERT INTO `auth_permission` VALUES (8, 'Can view permission', 2, 'view_permission');
INSERT INTO `auth_permission` VALUES (9, 'Can add group', 3, 'add_group');
INSERT INTO `auth_permission` VALUES (10, 'Can change group', 3, 'change_group');
INSERT INTO `auth_permission` VALUES (11, 'Can delete group', 3, 'delete_group');
INSERT INTO `auth_permission` VALUES (12, 'Can view group', 3, 'view_group');
INSERT INTO `auth_permission` VALUES (13, 'Can add user', 4, 'add_user');
INSERT INTO `auth_permission` VALUES (14, 'Can change user', 4, 'change_user');
INSERT INTO `auth_permission` VALUES (15, 'Can delete user', 4, 'delete_user');
INSERT INTO `auth_permission` VALUES (16, 'Can view user', 4, 'view_user');
INSERT INTO `auth_permission` VALUES (17, 'Can add content type', 5, 'add_contenttype');
INSERT INTO `auth_permission` VALUES (18, 'Can change content type', 5, 'change_contenttype');
INSERT INTO `auth_permission` VALUES (19, 'Can delete content type', 5, 'delete_contenttype');
INSERT INTO `auth_permission` VALUES (20, 'Can view content type', 5, 'view_contenttype');
INSERT INTO `auth_permission` VALUES (21, 'Can add session', 6, 'add_session');
INSERT INTO `auth_permission` VALUES (22, 'Can change session', 6, 'change_session');
INSERT INTO `auth_permission` VALUES (23, 'Can delete session', 6, 'delete_session');
INSERT INTO `auth_permission` VALUES (24, 'Can view session', 6, 'view_session');
INSERT INTO `auth_permission` VALUES (25, 'Can add department', 7, 'add_department');
INSERT INTO `auth_permission` VALUES (26, 'Can change department', 7, 'change_department');
INSERT INTO `auth_permission` VALUES (27, 'Can delete department', 7, 'delete_department');
INSERT INTO `auth_permission` VALUES (28, 'Can view department', 7, 'view_department');
INSERT INTO `auth_permission` VALUES (29, 'Can add user info', 8, 'add_userinfo');
INSERT INTO `auth_permission` VALUES (30, 'Can change user info', 8, 'change_userinfo');
INSERT INTO `auth_permission` VALUES (31, 'Can delete user info', 8, 'delete_userinfo');
INSERT INTO `auth_permission` VALUES (32, 'Can view user info', 8, 'view_userinfo');
INSERT INTO `auth_permission` VALUES (33, 'Can add admin info', 9, 'add_admininfo');
INSERT INTO `auth_permission` VALUES (34, 'Can change admin info', 9, 'change_admininfo');
INSERT INTO `auth_permission` VALUES (35, 'Can delete admin info', 9, 'delete_admininfo');
INSERT INTO `auth_permission` VALUES (36, 'Can view admin info', 9, 'view_admininfo');
INSERT INTO `auth_permission` VALUES (37, 'Can add task', 10, 'add_task');
INSERT INTO `auth_permission` VALUES (38, 'Can change task', 10, 'change_task');
INSERT INTO `auth_permission` VALUES (39, 'Can delete task', 10, 'delete_task');
INSERT INTO `auth_permission` VALUES (40, 'Can view task', 10, 'view_task');
INSERT INTO `auth_permission` VALUES (41, 'Can add orders', 11, 'add_orders');
INSERT INTO `auth_permission` VALUES (42, 'Can change orders', 11, 'change_orders');
INSERT INTO `auth_permission` VALUES (43, 'Can delete orders', 11, 'delete_orders');
INSERT INTO `auth_permission` VALUES (44, 'Can view orders', 11, 'view_orders');
INSERT INTO `auth_permission` VALUES (45, 'Can add city', 12, 'add_city');
INSERT INTO `auth_permission` VALUES (46, 'Can change city', 12, 'change_city');
INSERT INTO `auth_permission` VALUES (47, 'Can delete city', 12, 'delete_city');
INSERT INTO `auth_permission` VALUES (48, 'Can view city', 12, 'view_city');

-- ----------------------------
-- Table structure for auth_user
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `last_login` datetime(6) NULL DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `first_name` varchar(150) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `last_name` varchar(150) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `email` varchar(254) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `username`(`username` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of auth_user
-- ----------------------------

-- ----------------------------
-- Table structure for auth_user_groups
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_user_groups_user_id_group_id_94350c0c_uniq`(`user_id` ASC, `group_id` ASC) USING BTREE,
  INDEX `auth_user_groups_group_id_97559544_fk_auth_group_id`(`group_id` ASC) USING BTREE,
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of auth_user_groups
-- ----------------------------

-- ----------------------------
-- Table structure for auth_user_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq`(`user_id` ASC, `permission_id` ASC) USING BTREE,
  INDEX `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm`(`permission_id` ASC) USING BTREE,
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of auth_user_user_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for django_admin_log
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  `object_repr` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `action_flag` smallint UNSIGNED NOT NULL,
  `change_message` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `content_type_id` int NULL DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `django_admin_log_content_type_id_c4bce8eb_fk_django_co`(`content_type_id` ASC) USING BTREE,
  INDEX `django_admin_log_user_id_c564eba6_fk_auth_user_id`(`user_id` ASC) USING BTREE,
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `django_admin_log_chk_1` CHECK (`action_flag` >= 0)
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_admin_log
-- ----------------------------

-- ----------------------------
-- Table structure for django_content_type
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `model` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `django_content_type_app_label_model_76bd3d3b_uniq`(`app_label` ASC, `model` ASC) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 13 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES (1, 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES (3, 'auth', 'group');
INSERT INTO `django_content_type` VALUES (2, 'auth', 'permission');
INSERT INTO `django_content_type` VALUES (4, 'auth', 'user');
INSERT INTO `django_content_type` VALUES (5, 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES (9, 'myapp', 'admininfo');
INSERT INTO `django_content_type` VALUES (12, 'myapp', 'city');
INSERT INTO `django_content_type` VALUES (7, 'myapp', 'department');
INSERT INTO `django_content_type` VALUES (11, 'myapp', 'orders');
INSERT INTO `django_content_type` VALUES (10, 'myapp', 'task');
INSERT INTO `django_content_type` VALUES (8, 'myapp', 'userinfo');
INSERT INTO `django_content_type` VALUES (6, 'sessions', 'session');

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 21 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES (1, 'contenttypes', '0001_initial', '2022-07-26 08:22:37.257078');
INSERT INTO `django_migrations` VALUES (2, 'auth', '0001_initial', '2022-07-26 08:22:38.028658');
INSERT INTO `django_migrations` VALUES (3, 'admin', '0001_initial', '2022-07-26 08:22:38.319003');
INSERT INTO `django_migrations` VALUES (4, 'admin', '0002_logentry_remove_auto_add', '2022-07-26 08:22:38.329982');
INSERT INTO `django_migrations` VALUES (5, 'admin', '0003_logentry_add_action_flag_choices', '2022-07-26 08:22:38.340837');
INSERT INTO `django_migrations` VALUES (6, 'contenttypes', '0002_remove_content_type_name', '2022-07-26 08:22:38.436617');
INSERT INTO `django_migrations` VALUES (7, 'auth', '0002_alter_permission_name_max_length', '2022-07-26 08:22:38.519539');
INSERT INTO `django_migrations` VALUES (8, 'auth', '0003_alter_user_email_max_length', '2022-07-26 08:22:38.606846');
INSERT INTO `django_migrations` VALUES (9, 'auth', '0004_alter_user_username_opts', '2022-07-26 08:22:38.618379');
INSERT INTO `django_migrations` VALUES (10, 'auth', '0005_alter_user_last_login_null', '2022-07-26 08:22:38.715441');
INSERT INTO `django_migrations` VALUES (11, 'auth', '0006_require_contenttypes_0002', '2022-07-26 08:22:38.722584');
INSERT INTO `django_migrations` VALUES (12, 'auth', '0007_alter_validators_add_error_messages', '2022-07-26 08:22:38.733668');
INSERT INTO `django_migrations` VALUES (13, 'auth', '0008_alter_user_username_max_length', '2022-07-26 08:22:38.821198');
INSERT INTO `django_migrations` VALUES (14, 'auth', '0009_alter_user_last_name_max_length', '2022-07-26 08:22:38.912261');
INSERT INTO `django_migrations` VALUES (15, 'auth', '0010_alter_group_name_max_length', '2022-07-26 08:22:38.993926');
INSERT INTO `django_migrations` VALUES (16, 'auth', '0011_update_proxy_permissions', '2022-07-26 08:22:39.009127');
INSERT INTO `django_migrations` VALUES (17, 'auth', '0012_alter_user_first_name_max_length', '2022-07-26 08:22:39.099148');
INSERT INTO `django_migrations` VALUES (18, 'sessions', '0001_initial', '2022-07-26 08:22:39.158514');
INSERT INTO `django_migrations` VALUES (19, 'myapp', '0001_initial', '2022-07-26 08:27:38.210737');
INSERT INTO `django_migrations` VALUES (20, 'myapp', '0002_city', '2022-07-28 02:07:30.497012');

-- ----------------------------
-- Table structure for django_session
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session`  (
  `session_key` varchar(40) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `session_data` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`) USING BTREE,
  INDEX `django_session_expire_date_a5c62663`(`expire_date` ASC) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_session
-- ----------------------------
INSERT INTO `django_session` VALUES ('714l8kdhv49p8bn3si4j4kcz7lxaxvyv', 'eyJpbWFnZV9jb2RlIjoieXBQUSIsIl9zZXNzaW9uX2V4cGlyeSI6MzAwLCJpbmZvIjp7ImlkIjoxLCJ1c2VybmFtZSI6ImNpZCJ9fQ:1oGt7g:fQSfdGDlEpKTkoSO_B6YK0PDqTEmocTr9QUyPn1EP-8', '2022-07-28 02:24:36.696682');
INSERT INTO `django_session` VALUES ('g6vbd7k6k0pb60m1pkss8g3zuv5srhic', 'eyJpbWFnZV9jb2RlIjoiYWY0eCIsIl9zZXNzaW9uX2V4cGlyeSI6NjA0ODAwLCJpbmZvIjp7ImlkIjoxLCJ1c2VybmFtZSI6ImNpZCJ9fQ:1oGtFE:QrdL_JSkZywdUUdKHQi1fB5_5kTX_OCxdiLdREQInBk', '2022-08-04 02:27:24.373274');

-- ----------------------------
-- Table structure for myapp_admininfo
-- ----------------------------
DROP TABLE IF EXISTS `myapp_admininfo`;
CREATE TABLE `myapp_admininfo`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `password` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of myapp_admininfo
-- ----------------------------
INSERT INTO `myapp_admininfo` VALUES (1, 'cid', '635bc22614d72cb35ea09ed410ed1b31');

-- ----------------------------
-- Table structure for myapp_city
-- ----------------------------
DROP TABLE IF EXISTS `myapp_city`;
CREATE TABLE `myapp_city`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `count` int NOT NULL,
  `img` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of myapp_city
-- ----------------------------
INSERT INTO `myapp_city` VALUES (1, '长沙', 1200, 'city/12.jpg');
INSERT INTO `myapp_city` VALUES (2, '武汉', 60000, 'city/2.jpg');

-- ----------------------------
-- Table structure for myapp_department
-- ----------------------------
DROP TABLE IF EXISTS `myapp_department`;
CREATE TABLE `myapp_department`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `title` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of myapp_department
-- ----------------------------
INSERT INTO `myapp_department` VALUES (1, '运维部');
INSERT INTO `myapp_department` VALUES (2, '开发部');

-- ----------------------------
-- Table structure for myapp_orders
-- ----------------------------
DROP TABLE IF EXISTS `myapp_orders`;
CREATE TABLE `myapp_orders`  (
  `oid` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `title` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `price` double NOT NULL,
  `status` smallint NOT NULL,
  `admin_id` bigint NULL DEFAULT NULL,
  PRIMARY KEY (`oid`) USING BTREE,
  INDEX `myapp_orders_admin_id_055ece3d_fk_myapp_admininfo_id`(`admin_id` ASC) USING BTREE,
  CONSTRAINT `myapp_orders_admin_id_055ece3d_fk_myapp_admininfo_id` FOREIGN KEY (`admin_id`) REFERENCES `myapp_admininfo` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of myapp_orders
-- ----------------------------
INSERT INTO `myapp_orders` VALUES ('202207261630399830108', 'LOL', 11, 2, 1);
INSERT INTO `myapp_orders` VALUES ('202207261638002241635', '吃饭', 12, 1, 1);
INSERT INTO `myapp_orders` VALUES ('202207261850404958587', '英雄联盟', 34, 3, 1);
INSERT INTO `myapp_orders` VALUES ('202207261910055087337', 'kkkkk', 22, 3, 1);
INSERT INTO `myapp_orders` VALUES ('202207261917274339373', 'LOL', 156, 1, 1);
INSERT INTO `myapp_orders` VALUES ('202207262004295042274', 'wwe', 12, 1, 1);
INSERT INTO `myapp_orders` VALUES ('202207262004474377787', 'LOL666', 66, 1, 1);

-- ----------------------------
-- Table structure for myapp_task
-- ----------------------------
DROP TABLE IF EXISTS `myapp_task`;
CREATE TABLE `myapp_task`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `level` smallint NOT NULL,
  `title` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `detail` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `user_id` bigint NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `myapp_task_user_id_cac68a36_fk_myapp_userinfo_id`(`user_id` ASC) USING BTREE,
  CONSTRAINT `myapp_task_user_id_cac68a36_fk_myapp_userinfo_id` FOREIGN KEY (`user_id`) REFERENCES `myapp_userinfo` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of myapp_task
-- ----------------------------

-- ----------------------------
-- Table structure for myapp_userinfo
-- ----------------------------
DROP TABLE IF EXISTS `myapp_userinfo`;
CREATE TABLE `myapp_userinfo`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `password` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `age` int NOT NULL,
  `gender` smallint NOT NULL,
  `account` decimal(10, 2) NULL DEFAULT NULL,
  `create_time` datetime(6) NULL DEFAULT NULL,
  `department_id` bigint NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `myapp_userinfo_department_id_953c883d_fk_myapp_department_id`(`department_id` ASC) USING BTREE,
  CONSTRAINT `myapp_userinfo_department_id_953c883d_fk_myapp_department_id` FOREIGN KEY (`department_id`) REFERENCES `myapp_department` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of myapp_userinfo
-- ----------------------------
INSERT INTO `myapp_userinfo` VALUES (1, '熊嘉亮', '123', 22, 1, 2000.00, '2022-07-26 08:31:00.000000', 1);

SET FOREIGN_KEY_CHECKS = 1;
