import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Nation': ['India', 'India', 'Pakistan', 'Pakistan', 'Bangladesh', 'Bangladesh', 'Nepal', 'Nepal'],
    'Category': ['A', 'B', 'A', 'B', 'A', 'B', 'A', 'B'],
    'Sales': [10, 15, 20, 25, 30, 35, 40, 45]
}

df = pd.DataFrame(data)
pivot_df = df.pivot(index='Nation', columns='Category', values='Sales')
pivot_df.plot(kind='bar', stacked=False)
plt.title('Sales by Nation and Category')
plt.xlabel('Nation')
plt.ylabel('Sales')
plt.show()