from data.data import df
import matplotlib.pyplot as plt

variable_name = "Total income"

df_variable = df[df['Variable_name'] == variable_name]

trend_data = df_variable.groupby('Year')['Value'].sum()

plt.figure(figsize=(10, 5))
plt.plot(trend_data.index, trend_data.values, marker='o', linestyle='-', color='b')
plt.xlabel("Year")
plt.ylabel("Total Income")
plt.title(f"Trend of {variable_name} Over the Years")
plt.grid(True)
plt.show()