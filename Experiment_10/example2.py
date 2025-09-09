import matplotlib.pyplot as plt

# Data for multiple lines
x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]
y2 = [1, 3, 5, 7, 9]

# Plot lines
plt.plot(x, y1, label='Line 1', color='blue')
plt.plot(x, y2, label='Line 2', color='red')

# Add Labels, Title, Legend
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("Multi-Line Chart of Ek_3_Saniya_Mamti_16")
plt.legend()
plt.show()