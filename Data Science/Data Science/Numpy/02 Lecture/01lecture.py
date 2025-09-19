import numpy as np

# data = np.array([10, 20, np.nan, 40, 50])
# print("Original:", data)

# # Check missing values
# print("Is NaN:", np.isnan(data))

# # Replace NaN with 0
# print("NaN to 0:", np.nan_to_num(data))

# # Replace NaN with mean
# mean_val = np.nanmean(data)
# data[np.isnan(data)] = mean_val
# print("NaN replaced with mean:", data)



scores = np.array([45, 60, 72, 88, 53, 95, 70])
# print(scores)
# print("Mean:", np.mean(scores))
print("Median:", np.median(scores))
# print("Std Dev:", np.std(scores))
# print("Variance:", np.var(scores))
print("90th Percentile:", np.percentile(scores, 90))
print("50th Percentile:", np.percentile(scores, 50))
print("100th Percentile:", np.percentile(scores, 100))


# print(np.sqrt(280))




# 45 - 69 = -24   = 576
# 60 - 69 = -9    = 81
# 72 - 69 = 3     = 9
# 88 - 69 = 19    = 361
# 53 - 69 = -16   = 256
# 70 - 69 = 1     = 1
# 95 - 69 = 26    = 676   => 1960 / 7 = 280 = 16.733



# marks = np.array([35, 78, 62, 30, 49])
# result = np.where(marks >= 40, "Pass", "Fail")
# print(result)



# arr = np.array([5, 2, 7, 2, 8, 5, 9])
            #   0  1  2  3  4  5  6
            #   1  3  0  5  2  4  6

            # 2 2 5 5 7 8 9


# print("Sorted:", np.sort(arr))
# print("Indices of sorted:", np.argsort(arr))
# print("Unique values:", np.unique(arr))



# data = np.array([10, 20, 30, 40, 50])
# norm_data = (data - data.min()) / (data.max() - data.min())
# print("Normalized:", norm_data)

# min = 10
# max = 50


# 10 = 10 - 10 / 50 - 10 => 0
# 20 = 20 - 10 / 50 - 10 => 0.25
# 30 = 30 - 10 / 50 - 10 => 0.5
# 40 = 40 - 10 / 50 - 10 => 0.75
# 50 = 50 - 10 / 50 - 10 => 1