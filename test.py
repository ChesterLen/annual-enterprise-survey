import pandas as pd

data = {
    'Values': ['value1', 'value2', 'value3'],
    'Words': ['word1', 'word2']  # Shorter list
}

df = pd.DataFrame({key: pd.Series(value) for key, value in data.items()})
df = df.fillna('None')

print(df)
