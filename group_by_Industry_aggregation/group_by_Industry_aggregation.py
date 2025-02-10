from data.data import df

summary_stats = df.groupby('Industry_aggregation_NZSIOC')['Value'].agg(['sum', 'mean', 'min', 'max'])

summary_stats.columns = ['Total Value', 'Average Value', 'Min Value', 'Max Value']

print(summary_stats)
