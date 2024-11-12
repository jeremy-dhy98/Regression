import matplotlib.pyplot as plt
import  numpy as np

# Plot confusion matrix or rep data that that depends on 2 independent vars
# Need 2 arrays af categorical data and a 2D array to rep the data to color code
vegetables = ["cucumber", "tomato", "lettuce", "asparagus", "potato", "wheat", "barley"]
farmers = ["Farmer Joe", "Upland Bros", "Jeremy Gardening", "Isaac greens", "Organiculture",\
           "BioGoods Ltd", "Cornylee Corp"]
harvest = np.array([[0.8, 2.4, 2.5, 3.9, 0.0, 4.0, 0.0],\
                    [2.4, 0.0, 4.0, 1.0, 2.7, 0.0, 0.0],\
                    [1.1, 2.4, 0.8, 4.3, 1.9, 4.4, 0.0],\
                    [0.6, 0.0, 0.3, 0.0, 3.1, 0.0, 0.0],\
                    [0.7, 1.7, 0.6, 2.6, 2.2, 6.2, 0.0],\
                    [1.3, 1.2, 0.0, 0.0, 0.0, 3.2, 5.1],\
                    [0.1, 2.0, 0.0, 1.4, 0.0, 1.9, 6.3]])
fig, ax = plt.subplots(figsize=(5, 5))
ax.imshow(harvest)

#  Show ticks and label them with respective list entries
ax.set_xticks(np.arange(len(farmers)), labels=farmers)
ax.set_yticks(np.arange(len(vegetables)), labels=vegetables)

# Rotate the ticklabels and set their alighnment
plt.setp(ax.get_xticklabels(), rotation=45, ha="right",\
         rotation_mode="anchor")

# Loop over data dimensions and create text annotations
for i in range(len(vegetables)):
    for j in range(len(farmers)):
        text = ax.text(j, i, harvest[i, j], ha="center", va="center", color="w")

ax.set_title("Harvest af local farmers(tons/year)")
fig.tight_layout()
plt.savefig("annotation_heatmap.png")
plt.show()