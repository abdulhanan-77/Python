# Lists: Ordered, Mutable, Allows Duplicate Elements

# Initialize a list with fruits
fruits = ["banana", "cherry", "apple"]
print("Original fruits list:", fruits)

# Create an empty list using the list() constructor
empty_list = list()
print("Empty list:", empty_list)

# List with mixed data types, including duplicate elements
mixed_list = [5, True, "apple", "apple"]
print("Mixed list with duplicates:", mixed_list)

# Access the first and last items in the fruits list
first_item = fruits[0]
last_item = fruits[-1]
print("First item:", first_item, "| Last item:", last_item)

# Iterate through the fruits list and print each item
for fruit in fruits:
    print("Fruit in the list:", fruit)

# Check if "banana" is in the fruits list
if "banana" in fruits:
    print("Banana is in the list.")
else:
    print("Banana is not in the list.")

# Print the length of the fruits list
print("Length of fruits list:", len(fruits))

# Add a new item to the end of the fruits list
fruits.append("mangoes")
print("After appending mangoes:", fruits)

# Insert a new item at index 1
fruits.insert(1, "blueberry")
print("After inserting blueberry at index 1:", fruits)

# Remove and return the last item from the fruits list
removed_item = fruits.pop()
print("Removed last item:", removed_item)
print("List after pop:", fruits)

# Remove the first occurrence of "cherry"
fruits.remove("cherry")
print("List after removing 'cherry':", fruits)

# Clear the entire fruits list
fruits.clear()
print("Fruits list after clearing:", fruits)

# Initialize a list with fruits
fruits = ["banana", "cherry", "apple", "mangoes", "blueberry"]

# Sort the fruits list in alphabetical order
fruits.sort()
print("Fruits list after sorting:", fruits)

# Reverse the order of the sorted fruits list
fruits.reverse()
print("Fruits list after reversing:", fruits)

# Initialize a list with integers
numbers = [1, 5, 2, -3]

# Reverse the order of the numbers list
numbers.reverse()
print("Numbers list after reversing:", numbers)

# Sort the numbers list in ascending order
numbers.sort()
print("Numbers list after sorting:", numbers)

# Sort the numbers list in descending order
numbers.sort(reverse=True)
print("Numbers list after sorting in descending order:", numbers)

# Create a sorted copy of the numbers list without modifying the original
sorted_numbers = sorted(numbers)
print("Original numbers list:", numbers)
print("Sorted copy of numbers list:", sorted_numbers)

# Create a list with five zeroes
zeros_list = [0] * 5
print("List of five zeros:", zeros_list)

# Concatenate zeros_list with another list of integers
combined_list = zeros_list + numbers
print("Concatenated list:", combined_list)

# Demonstrate list slicing
sliced_list_a = combined_list[1:5]
sliced_list_b = combined_list[:5]
sliced_list_c = combined_list[1:]
print("Slice from index 1 to 4:", sliced_list_a)
print("Slice from start to index 4:", sliced_list_b)
print("Slice from index 1 to end:", sliced_list_c)

# Slice with a step of 2
step_sliced_list = combined_list[::2]
print("List sliced with step of 2:", step_sliced_list)

# Copy a list by reference
referenced_list = fruits
print("Referenced list:", referenced_list)

# Modifying referenced_list will also modify fruits
referenced_list.append("lemon")
print("Referenced list after appending lemon:", referenced_list)
print("Original fruits list after modification:", fruits)

# Copy a list using the copy() method
copied_list_1 = fruits.copy()
copied_list_1.append("blueberry")
print("Original fruits list after copying:", fruits)
print("Copied list 1 after appending blueberry:", copied_list_1)

# Copy a list using the list() constructor
copied_list_2 = list(fruits)
copied_list_2.append("pineapple")
print("Copied list 2 after appending pineapple:", copied_list_2)
print("Original fruits list after copying:", fruits)

# Copy a list using slicing
copied_list_3 = fruits[:]
copied_list_3.append("mangoes")
print("Copied list 3 after appending mangoes:", copied_list_3)
print("Original fruits list after copying:", fruits)

# List comprehension to create a new list of squares
original_numbers = [1, 2, 3, 4, 5]
squared_numbers = [num * num for num in original_numbers]
print("Original numbers list:", original_numbers)
print("Squared numbers list:", squared_numbers)
