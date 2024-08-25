# Dictionaries: Key-value pairs, Unordered, Mutable

# Creating a dictionary using curly braces
person_info = {"name": "Max", "age": 28, "city": "New York"}
print("Initial dictionary:", person_info)

# Creating a dictionary using the dict() constructor
person_info2 = dict(name="Marry", age=27, city="Boston")
print("Another dictionary using dict():", person_info2)

# Accessing a value by its key
name_value = person_info2["name"]
print("Accessed name value:", name_value)

# Accessing another value by its key
age_value = person_info2["age"]
print("Accessed age value:", age_value)

# Adding a new key-value pair to the dictionary
person_info["email"] = "max@xyz.com"
print("After adding email:", person_info)

# Updating the value of an existing key
person_info["email"] = "coolmax@xyz.com"
print("After updating email:", person_info)

# Removing a key-value pair using the del keyword
del person_info["email"]
print("After deleting email:", person_info)

# Removing a key-value pair using the pop() method
person_info.pop("age")
print("After popping age:", person_info)

# Removing the last inserted key-value pair using popitem()
person_info.popitem()
print("After popitem():", person_info)

# Checking if a key exists in the dictionary
if "name" in person_info2:
    print("Name found in person_info2:", person_info2["name"])

# Accessing a value with exception handling (to avoid KeyError)
try:
    print("Accessing name in person_info2:", person_info2["name"])
except KeyError:
    print("Key not found")

# Iterating over dictionary keys
for key in person_info2:
    print("Key:", key)

# Iterating over dictionary keys explicitly using keys() method
for key in person_info2.keys():
    print("Key from keys() method:", key)

# Iterating over dictionary values using values() method
for value in person_info2.values():
    print("Value from values() method:", value)

# Iterating over both keys and values using items() method
for key, value in person_info2.items():
    print(f"{key} : {value}")

# Copying a dictionary by reference (shallow copy)
dict_copy_ref = person_info2
print("Dictionary copy by reference:", dict_copy_ref)

# Modifying the copy also affects the original dictionary
dict_copy_ref["email"] = "max@xyz.com"
print("Modified copy by reference:", dict_copy_ref)
print("Original after modification via reference:", person_info2)

# Copying a dictionary using the copy() method (deep copy)
dict_copy_deep = person_info2.copy()
dict_copy_deep["email"] = "cool@xyz.com"
print("Deep copy with added email:", dict_copy_deep)
print("Original dictionary after deep copy:", person_info2)

# Copying a dictionary using the dict() constructor (deep copy)
dict_copy_constructor = dict(person_info2)
dict_copy_constructor["email"] = "maxyyyyy@xyz.com"
print("Constructor copy with added email:", dict_copy_constructor)
print("Original dictionary after constructor copy:", person_info2)

# Merging two dictionaries using the update() method
dict_1 = {"name": "Max", "age": "28", "email": "hanan@google.com"}
dict_2 = dict(name="Mary", age=27, city="Boston")

dict_1.update(dict_2)
print("Merged dictionary using update():", dict_1)

# Dictionary with numerical keys and values
square_dict = {3: 9, 6: 36, 9: 81}
print("Dictionary with squares:", square_dict)

# Accessing a value in a dictionary with numerical keys
value_at_key_3 = square_dict[3]
print("Value at key 3:", value_at_key_3)

# Using a tuple as a dictionary key
tuple_key = (8, 7)
tuple_dict = {tuple_key: 15}
print("Dictionary with tuple as key:", tuple_dict)

# Explanation of Key Concepts:
# Key-Value Pairs:
# Dictionaries store data in pairs, where each key is unique, and is associated with a value.

# Unordered:
# Dictionaries do not maintain order of elements. The order of items is not guaranteed and can change over time.

# Mutable:
# Dictionaries are mutable, meaning you can modify, add, or remove key-value pairs after the dictionary has been created.

# Accessing Elements:
# Access elements by their keys. If a key does not exist, attempting to access it will raise a KeyError. Exception handling can be used to avoid this error.

# Adding and Updating:
# Add new key-value pairs or update existing ones using standard assignment syntax.

# Removing Elements:
# Remove elements using del, pop(), or popitem().

# Iterating Through Dictionary:
# Loop through keys, values, or both keys and values using keys(), values(), and items() methods respectively.

# Copying Dictionaries:
# Copying can be done by reference (shallow copy) or by creating a deep copy using copy() or dict().

# Using Tuples as Keys:
# Since tuples are immutable, they can be used as dictionary keys, which is useful for storing complex key types.

# Merging Dictionaries:
# Use the update() method to merge two dictionaries, which will overwrite values of matching keys from the original dictionary.


