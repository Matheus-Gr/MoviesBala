-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Tempo de geração: 09-Abr-2021 às 13:05
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
-- Banco de dados: `sql10404400`
--

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
) ENGINE=MyISAM AUTO_INCREMENT=55 DEFAULT CHARSET=utf8;

--
-- Extraindo dados da tabela `movies`
--

INSERT INTO `movies` (`movie_id`, `user_id`, `title`) VALUES
(54, 5, 'O diabo de cada dia'),
(53, 5, 'Shaun Carneiro 2019'),
(52, 5, 'Os 12 macacos'),
(51, 4, 'Ó Paí, Ó'),
(50, 4, 'Tropa de Elite'),
(49, 4, 'Invasão zumbi'),
(48, 2, 'The dirt'),
(47, 2, 'Bad boys for life'),
(46, 1, 'Her'),
(45, 1, 'Inception'),
(44, 1, 'Blade Runner, 1982'),
(43, 1, 'Os homens são de Marte'),
(42, 5, 'Get Out'),
(41, 3, 'Os Oito Odiados'),
(40, 3, 'O Gângster'),
(39, 5, 'Whiplash'),
(38, 5, 'Ilha do Medo'),
(37, 3, 'O poderoso chefão');

-- --------------------------------------------------------

--
-- Estrutura da tabela `posters`
--

