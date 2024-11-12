import matplotlib.pyplot as plt
import numpy as np



days = ["Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"]
max_t = [29, 33, 36, 39, 30, 40, 35]
min_t = [26, 22, 16, 27, 25, 18, 23]

def avgt():
    avgt = list(map(lambda x1, x2 : (x1+x2)/2, max_t, min_t))
    return avgt

avg_t = avgt()
# print(avg_t)

# Multiple plots
plot1 = plt.plot(days, max_t, label="Max", marker="D")
plot2 = plt.plot(days, min_t, label="Min", marker="o")
plot3 = plt.plot(days, avg_t, label="Avg", marker="x")
plt.xlabel("Days")
plt.ylabel("Temperature")
plt.title("WeatherAnalysis")
plt.legend(loc="best", shadow=True, fontsize="large")
plt.savefig("multi_linegraph.png")
# plt.show()