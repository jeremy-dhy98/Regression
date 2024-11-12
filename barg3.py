import matplotlib.pyplot as plt
import numpy as np
from pro_bargrph import companies, revenues
from barg2 import profits

y = np.arange(len(companies))

fig,ax = plt.subplots(figsize=(5,4))
ax.barh(companies, revenues, label="Revenues", color="tab:blue", height=.4)
ax.barh(companies, profits, label="Profits", color="tab:red", height=.4)
ax.set_xlabel("Company")
ax.set_ylabel("Profits & revenues")
ax.set_title("Company Vs Profits & revenue")
ax.legend(shadow=True, fontsize="x-large", loc="best")
plt.savefig("barg_2in1_(OOstyle).png")