import pandas as pd

data = {
    'employee_id': [101, 102, 103, 104, 105, 106],
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank'],
    'department': ['HR', 'IT', 'Finance', 'IT', 'HR', 'Finance'],
    'salary': [5000, 6000, 5500, 7000, 4800, 6200],
    'hire_date': ['2019-01-10', '2020-03-15', '2018-07-23', '2021-06-01', '2017-11-30', '2022-02-20'],
    'gender': ['F', 'M', 'M', 'M', 'F', 'M'],
    'performance_score': [3, 4, 5, 2, 4, 3]
}

df = pd.DataFrame(data)
df.to_csv('C:/Users/user/Desktop/employee_data_practice.csv', index=False)
