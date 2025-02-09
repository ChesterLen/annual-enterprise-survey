from data.data import df

df_2023 = df.loc[df['Year'] == 2023]

df_income = df_2023.loc[df['Variable_name'] == 'Total income']

top_industry = df_income.groupby('Industry_name_NZSIOC')['Value'].sum().idxmax()

max_income = df_income.groupby('Industry_name_NZSIOC')['Value'].sum().max()

print(f"The industry with the highest total income in 2023 is: {top_industry} with an income of {max_income}")