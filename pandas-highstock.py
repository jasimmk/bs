import pandas as pd

table = pd.read_csv('data-valid.csv',index_col=[0,1])
print table.idxmax()

