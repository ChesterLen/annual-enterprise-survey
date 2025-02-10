from data.data import df

total_income = df[df['Variable_name'] == 'Total income']
total_expenditure = df[df['Variable_name'] == 'Total expenditure']

income_vs_expenditure = (
    total_income.groupby('Industry_name_NZSIOC')['Value'].sum()
    .to_frame(name='Total Income')
    .join(
        total_expenditure.groupby('Industry_name_NZSIOC')['Value'].sum()
        .to_frame(name='Total Expenditure'),
        how='outer'
    )
)

income_vs_expenditure = income_vs_expenditure.fillna(0)

income_vs_expenditure['Comparison'] = income_vs_expenditure.apply(
    lambda row: 'Income > Expenditure' if row['Total Income'] > row['Total Expenditure'] else
                'Income < Expenditure' if row['Total Income'] < row['Total Expenditure'] else
                'Income = Expenditure', axis=1
)

print(income_vs_expenditure)