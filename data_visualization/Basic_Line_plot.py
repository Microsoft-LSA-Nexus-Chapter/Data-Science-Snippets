import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Year': [2019, 2020, 2021, 2022, 2023, 2024],
    'Sales': [200, 250, 300, 350, 400, 450],
    'Profit': [10, 40, 100, 80, 200, 150]
}

df = pd.DataFrame(data)
ax = df.plot(x='Year', y='Sales', kind='line', marker='o', title='Sales and Profit Over Years')
df.plot(x='Year', y='Profit', kind='line', marker='s', ax=ax, secondary_y=True)
ax.set_ylabel('Sales')
ax.right_ax.set_ylabel('Profit')
ax.grid(True)
plt.show()