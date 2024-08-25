# Introduction to Decorators
# Decorators in Python are a powerful tool that allows you to modify or extend the behavior of functions or methods without changing their code. Decorators are often used for logging, access control, caching, and more.

# Basic Decorator Syntax

def decorator_name(func):
    def wrapper(*args, **kwargs):
        # Code to execute before calling the original function
        result = func(*args, **kwargs)
        # Code to execute after calling the original function
        return result
    return wrapper

@decorator_name
def function_name(parameters):
    # Function body
    pass

# 1. Basic Function Decorator Example
import functools

# Define a decorator function that adds behavior before and after the function call
def start_end_decorator(func):
    @functools.wraps(func)  # Preserve the original function's information
    def wrapper(*args, **kwargs):
        print("Start")  # Code to run before the function
        result = func(*args, **kwargs)  # Call the original function
        print("End")  # Code to run after the function
        return result  # Return the result of the original function
    return wrapper  # Return the wrapper function

# Use the decorator on a function
@start_end_decorator
def add5(x):
    return x + 5

# print(help(add5))
# print(add5.__name__)

# Call the decorated function
result = add5(10)
print(result)

# 2. Decorators with Arguments
# You can also create decorators that take arguments, allowing more customization.
# Define a decorator that accepts arguments
def repeat(num_times):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):  # Repeat the function call a specified number of times
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

# Use the decorator with an argument
@repeat(num_times=3)
def greet(name):
    print(f"Hello {name}")

# Call the decorated function
greet("John")

# 3. Combining Multiple Decorators
# You can apply multiple decorators to a single function. They will be applied from the innermost to the outermost.
@start_end_decorator
@repeat(num_times=3)
def say_hello(name):
    """
    This function prints a personalized greeting and returns it.

    Parameters:
    name (str): The name of the person to greet.

    Returns:
    str: The personalized greeting message.
    """
    greeting = f"Hello {name}"
    print(greeting)
    return greeting

# Call the decorated function
say_hello("John")

# 4. Class Decorators
# Class decorators allow you to wrap function calls inside a class, maintaining state across calls.
# Define a class decorator
class CountCalls:
    def __init__(self, func):
        self.func = func  # Store the function to be decorated
        self.num_calls = 0  # Initialize a counter for the number of calls

    def __call__(self, *args, **kwargs):
        self.num_calls += 1  # Increment the counter each time the function is called
        print(f"This function has been called {self.num_calls} times")
        return self.func(*args, **kwargs)  # Call the original function

# Use the class decorator
@CountCalls
def say_hello2():
    print("Hello, World!")

# Call the decorated function multiple times
say_hello2()
say_hello2()

# Explanation of the Code:

# start_end_decorator:
# This function is a basic decorator that prints "Start" before executing the function and "End" after.
# The @functools.wraps(func) decorator is used to preserve the original function's metadata (such as name and docstring).

# repeat Decorator:
# This decorator takes an argument (num_times) to repeat the execution of the decorated function a specified number of times.
# The wrapper function inside repeat handles the looping.

# Combining Decorators:
# Multiple decorators can be stacked on a single function. They are applied from the innermost (closest to the function) to the outermost.

# Class Decorator CountCalls:
# This class decorator keeps track of how many times a function has been called by maintaining a counter (num_calls).
# The __call__ method makes instances of the class callable, behaving like a function.

# Key Points:
# Decorators wrap a function, adding additional behavior without modifying the function itself.
# functools.wraps helps to maintain the metadata of the original function.
# Class decorators can be used to maintain state across multiple function calls.
# You can stack multiple decorators on a function to layer behaviors.
 