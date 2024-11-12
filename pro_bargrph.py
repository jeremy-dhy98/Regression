import matplotlib.pyplot as plt
# import numpy as np

companies = ["GOOGLE", "MCSF", "AMZ", "FB"]
revenues = [700, 450, 550, 646]

fig , ax = plt.subplots(figsize=(5, 4))
ax.bar(companies, revenues, label="Revenue", color="tab:grey", width=0.4)
ax.set_xlabel("Company")
ax.set_ylabel("Revenue")
ax.set_title("Company Vs Revenue")
ax.legend(loc="best", fontsize="large", shadow=True)
# ax.axis((0, 5, 0, 900))
plt.savefig("bargraph.png")
# plt.show()