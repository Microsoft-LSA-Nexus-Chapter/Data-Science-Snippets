import matplotlib.pyplot as plt

# initializing the data
x = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
y1 = [2345, 3000, 4975, 5067, 6700, 7890, 8000, 9012, 10023, 12069]

# plotting the data for x and y1 and adding a label Y1
plt.plot(x, y1, label='Y1')

y2 = [3986, 4253, 4986, 5825, 7244, 8321, 9575, 10056, 10489, 11099]

# plotting data for x, y1 and y2 and adding a label Y2
plt.plot(x,y2, label='Y2')

# adding title to the plot
plt.title("Line Chart")

# adding label on the y-axis
plt.ylabel('Y-Axis')

# adding label on the x-axis
plt.xlabel('X-Axis')

# adding a guide or key or legend to the graph
plt.legend()

# adding grid
plt.grid()

plt.show()
