# Itertools: product, permutations, combinations, accumulate, groupby, and infinite iterators

from itertools import product

# product: Cartesian product of input iterables
a = [1, 2]
b = [3, 4]
prod = product(a, b)  # Cartesian product of lists a and b
print("Product:", list(prod))

from itertools import permutations

# permutations: Returns all possible orderings of an input iterable
a = [1, 2, 3]
perm = permutations(a)  # All possible permutations of list a
print("Permutations:", list(perm))

from itertools import combinations, combinations_with_replacement

# combinations: Returns all possible combinations of the elements in an iterable
a = [1, 2, 3, 4]
comb = combinations(a, 2)  # Combinations of length 2
print("Combinations:", list(comb))

# combinations_with_replacement: Combinations with repeated elements
comb_wr = combinations_with_replacement(a, 2)  # Combinations of length 2 with replacement
print("Combinations with replacement:", list(comb_wr))

from itertools import accumulate
import operator

# accumulate: Returns accumulated sums, or the accumulated result of a binary function (e.g., multiplication)
a = [1, 2, 3, 4, 5]
acc = accumulate(a)  # Default is sum accumulation
print("Accumulate (sum):", list(acc))

# Using operator.mul for multiplication accumulation
acc1 = accumulate(a, func=operator.mul)
print("Original list:", a)
print("Accumulate (multiplication):", list(acc1))

a1 = [1, 2, 6, 3, 9, 0]
acc2 = accumulate(a1, func=max)  # Accumulating maximum values
print("Accumulate (max):", list(acc2))

from itertools import groupby

# groupby: Groups elements of an iterable based on a specified key function
persons = [{'name': 'Tim', 'age': 25},
           {'name': 'Dan', 'age': 25},
           {'name': 'Lisa', 'age': 27},
           {'name': 'Claire', 'age': 28}]

group_obj1 = groupby(persons, key=lambda x: x['age'])
print("Grouping by age:")
for key, value in group_obj1:
    print(f"Age {key}:", list(value))

# Grouping numbers based on whether they are smaller than 3
a = [1, 2, 3, 4]
group_obj = groupby(a, key=lambda x: x < 3)
print("Grouping numbers by < 3:")
for key, value in group_obj:
    print(key, list(value))

from itertools import count, cycle, repeat

# count: Infinite iterator that returns evenly spaced values starting with a specified number
print("Count from 10 to 20:")
for i in count(10):
    print(i)
    if i == 20:
        break  # Breaking the infinite loop

# cycle: Infinite iterator that returns elements from the iterable and repeats indefinitely
a = [1, 2, 3]
print("Cycling through list [1, 2, 3]:")
for i in cycle(a):
    print(i)
    if i == 3:
        break  # Breaking the cycle after one complete round

# repeat: Repeats the object for a specified number of times (or infinitely if no number is given)
print("Repeat number 1 ten times:")
for i in repeat(1, 10):
    print(i)

# Explanation of Key Concepts:

# product:
# product() computes the Cartesian product of input iterables, returning all possible pairs of elements from the input iterables.

# permutations:
# permutations() returns all possible orderings of an input iterable. If the input is [1, 2, 3], it returns all possible sequences containing those elements.

# combinations:
# combinations() returns all possible combinations of the elements in the iterable, without regard to order. combinations_with_replacement() allows elements to be repeated.

# accumulate:
# accumulate() returns accumulated sums (or results of another binary function) of elements in an iterable. It’s useful for cumulative calculations.

# groupby:
# groupby() groups elements of an iterable based on a key function. It’s often used for sorting and grouping elements in data analysis.

# count, cycle, repeat (Infinite Iterators):
# count() generates an infinite sequence of numbers starting from a specified number.
# cycle() infinitely iterates over an iterable, repeating the elements indefinitely.
# repeat() repeats an object for a specified number of times, useful for generating constant sequences.


