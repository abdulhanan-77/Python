# Sets: Unordered, Mutable, No Duplicates

# Creating a set with unique integers
unique_numbers = {1, 2, 3, 4, 5}
print("Unique numbers set:", unique_numbers)

# Creating a set with duplicate elements; duplicates are automatically removed
duplicate_numbers = {1, 2, 3, 3, 4, 5, 3, 4, 5, 6}
print("Set with duplicates removed:", duplicate_numbers)

# Creating a set from a list
list_to_set = set([1, 2, 3, 4, 5])
print("Set created from list:", list_to_set)

# Creating a set from a string; notice the unordered and unique characters
string_set = set("Hello, World!")
print("Set created from string:", string_set)

# Demonstrating an empty dictionary, which is not a set
empty_dict = {}
print("Type of empty_dict:", type(empty_dict))

# Creating an empty set correctly
empty_set = set()
print("Type of empty_set:", type(empty_set))

# Add elements to a set
duplicate_numbers.add(7)
duplicate_numbers.add(8)
print("After adding elements to set:", duplicate_numbers)

# Removing elements from a set using remove() and discard()
duplicate_numbers.remove(4)  # Raises KeyError if not found
duplicate_numbers.discard(3)  # Does not raise an error if not found
print("After removing elements:", duplicate_numbers)

# Removing and returning an arbitrary element from the set using pop()
popped_element = duplicate_numbers.pop()
print("Popped element:", popped_element)
print("Set after pop():", duplicate_numbers)

# Clearing all elements from the set
duplicate_numbers.clear()
print("Set after clear():", duplicate_numbers)

# Iterating through a set
for element in list_to_set:
    print("Element in list_to_set:", element)

# Checking membership in a set
if 1 in list_to_set:
    print("1 is in list_to_set")

# Set operations: Union, Intersection, Difference, Symmetric Difference

# Define three sets: odds, evens, and primes
odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

# Union: Combines all elements from both sets
union_set = odds.union(evens)
print("Union of odds and evens:", union_set)

# Intersection: Elements common to both sets
intersection_set = odds.intersection(primes)
print("Intersection of odds and primes:", intersection_set)

# Define two more sets for further operations
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}
setC = {7, 8}

# Difference: Elements in setA but not in setB
difference_set = setA.difference(setB)
print("Difference of setA and setB:", difference_set)

# Symmetric Difference: Elements in either setA or setB but not in both
symmetric_difference_set = setB.symmetric_difference(setA)
print("Symmetric difference between setA and setB:", symmetric_difference_set)

# Update setA by adding elements from setB
setA.update(setB)
print("setA after update with setB:", setA)

# Update setA to keep only elements that are also in setB
setA.intersection_update(setB)
print("setA after intersection_update with setB:", setA)

# Update setA to remove elements found in setC
setA.difference_update(setC)
print("setA after difference_update with setC:", setA)

# Update setA to keep only elements not found in setC (symmetric difference)
setA.symmetric_difference_update(setC)
print("setA after symmetric_difference_update with setC:", setA)

# Subset and Superset checks

# Check if setA is a subset of setB
is_subset = setA.issubset(setB)
print("Is setA a subset of setB?", is_subset)

# Check if setB is a subset of setA
is_subset = setB.issubset(setA)
print("Is setB a subset of setA?", is_subset)

# Check if setA is a superset of setB
is_superset = setA.issuperset(setB)
print("Is setA a superset of setB?", is_superset)

# Check if setB is a superset of setA
is_superset = setB.issuperset(setA)
print("Is setB a superset of setA?", is_superset)

# Check if setA and setB are disjoint (no common elements)
is_disjoint = setA.isdisjoint(setB)
print("Are setA and setB disjoint?", is_disjoint)

# Check if setA and setC are disjoint
is_disjoint = setA.isdisjoint(setC)
print("Are setA and setC disjoint?", is_disjoint)

# Copying sets

# Copy by reference (shallow copy)
setD = {1, 3, 5, 6, 8, 0, 2}
setD_copy_ref = setD
print("Shallow copy (reference) of setD:", setD_copy_ref)

# Modifying the copy also affects the original set
setD_copy_ref.add(11)
print("Modified shallow copy:", setD_copy_ref)
print("Original set after modification via reference:", setD)

# Deep copy using the set() constructor
setD_copy_deep = set(setD)
setD_copy_deep.add(17)
print("Deep copy with added element:", setD_copy_deep)
print("Original set after deep copy:", setD)

# Immutable Sets: Frozenset

# Creating a frozenset (immutable set)
immutable_set = frozenset([1, 2, 3, 4])
print("Immutable frozenset:", immutable_set)

# Attempting to add an element to a frozenset will raise an AttributeError
# immutable_set.add(2)  # This line would raise an error if uncommented

# Explanation of Key Concepts:

# No Duplicates:
# Sets automatically remove duplicate elements. Each element in a set is unique.

# Unordered:
# Sets do not maintain any particular order of elements. As a result, elements are stored in an arbitrary order.

# Mutable:
# Sets are mutable, meaning you can add, remove, or update elements after the set has been created.

# Set Operations:
# Union: Combines elements from multiple sets.
# Intersection: Finds common elements between sets.
# Difference: Finds elements in one set but not in another.
# Symmetric Difference: Finds elements in either of the sets but not in both.

# Subset and Superset:
# A set A is a subset of set B if all elements of A are also in B.
# A set A is a superset of set B if all elements of B are also in A.

# Disjoint Sets:
# Two sets are disjoint if they have no elements in common.

# Copying Sets:
# Sets can be copied by reference (shallow copy) or by creating a new set (deep copy).

# Frozenset:
# A frozenset is an immutable version of a set. Once created, you cannot modify it by adding or removing elements.