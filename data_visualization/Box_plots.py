import matplotlib.pyplot as plt
import pandas as pd
data = {
    'Category': ['A']*10 + ['B']*10,
    'Value': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
}
df = pd.DataFrame(data)
df.boxplot(by='Category')
plt.title('Box Plot Example')
plt.suptitle('')
plt.xlabel('Category')
plt.ylabel('Value')
plt.show()