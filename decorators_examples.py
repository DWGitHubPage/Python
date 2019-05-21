# Python3.7.3
# Closure & Decorator examples.


# Closures.

def outer_function(msg):
    def inner_function():
        print(msg)
    return inner_function

hi_func = outer_function("Hi")
bye_func = outer_function("Bye")
hi_func()
bye_func()


# Basic decorator function.

def decorator_function(original_function):
    def wrapper_function():
        print("wrapper executed this before {}".format(original_function.__name__))
        return original_function()
    return wrapper_function

@decorator_function
def display():
    print("display function ran")
    
display()

# Example 2.

def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print("wrapper executed this before {}".format(original_function.__name__))
        return original_function(*args, **kwargs)
    return wrapper_function

    
@decorator_function
def display():
    print("display function ran")

@decorator_function
def display_info(name, age):
    print("display_info ran with arguments ({}, {})".format(name, age))

display_info("John", 34)
display()


# Example 3.

def my_logger(orig_func):
    import logging
    logging.basicConfig(filename="{}.log".format(orig_func.__name__), level=logging.INFO)

    def wrapper(*args, **kwargs):
        logging.info(
            "Ran with args: {}, and kwargs: {}".format(args, kwargs))
        return orig_func(*args, **kwargs)

        return wrapper

def my_timer(orig_func):
    import time

    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print("{} ran in: {} sec".format(orig_func.__name__, t2))
        return result

    return wrapper

import time 
@my_timer
def display_info(name, age):
    time.sleep(1)
    print("display_info ran with arguments ({}, {})".format(name, age))

display_info("Hank", 33)
