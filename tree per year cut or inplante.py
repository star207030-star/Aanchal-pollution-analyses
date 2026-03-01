# Program to create bar chart of global tree statistics

import matplotlib.pyplot as plt

# Data (in Billions per year)
trees_cut = 15
trees_planted = 7.5
target_planting = 25

# Categories
categories = [
    "Trees Cut Per Year",
    "Trees Planted Currently",
    "Suggested Planting Target"
]

values = [trees_cut, trees_planted, target_planting]

# Create bar chart
plt.figure()
plt.bar(categories, values)

# Labels and Title
plt.xlabel("Category")
plt.ylabel("Trees (Billions per Year)")
plt.title("Global Tree Planting vs Cutting Per Year")

# Rotate labels
plt.xticks(rotation=20)

# Show graph
plt.show()
