# bar char and histogram.

import matplotlib.pyplot as plt

#defind data
data={
    "city": ["delhi","mumbai","banglore","new york","london","beijig"],
    "population" :[8.4,9.4,10.4,11.4,12.4,13.4]
}

#setup figure and subplots
plt.figure(figsize=(12,5))

#bar char
plt.subplot(1,2,1)
plt.bar(data["city"],data["population"],color="lightgreen")
plt.xlabel("city")
plt.ylabel("population(in millions)")
plt.title("population across globe")
plt.xticks(rotation=45)

# hist
plt.subplot(1,2,2)
plt.hist(data["population"],bins=4,color="lightgreen",edgecolor="black")
plt.xlabel("population(in millions)")
plt.ylabel("frequency")
plt.title("population ditribution")

#display
plt.tight_layout()
plt.show()