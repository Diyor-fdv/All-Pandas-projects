import pandas as pd
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
df.to_csv('C:/Users/user/Desktop/salaries', index=False)
