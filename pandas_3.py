import pandas as pd
import numpy as np

data = {
    'Name': ['Anna', 'Bohdan', 'Maria'],
    'Age': [25, 30, 22],
    'City': ['Kyiv', 'Lviv', 'Odesa']
}

df = pd.DataFrame(data, index=['id_100', 'id_101', 'id_102'])

print('---my first dataframe---')
print(df)

# one series
print(df['Name'])

print(df.loc['id_101', 'Age'])

# bool indexing
filtered_result = df['Age'] > 24
print(filtered_result)

print(df[filtered_result])


filtered_result_city = df['City'] == 'Lviv'
print(filtered_result_city)

print('---only Lviv based ---')
print(df[filtered_result_city])

print('-- new series added ---')
df['Age_next_year'] = df['Age'] + 1
print(df)

# save to csv
# df.to_csv('my_first_df.csv')

# create new series ( based on py list
hobby_list = ['piano', 'swimming', 'tenis']
df['Hobby'] = hobby_list
print(df)

# update=refresh=rewrite csv
df.to_csv('my_first_df.csv')

print('--loaded from csv--')
df_new = pd.read_csv('my_first_df.csv', index_col=0)
print(df_new)