DROP TABLE IF EXISTS `posters`;
CREATE TABLE IF NOT EXISTS `posters` (
  `movie_id` int(11) NOT NULL,
  `url` varchar(1000) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `posters`
--

INSERT INTO `posters` (`movie_id`, `url`) VALUES
(1, 'https://m.media-amazon.com/images/M/MV5BMmU0MjBlYzYtZWY0MC00MjliLWI3ZmUtMzhlZDVjMWVmYWY4XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg'),
(2, 'https://m.media-amazon.com/images/M/MV5BNDY4MTQwMzc1MV5BMl5BanBnXkFtZTcwNzcwNTM5Ng@@._V1_UX182_CR0,0,182,268_AL_.jpg'),
(3, 'https://m.media-amazon.com/images/M/MV5BYjE4YzU1YWMtYzE3Zi00ZjViLWJjMmEtOTA1NWVkNGFlM2U5XkEyXkFqcGdeQXVyODE0OTU5Nzg@._V1_UX182_CR0,0,182,268_AL_.jpg'),
(4, 'https://m.media-amazon.com/images/M/MV5BMDg3OTc2OTQtZDA0My00YTJiLTg3ZTYtOGYwZWM1NWVhZDdiXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg'),
(5, 'https://m.media-amazon.com/images/M/MV5BMDE5OWMzM2QtOTU2ZS00NzAyLWI2MDEtOTRlYjIxZGM0OWRjXkEyXkFqcGdeQXVyODE5NzE3OTE@._V1_UX182_CR0,0,182,268_AL_.jpg'),
(6, 'https://m.media-amazon.com/images/M/MV5BMjIyNTQ5NjQ1OV5BMl5BanBnXkFtZTcwODg1MDU4OA@@._V1_UX182_CR0,0,182,268_AL_.jpg'),
(7, 'https://m.media-amazon.com/images/M/MV5BMzdiMDI0NDItMzdjOC00MzQwLWEwZGUtN2JjZDBkYmU3YjNhXkEyXkFqcGdeQXVyNjA3MzE2ODE@._V1_UX182_CR0,0,182,268_AL_.jpg'),
(8, 'https://m.media-amazon.com/images/M/MV5BZTJmNTZlZWUtZTQ2Yi00YTFjLWFiNzctYzFlNmZmZGMzYTlmXkEyXkFqcGdeQXVyMjQ2MTk1OTE@._V1_UY268_CR4,0,182,268_AL_.jpg'),
(9, 'https://m.media-amazon.com/images/M/MV5BMTg4MzMzMTY0OF5BMl5BanBnXkFtZTYwNzM3MTg2._V1_UX182_CR0,0,182,268_AL_.jpg'),
(10, 'https://m.media-amazon.com/images/M/MV5BMTc0YzA4YjQtZGZkMi00ZmRjLWFmM2ItMDcxZTYzZGU3ZTI1XkEyXkFqcGdeQXVyNDQ2MTMzODA@._V1_UX182_CR0,0,182,268_AL_.jpg'),
(11, 'https://m.media-amazon.com/images/M/MV5BMTc2MTQ3MDA1Nl5BMl5BanBnXkFtZTgwODA3OTI4NjE@._V1_UX182_CR0,0,182,268_AL_.jpg'),
(12, 'https://m.media-amazon.com/images/M/MV5BMTI4MjQ1MDE1MV5BMl5BanBnXkFtZTcwNzIxMDk0Mw@@._V1_UY268_CR0,0,182,268_AL_.jpg'),
(13, 'https://m.media-amazon.com/images/M/MV5BYTU1YWY5MDItYmJiNC00NzdkLTlmZjgtMjBlYjI2NGIzYmI0XkEyXkFqcGdeQXVyMDA4NzMyOA@@._V1_UY268_CR2,0,182,268_AL_.jpg'),
(14, 'https://m.media-amazon.com/images/M/MV5BMTQwNTMyNjc5Ml5BMl5BanBnXkFtZTcwOTI2MTQ0Mg@@._V1_UX182_CR0,0,182,268_AL_.jpg'),
(15, 'https://m.media-amazon.com/images/M/MV5BZTM2ZGJmNjQtN2UyOS00NjcxLWFjMDktMDE2NzMyNTZlZTBiXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_UX182_CR0,0,182,268_AL_.jpg'),
(16, 'https://m.media-amazon.com/images/M/MV5BMzcyMzU4MDUtM2JhOC00ZDg2LTg5MGMtZjc2OGMyMjhlMGE2XkEyXkFqcGdeQXVyMTkxNjUyNQ@@._V1_UX182_CR0,0,182,268_AL_.jpg'),
(17, 'https://m.media-amazon.com/images/M/MV5BZWQ3YmU4ZjYtZGE2Ni00NjhiLTk2NTMtYmVmYmNkNWViYzUxXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg'),
(18, 'https://m.media-amazon.com/images/M/MV5BODRiNmFhY2EtMGY2OC00YjI2LWIyYjQtYzFiM2ZhNjdhYzE4XkEyXkFqcGdeQXVyNDY5MTUyNjU@._V1_UX182_CR0,0,182,268_AL_.jpg'),
(19, 'https://m.media-amazon.com/images/M/MV5BMjE4MDQxMDg3MF5BMl5BanBnXkFtZTgwNjQ0MTcwMzI@._V1_UX182_CR0,0,182,268_AL_.jpg'),
(20, 'https://m.media-amazon.com/images/M/MV5BMTExMzU0ODcxNDheQTJeQWpwZ15BbWU4MDE1OTI4MzAy._V1_UX182_CR0,0,182,268_AL_.jpg'),
(21, 'https://m.media-amazon.com/images/M/MV5BMTQzNzg0NDI2MF5BMl5BanBnXkFtZTgwMzgxNzY2MTE@._V1_UX182_CR0,0,182,268_AL_.jpg'),
(22, 'https://m.media-amazon.com/images/M/MV5BMTEzOTg2NWQtYjZmZC00NWQ5LTk0ZTQtMDFlNWNhNGU3N2U3XkEyXkFqcGdeQXVyMTMxMTY0OTQ@._V1_UY268_CR4,0,182,268_AL_.jpg'),
(23, 'https://m.media-amazon.com/images/M/MV5BNzA1Njg4NzYxOV5BMl5BanBnXkFtZTgwODk5NjU3MzI@._V1_UX182_CR0,0,182,268_AL_.jpg'),
(24, 'https://m.media-amazon.com/images/M/MV5BMDIzODcyY2EtMmY2MC00ZWVlLTgwMzAtMjQwOWUyNmJjNTYyXkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_UX182_CR0,0,182,268_AL_.jpg'),
(25, 'https://m.media-amazon.com/images/M/MV5BMTg1OTkxNDgyMV5BMl5BanBnXkFtZTgwMjEzNTc0ODE@._V1_UX182_CR0,0,182,268_AL_.jpg'),
(26, 'https://m.media-amazon.com/images/M/MV5BODAwMDFjNjktMWY2Mi00MmVhLWI0MjYtNzg4OTI0NzA5YzBjXkEyXkFqcGdeQXVyNTIzOTk5ODM@._V1_UX182_CR0,0,182,268_AL_.jpg'),
(27, 'https://m.media-amazon.com/images/M/MV5BNDE5NjQzMDkzOF5BMl5BanBnXkFtZTcwODI3ODI3MQ@@._V1_UY268_CR4,0,182,268_AL_.jpg'),
(28, 'https://m.media-amazon.com/images/M/MV5BODNiZmY2MWUtMjFhMy00ZmM2LTg2MjYtNWY1OTY5NGU2MjdjL2ltYWdlXkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_UY268_CR1,0,182,268_AL_.jpg'),
(29, 'https://m.media-amazon.com/images/M/MV5BN2EwM2I5OWMtMGQyMi00Zjg1LWJkNTctZTdjYTA4OGUwZjMyXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_UX182_CR0,0,182,268_AL_.jpg'),
(30, 'https://m.media-amazon.com/images/M/MV5BZDhkMjUyYjItYWVkYi00YTM5LWE4MGEtY2FlMjA3OThlYmZhXkEyXkFqcGdeQXVyODk4OTc3MTY@._V1_UX182_CR0,0,182,268_AL_.jpg'),
(31, 'https://m.media-amazon.com/images/M/MV5BODY3OGEyMTgtYTZjZi00Y2YzLWFjY2UtMjEwYWE1MjRkOTc4XkEyXkFqcGdeQXVyODQxMTI4MjM@._V1_UX182_CR0,0,182,268_AL_.jpg'),
(32, 'https://m.media-amazon.com/images/M/MV5BMjM3MjQ1MzkxNl5BMl5BanBnXkFtZTgwODk1ODgyMjI@._V1_UX182_CR0,0,182,268_AL_.jpg'),
(33, 'https://m.media-amazon.com/images/M/MV5BMTY4NzcwODg3Nl5BMl5BanBnXkFtZTcwNTEwOTMyMw@@._V1_UX182_CR0,0,182,268_AL_.jpg'),
(34, 'https://m.media-amazon.com/images/M/MV5BMmEzNTkxYjQtZTc0MC00YTVjLTg5ZTEtZWMwOWVlYzY0NWIwXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_UX182_CR0,0,182,268_AL_.jpg'),
(35, 'https://m.media-amazon.com/images/M/MV5BMzAwNjU1OTktYjY3Mi00NDY5LWFlZWUtZjhjNGE0OTkwZDkwXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg'),
(36, 'https://m.media-amazon.com/images/M/MV5BOTMwYjc5ZmItYTFjZC00ZGQ3LTlkNTMtMjZiNTZlMWQzNzI5XkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_UX182_CR0,0,182,268_AL_.jpg'),
(37, 'https://m.media-amazon.com/images/M/MV5BM2MyNjYxNmUtYTAwNi00MTYxLWJmNWYtYzZlODY3ZTk3OTFlXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_UY268_CR3,0,182,268_AL_.jpg'),
(38, 'https://m.media-amazon.com/images/M/MV5BYzhiNDkyNzktNTZmYS00ZTBkLTk2MDAtM2U0YjU1MzgxZjgzXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_UX182_CR0,0,182,268_AL_.jpg'),
(39, 'https://m.media-amazon.com/images/M/MV5BOTA5NDZlZGUtMjAxOS00YTRkLTkwYmMtYWQ0NWEwZDZiNjEzXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_UX182_CR0,0,182,268_AL_.jpg'),
(40, 'https://m.media-amazon.com/images/M/MV5BMjFmZGI2YTEtYmJhMS00YTE5LWJjNjAtNDI5OGY5ZDhmNTRlXkEyXkFqcGdeQXVyODAwMTU1MTE@._V1_UX182_CR0,0,182,268_AL_.jpg'),
(41, 'https://m.media-amazon.com/images/M/MV5BMjA1MTc1NTg5NV5BMl5BanBnXkFtZTgwOTM2MDEzNzE@._V1_UX182_CR0,0,182,268_AL_.jpg'),
(42, 'https://m.media-amazon.com/images/M/MV5BMjUxMDQwNjcyNl5BMl5BanBnXkFtZTgwNzcwMzc0MTI@._V1_UX182_CR0,0,182,268_AL_.jpg'),
(43, 'https://m.media-amazon.com/images/M/MV5BMTg5NDM2ODUtZWVlOC00YTdmLWI0NGYtZjFhNmJjZTEyYTdkXkEyXkFqcGdeQXVyMTkzODUwNzk@._V1_UX182_CR0,0,182,268_AL_.jpg'),
(44, 'https://m.media-amazon.com/images/M/MV5BNzQzMzJhZTEtOWM4NS00MTdhLTg0YjgtMjM4MDRkZjUwZDBlXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_UX182_CR0,0,182,268_AL_.jpg'),
(45, 'https://m.media-amazon.com/images/M/MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@._V1_UX182_CR0,0,182,268_AL_.jpg'),
(46, 'https://m.media-amazon.com/images/M/MV5BMjA1Nzk0OTM2OF5BMl5BanBnXkFtZTgwNjU2NjEwMDE@._V1_UX182_CR0,0,182,268_AL_.jpg'),
(47, 'https://m.media-amazon.com/images/M/MV5BMWU0MGYwZWQtMzcwYS00NWVhLTlkZTAtYWVjOTYwZTBhZTBiXkEyXkFqcGdeQXVyMTkxNjUyNQ@@._V1_UX182_CR0,0,182,268_AL_.jpg'),
(48, 'https://m.media-amazon.com/images/M/MV5BODhiMzkwYTctYzgwOC00MDM2LWExYjQtMzY4MDljZjQ3M2RmXkEyXkFqcGdeQXVyNDg4NjY5OTQ@._V1_UX182_CR0,0,182,268_AL_.jpg'),
(49, 'https://m.media-amazon.com/images/M/MV5BMTkwOTQ4OTg0OV5BMl5BanBnXkFtZTgwMzQyOTM0OTE@._V1_UX182_CR0,0,182,268_AL_.jpg'),
(50, 'https://m.media-amazon.com/images/M/MV5BYmI1ODU5ZjMtNWUyNC00YzllLThjNzktODE1M2E4OTVmY2E5XkEyXkFqcGdeQXVyMTExNzQzMDE0._V1_UY268_CR3,0,182,268_AL_.jpg'),
(51, 'https://m.media-amazon.com/images/M/MV5BY2RkZWVmOGUtMmNiNy00NWRiLWExZjktMDM0MTdmZTlmNWUyXkEyXkFqcGdeQXVyMTY2MzYyNzA@._V1_UY268_CR0,0,182,268_AL_.jpg'),
(52, 'https://m.media-amazon.com/images/M/MV5BN2Y2OWU4MWMtNmIyMy00YzMyLWI0Y2ItMTcyZDc3MTdmZDU4XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg'),
(53, 'https://m.media-amazon.com/images/M/MV5BNTdjZjBkMDMtODBlNi00N2E0LWE1OGItOTgxODNmMDkzNGJmXkEyXkFqcGdeQXVyNjg2NjQwMDQ@._V1_UX182_CR0,0,182,268_AL_.jpg'),
(54, 'https://m.media-amazon.com/images/M/MV5BZmE1NmVmN2EtMjZmZC00YzAyLWE4MWEtYjY5YmExMjUxODU1XkEyXkFqcGdeQXVyMTkxNjUyNQ@@._V1_UX182_CR0,0,182,268_AL_.jpg');

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
