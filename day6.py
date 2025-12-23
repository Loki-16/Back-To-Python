# # Task 1.1
# import numpy as np
# arr1 = np.array([5,10,15,20])
# arr2 = np.array([0,0,0,0,0,0]) # for faster creation of zero array np.zeros(6)
# arr3 = np.array([[1,1,1],[1,1,1]]) # for faster creation of ones 2d array np.ones((2,3)) 
# print(arr1)
# print(arr1.dtype)
# print(arr2)
# print(arr2.dtype)
# print(arr3)
# print(arr3.dtype)

# # Task 1.2
# arr4 = np.array([1,2,3,4,5,6])
# arr5 = np.array([1,1.2,3.4,6,7.8])
# print(arr4)
# print(arr4.dtype)
# print(arr5)
# print(arr5.dtype)

# # Task 1.3
# arr6 = np.arange(0,10)
# arr7 = np.linspace(0,1,5)
# print(arr6)
# print(arr7)

# # Task 2.1
# import numpy as np
# arr = np.array([10,20,30,40,50,60])
# print(arr[0])
# print(arr[-1])
# print(arr[1:4])
# print(arr[::2])

# # Task 2.2
# import numpy as np
# arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(arr[1,1])
# print(arr[0,:])
# print(arr[:,1])
# print(arr[0:2,1:3])

# # Task 2.3
# arr[2,2] = 99
# arr[0,:] = 0
# print(arr)

# Task 3.1
import numpy as np
arr = np.arange(1,7)
print(arr)
print(arr.shape)

# Task 3.2
arr = arr.reshape(2,3)   # .reshape() in itself is a copy not view
print(arr)
print(arr.shape)

# Task 3.3
arr = arr.reshape(2,-1)
print(arr)
print(arr.shape)

# Task 3.4
arr = arr.reshape(-1,1)
print(arr)
print(arr.shape)