\ifndef{applyingModelFramework}
\define{applyingModelFramework}

\editme

\subsection{Applying Model Framework}

\notes{You should now try out the model framework that we described above on a dataset derived from the 2021 UK Census Dataset. Let's start by downloading the data.}

\code{import requests
import zipfile
import io
import os
import pandas as pd}

\code{def download_census_data(code, base_dir=''):
  url = f'https://www.nomisweb.co.uk/output/census/2021/census2021-{code.lower()}.zip'
  extract_dir = os.path.join(base_dir, os.path.splitext(os.path.basename(url))[0])

  if os.path.exists(extract_dir) and os.listdir(extract_dir):
    print(f"Files already exist at: {extract_dir}.")
    return

  os.makedirs(extract_dir, exist_ok=True)
  response = requests.get(url)
  response.raise_for_status()

  with zipfile.ZipFile(io.BytesIO(response.content)) as zip_ref:
    zip_ref.extractall(extract_dir)

  print(f"Files extracted to: {extract_dir}")}

\code{def load_census_data(code, level='msoa'):
  return pd.read_csv(f'census2021-{code.lower()}/census2021-{code.lower()}-{level}.csv')}

\code{download_census_data('TS007') # Age by single year of age

age_df = load_census_data('TS007', level='ltla')
# Preparing the columns we want
age_df = age_df.drop(age_df.columns[[0,2,3,4,10,16,23,28,34,45,61,77,88,99,115]], axis=1).set_index('geography')
age_df.columns = range(100)}

\notes{Below we will plot the overall age structure of the UK population in 2021. This profile is not very straightforward, and has historical reasons. Have a look online to understand the data better - you should see a similar chart [here](https://en.wikipedia.org/wiki/Demographics_of_England).}

\code{plt.scatter(range(100), age_df.sum(axis=0))
plt.show()}

\notes{The data looks very different when we look at individual cities. For example, Cambridge has a very different age profile than most of the UK.}

\code{x_values = range(100)

plt.scatter(x_values, age_df.loc['Cambridge'], label='Cambridge')

plt.legend()
plt.show()}

\notes{Now try to use the framework that we have derived to explain the two data-sets above. There is no right or wrong answer here, what we are looking for is a motivation of why you have made the choices that you have madeand how this effects the conclusions that you can draw.}

\exercise{Would it make sense to split up the data-set in different regions and fit separate models If so, what is the criteria that you split the data using?}

\exercise{What would be a sensible design matrix?}

\exercise{What GLM models would make sense to fit?}

\notes{During the check-session we will ask you a few questions on how you have reasoned when fitting the data. Again, what we are looking for is motivation not "the best fit".}

\endif