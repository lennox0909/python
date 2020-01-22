-- phpMyAdmin SQL Dump
-- version 4.9.0.1
-- https://www.phpmyadmin.net/
--
-- 主機： localhost
-- 產生時間： 2019 年 08 月 21 日 12:13
-- 伺服器版本： 10.4.6-MariaDB
-- PHP 版本： 7.3.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 資料庫： `0821db`
--

-- --------------------------------------------------------

--
-- 資料表結構 `member`
--

CREATE TABLE `member` (
  `id` int(11) NOT NULL,
  `name` varchar(200) NOT NULL,
  `birthday` date NOT NULL,
  `address` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 傾印資料表的資料 `member`
--

INSERT INTO `member` (`id`, `name`, `birthday`, `address`) VALUES
(11, 'Leno', '1990-01-01', 'Taipei City'),
(12, 'Apple', '2019-05-15', 'New Taipei City'),
(13, 'Banana', '2019-03-20', 'CA, USA'),
(14, 'Guava', '2000-02-21', 'IL, USA'),
(15, 'Orange', '2009-08-30', 'NY, USA'),
(16, 'Sakamoto', '1980-01-29', 'Tokyo'),
(17, 'Erica', '1993-03-30', 'Jakarta'),
(20, 'Alice', '2019-05-06', 'London'),
(21, 'Brian', '2001-09-30', 'NY, USA');

-- --------------------------------------------------------

--
-- 資料表結構 `telephone`
--

CREATE TABLE `telephone` (
  `id` int(11) NOT NULL,
  `tel` varchar(200) NOT NULL,
  `id_member` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 傾印資料表的資料 `telephone`
--

INSERT INTO `telephone` (`id`, `tel`, `id_member`) VALUES
(1, '0933-123456', 11),
(2, '0921-977000', 12),
(3, '0923-123123', 13),
(4, '0940-167366', 14),
(5, '0943-121233', 15),
(6, '0977-123333', 16),
(10, '0911-111000', 17),
(11, '0912-111-234', 20),
(12, '0911-145145', 21),
(13, '0933-129-000', 11),
(14, '0921-999888', 16),
(17, '111', 21),
(20, '143', 21),
(21, '0955-057845', 20);

--
-- 已傾印資料表的索引
--

--
-- 資料表索引 `member`
--
ALTER TABLE `member`
  ADD PRIMARY KEY (`id`);

--
-- 資料表索引 `telephone`
--
ALTER TABLE `telephone`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_member` (`id_member`);

--
-- 在傾印的資料表使用自動遞增(AUTO_INCREMENT)
--

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `member`
--
ALTER TABLE `member`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `telephone`
--
ALTER TABLE `telephone`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- 已傾印資料表的限制式
--

--
-- 資料表的限制式 `telephone`
--
ALTER TABLE `telephone`
  ADD CONSTRAINT `xxx` FOREIGN KEY (`id_member`) REFERENCES `member` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
