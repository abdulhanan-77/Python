import random

# 1. random.random()
# Generates a random floating-point number between 0.0 and 1.0.
a = random.random()
print(a)

# 2. random.uniform(a, b)
# Generates a random floating-point number between the given range [a, b].
b = random.uniform(1, 10)
print(b)

# 3. random.randint(a, b)
# Generates a random integer between a and b (both inclusive).
c = random.randint(1, 10)
print(c)

# 4. random.randrange(start, stop)
# Generates a random integer between start and stop-1.
d = random.randrange(1, 10)
print(d)

# 5. random.normalvariate(mu, sigma)
# Generates a random floating-point number from a normal distribution with mean (mu) and standard deviation (sigma).
e = random.normalvariate(0, 1)
print(e)

# 6. random.choice(sequence)
# Returns a random element from the non-empty sequence.
myList = list("ABDASFSFlijojl")
print(myList)
f = random.choice(myList)
print(f)

# 7. random.sample(population, k)
# Returns a list of k unique elements chosen from the population sequence.
g = random.sample(myList, 3)
print(g)

# 8. random.choices(population, k)
# Returns a list of k elements chosen from the population sequence. Elements can be repeated.
h = random.choices(myList, k=3)
print(h)

# 9. random.shuffle(x)
# Shuffles the sequence x in place.
i = random.shuffle(myList)
print(myList)

# 10. random.seed(a)
# Initializes the random number generator. Using the same seed will produce the same sequence of random numbers.
random.seed(1)
print(random.random())  # This will always print the same number for the same seed.
print(random.randint(1, 10))
random.seed(1)
print(random.random())  # Resetting the seed will produce the same sequence again.
print(random.randint(1, 10))

# 11. secrets module
# The secrets module is used for generating cryptographically strong random numbers.

import secrets

# 11a. secrets.randbelow(n)
# Returns a random integer between 0 and n-1.
a1 = secrets.randbelow(10)
print(a1)

# 11b. secrets.randbits(k)
# Returns an integer with k random bits.
a2 = secrets.randbits(8)
print(a2)

# 11c. secrets.choice(sequence)
# Returns a randomly-chosen element from the sequence.
myList2 = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
a3 = secrets.choice(myList2)
print(a3)

# 12. numpy module
# The numpy module is used for performing operations on arrays and matrices, including random number generation.

import numpy as np

# 12a. np.random.rand(d0, d1, ..., dn)
# Generates an array of shape (d0, d1, ..., dn) with random floats in the range [0, 1).
a4 = np.random.rand(3, 3)
print(a4)

# 12b. np.random.randint(low, high=None, size=None)
# Generates an array of random integers from low (inclusive) to high (exclusive).
a5 = np.random.randint(1, 10, size=(3, 3))
print(a5)

# 12c. np.random.shuffle(x)
# Shuffles the contents of a multi-dimensional array along the first axis.
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr)
np.random.shuffle(arr)  # Shuffles the array rows in place.
print(arr)

# 12d. np.random.seed(seed)
# Sets the random seed for numpy's random number generator.
np.random.seed(1)
print(np.random.rand(3, 3))
np.random.seed(1)
print(np.random.rand(3, 3))  # Resetting the seed produces the same sequence.
np.random.seed(2)
print(np.random.rand(3, 3))
np.random.seed(2)
print(np.random.rand(3, 3))  # Resetting the seed produces the same sequence.

# Explanation of Random Number Generation:

# random Module:
    # Provides various methods for generating random numbers.
    # random.random() generates a float between 0.0 and 1.0.
    # random.uniform(a, b) generates a float between a and b.
    # random.randint(a, b) generates an integer between a and b.
    # random.randrange(start, stop) generates an integer from start to stop-1.
    # random.normalvariate(mu, sigma) generates a float based on the normal distribution with mean mu and standard deviation sigma.
    # random.choice(sequence) selects a random element from a non-empty sequence.
    # random.sample(population, k) selects k unique elements from a population.
    # random.choices(population, k) selects k elements with replacement (elements can be repeated).
    # random.shuffle(x) shuffles the elements in a sequence in place.
    # random.seed(a) sets the seed for the random number generator, allowing reproducibility.

# secrets Module:
    # Used for generating cryptographically secure random numbers.
    # secrets.randbelow(n) generates a random integer between 0 and n-1.
    # secrets.randbits(k) generates an integer with k random bits.
    # secrets.choice(sequence) selects a random element from a sequence.

# numpy Module:
    # numpy provides random number generation functions that operate on arrays.
    # np.random.rand(d0, d1, ..., dn) generates an array of random floats.
    # np.random.randint(low, high, size) generates an array of random integers.
    # np.random.shuffle(x) shuffles the contents of an array along the first axis.
    # np.random.seed(seed) sets the seed for numpy's random number generator, ensuring reproducibility.

# Key Points:
    # Random number generation is crucial in many applications, from simulations to security.
    # The random module is suitable for general-purpose random number generation.
    # The secrets module is designed for cryptographic purposes, ensuring strong randomness.
    # The numpy module is ideal for working with arrays and matrices in scientific computing.
