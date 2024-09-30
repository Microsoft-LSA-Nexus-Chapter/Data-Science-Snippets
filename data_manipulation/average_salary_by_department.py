import pandas as pd

# Sample data
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma'],
    'Department': ['Sales', 'HR', 'Sales', 'IT', 'HR'],
    'Salary': [60000, 50000, 70000, 65000, 52000]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Data manipulation: Group by 'Department' and calculate average salary
avg_salary_by_dept = df.groupby('Department')['Salary'].mean().reset_index()

# Sort the result by average salary in descending order
avg_salary_by_dept = avg_salary_by_dept.sort_values(by='Salary', ascending=False)

print("Average Salary by Department:")
print(avg_salary_by_dept)
