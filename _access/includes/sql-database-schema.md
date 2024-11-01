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

\notes{The `schema` defines an id field in the table (i.e., `db_id`), which must be unique and will play the role of [primary key](https://www.geeksforgeeks.org/primary-key-in-dbms/), which is a crucial concept in relational databases. The following code sets up the primary key for our table and makes it auto increment when a new row (i.e., record) is insterted into the table.}

\code{%%sql
--
-- Primary key for table `pp_data`
--
ALTER TABLE `pp_data`
ADD PRIMARY KEY (`db_id`);

ALTER TABLE `pp_data`
MODIFY db_id bigint(20) unsigned NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1;}

\notes{We've created our first table in the database with its respective primary key. Now we need to populate it. There are different methods to do that. [Some of them more efficient than others](https://dev.to/arctype/load-data-infile-vs-insert-in-mysql-why-how-when-247f#:~:text=%E2%80%8BWhen%20working%20with%20MySQL,way%20faster%20than%20INSERT%20does.). In our case, given the size of our data set, we will take advantage of the csv files we downloaded in the first part of this lab. The command `LOAD DATA LOCAL INFILE` allows uploading data to the table from a CSV file. We must specify the name of the local file, the name of the table, and the format of the CSV file we want to use (i.e., separators, enclosers, termination line characters, etc.)}

\notes{The following command uploads the data of the transactions that took place in 1995.}

\code{%sql USE `ads_2024`;
%sql LOAD DATA LOCAL INFILE "./pp-1995-part1.csv" INTO TABLE `pp_data` FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED by '"' LINES STARTING BY '' TERMINATED BY '\n';
%sql LOAD DATA LOCAL INFILE "./pp-1995-part2.csv" INTO TABLE `pp_data` FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED by '"' LINES STARTING BY '' TERMINATED BY '\n';}

\notes{If we want to upload the data for all the years, we will need a command for each CSV in our dataset. Alternatively, we can use Python code together with SQL magic commands as follows:}

\code{# WARNING: This code will take a long time to finish (i.e., more than 30 minutes) given our dataset's size. The print informs the uploading progress by year.
for year in range(1996,2025):
  print ("Uploading data for year: " + str(year))
  for part in range(1,3):
    file_name = "./pp-" + str(year) + "-part" + str(part) + ".csv"
    %sql LOAD DATA LOCAL INFILE "$file_name" INTO TABLE `pp_data` FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED by '"' LINES STARTING BY '' TERMINATED BY '\n';}

\notes{Now that we uploaded the data, we can retrieve it from the table. We can select the first 5 elements in the `pp_data` using this command:}

\code{%%sql
USE `ads_2024`;
SELECT * FROM `pp_data` LIMIT 5;}

\notes{We can also count the number of rows in our table. It can take more than 5 minutes to finish. There are almost 30 million of records in the dataset.}

\code{%sql select count(*) from `pp_data`;}

\endif
