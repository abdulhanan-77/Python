# Lambda Functions: Small anonymous functions with a single expression
# Syntax: lambda arguments: expression

# Example 1: Simple lambda function that adds 10 to a given number
add10 = lambda x: x + 10
print("Add 10 to 5:", add10(5))

# Example 2: Lambda function that multiplies two numbers
mult = lambda x, y: x * y
print("Multiply 2 and 7:", mult(2, 7))

# Using lambda to sort a list of tuples by the second element (y-coordinate)
points2D = [(1, 2), (15, 1), (5, -1), (10, 4)]

# Sort by the second value in each tuple
points2D_sorted = sorted(points2D, key=lambda x: x[1])
print("Original points:", points2D)
print("Points sorted by y-coordinate:", points2D_sorted)

# Sort by the sum of both values in each tuple
points2D_sorted1 = sorted(points2D, key=lambda x: x[0] + x[1])
print("Points sorted by sum of x and y:", points2D_sorted1)

# Map Function: Applies a function to every item in an iterable (e.g., list) and returns a map object
# Syntax: map(func, seq)

a = [1, 2, 3, 4, 5]
# Doubling each element in the list
b = map(lambda x: x * 2, a)
print("Doubled values using map:", list(b))

# Equivalent using list comprehension
c = [x * 2 for x in a]
print("Doubled values using list comprehension:", c)

# Filter Function: Filters elements in an iterable based on a condition, returning only those that meet the condition
# Syntax: filter(func, seq)

# Filtering out only even numbers from the list
d = filter(lambda x: x % 2 == 0, a)
print("Even values using filter:", list(d))

# Equivalent using list comprehension
e = [x for x in a if x % 2 == 0]
print("Even values using list comprehension:", e)

# Reduce Function: Applies a rolling computation to sequential pairs of values in a list
# Syntax: reduce(func, seq)

from functools import reduce
# Multiplying all elements in the list together
f = reduce(lambda x, y: x * y, a)
print("Product of all elements using reduce:", f)

# Explanation of Concepts:

# Lambda Functions:
# Lambda functions are small, anonymous functions defined using the lambda keyword. They can have any number of arguments but only one expression, which is evaluated and returned.

# Sorting with Lambda:
# sorted() can take a lambda function as a key argument to customize the sorting behavior. For example, you can sort tuples by their second element or by the sum of their elements.

# Map Function:
# The map() function applies a given function to all items in an input list. The result is a map object, which can be converted to a list if needed.

# Filter Function:
# The filter() function filters elements from an iterable based on a function that returns either True or False. Only the elements that satisfy the condition are returned.

# Reduce Function:
# reduce() applies a rolling computation to sequential pairs in a list, such as summing or multiplying all elements together. It's useful for cumulative operations where the result of one computation is used in the next.




