import matplotlib.pyplot as plt

years = [2020, 2021, 2022, 2023, 2024]

delhi = [85, 95, 90, 100, 108]
kolkata = [45, 60, 52, 48, 46]
mumbai = [38, 44, 42, 40, 32]
hyderabad = [35, 40, 45, 42, 30]
bengaluru = [28, 30, 32, 31, 29]
chennai = [25, 27, 26, 28, 30]

plt.figure()

plt.plot(years, delhi, marker='o', label="Delhi")
plt.plot(years, kolkata, marker='o', label="Kolkata")
plt.plot(years, mumbai, marker='o', label="Mumbai")
plt.plot(years, hyderabad, marker='o', label="Hyderabad")
plt.plot(years, bengaluru, marker='o', label="Bengaluru")
plt.plot(years, chennai, marker='o', label="Chennai")

plt.xlabel("Year")
plt.ylabel("PM2.5 (µg/m3)")
plt.title("PM2.5 Annual Average (2020-2024)")
plt.legend()

plt.show()