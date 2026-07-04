import numpy as np

arr = np.array([
    [10,20,30,40],
    [50,60,70,80],
    [90,100,110,120]
])

print("Original Array")
print(arr)

print("\nElement (1,2):")
print(arr[1,2])

print("\nLast Element:")
print(arr[-1,-1])

print("\nFirst Row:")
print(arr[0])

print("\nSecond Column:")
print(arr[:,1])

print("\nFirst Two Rows:")
print(arr[0:2])

print("\nFirst Two Columns:")
print(arr[:,0:2])

print("\nSub Array:")
print(arr[1:3,1:3])

a = np.array([10,20,30,40,50,60])

print("\nEvery Second Element:")
print(a[::2])

print("\nReverse:")
print(a[::-1])

arr[0,0] = 999

print("\nModified Array:")
print(arr)