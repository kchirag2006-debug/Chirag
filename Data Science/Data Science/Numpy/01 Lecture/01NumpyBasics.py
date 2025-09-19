import numpy as np

print("Numpy")



# 1D Array 

arr = np.array([1, 2, 3, 4, 5 ])

print(arr)



# 2D Array 

arr2d = np.array([[1, 2, 3, 4], [5,6,7,8]])

print(arr2d)

# 3D Array 

arr3d = np.array([[1, 2, 3, 4], [5,6,7,8], [9,7,8,9]])

print(arr3d)


# Size

print(arr.size)
print(arr2d.size)
print(arr3d.size)

# shape

print(arr.shape)
print(arr2d.shape)
print(arr3d.shape)


# dtype

print(arr.dtype)
print(arr2d.dtype)
print(arr3d.dtype)



# Zeroes 


print(np.zeros((2)))
print(np.zeros((2, 4)))
print(np.zeros((3, 4)))

# ones 


print(np.ones((2)))
print(np.ones((2, 4)))
print(np.ones((3, 4)))



# sqrt 

# print(np.sqrt(arr3d))

a = [1, 4, 9, 16, 25, 36, 49, 64, 81]

print(np.sqrt(a))

# Sum 

print(np.sum(arr))

# Mean


print(np.mean(arr))


# max 

print(np.max(arr))

# random 

print(np.random.rand(3,3))
print(np.random.randint(0,10, 5))


# transpose 
print(arr)
print(np.transpose(arr))
print(arr2d)
print(np.transpose(arr2d))
print(arr3d)
print(np.transpose(arr3d))


# ravel
print(arr)
print(np.ravel(arr))
print(arr2d)
print(np.ravel(arr2d))
print(arr3d)
print(np.ravel(arr3d))