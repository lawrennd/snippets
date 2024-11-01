\ifndef{tableJoins}
\define{tableJoins}

\editme

\subsection{Joining Tables}

\notes{When we have two tables with data tha describe the same object, then it makes sense to join the tables together to enrich our knowledge about the object. For example, while the `pp_data` tell us about the transactions a house have been involved, the `postcode_data` tell us details about the location of the house. By joining both, we could answer more interesting questions like what are the coordinates of the most expensive house in 2024?}

\notes{The join of the tables must be done by matching the columns the tables share. In this case, the `pp_data` and the `postcode_data` tables share the column `postcode`. This operation can take long time because the number of records in each database is huge.}

\notes{You will find the issue of operations taking too long when handling large data sets in different scenarios. An appropriate strategy to overcome such issues is to index the tables. Indexing is a way to organise the data so the queries are more efficient time-wise. Now the task is to select the right columns to create the index. This decision depends on the columns we are using in the SQL operations. In the join case, we are selecting and matching records in each table using the `postcode` column. It makes sense then to create an index for these columns. The following code indexes the table `pp_data` by `postcode`.}

\code{# WARNING: Giving the size of the table, this operation takes around 8 minutes.
# If your database is not responsive, check the status of your database on the AWS dashboard. You can restart the database from the dashboard.
%%sql
USE `ads_2024`;
CREATE INDEX idx_pp_postcode ON pp_data(postcode);}
\notes{Let's try our join the tables for year 2024 now:}
\code{%%sql
USE `ads_2024`;
select * from pp_data as pp inner join postcode_data as po on pp.postcode = po.postcode where pp.date_of_transfer BETWEEN '2024-01-01' AND '2024-12-31' limit 5;}

\exercise{The index made a difference in the time the join operation took to finish. Let's see if indexing the table `postcode_data` by `postcode` has any additional effect.}

\notes{And, let's try the join again:}

\code{%%sql
USE `ads_2024`;
select * from pp_data as pp inner join postcode_data as po on pp.postcode = po.postcode where pp.date_of_transfer BETWEEN '2024-01-01' AND '2024-12-31' limit 5;}

\notes{Do you see any difference after adding the new index? Why?}

\subsection{Database Python Client}

\notes{Now let's focus on the second way of interacting with the database server. We can use Python code to create a client that communicates with our database server. For this, we need to install the following libraries.}

\setupcode{%pip install ipython-sql}

\code{%pip install PyMySQL}

\notes{Let's create a method in Python to establish a database connection wherever we like. It should look like the following code:}

\setupcode{import pymysql}

\helpercode{def create_connection(user, password, host, database, port=3306):
    """ Create a database connection to the MariaDB database
        specified by the host url and database name.
    :param user: username
    :param password: password
    :param host: host url
    :param database: database name
    :param port: port number
    :return: Connection object or None
    """
    conn = None
    try:
        conn = pymysql.connect(user=user,
                               passwd=password,
                               host=host,
                               port=port,
                               local_infile=1,
                               db=database
                               )
        print(f"Connection established!")
    except Exception as e:
        print(f"Error connecting to the MariaDB Server: {e}")
    return conn}

\notes{Please add the code above to your fynesse library. We can now call this function to get a connection:}

\notes{Now let's define a Python method that uploads to a table the data product of the join operation between the tables `pp_data` and `postcode_data`. For this, we first need to create the table that will store this data.}

\code{%%sql
USE `ads_2024`;
--
-- Table structure for table `prices_coordinates_data`
--
DROP TABLE IF EXISTS `prices_coordinates_data`;
CREATE TABLE IF NOT EXISTS `prices_coordinates_data` (
  `price` int(10) unsigned NOT NULL,
  `date_of_transfer` date NOT NULL,
  `postcode` varchar(8) COLLATE utf8_bin NOT NULL,
  `property_type` varchar(1) COLLATE utf8_bin NOT NULL,
  `new_build_flag` varchar(1) COLLATE utf8_bin NOT NULL,
  `tenure_type` varchar(1) COLLATE utf8_bin NOT NULL,
  `locality` tinytext COLLATE utf8_bin NOT NULL,
  `town_city` tinytext COLLATE utf8_bin NOT NULL,
  `district` tinytext COLLATE utf8_bin NOT NULL,
  `county` tinytext COLLATE utf8_bin NOT NULL,
  `country` enum('England', 'Wales', 'Scotland', 'Northern Ireland', 'Channel Islands', 'Isle of Man') NOT NULL,
  `latitude` decimal(11,8) NOT NULL,
  `longitude` decimal(10,8) NOT NULL,
  `db_id` bigint(20) unsigned NOT NULL
) DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=1 ;}

\endif
