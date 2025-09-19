import numpy as np

data = np.loadtxt("numbers.csv", delimiter=",", skiprows=1, )  # skip header
print("Data:\n", data)
print("Shape:", data.shape)



# data = np.genfromtxt("students.csv", delimiter=",", skip_header=1, filling_values=0)
# print("Data:\n", data)



data = np.genfromtxt("students.csv", delimiter=",", skip_header=1)

marks = data[:,2]  # third column
print(marks)
mean_marks = np.nanmean(marks)
print(mean_marks)
marks = np.nan_to_num(marks, nan=mean_marks)

print("Marks after handling NaN:", marks)
print(np.sort(marks))
print("Top 2 Marks:", np.sort(marks)[-2:])



arr = np.array([[1, 90], [2, 85], [3, 95]])
np.savetxt("output.csv", arr, delimiter=",", fmt="%d", header="ID,Marks", comments='')
print("Data saved to output.csv")




