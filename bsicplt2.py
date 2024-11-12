import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3, 4])
marks = [45, 60, 67, 54]

# Numerical vs Numerical
plot = plt.plot(x, marks, marker="D", markersize=10,\
                color="black", alpha=0.9)
plt.savefig("line_graph.png")
# plt.show()