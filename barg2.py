import  matplotlib.pyplot as plt
import  numpy as np
from pro_bargrph import companies, revenues

profits = [250, 150, 300, 250]
y= np.arange(len(companies))
# print(y)

fig, ax = plt.subplots(figsize=(5, 4))
ax.bar(companies, profits, color="tab:red", width=0.4, label="Profits")
ax.set_xlabel("Company")
ax.set_ylabel("Profits")
ax.set_title("Company Vs Profits")
ax.legend(shadow=True, fontsize="small", loc="best")
plt.savefig("barg2.png")
# plt.show()
