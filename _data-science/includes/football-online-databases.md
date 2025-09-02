\ifndef{footballOnlineDatabases}
\define{footballOnlineDatabases}

\editme

\subsection{Online Databases}

\notes{An example would be Amazon AWS Relational Database (RDS)}

\code{# import pandas as pd, sqlalchemy as sa

# df = pd.read_csv("football_data/players.csv")

# DATABASE_URL = "postgresql+psycopg2://USER:PASSWORD@HOST:5432/DBNAME"
# engine = sa.create_engine(DATABASE_URL)

# with engine.begin() as conn:
#     conn.exec_driver_sql("DROP TABLE IF EXISTS players")
#     df.to_sql("players", conn, if_exists="replace", index=False)
#     for row in conn.exec_driver_sql("SELECT playerid FROM players WHERE potential > 92"):
#         print(row)}

\subsubsection{Online Storage}

\notes{For example Amazon AWS Simple Storage Service (S3)}

\code{# import boto3

# bucket = "your-bucket-name"
# key = "players.csv"
# filename = "players.csv"

# s3 = boto3.client("s3")

# # Upload file
# s3.upload_file(filename, bucket, key)
# print("Uploaded", filename, "to s3://"+bucket+"/"+key)

# # Download file
# s3.download_file(bucket, key, "players_downloaded.csv")
# print("Downloaded to players_downloaded.csv")}

\subsubsection{Exercises}

\subsubsection{Exercise 1: Make a database}

\subsubsection{1.1 Create a full SQL database from the following tables:}

\notes{- players.csv
- teams.csv
- leagues.csv
- countries.csv
- teamplayerlinks.csv
- leagueteamlinks.csv
- models.csv}

\code{# TODO}

\subsubsection{1.2 Make the appropriate indices:}

\notes{- playerid
- teamid
- leagueid}

\code{# TODO}

\endif
