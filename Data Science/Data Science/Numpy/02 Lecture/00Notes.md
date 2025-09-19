# Lecture 2 – NumPy for Data Analysis

##  Learning Objectives
-  Handle missing values (NaN) in NumPy arrays.
-  Perform descriptive statistics (mean, median, std, var, percentile).
-  Apply conditional filtering with np.where.
-  Sort data and find unique values.
-  Normalize datasets using broadcasting.
-  Work with real-world CSV datasets in NumPy.

---

##  1. Handling Missing Data in NumPy

Sometimes datasets contain missing values (NaN). NumPy provides functions to handle them.

**Functions:**
- `np.nan` → Represents missing values.
- `np.isnan(arr)` → Checks if elements are NaN.
- `np.nanmean(arr)` → Calculates mean while ignoring NaN.
- `np.nan_to_num(arr)` → Replace NaN with 0 or a chosen value.

**Example:**
```python
import numpy as np

data = np.array([10, 20, np.nan, 40, 50])
print("Original:", data)

# Check missing values
print("Is NaN:", np.isnan(data))

# Replace NaN with 0
print("NaN to 0:", np.nan_to_num(data))

# Replace NaN with mean
mean_val = np.nanmean(data)
data[np.isnan(data)] = mean_val
print("NaN replaced with mean:", data)
```

---

##  2. Descriptive Statistics

NumPy can calculate summary statistics directly.

**Functions:**
- `np.mean(arr)` → Average
- `np.median(arr)` → Median
- `np.std(arr)` → Standard Deviation
- `np.var(arr)` → Variance
- `np.percentile(arr, 90)` → 90th percentile

**Example:**
```python
scores = np.array([45, 60, 72, 88, 53, 95, 70])
print("Mean:", np.mean(scores))
print("Median:", np.median(scores))
print("Std Dev:", np.std(scores))
print("Variance:", np.var(scores))
print("90th Percentile:", np.percentile(scores, 90))
```

---

##  3. Conditional Filtering with np.where

`np.where` is useful to apply conditions to arrays.

**Example: Pass/Fail classification**
```python
marks = np.array([35, 78, 62, 90, 49])
result = np.where(marks >= 40, "Pass", "Fail")
print(result)
```

---

##  4. Sorting & Unique Values

**Functions:**
- `np.sort(arr)` → Sorts array
- `np.argsort(arr)` → Returns sorted indices
- `np.unique(arr)` → Finds unique values

**Example:**
```python
arr = np.array([5, 2, 7, 2, 8, 5, 9])
print("Sorted:", np.sort(arr))
print("Indices of sorted:", np.argsort(arr))
print("Unique values:", np.unique(arr))
```

---

##  5. Broadcasting for Normalization

Data needs to be scaled (normalized) before analysis.

**Formula:**
```
X_norm = (X - X_min) / (X_max - X_min)
```

**Example:**
```python
data = np.array([10, 20, 30, 40, 50])
norm_data = (data - data.min()) / (data.max() - data.min())
print("Normalized:", norm_data)
```

---

##  6. Real Dataset Example (CSV)

**Example: Load CSV data**
```python
# CSV Example: students.csv
# Name, Age, Marks
# A, 18, 75
# B, 19, 82
# C, 20, NaN
# D, 18, 65

data = np.genfromtxt("students.csv", delimiter=",", skip_header=1, usecols=(1,2))
print("Data:\n", data)

# Handle NaN in Marks
marks = data[:,1]
mean_marks = np.nanmean(marks)
marks = np.nan_to_num(marks, nan=mean_marks)

print("Marks after handling NaN:", marks)

# Stats
print("Average Marks:", np.mean(marks))
print("Top 3 Marks:", np.sort(marks)[-3:])
```

---

##  Practice Set – Day 2

1. Create an array with NaN values and replace them with the column mean.
2. Given student marks `[45, 67, 89, 34, 56, 78, 90]`, calculate mean, median, std, and 75th percentile.
3. Generate 50 random ages between 18–30 and find unique ages.
4. Normalize the dataset `[100, 200, 300, 400, 500]` using broadcasting.
      