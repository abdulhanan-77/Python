# Strings: Ordered, Immutable, Text Representation

# Creating a string
my_string = "Hello World!"
print("String:", my_string)

# Multiline string with line continuation using backslash
my_string2 = """Hello\
 World!"""
print("Multiline string with line continuation:", my_string2)

# Accessing a character from the string by index
char = my_string[0]
print("First character of the string:", char)

# Uncommenting the following line will raise a TypeError since strings are immutable
# my_string[0] = 'g'

# Slicing a string
my_string4 = "Hello Tom!"
substring = my_string4[6:11]
print("Substring (slice):", substring)

# Reversing a string using slicing
reversed_string = my_string4[::-1]
print("Reversed string:", reversed_string)

# Concatenating two strings
sentence = my_string4 + my_string
print("Concatenated string:", sentence)

# Iterating through a string
for char in my_string4:
    print("Character in my_string4:", char)

# Checking for a substring within a string
if 'e' in my_string4:
    print("'e' is in my_string4")
else:
    print("'e' is not in my_string4")

# Trimming whitespace from the string
my_string5 = '   Hello World!    '
print("String with leading/trailing spaces:", my_string5)

# Stripping whitespace from the string
my_string5 = my_string5.strip()
print("String after strip():", my_string5)

# String Methods

# Convert to uppercase
print("Uppercase string:", my_string5.upper())

# Convert to lowercase
print("Lowercase string:", my_string5.lower())

# Check if the string starts with a specific character
print("Does my_string5 start with 'H'?", my_string5.startswith('H'))

# Check if the string ends with a specific character
print("Does my_string5 end with '!'?", my_string5.endswith('!'))

# Find the position of the first occurrence of a substring
print("Position of first 'o':", my_string5.find('o'))
print("Position of 'lo':", my_string5.find('lo'))

# Count occurrences of a substring
print("Count of 'o' in my_string5:", my_string5.count('o'))

# Replace a substring with another
print("Replace 'World' with 'Universe':", my_string5.replace('World', 'Universe'))
print("String after replace:", my_string5)

# Splitting and Joining Strings

# Splitting a string into a list of words
my_string6 = "How are you doing?"
my_list = my_string6.split()
print("List after split():", my_list)

# Joining a list of words back into a string without spaces
new_string = ''.join(my_list)
print("Joined string without spaces:", new_string)

# Joining a list of words back into a string with spaces
new_string2 = ' '.join(my_list)
print("Joined string with spaces:", new_string2)

# String Performance Consideration

# Creating a large list of characters
my_list2 = ['a'] * 100000

from timeit import default_timer as timer

# Bad way: Concatenating strings in a loop (inefficient)
start = timer()
my_string7 = ''
for i in my_list2:
    my_string7 += i
stop = timer()
print("Time taken for inefficient string concatenation:", stop-start)

# Good way: Using join() for efficient string concatenation
start = timer()
my_string7 = ''.join(my_list2)
stop = timer()
print("Time taken for efficient string concatenation using join():", stop-start)

# String Formatting

# Formatting with % operator
name = "John"
age = 30
city = "New York"
print("Formatted string using % operator: My name is %s, I am %d years old, and I live in %s." % (name, age, city))

# Formatting with str.format()
print("Formatted string using .format(): My name is {}, I am {} years old, and I live in {}.".format(name, age, city))

# Formatting with f-strings (Python 3.6+)
print(f"Formatted string using f-strings: My name is {name}, I am {age} years old, and I live in {city}.")

# Assigning an f-string to a variable
my_string8 = f"My name is {name}, I am {age} years old, and I live in {city}."
print("Assigned f-string:", my_string8)

# Explanation of Key Concepts:

# Ordered:
# Strings maintain the order of characters as they are entered. You can access specific characters using indexing.

# Immutable:
# Once a string is created, it cannot be modified. Any operation that seems to modify a string actually creates a new one.

# Text Representation:
# Strings are used to represent text data in Python. They can be created using single, double, or triple quotes for multiline strings.

# String Methods:
# Python provides various methods for manipulating strings, such as upper(), lower(), strip(), replace(), etc.

# Slicing:
# You can extract a part of a string using slicing, where you specify the start and end indices.

# String Concatenation:
# Strings can be concatenated using the + operator.

# String Formatting:
# Python offers several ways to format strings, including the % operator, str.format(), and f-strings, which allow for the insertion of variables into strings.

# Performance Considerations:
# When building large strings, using ''.join() is more efficient than concatenating strings in a loop.