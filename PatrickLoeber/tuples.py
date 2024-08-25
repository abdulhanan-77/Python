# Tuples: Ordered, Immutable, Allows Duplicate Elements

# Creating a tuple without parentheses (tuple packing)
person_info = "Max", 28, "Boston"
print("Tuple with multiple elements:", person_info)

# Creating a string, not a tuple (missing comma)
single_element_string = ("Max")
print("Type when creating a tuple without a comma:", type(single_element_string))

# Creating a single-element tuple (note the comma)
single_element_tuple = ("Max",)
print("Type when creating a single-element tuple:", type(single_element_tuple))

# Creating a tuple using the tuple() constructor
constructed_tuple = tuple(["Max", 28, "Boston"])
print("Tuple created using tuple() constructor:", constructed_tuple)

# Accessing tuple elements by index
first_item = constructed_tuple[0]
print("First item in the tuple:", first_item)

# Iterating through a tuple
for item in constructed_tuple:
    print("Item in the tuple:", item)

# Checking if an item exists in the tuple
if "Max" in constructed_tuple:
    print("Max is in the tuple.")
else:
    print("Max is not in the tuple.")

# Tuple with duplicate elements
fruit_tuple = ('a', 'p', 'p', 'l', 'e')
print("Length of fruit_tuple:", len(fruit_tuple))

# Counting occurrences of an element in the tuple
print("Count of 'p' in fruit_tuple:", fruit_tuple.count('p'))

# Finding the index of the first occurrence of an element
print("Index of first 'p' in fruit_tuple:", fruit_tuple.index('p'))

# Converting a tuple to a list (Mutable Conversion)
fruit_list = list(fruit_tuple)
print("Converted to list:", fruit_list)

# Converting a list back to a tuple
converted_tuple = tuple(fruit_list)
print("Converted back to tuple:", converted_tuple)

# Tuple Slicing: Extracting portions of a tuple
numeric_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)

# Slicing from index 2 to 4
slice_b = numeric_tuple[2:5]
# Reversing the tuple
reversed_tuple = numeric_tuple[::-1]
# Slicing with a step of 3
step_slice = numeric_tuple[0::3]
print("Slice from index 2 to 4:", slice_b)
print("Reversed tuple:", reversed_tuple)
print("Tuple sliced with step of 3:", step_slice)

# Tuple Unpacking: Assigning tuple elements to variables
unpacked_tuple = "Max", 28, "Boston"

name, age, city = unpacked_tuple
print("Unpacked name:", name)
print("Unpacked age:", age)
print("Unpacked city:", city)

# Extended Tuple Unpacking: Handling remaining elements
numeric_tuple_2 = (1, 2, 3, 4, 5, 6)
first_element, *middle_elements, last_element = numeric_tuple_2
print("First element:", first_element)
print("Last element:", last_element)
print("Middle elements:", middle_elements)

# Comparing Memory Usage between List and Tuple
import sys
sample_list = [0, 1, 2, "hello", True]
sample_tuple = (0, 1, 2, "hello", True)
print("Size of list in bytes:", sys.getsizeof(sample_list), "bytes")
print("Size of tuple in bytes:", sys.getsizeof(sample_tuple), "bytes")

# Comparing Execution Time for List and Tuple Creation
import timeit
list_creation_time = timeit.timeit(stmt="[0,1,2,3,4,5]", number=1000000)
tuple_creation_time = timeit.timeit(stmt="(0,1,2,3,4,5)", number=1000000)
print("Time to create list:", list_creation_time)
print("Time to create tuple:", tuple_creation_time)


# Explanation of Key Concepts:

# Tuple Packing and Unpacking:
# Packing refers to grouping multiple values into a tuple, like person_info = "Max", 28, "Boston".
# Unpacking allows you to assign tuple elements to individual variables, like name, age, city = person_info.

# Immutability:
# Tuples are immutable, meaning once created, their elements cannot be modified.

# Tuple Construction:
# Tuples can be created using parentheses or the tuple() constructor. A single-element tuple requires a trailing comma.

# Indexing and Slicing:
# You can access tuple elements by their index and extract slices (subsets) of tuples.

# Memory Efficiency:
# Tuples use less memory compared to lists because they are immutable.

# Performance Efficiency:
# Tuples are faster than lists in terms of creation and access because of their immutability.