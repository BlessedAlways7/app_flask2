-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 13, 2024 at 03:13 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `agence`
--

-- --------------------------------------------------------

--
-- Table structure for table `departement`
--

CREATE TABLE `departement` (
  `nom` varchar(25) CHARACTER SET armscii8 COLLATE armscii8_general_ci NOT NULL,
  `emplacement` varchar(50) CHARACTER SET armscii8 COLLATE armscii8_general_ci NOT NULL,
  `direction` varchar(20) CHARACTER SET armscii8 COLLATE armscii8_general_ci NOT NULL,
  `id` int(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `departement`
--

INSERT INTO `departement` (`nom`, `emplacement`, `direction`, `id`) VALUES
('Sandler', '3ieme etage', 'HR', 1),
('Marquis', 'S1', 'Laboratoire', 5),
('Valentino', '1ier etage', 'Urgence', 8);

-- --------------------------------------------------------

--
-- Table structure for table `employe`
--

CREATE TABLE `employe` (
  `nom` varchar(25) CHARACTER SET armscii8 COLLATE armscii8_general_ci NOT NULL,
  `prenom` varchar(25) CHARACTER SET armscii8 COLLATE armscii8_general_ci NOT NULL,
  `matricule` varchar(25) CHARACTER SET armscii8 COLLATE armscii8_general_ci NOT NULL,
  `fonction` varchar(50) CHARACTER SET armscii8 COLLATE armscii8_general_ci NOT NULL,
  `departement` varchar(50) CHARACTER SET armscii8 COLLATE armscii8_general_ci NOT NULL,
  `id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `employe`
--

INSERT INTO `employe` (`nom`, `prenom`, `matricule`, `fonction`, `departement`, `id`) VALUES
('Bonnet', 'Sam', 'jfcf5198vc', 'Organisateur', 'IT', 1),
('Labrie', 'Stephane', 'fkt002547', 'analyste', 'IT', 3),
('Diallo', 'Amadou', 'AM24242', 'Developpeur web', 'IT', 7),
('Lapierre', 'Jean', 'sccsc77897', 'Technicien', 'Imagerie', 10),
('Lafrance', 'Jeanne', 'hxuswhxju87988', 'Dieticienne', 'Pharmacie', 12),
('Lambert', 'Jean-Francois', 'sfcfedfc768', 'developpement web', 'IT', 13),
('France', 'Zoe', 'dvcd6776', 'Web', 'IT', 14),
('Marquis', 'France', 'cecws4654', 'Secretaire', 'HR', 15);

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(20) NOT NULL,
  `nom_complet` varchar(45) CHARACTER SET armscii8 COLLATE armscii8_general_ci DEFAULT NULL,
  `username` varchar(45) CHARACTER SET armscii8 COLLATE armscii8_general_ci DEFAULT NULL,
  `password` varchar(150) CHARACTER SET armscii8 COLLATE armscii8_general_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `nom_complet`, `username`, `password`) VALUES
(1, 'Jean Marchand', 'marchandJean', 'Marchan$#'),
(2, 'Berube Samuel', 'Sam4Beru', '$2b$12$zM0BYSpJorI4CRofz9FsoumClYwBPi2Rbs5ealEZNLcw0wca8J4UW'),
(4, 'Miguel Lecompte', 'MLcompte', '$2b$12$i2DIOFkxQwdVNTXsO4Kki.Y00PTvrTyFlNBu0Q3roe6g48vyF9f/S'),
(5, 'Diallo Abdou', 'Diallo123', '$2b$12$OAriZ3E5cu.2xg7qdNKE3O1N/9h7QgwXzDG7kVwKB9Z/Wcz.ZgrnS');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `departement`
--
ALTER TABLE `departement`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `employe`
--
ALTER TABLE `employe`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `matricule` (`matricule`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `departement`
--
ALTER TABLE `departement`
  MODIFY `id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `employe`
--
ALTER TABLE `employe`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
