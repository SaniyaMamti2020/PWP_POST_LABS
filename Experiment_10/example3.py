import matplotlib.pyplot as plt

# Sample Data
languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

# Create Bar Chart
plt.bar(languages, popularity, color='green')

# Labels and Title
plt.xlabel("Programming Languages")
plt.ylabel("Popularity (%)")
plt.title("Bar Chart of Ek_3_Saniya_Mamti_16")
plt.show()