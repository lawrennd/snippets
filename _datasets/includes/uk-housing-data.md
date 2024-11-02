\ifndef{ukHousingData}
\define{ukHousingData}

\editme

\subsection{UK Housing Datasets}

\notes{The UK Price Paid data for housing in dates back to 1995 and contains millions of transactions. This database is available at the [gov.uk site](https://www.gov.uk/government/statistical-data-sets/price-paid-data-downloads). The total data is over 4 gigabytes in size and it is available in a single file or in multiple files splitted by years and semester. For example, the first part of the data for 2018 is stored at <http://prod.publicdata.landregistry.gov.uk.s3-website-eu-west-1.amazonaws.com/pp-2018-part1.csv>. By applying the divide and conquer principle, we will download the splitted data because these files is less than 100MB each which makes them easier to manage.}

\notes{Let's download first the two files that contain the price paid data for the transactions that took place in the year 1995:}

\setupcode{import requests}

\code{# Base URL where the dataset is stored 
    base_url = "http://prod.publicdata.landregistry.gov.uk.s3-website-eu-west-1.amazonaws.com"}
    # Downloading part 1 from 1995
    file_name_part_1 = "/pp-1995-part1.csv"
    url = base_url + file_name_part_1
    response = requests.get(url)
    if response.status_code == 200:
      with open("." + file_name_part_1, "wb") as file:
        file.write(response.content)

    # Downloading part 2 from 1995
    file_name_part_2 = "/pp-1995-part2.csv"
    url = base_url + file_name_part_2
    response = requests.get(url)
    if response.status_code == 200:
      with open("." + file_name_part_2, "wb") as file:
        file.write(response.content)}

\notes{The data is downloaded as CSV files in the files explorer of this notebook. You can see that the two pieces of code that download the data are quite similar. It makes sense to use a for loop to automate the way we access the dataset for the different years. The following code will download the data from 1996 to 2010.}

\code{# Base URL where the dataset is stored 
    base_url = "http://prod.publicdata.landregistry.gov.uk.s3-website-eu-west-1.amazonaws.com"}
    # File name with placeholders
    file_name = "/pp-<year>-part<part>.csv"

    for year in range(1996,2011):
      print ("Downloading data for year: " + str(year))
      for part in range(1,3):
        url = base_url + file_name.replace("<year>", str(year)).replace("<part>", str(part))
        response = requests.get(url)
        if response.status_code == 200:
          with open("." + file_name.replace("<year>", str(year)).replace("<part>", str(part)), "wb") as file:
            file.write(response.content)}

\notes{If we think of reusability, it would be good to create a function that can be called from anywhere in your code.}

\setupcode{import requests}

\helpercode{def download_price_paid_data(year_from, year_to):
    # Base URL where the dataset is stored 
    base_url = "http://prod.publicdata.landregistry.gov.uk.s3-website-eu-west-1.amazonaws.com"
    """Download UK house price data for given year range"""
    # File name with placeholders
    file_name = "/pp-<year>-part<part>.csv"
    
    for year in range(year_from, (year_to+1)):
        print (f"Downloading data for year: {year}")
        for part in range(1,3):
            url = base_url + file_name.replace("<year>", str(year)).replace("<part>", str(part))
            response = requests.get(url)
            if response.status_code == 200:
                with open("." + file_name.replace("<year>", str(year)).replace("<part>", str(part)), "wb") as file:
                    file.write(response.content)}

\notes{Now we can call the function to download the data between two given years. For example, let's download the data from 2011 to 2020 by calling the defined function.}

\code{download_price_paid_data(2011, 2020)}

\exercise{Add this function to your fynesse library and download the data from 2021 to 2024 using your library.}

\endif
