import matplotlib.pyplot as plt
import  numpy as np
from barg3 import companies, revenues, profits

y = np.arange(len(companies))

plt.xticks(y, companies)
plt.ylabel("Profit&revenues")
plt.xlabel("Company")
plt.title("Company Vs Profit&revenues")
plt.barh(y-.2, revenues, color="tab:blue", height=.4, )
plt.barh(y+.2, profits, color="tab:red", height=.4, )
plt.legend(shadow=True, loc="best", fontsize="x-large")
plt.savefig("barg_2_in_1(MATLABstyle-Horz).png")
# plt.show()
