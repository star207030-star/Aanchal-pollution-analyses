import matplotlib.pyplot as plt

countries = [
    "China", "USA", "South Korea", "Iran", "Australia",
    "Spain", "UK", "Canada", "Malaysia", "Sweden",
    "South Africa", "Indonesia", "Saudi Arabia",
    "Portugal", "Poland", "Nigeria", "Vietnam",
    "Turkey", "Denmark", "Switzerland", "Italy",
    "Morocco", "Brazil", "Czech Republic",
    "Hong Kong", "India"
]

percentages = [
    18.5, 12.3, 11.1, 7.4, 7.4,
    6.2, 3.7, 3.7, 3.7, 2.4,
    2.4, 2.4, 2.4,
    1.2, 1.2, 1.2, 1.2,
    1.2, 1.2, 1.2, 1.2,
    1.2, 1.2, 1.2,
    1.2, 1.2
]

# Combine country and percentage into one label
labels = [f"{country} ({percent}%)" for country, percent in zip(countries, percentages)]

plt.figure(figsize=(10, 10))
plt.pie(percentages, labels=labels, labeldistance=1.1)  # labels outside
plt.title("Country-wise Percentage Distribution")
plt.show()