"""
def say_hello():
    print("Hello!")

def repeat_me(func, num_repeats):
    for _ in range(num_repeats):
        func()

repeat_me(say_hello, 5)  # Will print "Hello!" 5x
"""

"""
def my_decorator1(num_repeats):
    def my_decorator(func):
        def wrapper():
            for _ in range(num_repeats):
                func()
        return wrapper
    return my_decorator

@my_decorator1(5)
def print_name():
    print("John")

print_name()
"""

"""
import time

def timer(func):
    ## Output the time the inner function takes
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print (f"Finished in {run_time:.4f} secs")
        return value
    return wrapper_timer

@timer
def wait_half_second():
    time.sleep(0.5)
    return "Done"

@timer
def wait_half_second_2():
    time.sleep(1)
    return "Done"

@timer
def wait_half_second_3(seconds_to_sleep):
    time.sleep(seconds_to_sleep)
    return "Done"

wait_half_second()
wait_half_second_2()
wait_half_second_3(2)
"""


"""
# Callback to Dash application
callback_dict = {}

def wrap_output(before, after, greeting_type):
    def decorator_wrap_output(func):
        #callback_dict[greeting_type] = func
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return before + result + after
        callback_dict[greeting_type] = wrapper
        return wrapper
    return decorator_wrap_output

@wrap_output("begin:", ":end", "for_hello")
def hello():
    return "Hello, World!"

@wrap_output("begin:", ":end", "for_goodbye")
def goodbye():
    return "Goodbye, World!"

print(callback_dict["for_hello"]()) # Will print "begin:Hello, World!:end"

print(callback_dict["for_goodbye"]()) # Will print "begin:Goodbye, World!:end"
"""

"""
# Python List Comprehensions
integer_list = [x for x in range(2)]
print(type(integer_list))
for item in integer_list:
    print(item)
for item in integer_list:
    print(item)

# Generator Expressions
integer_list_2 = (x for x in range(2))
print(type(integer_list_2))
for item in integer_list_2:
    print(item)
for item in integer_list_2:
    print(item)
"""
"""
# closures
def make_secret(secret):
    def wrapper(guess):
        if guess == secret:
            print("You got it!")
        else:
            print("Nope")
    return wrapper

game1 = make_secret("swordfish")
print(type(game1))
game2 = make_secret("magic")


game1("magic") # Prints nope
game1("swordfish") # Prints you got it
game2("magic") # Prints you got it
"""

def make_secret(secret):
    bad_guesses = 0
    def did_you_guess(guess):
        nonlocal bad_guesses
        if guess == secret:
            print("You got it!")
        else:
            bad_guesses+=1
            print(f"Nope, bad guesses: {bad_guesses}")
    return did_you_guess

game1 = make_secret("swordfish")
game1("magic") # Prints nope, bad guesses 1
game1("magic") # Prints nope, bad guesses 2
game1("swordfish") # Prints you got it


def lwl(sent):
    print(sent == None)
    print(sent == '')

print("-----------")
lwl('')
print("-----------")
lwl(None)
