-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Tempo de geração: 08-Abr-2021 às 21:19
-- Versão do servidor: 5.7.31
-- versão do PHP: 7.3.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `movies_bala`
--
CREATE DATABASE IF NOT EXISTS `movies_bala` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `movies_bala`;

-- --------------------------------------------------------

--
-- Estrutura da tabela `movies`
--

DROP TABLE IF EXISTS `movies`;
CREATE TABLE IF NOT EXISTS `movies` (
  `movie_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `title` varchar(255) CHARACTER SET utf8 COLLATE utf8_swedish_ci NOT NULL,
  PRIMARY KEY (`movie_id`),
  KEY `flag` (`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=59 DEFAULT CHARSET=utf8;

--
-- Extraindo dados da tabela `movies`
--

INSERT INTO `movies` (`movie_id`, `user_id`, `title`) VALUES
(58, 3, 'O poderoso chefão'),
(57, 5, 'Ilha do Medo'),
(56, 5, 'Whiplash'),
(51, 3, 'O Gângster'),
(49, 3, 'Os Oito Odiados'),
(53, 5, 'Get Out'),
(37, 1, 'Os homens são de Marte'),
(38, 1, 'Blade Runner, 1982'),
(39, 1, 'Inception'),
(40, 1, 'Her'),
(41, 2, 'Bad boys for life'),
(42, 2, 'The dirt'),
(43, 4, 'Invasão zumbi'),
(44, 4, 'Tropa de Elite'),
(45, 4, 'Ó Paí, Ó'),
(46, 5, 'Os 12 macacos'),
(47, 5, 'Shaun Carneiro 2019'),
(48, 5, 'O diabo de cada dia');

-- --------------------------------------------------------

--
-- Estrutura da tabela `users`
--

DROP TABLE IF EXISTS `users`;
CREATE TABLE IF NOT EXISTS `users` (
  `user_id` mediumint(9) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) CHARACTER SET utf8 COLLATE utf8_swedish_ci NOT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `users`
--

INSERT INTO `users` (`user_id`, `name`) VALUES
(1, 'Apu'),
(2, 'Pikeno'),
(3, 'Zero'),
(4, 'John'),
(5, 'Rei'),
(6, 'Curu'),
(7, 'Beto'),
(8, 'Juuj');

-- --------------------------------------------------------

--
-- Estrutura da tabela `watched`
--

DROP TABLE IF EXISTS `watched`;
CREATE TABLE IF NOT EXISTS `watched` (
  `movie_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `title` varchar(255) CHARACTER SET utf8 COLLATE utf8_swedish_ci NOT NULL,
  `rotten` float DEFAULT NULL,
  `Apu` float DEFAULT NULL,
  `Pikeno` float DEFAULT NULL,
  `Zero` float DEFAULT NULL,
  `John` float DEFAULT NULL,
  `Rei` float DEFAULT NULL,
  `Curu` float DEFAULT NULL,
  `Beto` float DEFAULT NULL,
  `Juuj` float DEFAULT NULL,
  PRIMARY KEY (`movie_id`),
  KEY `flag` (`user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- Extraindo dados da tabela `watched`
--

INSERT INTO `watched` (`movie_id`, `user_id`, `title`, `rotten`, `Apu`, `Pikeno`, `Zero`, `John`, `Rei`, `Curu`, `Beto`, `Juuj`) VALUES
(1, 2, 'Corrente do Mal', 67, 3.5, 3.5, 3, NULL, NULL, NULL, NULL, NULL),
(2, 1, 'A perseguição', 57, 3, 2.5, 3, NULL, NULL, NULL, NULL, NULL),
(3, 3, '7500', 80, 4, 4, 4, NULL, NULL, NULL, NULL, NULL),
(4, 6, 'Colheita Maldita', 20, 1, 0, 0.5, NULL, NULL, 2.5, NULL, NULL),
(5, 1, 'O Regresso', 95, 5, 5, 5, 4, NULL, NULL, NULL, NULL),
(6, 2, 'Django Livre', 92, 4.5, 5, 4, 5, NULL, NULL, NULL, NULL),
(7, 3, 'Inferno na Fronteira', 58, 3, 2.5, 2.5, NULL, NULL, 3.5, NULL, NULL),
(8, 1, 'Rec', 78, 4, 4.5, 4, 3, NULL, NULL, NULL, NULL),
(9, 4, 'Scooby-Doo', 62, 3, 3, 2.5, 2, NULL, 5, NULL, NULL),
(10, 3, 'Undisputed III: Redemption', 77, 3.5, 4, 4, NULL, NULL, NULL, NULL, NULL),
(11, 2, 'Perdido em Marte', 93, 5, 5, 4, NULL, NULL, NULL, NULL, NULL),
(12, 1, 'Rec 2', 63, 3.5, 3, 3, NULL, NULL, NULL, NULL, NULL),
(13, 3, 'Dreamkatcher', 60, 3, 3, 3, NULL, NULL, NULL, NULL, NULL),
(14, 2, 'Arraste-me para o Inferno', 83, 4, 4.5, 4, NULL, NULL, NULL, NULL, NULL),
(15, 1, 'Psicopata Americano', 77, 4, 4, 3.5, NULL, NULL, NULL, NULL, NULL),
(16, 3, 'Destruição final', 78, 3.5, 4.5, 4, NULL, NULL, NULL, 3.5, NULL),
(17, 1, 'A possessão de Deborah Logan', 87, 4, 4.5, 4.5, NULL, NULL, NULL, NULL, NULL),
(18, 4, 'Constantine', 70, 3.5, 3.5, 3.5, NULL, NULL, NULL, NULL, NULL),
(19, 3, 'Onde esta segunda', 65, 3, 3.5, 3.5, NULL, 3, NULL, NULL, NULL),
(20, 2, 'Arrival', 77, 4, 4, 3.5, NULL, NULL, NULL, NULL, NULL),
(21, 1, 'Assim na terra como no Inferno', 80, 4, 4, 4, NULL, NULL, NULL, NULL, NULL),
(22, 5, 'Ethel e Ernest', 68, 3, 4, 3, NULL, 3.5, NULL, NULL, 3.5),
(23, 2, 'Blade Runner 2049', 82, 4.5, 4, 4, NULL, 4, NULL, NULL, NULL),
(24, 1, 'Show de Truman', 82, 4, 4, 4, NULL, 4.5, NULL, NULL, NULL),
(25, 2, 'Lights Out', 80, 4, 4, 4, NULL, NULL, NULL, NULL, NULL),
(26, 4, 'Dupla Implacável', 66, 3, 3, 3.5, 4, 3, NULL, NULL, NULL),
(27, 2, 'Trovão tropical', 70, 3, 3.5, 3.5, NULL, 4, NULL, NULL, NULL),
(28, 3, 'Efeito Borboleta', 82, 4, 4.5, 3.5, NULL, 4.5, NULL, NULL, NULL),
(29, 2, 'Mad Max: Estrada da Fúria', 72, 3.5, 4.5, 3, NULL, 3.5, NULL, NULL, NULL),
(30, 5, 'Jóias Brutas', 72, 4, 3.5, 3.5, NULL, 3.5, NULL, NULL, NULL),
(31, 3, 'A hora da sua morte', 67, 3, 3.5, 3.5, NULL, NULL, NULL, NULL, NULL),
(32, 1, 'Baby Driver', 95, 4.5, 5, 4, 5, 5, NULL, 5, NULL),
(33, 5, 'Brilho Eterno de uma Mente sem Lembranças', 78, 4, 3.5, 4, 3.5, 4.5, NULL, NULL, NULL),
(34, 3, 'Fight Club', 82, 4, 4.5, 4, 4.5, 3.5, NULL, NULL, NULL),
(35, 4, 'A vida de Brian', 48, 2.5, 2.5, 2.5, 2, NULL, NULL, NULL, NULL),
(36, 1, 'Cidade de Deus', 100, 5, 5, 5, NULL, 5, NULL, NULL, NULL);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
