
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'name': ['Harry', 'Hermione', 'Ron', 'Draco', 'Luna', 'Neville', 'Cedric', 'Cho'],
    'house': ['Gryffindor', 'Gryffindor', 'Gryffindor', 'Slytherin', 'Ravenclaw', 'Gryffindor', 'Hufflepuff', 'Ravenclaw'],
    'age': [17, 17, 17, 17, 16, 17, 18, 17],
    'wand_length': [11, 10.75, 14, 10, 13.5, 13, 12.25, 11]
}
df = pd.DataFrame(data)


print("Harry Potter Characters Dataset:")
print(df)

house_counts = df['house'].value_counts()
print("\nNumber of characters in each house:")
print(house_counts)


plt.figure(figsize=(6, 4))
house_counts.plot(kind='bar', color=['red', 'green', 'blue', 'yellow'])
plt.title('Character Distribution by House')
plt.xlabel('House')
plt.ylabel('Number of Characters')
plt.show()


avg_wand_length = df['wand_length'].mean()
print("\nAverage wand length:", avg_wand_length)

gryffindor_students = df[df['house'] == 'Gryffindor']
print("\nGryffindor Students:")
print(gryffindor_students)
