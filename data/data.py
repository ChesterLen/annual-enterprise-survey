import pandas as pd

data = pd.read_csv('../annual-enterprise-survey-2023-financial-year-provisional.csv')

df = pd.DataFrame(data)

#  clean data
df_duplicates = df.duplicated().sum()

if df_duplicates:
    df = df.drop_duplicates()

df_missing_values = df.isnull().sum()

if df_missing_values.sum() > 0:
    df.fillna('None', inplace=True)

df['Year'] = pd.to_datetime(df['Year'], format='%Y').dt.year
df['Value'] = pd.to_numeric(df['Value'], errors='coerce')