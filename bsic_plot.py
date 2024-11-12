import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

students = np.array(["Jeremy", "Peter", "John", "Esther"])
marks = np.array([56, 70, 68, 83])

#Continuous vs Categorical
plot = plt.plot(students, marks, color="tab:red", marker="D",\
                linestyle="dashdot", linewidth=2)
plt.xticks()
plt.xlabel("Student")
plt.ylabel("Marks/Score")
plt.title("Student Vs Score(Maths)")
plt.savefig("Student_marks.png")
# plt.show()