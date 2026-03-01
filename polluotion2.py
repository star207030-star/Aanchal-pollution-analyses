import matplotlib.pyplot as plt
import numpy as np

years = ['2020', '2021', '2022', '2023', '2024']

low = [10, 12, 15, 11, 14]
moderate = [20, 18, 22, 19, 21]
high = [30, 28, 25, 27, 26]
very_high = [40, 42, 38, 43, 39]

plt.figure()

plt.bar(years, low, label="Low")
plt.bar(years, moderate, bottom=low, label="Moderate")
plt.bar(years, high, bottom=np.array(low)+np.array(moderate), label="High")
plt.bar(years, very_high, bottom=np.array(low)+np.array(moderate)+np.array(high), label="Very High")

plt.xlabel("Year")
plt.ylabel("Percentage of Hours")
plt.title("Annual Hours at Different PM2.5 Levels (New Delhi)")
plt.legend()

plt.show()