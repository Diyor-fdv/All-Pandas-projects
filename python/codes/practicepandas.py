import pandas as pd
# df = pd.read_csv("C:/Users/user/Desktop/python/spotify_data_dictionary_Description.csv")
# print(df.iloc[0:4])
# print(df.columns)
# print(df.iloc[1,1])
# df.sort_values(['Field','Description'],ascending=[1,0])
# df
# df['Field'] = df.iloc[:, 4:10].sum(axis=1)
# cols = list(df.columns)
# df = df[cols[0:4]+[cols[-1]]+cols[4:12]]
# df.head(5)
# df.to_csv('C:/Users/user/Desktop/newmody.txt', index=False, sep='\t')
# new_df = df.loc[(df['Field'] == 'Diyorbek')]
# new_df.reset_index(drop=True, inplace=True)
# new_df
# new_df.to_csv('C:/Users/user/Desktop/filtered.csv')
# df['count']=1
# df.groupby(['Field','Description']).count()['count']
# result_df = pd.DataFrame()

# for chunk in pd.read_csv('C:/Users/user/Desktop/filtered.csv', chunksize=5):
#     group = chunk.groupby(['Field']).count()
#     result_df = pd.concat([result_df, group])

# print(result_df)
df = pd.read_csv("C:/Users/user/Desktop/python/employee_data_practice.csv")
df['bonus'] = df['salary'].apply(lambda x: x * 0.10 if x < 6000 else x * 0.05)
df['gender'] = df['gender'].map({'M': 'Male', 'F': 'Female'})
pivot = pd.pivot_table(df, values='salary', index='department', aggfunc='mean')
df['hire_date'] = pd.to_datetime(df['hire_date'])
df['years_experience'] = 2025 - df['hire_date'].dt.year
df['rolling_avg_salary'] = df['salary'].rolling(window=3).mean()
it_males = df.query("department == 'IT' and gender == 'M'")
outliers = df[df['salary'] > 6500]
print(df)







