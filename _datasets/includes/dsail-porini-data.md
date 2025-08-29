\ifndef{dsailPoriniData}
\define{dsailPoriniData}

\editme

\subsection{DSAIL-Porini Camera Trap Dataset}

\notes{Head over to https://data.mendeley.com/datasets/6mhrhn7rxc/6 to explore the DSAIL-Porini dataset. This dataset contains camera trap images and annotations from Kenya, providing rich information about wildlife patterns and behavior.

We'll work with the [`camera_trap_dataset_annotation.xlsx`](https://data.mendeley.com/public-files/datasets/6mhrhn7rxc/files/641e83c9-16a3-485c-b247-b5701f8a5540/file_downloaded) file which contains metadata about animal sightings.}

\setupcode{import os
import requests
import pandas as pd}

\code{def download_if_not_exists(url, filepath):
    """Download file if it doesn't exist locally"""
    if os.path.exists(filepath):
        print(f"File already exists: {filepath}")
    else:
        print(f"Downloading: {url}")
        response = requests.get(url, stream=True)
        response.raise_for_status()
        with open(filepath, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"Downloaded to: {filepath}")
    return filepath}

\code{# Download the DSAIL-Porini dataset
porini_file = download_if_not_exists(
    'https://data.mendeley.com/public-files/datasets/6mhrhn7rxc/files/641e83c9-16a3-485c-b247-b5701f8a5540/file_downloaded', 
    'camera_trap_dataset_annotation.xlsx'
)

porini_df = pd.read_excel(porini_file)
porini_df.head()}

\notes{This dataset represents a typical real-world scenario where we have rich, messy data that requires careful preprocessing. The camera trap setup provides both temporal and spatial dimensions that we can exploit for analysis.}

\endif
