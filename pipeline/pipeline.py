import sys
import pandas as pd 
print('arguments', sys.argv)
month = int(sys.argv[1])
df = pd.DataFrame({"Day": [1, 2], "num_passengers": [3, 4]})
df['month'] = month
print(df.head())

df.to_parquet(f"output.month={month}.parquet")

pd.DataFrame()
print(f'hello pipeline, month ={month}')