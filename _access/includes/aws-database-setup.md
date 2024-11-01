\ifndef{awsDatabaseSetup}
\define{awsDatabaseSetup}

\editme

\subsection{Cloud Hosted Database}

\notes{The size of the data makes it unwieldy to manipulate directly in python frameworks such as `pandas`. As a result we will host and access the data in a *relational database*.}

\notes{Using the following ideas:
1. A cloud hosted database (such as MariaDB hosted on the AWS RDS service).
2. SQL code wrapped in appropriately structured python functions.
3. Joining databases tables.
You will construct a database containing tables that contain all house prices, latitudes and longitudes from the UK house price data base since 1995.}

\notes{*** You will manipulate large datasets along this practical and the final assessment. If your database is blocked or is not responsive after any operation, have a look at the databases dashboard to see if it is using too much CPU. Reboot the database if that is the case.***}
\notes{***If you encounter problems with the online notebook (e.g., interrupted connections with the AWS server), you can use a local IDE to work in your machine.***}

\subsubsection{Creating a MariaDB Server on AWS}

\notes{1. Log in to your AWS account and go to the AWS RDS console [here](https://console.aws.amazon.com/rds/home).
2. Make sure **the region is set to Europe (London) which is denoted as eu-west-2.**
3. Scroll down to "Create Database". Do *not* create an Aurora database instance.
4. `Standard Create` should be selected. In the box below, which is titled `Engine Options` you should select `MariaDB`. You can leave the `Version` as it's set.}

\figure{\includepng{\diagramsDir/cloud/aws-select-mariadb-rds}{60%}}{The AWS console box for selecting the `MariaDB` engine.}{aws-mariadb-select}

\notes{5. In the box below that, make sure you select `Free tier`.}

\figure{\includepng{\diagramsDir/cloud/aws-select-free-tier}{60%}}{Make sure you select the free tier option for your database server.}{aws-free-tier}

\notes{6. Name your database server. For your setup we suggest you use `database-ads-<CRSid>` for the name. `<CRSid>` **corresponds to your CRSid. So, every student has an independent database.**
7. Set a master password for accessing the database server as admin.}

\figure{\includepng{\diagramsDir/cloud/aws-mariadb-settings}{60%}}{Set the password and username for the database server access.}{aws-mariadb-settings}

\notes{8. Leave the `DB instance class` as it is.
9. Leave the `DB instance size` at the default setting. Leave the storage type and allocated storage at the default settings of `General Purpose` (SSD) and `20`.
10. *Disable* autoscaling in the `Storage Autoscaling` option.
11. In the connectivity leave the VPC selection as `Default VPC` and *enable* `Publicly accessible` so that you'll have an IP address for your database.
12. In `VPC security group` select `Create new` to create a new security group for the instance.
13. Write `ADSMariaDB` as the group name for the VPC security group.
14. Leave the rest as it is and select `Create database` at the bottom to launch the database server.}

\notes{*Note:* by setting the inbound rule to `0.0.0.0/0` we have opened up access to *any* IP address. If this were production code you wouldn't do this, you would specify a range of addresses or the specific address of the compute server that needed to access the system. Because we're using Google colab or another notebook client to access, and we can't control the IP address of that access, for simplicity we've set it up so that any IP address can access the database, but that is *not good practice* for production systems.}

\endif
