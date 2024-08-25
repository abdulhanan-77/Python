# Errors and Exceptions

# 1. Syntax Errors:
# Syntax errors occur when the Python parser cannot understand the code due to incorrect syntax.
# Example:
# a = 5 print(a)  # This will raise a SyntaxError because there's no newline or semicolon separating the statements.

# 2. Exceptions:
# Exceptions are errors detected during execution. Unlike syntax errors, they occur after the syntax is parsed correctly.

# Examples of common exceptions:
# a = 5 + '10'  # Raises a TypeError because you can't add an integer and a string.
# import somemodule  # Raises a ModuleNotFoundError because the module does not exist.
# a = 5
# b = c  # Raises a NameError because 'c' is not defined.
# f = open('somefile.text')  # Raises a FileNotFoundError because the file does not exist.
# a = [1, 2, 3]
# a.remove(4)  # Raises a ValueError because 4 is not in the list.
# a[4]  # Raises an IndexError because the index 4 is out of range.
# my_dict = {'name': 'Max'}
# my_dict['age']  # Raises a KeyError because the key 'age' is not in the dictionary.

# 3. Raising Exceptions:
# You can manually raise exceptions using the 'raise' keyword.

x = -5
# if x < 0:
#     raise Exception('x should be positive')  # Raises a generic Exception with a custom message.

# 4. Asserting Conditions:
# The 'assert' statement is used to test if a condition is True. If the condition is False, an AssertionError is raised.

# assert(x >= 0), 'x is not positive'  # Raises an AssertionError if x is negative, with a custom message.

# 5. Try-Except Blocks:
# The try-except block is used to handle exceptions and prevent the program from crashing.

try:
    a = 5 / 0  # This will raise a ZeroDivisionError
except:
    print('An error occurred')  # A general except clause catches all exceptions.

try:
    a = 5 / 0
except Exception as e:
    print(e)  # This will print the specific error message: 'division by zero'.

# Handling multiple exceptions:
try:
    a = 5 / 1
    b = a + '10'  # This will raise a TypeError
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)  # This will print the error message: "unsupported operand type(s) for +: 'float' and 'str'"
else:
    print('No error occurred')  # This block will execute if no exception is raised.

# The 'finally' block:
# The finally block is used to execute code that should run regardless of whether an exception occurred or not.

try:
    a = 5 / 1
    b = a + '10'  # Raises a TypeError
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:
    print('No error occurred')
finally:
    print('This block will always execute')  # This will always run, regardless of the exception.

# 6. Custom Exceptions:
# You can create custom exceptions by subclassing the built-in Exception class.

class ValueTooHighError(Exception):
    pass  # A custom exception that doesn't add any additional functionality.

class ValueTooLowError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value

# Function that uses the custom exceptions
def test_value(x):
    if x > 10:
        raise ValueTooHighError('Value is too high')
    if x < 5:
        raise ValueTooLowError('Value is too low', x)

# Handling custom exceptions:
try:
    test_value(1)  # This will raise the ValueTooLowError
except ValueTooHighError as e:
    print(e)
except ValueTooLowError as e:
    print(e.message, e.value)  # This will print: "Value is too low 1"

# Explanation of Errors and Exceptions:

# Syntax Errors:
# Occur when the code is not written correctly according to Python's syntax rules.
# Example: Missing colons, incorrect indentation, or incomplete statements.

# Exceptions:
# Exceptions occur during runtime and cause the program to stop executing.

# Common exceptions:
# TypeError: Operation or function is applied to an object of inappropriate type.
# NameError: Local or global name is not found.
# FileNotFoundError: An attempt to open a file that does not exist.
# ValueError: Function receives an argument of the right type but an inappropriate value.
# IndexError: Sequence subscript is out of range.
# KeyError: Attempt to access a dictionary with a key that doesn't exist.

# Raising Exceptions:
# You can use raise to trigger an exception manually.
# Useful for enforcing certain conditions in your code.

# Assertions:
# The assert statement tests a condition.
# If the condition is False, an AssertionError is raised, optionally with a custom message.

# Try-Except Blocks:
# Used to catch and handle exceptions.
# Prevents the program from crashing and allows you to manage errors gracefully.
# You can handle specific exceptions with multiple except clauses or handle any exception with a general except clause.
# The else block runs if no exception was raised.
# The finally block runs no matter what, typically used for cleanup actions.

# Custom Exceptions:
# You can create custom exceptions for specific error conditions in your code.
# Subclassing the Exception class allows you to define custom behavior for your exceptions.
