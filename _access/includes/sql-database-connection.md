\ifndef{sqlDatabaseConnection}
\define{sqlDatabaseConnection}

\editme

\subsection{Connecting to your Database Server}

\notes{Before you start, you're going to need the username and password you set-up above for accessing the database server. You will need to make use of it when your client connects to the server. It's good practice to never expose passwords in your code directly. So to protect your passowrd, we're going to create a `credentials.yaml` file locally that will store your username and password so that the client can access the server without ever showing your password in the notebook. This file will also score the URL and port of your database. You can get these details from your database connectivity and security details.}

\setupcode{import yaml
from ipywidgets import interact_manual, Text, Password}

\helpercode{@interact_manual(username=Text(description="Username:"),
                password=Password(description="Password:"),
                url=Text(description="URL:"),
                port=Text(description="Port:"))
def write_credentials(username, password, url, port):
    with open("credentials.yaml", "w") as file:
        credentials_dict = {'username': username,
                           'password': password,
                           'url': url,
                           'port': port}
        yaml.dump(credentials_dict, file)}

\notes{If you click `Run Interact` then the credentials you've selected will be saved in the `yaml` file.}

\notes{Then, we can read the server credentials using:}

\code{with open("credentials.yaml") as file:
  credentials = yaml.safe_load(file)
username = credentials["username"]
password = credentials["password"]
url = credentials["url"]
port = credentials["port"]}

\subsection{SQL Commands}

\notes{We have all the required data to interact with our database server. There are mainly two ways how we can do that. The first one is using magic SQL commands. For this option, we need to load the sql extension:}
\code{%load_ext sql}

\notes{We can now test our first database server connection using magic SQL. The first line establishes the connection and the second one list the databases. For now, you should see the databases that the engine has installed by default.}

\code{%sql mariadb+pymysql://$username:$password@$url?local_infile=1
%sql SHOW databases}
\notes{This connection also enables the uploading of local files as part of the connection (i.e., `local_infile=1`). We will use this property later.}

\endif
