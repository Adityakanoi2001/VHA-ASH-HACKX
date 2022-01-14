-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: May 27, 2021 at 01:56 PM
-- Server version: 8.0.22
-- PHP Version: 8.0.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `medico`
--

-- --------------------------------------------------------

--
-- Table structure for table `consult`
--

CREATE TABLE `consult` (
  `doctor_id` varchar(40) COLLATE utf8mb4_unicode_ci NOT NULL,
  `patient_mail` varchar(45) COLLATE utf8mb4_unicode_ci NOT NULL,
  `status` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT 'request not accepted',
  `timing` varchar(40) COLLATE utf8mb4_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `consult`
--

INSERT INTO `consult` (`doctor_id`, `patient_mail`, `status`, `timing`) VALUES
('101', 'a@gmail.com', 'Accepted', '2021-05-2915:55'),
('101', 'dhanush@gmail.com', 'Accepted', '2021-06-04 14:43'),
('101', 'barath@gmail.com', 'Accepted', '2021-06-04 15:50');

-- --------------------------------------------------------

--
-- Table structure for table `doctor`
--

CREATE TABLE `doctor` (
  `id` varchar(40) COLLATE utf8mb4_unicode_ci NOT NULL,
  `name` varchar(30) COLLATE utf8mb4_unicode_ci NOT NULL,
  `dept` varchar(40) COLLATE utf8mb4_unicode_ci NOT NULL,
  `image` varchar(30) COLLATE utf8mb4_unicode_ci NOT NULL,
  `timing` varchar(60) COLLATE utf8mb4_unicode_ci NOT NULL,
  `mail` varchar(40) COLLATE utf8mb4_unicode_ci NOT NULL,
  `pwd` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `link` varchar(40) COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `doctor`
--

INSERT INTO `doctor` (`id`, `name`, `dept`, `image`, `timing`, `mail`, `pwd`, `link`) VALUES
('101', 'Dr Charakara varthy', 'General', 'doctor1', 'Monday to Friday Timing 2:00 - 6.00 pm ', 'charaka@gmail.com', 'chakra12', 'meet.google.com/njs-xhvy-yuw'),
('102', 'Dr Ramesh', 'Cardiologist', 'doctor2', 'Monday to Friday Timing 2:00 - 6.00 pm', 'ramesh@gmail.com', 'ramesh12', 'meet.google.com/aip-zvup-rok'),
('103', 'Dr Tarun', 'Neurologist', 'doctor3', 'Monday to Friday Timing 2:00 - 6.00 pm', 'tarun@gmail.com', 'tarun12', 'meet.google.com/aip-zvup-rok'),
('104', 'Dr Hemant Kumar', 'ENT', 'doctor4', 'Monday to Friday Timing 2:00 - 6.00 pm', 'hemant@gmail.com', 'hemanth12', 'meet.google.com/sov-ritm-ehp'),
('105', 'Dr Krishnan', 'Dermitologist', 'doctor5', 'Monday to Friday Timing 2:00 - 6.00 pm', 'krishna@gmail.com', 'krishna12', 'meet.google.com/sov-ritm-ehp');

-- --------------------------------------------------------

--
-- Table structure for table `patient`
--

CREATE TABLE `patient` (
  `name` varchar(40) COLLATE utf8mb4_unicode_ci NOT NULL,
  `mail` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `pwd` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `age` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT 'Not yet set',
  `BMI` varchar(30) COLLATE utf8mb4_unicode_ci DEFAULT 'Not yet set',
  `location` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT 'Not yet set',
  `gender` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT 'Not yet set'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `patient`
--

INSERT INTO `patient` (`name`, `mail`, `pwd`, `age`, `BMI`, `location`, `gender`) VALUES
('Vikram c', 'a@gmail.com', '123', '23', '100', 'Theni', 'Male'),
('BARATH', 'barath@gmail.com', '123', '23', '100', 'coimbatore', 'Male'),
('Dhanush', 'dhanush@gmail.com', 'dhanush', 'Not yet set', 'Not yet set', 'Not yet set', 'Not yet set');

-- --------------------------------------------------------

--
-- Table structure for table `queries`
--

CREATE TABLE `queries` (
  `sno` int NOT NULL,
  `question` varchar(500) COLLATE utf8mb4_unicode_ci NOT NULL,
  `answer` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT 'Nil',
  `status` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT 'Nil'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `queries`
--

INSERT INTO `queries` (`sno`, `question`, `answer`, `status`) VALUES
(4, 'How to do firstaid for Snake bit', 'Wash the wound with water and tie with cloth', 'answered'),
(5, 'what to do as precaution when black fungus detected', 'Be clam and take anti fugus medicine and get first aid', 'answered'),
(6, 'how to do first aid for heat burns', 'Nil', 'Nil');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `doctor`
--
ALTER TABLE `doctor`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `patient`
--
ALTER TABLE `patient`
  ADD PRIMARY KEY (`mail`);

--
-- Indexes for table `queries`
--
ALTER TABLE `queries`
  ADD PRIMARY KEY (`sno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `queries`
--
ALTER TABLE `queries`
  MODIFY `sno` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
