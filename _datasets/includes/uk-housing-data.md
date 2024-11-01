\ifndef{ukHousingData}
\define{ukHousingData}

\editme

\subsection{UK Housing Datasets}

The UK Price Paid data for housing in dates back to 1995 and contains millions of transactions. This database is available at the [gov.uk site](https://www.gov.uk/government/statistical-data-sets/price-paid-data-downloads). The total data is over 4 gigabytes in size and it is available in a single file or in multiple files splitted by years and semester. For example, the first part of the data for 2018 is stored at <http://prod.publicdata.landregistry.gov.uk.s3-website-eu-west-1.amazonaws.com/pp-2018-part1.csv>. By applying the divide and conquer principle, we will download the splitted data because these files is less than 100MB each which makes them easier to manage.

\setupcode{import requests}

\code{# Base URL where the dataset is stored 
base_url = "http://prod.publicdata.landregistry.gov.uk.s3-website-eu-west-1.amazonaws.com"}

\helpercode{def download_price_paid_data(year_from, year_to):
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

\notes{Now we can call the function to download data between specified years:}

\code{download_price_paid_data(1995, 2020)}

\exercise{Add this function to your fynesse library and download the data from 2021 to 2024 using your library.}

\endif
