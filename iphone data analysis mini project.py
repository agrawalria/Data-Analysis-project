import pandas as pd
df = pd.read_csv("/workspaces/Data-Analysis-project/apple_products.csv")
#print(df.head())
#print(df.count())
max_mrp = df['Mrp'].max()
min_mrp = df['Mrp'].min()
#print(max_mrp)
#print(df[df['Mrp'] == max_mrp]['Product Name'])
#print(df[df['Mrp'] == min_mrp]['Product Name'])
#print(df[df['Mrp'] > 50000])
#print(list(df['Product Name'])[1][6:15].upper().strip())
df['Model_Name'] = df['Product Name'].str[6:15]
#print(df['Model_Name'])
print(df.sort_values(by=['Star Rating'], ascending= False))