import matplotlib.pyplot as plt

# Sample country data
countries = ['USA', 'Canada', 'Brazil', 'UK', 'India', 'China', 'Australia']
pm25 = [12, 8, 18, 15, 45, 50, 10]

plt.figure()
plt.bar(countries, pm25)

plt.xlabel("Countries")
plt.ylabel("PM2.5 (µg/m3)")
plt.title("2024 Global PM2.5 Levels")
plt.xticks(rotation=45)


plt.show()
