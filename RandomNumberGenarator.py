import numpy as np
rng = np.random.default_rng(seed=42)
flips = rng.integers(2, size=100000)
prob_heads=np.mean(flips)
print("EStimated prob of heads",prob_heads)

# Reproducibility
np.random.seed(42)

print("Random Float:")
print(np.random.rand(2,3))

print("\nRandom Integers:")
print(np.random.randint(1,100,(2,3)))

print("\nRandom Normal:")
print(np.random.randn(5))

print("\nRandom Choice:")
print(np.random.choice(["Red","Green","Blue"],5))

arr = np.array([1,2,3,4,5])

np.random.shuffle(arr)

print("\nShuffled Array:")
print(arr)

print("\nVectorized Operations")
a = np.array([10,20,30])

print("Addition:", a+5)
print("Multiplication:", a*2)
print("Square Root:", np.sqrt(a))
print("Sum:", np.sum(a))
print("Mean:", np.mean(a))
print("Maximum:", np.max(a))
print("Minimum:", np.min(a))