from data.data import df

total_income_per_industry_for_a_given_year = df.loc[df['Year'] == 2023].groupby('Industry_name_NZSIOC')['Value'].sum()

print(total_income_per_industry_for_a_given_year)