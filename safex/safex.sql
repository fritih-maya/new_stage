-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1
-- Généré le : mar. 08 avr. 2025 à 23:29
-- Version du serveur : 10.4.32-MariaDB
-- Version de PHP : 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `safex`
--

-- --------------------------------------------------------

--
-- Structure de la table `auth_app_department`
--

CREATE TABLE `auth_app_department` (
  `id_department` int(11) NOT NULL,
  `name_dep` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `auth_app_department`
--

INSERT INTO `auth_app_department` (`id_department`, `name_dep`) VALUES
(1, 'informatique'),
(2, 'marketing'),
(3, 'finance'),
(4, 'RH'),
(5, 'commerce'),
(6, 'réseaux'),
(7, 'securite'),
(8, 'dit');

-- --------------------------------------------------------

--
-- Structure de la table `auth_app_files`
--

CREATE TABLE `auth_app_files` (
  `id` bigint(20) NOT NULL,
  `name_file` varchar(50) NOT NULL,
  `date` datetime(6) NOT NULL,
  `file_upload` varchar(100) NOT NULL,
  `id_department_id` int(11) NOT NULL,
  `id_user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `auth_app_files`
--

INSERT INTO `auth_app_files` (`id`, `name_file`, `date`, `file_upload`, `id_department_id`, `id_user_id`) VALUES
(1, 'essai', '2025-02-24 19:41:21.310206', 'uploads/1-s2.0-S2772662223002308-main_lpDD4jI.pdf', 1, 2),
(5, 'essai3', '2025-02-28 23:50:34.291186', 'uploads/Sergeev_Yury.pdf', 1, 2),
(6, 'essai4', '2025-02-28 23:50:54.444472', 'uploads/Rapport_fin_etude_debab_djerboa_.pdf', 1, 2),
(8, 'essai-yanis', '2025-02-28 23:55:48.762061', 'uploads/2024TLSES052.pdf', 2, 4),
(9, 'essai5', '2025-03-01 22:19:54.973989', 'uploads/2024TLSES052_RgrdyFO.pdf', 1, 2),
(10, 'mark1', '2025-03-01 23:20:14.745017', 'uploads/2025.nakbanlp-1.9.pdf', 2, 2),
(12, 'mark_maintenant', '2025-03-02 14:11:10.006511', 'uploads/BEERREKBIA-BOURANE_6fncJi1.pdf', 2, 2),
(13, 'sujet', '2025-04-08 21:06:10.974648', 'uploads/Zitouni_3vfdEYt.pdf', 1, 5);

-- --------------------------------------------------------

--
-- Structure de la table `auth_app_user`
--

CREATE TABLE `auth_app_user` (
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `id_user` int(11) NOT NULL,
  `name_user` varchar(50) NOT NULL,
  `mail_user` varchar(50) NOT NULL,
  `password` varchar(128) NOT NULL,
  `type` varchar(50) NOT NULL,
  `departement_principal_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `auth_app_user`
--

INSERT INTO `auth_app_user` (`last_login`, `is_superuser`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`, `id_user`, `name_user`, `mail_user`, `password`, `type`, `departement_principal_id`) VALUES
('2025-04-08 21:07:47.782301', 1, '', '', '', 1, 1, '2025-02-24 17:48:19.595850', 1, 'admin', 'admin.admin@safex.dz', 'pbkdf2_sha256$260000$XrhLse3HN8jV2mfiWwI82d$z4BrIepNXp6kjS2CVdOyrCHV2tZpavtvj1Zaq+IyV0g=', 'employe_simple', NULL),
('2025-04-08 21:10:00.687739', 0, '', '', '', 0, 1, '2025-02-24 17:50:47.612750', 2, 'souheil', 'souheil.benamar@safex.dz', 'pbkdf2_sha256$260000$TpNJhjg6VR8HvnPCXF16vc$BarYILofgtoLv1FwG2F6Dy8PBGTmacEkXo58OBxmT24=', 'chef_service', 1),
('2025-03-01 23:31:36.310462', 0, '', '', '', 0, 1, '2025-02-24 17:59:39.765002', 3, 'anais', 'anais.fritih@safex.dz', 'pbkdf2_sha256$260000$KMq2XuvQ5ZSaNfBJefcbei$QPlNrgEe2olq7Zuqz15iY22itjuT5pashmoVKyImmIY=', 'chef_service', 4),
('2025-02-28 23:55:26.051812', 0, '', '', '', 0, 1, '2025-02-24 18:13:01.836767', 4, 'yanis', 'yanis.fritih@safex.dz', 'pbkdf2_sha256$260000$6vpaoDCjpuGhaWHbW9wRTp$OX2hJkxfpEv9h4vckmoEperkDjes0aGN5lvl1wRYXyg=', 'chef_service', 2),
('2025-04-08 21:05:17.584226', 0, '', '', '', 0, 1, '2025-02-24 18:20:51.872460', 5, 'maya', 'maya.fritih@safex.dz', 'pbkdf2_sha256$260000$TpNJhjg6VR8HvnPCXF16vc$BarYILofgtoLv1FwG2F6Dy8PBGTmacEkXo58OBxmT24=', 'employe_simple', 1),
('2025-03-02 14:11:52.348417', 0, '', '', '', 0, 1, '2025-03-01 23:22:29.247891', 6, 'mimi', 'mimi.mimi@safex.dz', 'pbkdf2_sha256$260000$f7SLb25P3og6onDZODNOuQ$NvQZPb5VXlU+jAV9Ok2OcL3ogf4a5uZQ/Kep6LYgO14=', 'employe_simple', 2),
('2025-03-01 23:27:33.106348', 0, '', '', '', 0, 1, '2025-03-01 23:26:04.317826', 7, 'farida', 'farida.chikh@safex.dz', 'pbkdf2_sha256$260000$2niwtyBbscjCEyEfa5qYyO$f1E05CSLjB6FQrraauINXk8gwOdF7CFTRWqrKAdDMXg=', 'chef_service', 1),
('2025-03-02 14:13:31.158014', 0, '', '', '', 0, 1, '2025-03-02 14:07:51.786671', 8, 'malik', 'malik.malik@safex.dz', 'pbkdf2_sha256$260000$P4B3UldbFv4oBhjTqkH0zP$VSI8rbSXVAWuO6GLD0l6Lcv5RGbobCet57Y0HuEfT1U=', 'chef_service', 3),
('2025-03-02 14:18:31.701991', 0, '', '', '', 0, 1, '2025-03-02 14:18:09.392531', 9, 'ramzi', 'ramzi.ramzi@safex.dz', 'pbkdf2_sha256$260000$s2w4ulv2mgwv1uiF2Nbxtc$I+aMoMeL6Lx24hCxuZUzgqOdMJLYf6lbxOI3TMiE1bI=', 'chef_service', 1),
('2025-03-10 11:54:48.171186', 0, '', '', '', 0, 1, '2025-03-06 03:34:08.366019', 10, 'MAYHEIL', 'mayheil@safex.dz', 'pbkdf2_sha256$260000$j0bP8uq3fzk7BsnKJdC7ef$uuqs8VoLxASFzyTdqYrCkkR6sMMgpr6hROv4INgMwvQ=', 'employe_simple', 1),
('2025-03-06 03:55:53.649142', 0, '', '', '', 0, 1, '2025-03-06 03:55:22.480942', 11, 'directeur', 'directeur@safex.dz', 'pbkdf2_sha256$260000$skbIAXmSohmFTh6J5yxwbQ$mpNYOYPRVxMqovujTYLTRhBFwpEhnhW/OXJGn64e8Yo=', 'directeur_general', 1),
('2025-04-08 21:11:17.353695', 0, '', '', '', 0, 1, '2025-04-08 21:04:03.019476', 13, 'kader', 'kader@safex.dz', 'pbkdf2_sha256$260000$TpNJhjg6VR8HvnPCXF16vc$BarYILofgtoLv1FwG2F6Dy8PBGTmacEkXo58OBxmT24=', 'chef_service', 8);

-- --------------------------------------------------------

--
-- Structure de la table `auth_app_userdepartmentrole`
--

CREATE TABLE `auth_app_userdepartmentrole` (
  `id` bigint(20) NOT NULL,
  `role` varchar(100) NOT NULL,
  `department_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `auth_app_userdepartmentrole`
--

INSERT INTO `auth_app_userdepartmentrole` (`id`, `role`, `department_id`, `user_id`) VALUES
(1, '7', 1, 2),
(2, '6', 2, 2),
(3, '7', 4, 3),
(4, '4', 1, 3),
(5, '2', 2, 4),
(6, '4', 1, 5),
(7, '4', 2, 6),
(8, '1', 1, 7),
(9, '5', 2, 7),
(10, '7', 4, 7),
(11, '5', 3, 8),
(12, '7', 1, 8),
(13, '7', 1, 9),
(14, '7', 2, 9),
(15, '1', 1, 10),
(16, '7', 1, 11),
(17, '7', 2, 11),
(18, '7', 3, 11),
(19, '7', 4, 11),
(20, '7', 5, 11),
(21, '7', 8, 13),
(22, '4', 1, 13),
(23, '1', 3, 13);

-- --------------------------------------------------------

--
-- Structure de la table `auth_app_user_groups`
--

CREATE TABLE `auth_app_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `auth_app_user_user_permissions`
--

CREATE TABLE `auth_app_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Structure de la table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add content type', 4, 'add_contenttype'),
(14, 'Can change content type', 4, 'change_contenttype'),
(15, 'Can delete content type', 4, 'delete_contenttype'),
(16, 'Can view content type', 4, 'view_contenttype'),
(17, 'Can add session', 5, 'add_session'),
(18, 'Can change session', 5, 'change_session'),
(19, 'Can delete session', 5, 'delete_session'),
(20, 'Can view session', 5, 'view_session'),
(21, 'Can add user', 6, 'add_user'),
(22, 'Can change user', 6, 'change_user'),
(23, 'Can delete user', 6, 'delete_user'),
(24, 'Can view user', 6, 'view_user'),
(25, 'Can add department', 7, 'add_department'),
(26, 'Can change department', 7, 'change_department'),
(27, 'Can delete department', 7, 'delete_department'),
(28, 'Can view department', 7, 'view_department'),
(29, 'Can add user department role', 8, 'add_userdepartmentrole'),
(30, 'Can change user department role', 8, 'change_userdepartmentrole'),
(31, 'Can delete user department role', 8, 'delete_userdepartmentrole'),
(32, 'Can view user department role', 8, 'view_userdepartmentrole'),
(33, 'Can add files', 9, 'add_files'),
(34, 'Can change files', 9, 'change_files'),
(35, 'Can delete files', 9, 'delete_files'),
(36, 'Can view files', 9, 'view_files');

-- --------------------------------------------------------

--
-- Structure de la table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2025-02-24 17:49:16.769112', '1', 'informatique', 1, '[{\"added\": {}}]', 7, 1),
(2, '2025-02-24 17:49:21.305253', '2', 'marketing', 1, '[{\"added\": {}}]', 7, 1),
(3, '2025-02-24 17:49:25.452563', '3', 'finance', 1, '[{\"added\": {}}]', 7, 1),
(4, '2025-02-24 17:49:29.722554', '4', 'RH', 1, '[{\"added\": {}}]', 7, 1),
(5, '2025-02-24 17:49:35.354151', '5', 'commerce', 1, '[{\"added\": {}}]', 7, 1),
(6, '2025-02-24 17:50:48.295067', '2', 'souheil', 1, '[{\"added\": {}}, {\"added\": {\"name\": \"user department role\", \"object\": \"souheil - informatique - select + upload + delete\"}}, {\"added\": {\"name\": \"user department role\", \"object\": \"souheil - marketing - upload + delete\"}}]', 6, 1),
(7, '2025-02-24 17:59:40.502346', '3', 'anais', 1, '[{\"added\": {}}, {\"added\": {\"name\": \"user department role\", \"object\": \"anais - RH - select + upload + delete\"}}, {\"added\": {\"name\": \"user department role\", \"object\": \"anais - informatique - select + upload\"}}]', 6, 1),
(8, '2025-02-24 18:13:02.599798', '4', 'yanis', 1, '[{\"added\": {}}, {\"added\": {\"name\": \"user department role\", \"object\": \"yanis - marketing - upload\"}}]', 6, 1),
(9, '2025-02-24 18:20:52.618088', '5', 'maya', 1, '[{\"added\": {}}, {\"added\": {\"name\": \"user department role\", \"object\": \"maya - informatique - select + upload\"}}]', 6, 1),
(10, '2025-03-01 23:22:30.010587', '6', 'mimi', 1, '[{\"added\": {}}, {\"added\": {\"name\": \"user department role\", \"object\": \"mimi - marketing - select + upload\"}}]', 6, 1),
(11, '2025-03-01 23:26:04.917210', '7', 'farida', 1, '[{\"added\": {}}, {\"added\": {\"name\": \"user department role\", \"object\": \"farida - informatique - select\"}}, {\"added\": {\"name\": \"user department role\", \"object\": \"farida - marketing - select + delete\"}}, {\"added\": {\"name\": \"user department role\", \"object\": \"farida - RH - select + upload + delete\"}}]', 6, 1),
(12, '2025-03-02 14:07:52.118068', '8', 'malik', 1, '[{\"added\": {}}, {\"added\": {\"name\": \"user department role\", \"object\": \"malik - finance - select + delete\"}}, {\"added\": {\"name\": \"user department role\", \"object\": \"malik - informatique - select + upload + delete\"}}]', 6, 1),
(13, '2025-03-02 14:18:09.718479', '9', 'ramzi', 1, '[{\"added\": {}}, {\"added\": {\"name\": \"user department role\", \"object\": \"ramzi - informatique - select + upload + delete\"}}, {\"added\": {\"name\": \"user department role\", \"object\": \"ramzi - marketing - select + upload + delete\"}}]', 6, 1),
(14, '2025-03-06 03:34:09.301564', '10', 'MAYHEIL', 1, '[{\"added\": {}}, {\"added\": {\"name\": \"user department role\", \"object\": \"MAYHEIL - informatique - select\"}}]', 6, 1),
(15, '2025-03-06 03:55:23.133404', '11', 'directeur', 1, '[{\"added\": {}}, {\"added\": {\"name\": \"user department role\", \"object\": \"directeur - informatique - select + upload + delete\"}}, {\"added\": {\"name\": \"user department role\", \"object\": \"directeur - marketing - select + upload + delete\"}}, {\"added\": {\"name\": \"user department role\", \"object\": \"directeur - finance - select + upload + delete\"}}, {\"added\": {\"name\": \"user department role\", \"object\": \"directeur - RH - select + upload + delete\"}}, {\"added\": {\"name\": \"user department role\", \"object\": \"directeur - commerce - select + upload + delete\"}}]', 6, 1),
(16, '2025-03-10 11:39:27.898683', '6', 'réseaux', 1, '[{\"added\": {}}]', 7, 1),
(17, '2025-03-10 11:47:34.336668', '12', 'essai', 1, '[{\"added\": {}}]', 6, 1),
(18, '2025-03-10 11:47:54.766361', '12', 'essai', 2, '[{\"changed\": {\"fields\": [\"Departement principal\"]}}]', 6, 1),
(19, '2025-03-10 11:51:20.751852', '12', 'essai', 2, '[{\"changed\": {\"fields\": [\"Active\"]}}]', 6, 1),
(20, '2025-03-10 11:53:50.788509', '12', 'essai', 3, '', 6, 1),
(21, '2025-04-08 20:58:36.870790', '7', 'securite', 1, '[{\"added\": {}}]', 7, 1),
(22, '2025-04-08 21:01:29.830609', '8', 'dit', 1, '[{\"added\": {}}]', 7, 1),
(23, '2025-04-08 21:04:03.890578', '13', 'kader', 1, '[{\"added\": {}}, {\"added\": {\"name\": \"user department role\", \"object\": \"kader - dit - select + upload + delete\"}}, {\"added\": {\"name\": \"user department role\", \"object\": \"kader - informatique - select + upload\"}}, {\"added\": {\"name\": \"user department role\", \"object\": \"kader - finance - select\"}}]', 6, 1);

-- --------------------------------------------------------

--
-- Structure de la table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(7, 'auth_app', 'department'),
(9, 'auth_app', 'files'),
(6, 'auth_app', 'user'),
(8, 'auth_app', 'userdepartmentrole'),
(4, 'contenttypes', 'contenttype'),
(5, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Structure de la table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2025-02-24 17:47:48.947237'),
(2, 'contenttypes', '0002_remove_content_type_name', '2025-02-24 17:47:49.102530'),
(3, 'auth', '0001_initial', '2025-02-24 17:47:49.683724'),
(4, 'auth', '0002_alter_permission_name_max_length', '2025-02-24 17:47:49.803268'),
(5, 'auth', '0003_alter_user_email_max_length', '2025-02-24 17:47:49.827735'),
(6, 'auth', '0004_alter_user_username_opts', '2025-02-24 17:47:49.865701'),
(7, 'auth', '0005_alter_user_last_login_null', '2025-02-24 17:47:49.907173'),
(8, 'auth', '0006_require_contenttypes_0002', '2025-02-24 17:47:49.919040'),
(9, 'auth', '0007_alter_validators_add_error_messages', '2025-02-24 17:47:49.957695'),
(10, 'auth', '0008_alter_user_username_max_length', '2025-02-24 17:47:49.992658'),
(11, 'auth', '0009_alter_user_last_name_max_length', '2025-02-24 17:47:50.019763'),
(12, 'auth', '0010_alter_group_name_max_length', '2025-02-24 17:47:50.045762'),
(13, 'auth', '0011_update_proxy_permissions', '2025-02-24 17:47:50.062696'),
(14, 'auth', '0012_alter_user_first_name_max_length', '2025-02-24 17:47:50.079122'),
(15, 'auth_app', '0001_initial', '2025-02-24 17:47:51.395355'),
(16, 'admin', '0001_initial', '2025-02-24 17:47:51.618196'),
(17, 'admin', '0002_logentry_remove_auto_add', '2025-02-24 17:47:51.645780'),
(18, 'admin', '0003_logentry_add_action_flag_choices', '2025-02-24 17:47:51.676711'),
(19, 'sessions', '0001_initial', '2025-02-24 17:47:51.755454');

-- --------------------------------------------------------

--
-- Structure de la table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('1kv2dlt0ueaf6p80yapygcqank3flelq', '.eJxVy8sOwiAQheF3mbVpKAMjuDTxOcgMDKHxkkbsyvjuVtOFbr9z_ickXh4tLV3vaSpwgBFh94vC-ay3z_I1nudhoz6crjxdjtvhr2rc25pYIss-10IUPKtDyjWilpUq7xWRhENRkuicIROimGqLyegdix0tvN52DTQ6:1u2GE1:66atel4kXQU9ARjpR1F0nV0HA3iN8LbLLxmNz8tv8_A', '2025-04-22 21:11:17.360706');

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `auth_app_department`
--
ALTER TABLE `auth_app_department`
  ADD PRIMARY KEY (`id_department`);

--
-- Index pour la table `auth_app_files`
--
ALTER TABLE `auth_app_files`
  ADD PRIMARY KEY (`id`),
  ADD KEY `auth_app_files_id_department_id_bbf1ac6a_fk_auth_app_` (`id_department_id`),
  ADD KEY `auth_app_files_id_user_id_27ba9707_fk_auth_app_user_id_user` (`id_user_id`);

--
-- Index pour la table `auth_app_user`
--
ALTER TABLE `auth_app_user`
  ADD PRIMARY KEY (`id_user`),
  ADD UNIQUE KEY `mail_user` (`mail_user`),
  ADD KEY `auth_app_user_departement_principa_8af88e28_fk_auth_app_` (`departement_principal_id`);

--
-- Index pour la table `auth_app_userdepartmentrole`
--
ALTER TABLE `auth_app_userdepartmentrole`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_app_userdepartmentrole_user_id_department_id_5a3200de_uniq` (`user_id`,`department_id`),
  ADD KEY `auth_app_userdepartm_department_id_ddd3a062_fk_auth_app_` (`department_id`);

--
-- Index pour la table `auth_app_user_groups`
--
ALTER TABLE `auth_app_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_app_user_groups_user_id_group_id_5f174ff0_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_app_user_groups_group_id_b4576925_fk_auth_group_id` (`group_id`);

--
-- Index pour la table `auth_app_user_user_permissions`
--
ALTER TABLE `auth_app_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_app_user_user_permi_user_id_permission_id_727a8e97_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_app_user_user_p_permission_id_cc1b2396_fk_auth_perm` (`permission_id`);

--
-- Index pour la table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Index pour la table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Index pour la table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Index pour la table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_app_user_id_user` (`user_id`);

--
-- Index pour la table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Index pour la table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `auth_app_department`
--
ALTER TABLE `auth_app_department`
  MODIFY `id_department` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT pour la table `auth_app_files`
--
ALTER TABLE `auth_app_files`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT pour la table `auth_app_user`
--
ALTER TABLE `auth_app_user`
  MODIFY `id_user` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT pour la table `auth_app_userdepartmentrole`
--
ALTER TABLE `auth_app_userdepartmentrole`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT pour la table `auth_app_user_groups`
--
ALTER TABLE `auth_app_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `auth_app_user_user_permissions`
--
ALTER TABLE `auth_app_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=37;

--
-- AUTO_INCREMENT pour la table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT pour la table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT pour la table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `auth_app_files`
--
ALTER TABLE `auth_app_files`
  ADD CONSTRAINT `auth_app_files_id_department_id_bbf1ac6a_fk_auth_app_` FOREIGN KEY (`id_department_id`) REFERENCES `auth_app_department` (`id_department`),
  ADD CONSTRAINT `auth_app_files_id_user_id_27ba9707_fk_auth_app_user_id_user` FOREIGN KEY (`id_user_id`) REFERENCES `auth_app_user` (`id_user`);

--
-- Contraintes pour la table `auth_app_user`
--
ALTER TABLE `auth_app_user`
  ADD CONSTRAINT `auth_app_user_departement_principa_8af88e28_fk_auth_app_` FOREIGN KEY (`departement_principal_id`) REFERENCES `auth_app_department` (`id_department`);

--
-- Contraintes pour la table `auth_app_userdepartmentrole`
--
ALTER TABLE `auth_app_userdepartmentrole`
  ADD CONSTRAINT `auth_app_userdepartm_department_id_ddd3a062_fk_auth_app_` FOREIGN KEY (`department_id`) REFERENCES `auth_app_department` (`id_department`),
  ADD CONSTRAINT `auth_app_userdepartm_user_id_980eee0c_fk_auth_app_` FOREIGN KEY (`user_id`) REFERENCES `auth_app_user` (`id_user`);

--
-- Contraintes pour la table `auth_app_user_groups`
--
ALTER TABLE `auth_app_user_groups`
  ADD CONSTRAINT `auth_app_user_groups_group_id_b4576925_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_app_user_groups_user_id_2b6e45f5_fk_auth_app_user_id_user` FOREIGN KEY (`user_id`) REFERENCES `auth_app_user` (`id_user`);

--
-- Contraintes pour la table `auth_app_user_user_permissions`
--
ALTER TABLE `auth_app_user_user_permissions`
  ADD CONSTRAINT `auth_app_user_user_p_permission_id_cc1b2396_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_app_user_user_p_user_id_b7c37328_fk_auth_app_` FOREIGN KEY (`user_id`) REFERENCES `auth_app_user` (`id_user`);

--
-- Contraintes pour la table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Contraintes pour la table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Contraintes pour la table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_app_user_id_user` FOREIGN KEY (`user_id`) REFERENCES `auth_app_user` (`id_user`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
