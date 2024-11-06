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

\exercise{The index made a difference in the time the join operation took to finish. Write the code to index the table `postcode_data` by `postcode`.}

\notes{And, let's try the join again:}

\code{%%sql
USE `ads_2024`;
select * from pp_data as pp inner join postcode_data as po on pp.postcode = po.postcode where pp.date_of_transfer BETWEEN '2024-01-01' AND '2024-12-31' limit 5;}

\exercise{Do you see any difference after adding the new index? Why?}

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

\code{#Write your code to establish a connection using your fynesee library}

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

\notes{We should define the primary key for this table too.}

\code{%%sql
ALTER TABLE `prices_coordinates_data`
ADD PRIMARY KEY (`db_id`);

ALTER TABLE `prices_coordinates_data`
MODIFY `db_id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=1;}

\notes{Indexing the table `pp_data` by date will be useful for populating the `prices_coordinates_data`. This index can take around 8 minutes to finish.}

\code{%%sql
USE `ads_2024`;
CREATE INDEX idx_pp_date_transfer ON pp_data(date_of_transfer);}

\notes{Now that the table exists in our database, let's create a method for uploading the join data. This method will upload the data for a given year and will use the logic we have used before but in Python code.}

\setupcode{import csv}

\setupcode{import time}

\helpercode{def housing_upload_join_data(conn, year):
  start_date = str(year) + "-01-01"
  end_date = str(year) + "-12-31"

  cur = conn.cursor()
  print('Selecting data for year: ' + str(year))
  cur.execute(f'SELECT pp.price, pp.date_of_transfer, po.postcode, pp.property_type, pp.new_build_flag, pp.tenure_type, pp.locality, pp.town_city, pp.district, pp.county, po.country, po.latitude, po.longitude FROM (SELECT price, date_of_transfer, postcode, property_type, new_build_flag, tenure_type, locality, town_city, district, county FROM pp_data WHERE date_of_transfer BETWEEN "' + start_date + '" AND "' + end_date + '") AS pp INNER JOIN postcode_data AS po ON pp.postcode = po.postcode')
  rows = cur.fetchall()

  csv_file_path = 'output_file.csv'

  # Write the rows to the CSV file
  with open(csv_file_path, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    # Write the data rows
    csv_writer.writerows(rows)
  print('Storing data for year: ' + str(year))
  cur.execute(f"LOAD DATA LOCAL INFILE '" + csv_file_path + "' INTO TABLE `prices_coordinates_data` FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED by '\"' LINES STARTING BY '' TERMINATED BY '\n';")
  conn.commit()
  print('Data stored for year: ' + str(year))}

\notes{Now, lets upload the joined data for 2024. This upload is going to take long time given the size of our datasets:}

\code{housing_upload_join_data(conn, 2024)}

\exercise{Add the `housing_upload_join_data` function to your fynesse library and write the code to upload the joined data for 2023.}

\notes{To finalise this lab, let's have a look at the structure of your database running the following code:}

\code{tables = %sql SHOW TABLES;

for row in tables:
    table_name = row[0]
    print(f"\nTable: {table_name}")
    
    table_status = %sql SHOW TABLE STATUS LIKE '{table_name}';
    approx_row_count = table_status[0][4] if table_status else 'Unable to fetch row count'
    print("\nApprox Row Count:", approx_row_count//100000/10, "M")

    first_5_rows = %sql SELECT * FROM `{table_name}` LIMIT 5;
    print(first_5_rows)
    
    indices = %sql SHOW INDEX FROM `{table_name}`;
    if indices:
        print("\nIndices:")
        for index in indices:
            print(f" - {index[2]} ({index[10]}): Column {index[4]}")
    else:
        print("\nNo indices set on this table.")}

\exercise{Write the output of the above code:}

\subsection{Summary}

\notes{In this practical, we have explored how to persist a couple of datasets in a relational database to facilitate future access. We configured a Cloud-hosted database server and had a look at two ways to interact with it. Then, we explored how to join tables using SQL and the benefits of indexing. The tables you created in this practical will be used along the course and we expect you use them for your final assignment. In the following practical, you will `assess` this data using different methods from visualisations to statistical analysis.}

\endif
