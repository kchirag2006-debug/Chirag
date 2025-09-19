# Lecture 3 -- Working with CSV Files in NumPy

##  Learning Objectives

- Learn how to read CSV files into NumPy arrays. 
- Understand the difference between `loadtxt` and `genfromtxt`. 
- Handle missing values (`NaN`) in CSV data.  
- Extract rows and columns from CSV data. 
- Perform analysis (mean, min, max, sum) on CSV columns. 
- Learn how to save NumPy arrays back into CSV files.

------------------------------------------------------------------------

##  1. Introduction to CSV Files

CSV (Comma Separated Values) = Common format for datasets.

Each row = record (like a student, a transaction, etc.).

Each column = field (like Name, Age, Marks).

Example: `students.csv`

    Name,Age,Marks
    A,18,75
    B,19,82
    C,20,
    D,18,65

------------------------------------------------------------------------

##  2. Reading CSV with `np.loadtxt`

Use when data is purely numeric (no missing values, no text).

**Example:**

``` python
import numpy as np

data = np.loadtxt("numbers.csv", delimiter=",", skiprows=1)  # skip header
print("Data:\n", data)
print("Shape:", data.shape)
```

If `numbers.csv` is:

    ID,Value
    1,10
    2,20
    3,30
    4,40

 **Output:**

    Data:
     [[ 1. 10.]
      [ 2. 20.]
      [ 3. 30.]
      [ 4. 40.]]
    Shape: (4, 2)

------------------------------------------------------------------------

##  3. Reading CSV with `np.genfromtxt`

More flexible → can handle missing values.

Supports filling missing values with default.

**Example:**

``` python
data = np.genfromtxt("students.csv", delimiter=",", skip_header=1)
print("Data:\n", data)
```

 **Output:**

    [[18. 75.]
     [19. 82.]
     [20. nan]
     [18. 65.]]

Notice → Missing marks became `nan`.

------------------------------------------------------------------------

##  4. Handling Missing Values

**Replace NaN with 0**

``` python
data = np.genfromtxt("students.csv", delimiter=",", skip_header=1, filling_values=0)
print("Data with NaN filled as 0:\n", data)
```

**Replace NaN with Column Mean**

``` python
data = np.genfromtxt("students.csv", delimiter=",", skip_header=1)

marks = data[:,1]  # second column
mean_marks = np.nanmean(marks)
marks = np.nan_to_num(marks, nan=mean_marks)

print("Marks after handling NaN:", marks)
```

------------------------------------------------------------------------

##  5. Selecting Rows and Columns

``` python
data = np.genfromtxt("students.csv", delimiter=",", skip_header=1)

ages = data[:,0]   # first column
marks = data[:,1]  # second column

print("Ages:", ages)
print("Marks:", marks)
print("Average Marks:", np.nanmean(marks))
print("Top 2 Marks:", np.sort(marks)[-2:])
```

------------------------------------------------------------------------

##  6. Saving Arrays to CSV

Use `np.savetxt()`

**Example:**

``` python
arr = np.array([[1, 90], [2, 85], [3, 95]])
np.savetxt("output.csv", arr, delimiter=",", fmt="%d", header="ID,Marks", comments='')
print("Data saved to output.csv")
```

 **Output CSV:**

    ID,Marks
    1,90
    2,85
    3,95

------------------------------------------------------------------------

##  7. Real-World Example -- Sales Dataset

`sales.csv`

    Product,Quantity,Price
    A,2,100
    B,5,200
    C,3,150
    D,4,

**Example Code:**

``` python
sales = np.genfromtxt("sales.csv", delimiter=",", skip_header=1)

quantity = sales[:,1]
price = sales[:,2]

# Handle NaN in price
mean_price = np.nanmean(price)
price = np.nan_to_num(price, nan=mean_price)

# Total sales for each row
total_sales = quantity * price
print("Total Sales per product:", total_sales)

# Overall total
print("Grand Total Sales:", np.sum(total_sales))
```

------------------------------------------------------------------------

##  Practice Set -- Day 3

1.  Load `students.csv` and calculate:

    -   Average marks
    -   Highest marks
    -   Lowest marks
    -   Replace missing values in marks with `0` and with mean. Compare
        results.

2.  Load `sales.csv` and calculate total sales (`Quantity × Price`).

3.  Extract only the second column of a CSV and find its mean and
    standard deviation.

4.  Save a new CSV file containing product, quantity, price, and total
    sales.

    `sales.csv`
    Product,Quantity,Price
    A,2,100
    B,5,200
    C,3,150
    D,4,

------------------------------------------------------------------------

##  Summary

1. Load real CSV datasets into NumPy. 
2. Clean missing values. 
3. Perform basic analysis
4. directly from CSV files. 
5. Save processed results back to CSV.
