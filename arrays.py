import numpy as np
#arr=np.array([[1,2,3],[4,5,6]])
#print(arr.shape)
#print(arr.ndim)
#print(arr.dtype)

import numpy as np

# -----------------------------
# 1. Create a 1D Array
# -----------------------------
arr1 = np.array([10, 20, 30, 40, 50])
print("1D Array:")
print(arr1)
print()

# -----------------------------
# 2. Create a 2D Array
# -----------------------------
arr2 = np.array([[1, 2, 3],
                 [4, 5, 6]])
print("2D Array:")
print(arr2)
print()

# -----------------------------
# 3. Array of Zeros
# -----------------------------
zeros = np.zeros((2, 3))
print("Zeros Array:")
print(zeros)
print()

# -----------------------------
# 4. Array of Ones
# -----------------------------
ones = np.ones((2, 3))
print("Ones Array:")
print(ones)
print()

# -----------------------------
# 5. Identity Matrix
# -----------------------------
identity = np.eye(3)
print("Identity Matrix:")
print(identity)
print()

# -----------------------------
# 6. arange()
# -----------------------------
numbers = np.arange(1, 11)
print("Using arange():")
print(numbers)
print()

# -----------------------------
# 7. linspace()
# -----------------------------
line = np.linspace(0, 10, 6)
print("Using linspace():")
print(line)
print()

# -----------------------------
# 8. Random Float Numbers
# -----------------------------
random_float = np.random.rand(2, 3)
print("Random Float Array:")
print(random_float)
print()

# -----------------------------
# 9. Random Integers
# -----------------------------
random_int = np.random.randint(1, 100, (2, 3))
print("Random Integer Array:")
print(random_int)
print()

# -----------------------------
# 10. Empty Array
# -----------------------------
empty = np.empty((2, 2))
print("Empty Array:")
print(empty)
print()

# -----------------------------
# 11. Full Array
# -----------------------------
full = np.full((2, 3), 7)
print("Full Array (filled with 7):")
print(full)
print()

# -----------------------------
# 12. Reshape
# -----------------------------
a = np.arange(1, 13)
reshape = a.reshape(3, 4)
print("Reshaped Array:")
print(reshape)
print()

# -----------------------------
# 13. Array Properties
# -----------------------------
print("Array Properties")
print("Shape :", reshape.shape)
print("Dimensions :", reshape.ndim)
print("Size :", reshape.size)
print("Data Type :", reshape.dtype)
