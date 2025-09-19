# import numpy as np

# 1.  Load students.csv and calculate:

# data = np.genfromtxt("students.csv", delimiter=",", skip_header=1)
# marks = data[:, 1]   

# avg_marks = np.nanmean(marks)
# highest = np.nanmax(marks)
# lowest = np.nanmin(marks)

# # print(avg_marks)
# print(highest)
# print(lowest)

# marks_zero = np.nan_to_num(marks, nan=0)
# avg_zero = np.mean(marks_zero)

# mean_val = np.nanmean(marks)
# marks_mean = np.where(np.isnan(marks), mean_val, marks)
# avg_mean = np.mean(marks_mean)

# print(avg_zero)
# print(avg_mean)




# 2. Load sales.csv and calculate total sales (Quantity × Price).

# data = np.genfromtxt("sales.csv", delimiter=",", skip_header=1, dtype=float, usecols=(2,3))

# price = data[:, 0]

# quantity = data[:, 1]

# total_sales = np.sum(price * quantity)

# print("Total Sales:", total_sales)


# 3. Extract only the second column of a CSV and find its mean and standard deviation.
#  col2 = np.genfromtxt("students.csv", delimiter=",", skip_header=1, usecols=1)

# mean_val = np.mean(col2)
# std_val = np.std(col2)
# print("Mean of 2nd column:", mean_val)
# print("Standard Deviation of 2nd column:", std_val)


# 3. Save a new CSV file containing product, quantity, price, and total sales. 
# sales.csv Product,Quantity,Price A,2,100 B,5,200 C,3,150 D,4,

# products = np.array(["A", "B", "C", "D"])
# quantity = np.array([2, 5, 3, 4])
# price = np.array([100, 200, 150, np.nan])   
# price = np.nan_to_num(price, nan=0)

# total_sales = quantity * price

# output = np.column_stack((products, quantity, price, total_sales))

# header = "Product,Quantity,Price,TotalSales"
# np.savetxt("sales_with_totals.csv", output, delimiter=",", fmt="%s", header=header, comments="")

# print("✅ New CSV file 'sales_with_totals.csv' created successfully!")