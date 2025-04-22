# 1. Simple Decorator with a Simple Function
def greet_decorator(func):
    # This is the decorator function. It takes another function 'func' as input.
    def wrapper():
        # This is the wrapper function. It adds behavior before and after calling 'func'.
        print("Hello!")
        func()  # Call the original function
        print("Goodbye!")
    return wrapper  # The decorator returns the modified function (wrapper)

@greet_decorator
def say_name():
    # This is a simple function with no arguments.
    print("My name is Alice.")

say_name()
# Output:
# Hello!
# My name is Alice.
# Goodbye!

print("\n" + "="*30 + "\n")

# 2. Simple Decorator with a Simple Function Having Inputs
def emphasize_decorator(func):
    # This decorator takes a function 'func' that accepts arguments.
    def wrapper(*args, **kwargs):
        # The wrapper can accept any positional (*args) and keyword (**kwargs) arguments.
        print("*" * 20)
        func(*args, **kwargs)  # Call the original function with its arguments
        print("*" * 20)
    return wrapper

@emphasize_decorator
def describe(item):
    # This function takes one argument 'item'.
    print(f"This is a {item}.")

describe("shiny apple")
# Output:
# ********************
# This is a shiny apple.
# ********************

print("\n" + "="*30 + "\n")

# 3. Simple Decorator Having Inputs with a Simple Function
def repeat_decorator(num_times):
    # This is a decorator factory. It takes an argument 'num_times'.
    def actual_decorator(func):
        # This is the actual decorator. It takes the function 'func' to be decorated.
        def wrapper(*args, **kwargs):
            # The wrapper will execute the original function multiple times.
            for _ in range(num_times):
                func(*args, **kwargs)
        return wrapper
    return actual_decorator  # The decorator factory returns the actual decorator

@repeat_decorator(num_times=2)
def wave():
    # This is a simple function with no arguments.
    print("Waving hello!")

wave()
# Output:
# Waving hello!
# Waving hello!