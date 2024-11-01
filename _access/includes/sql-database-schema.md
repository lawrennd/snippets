\ifndef{sqlDatabaseSchema}
\define{sqlDatabaseSchema}

\editme

\subsection{Database Schema}

\notes{As a first step after establishing a connection, we should create our own database in the server. We will use this relational database to store, structure, and access the different datasets we will manipulate during this course. We will use SQL code for this and once again magic commands:}

\code{%%sql
SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";

CREATE DATABASE IF NOT EXISTS `ads_2024` DEFAULT CHARACTER SET utf8 COLLATE utf8_bin;}

\code{%sql SHOW databases}

\notes{After the database is created in our server, we must tell it which database we will use. You will need to run this command after you create a new connection:}

\code{%%sql
USE `ads_2024`;}

\notes{A database is composed of tables where data records are stored in rows. The attributes of each record are the columns. We must define an `schema` to create a table in a database. The `schema` tells the database and the server what to expect in the columns of the table (i.e., names and data types of the columns).}

\notes{The `schema` is defined by the data we want to store. If we want to store the UK Price Paid data, we should have a look at [its description first](https://www.gov.uk/guidance/about-the-price-paid-data#explanations-of-column-headers-in-the-ppd). Also, we should a look at the data. Let's do that for the second semester of 2021.}

\setupcode{import pandas as pd}

\code{file_name = "./pp-2021-part2.csv"
data = pd.read_csv(file_name)
data.info(verbose=True)}

\notes{Based on the columns of the dataframe, we should define now the equivalent `schema` of the table in the SQL database. We will use once more SQL magic commands to create a table with the equivalent `schema`:}

\code{# WARNING: If you run this command after you have uploaded data to the table (in the steps below), you will delete the uploaded data as this command first drops the table if exists (DROP TABLE IF EXISTS `pp_data`;).
%%sql
--
-- Table structure for table `pp_data`
--
USE `ads_2024`;
DROP TABLE IF EXISTS `pp_data`;
CREATE TABLE IF NOT EXISTS `pp_data` (
  `transaction_unique_identifier` tinytext COLLATE utf8_bin NOT NULL,
  `price` int(10) unsigned NOT NULL,
  `date_of_transfer` date NOT NULL,
  `postcode` varchar(8) COLLATE utf8_bin NOT NULL,
  `property_type` varchar(1) COLLATE utf8_bin NOT NULL,
  `new_build_flag` varchar(1) COLLATE utf8_bin NOT NULL,
  `tenure_type` varchar(1) COLLATE utf8_bin NOT NULL,
  `primary_addressable_object_name` tinytext COLLATE utf8_bin NOT NULL,
  `secondary_addressable_object_name` tinytext COLLATE utf8_bin NOT NULL,
  `street` tinytext COLLATE utf8_bin NOT NULL,
  `locality` tinytext COLLATE utf8_bin NOT NULL,
  `town_city` tinytext COLLATE utf8_bin NOT NULL,
  `district` tinytext COLLATE utf8_bin NOT NULL,
  `county` tinytext COLLATE utf8_bin NOT NULL,
  `ppd_category_type` varchar(2) COLLATE utf8_bin NOT NULL,
  `record_status` varchar(2) COLLATE utf8_bin NOT NULL,
  `db_id` bigint(20) unsigned NOT NULL
) DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=1 ;}

\endif
