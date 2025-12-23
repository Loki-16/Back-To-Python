# import math
# print(math.sqrt(144))
# print(math.pi)
# print(math.factorial(5))

# from math import sqrt
# print(sqrt(225))
# from math import pi, sin
# print(f"{pi}\n{sin(pi/2)}")
# import math as m
# print(m.cos(0))
# print(m.tan(1))

# import mymath as mm
# print(mm.square(5))
# print(mm.cube(3))
# print(mm.add(3,3))

# write a file notes.txt
# with open("notes.txt","w") as file:
#     file.write("Python is fun\n")
#     file.write("I am learning file handling\n")
#     file.write("Day 5 practice\n")

#  Read a file notes.txt
# with open("notes.txt","r") as file:
#     data = file.read()
#     print(data)

#  Appending to an existing file without deleting its contents
# with open("notes.txt","a") as file:
#     file.write("Thin line was appended")

# Reading line by line
# with open("notes.txt","r") as file:
#     line_number = 0
#     for line in file:
#         line_number += 1
#         print(f'Line {line_number}: {line.strip("\n")}')

# # Numpy
# import numpy as np
# arr_1d = np.array([1,2,3,4,5])
# arr_2d = np.array([[1,2,3],[4,5,6]])
# print(arr_1d)
# print(type(arr_1d))
# print(arr_1d.shape)
# print(arr_2d)
# print(type(arr_2d))
# print(arr_2d.shape)

# arr = np.array([1,2,3,4,5])
# print(arr + 10)
# print(arr * 2)
# print(arr ** 2)

# arr = np.array([10,20,30,40,50])
# print(arr[0])
# print(arr[-1])
# print(arr[1:4])
# arr[2] = 300
# print(arr)


# arr = np.array([1,2,3,4,5,6])
# arr = arr.reshape(2,3)
# print(arr)
# print(arr.shape)
# print(np.sum(arr))
# print(np.mean(arr))
# print(np.max(arr))
# print(np.min(arr))