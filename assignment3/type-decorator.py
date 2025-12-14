def type_converter(type_of_output): # type_of_output would be a type, like str or int or float
    def do_convert(func):
       def do_convert(*args, **kwargs):
           x = func(*args, **kwargs)
           return type_of_output(x)
       return do_convert
    return do_convert

@type_converter(str)
def return_int():
    return 5

@type_converter(int)
def return_string():
    return "not a number"

"""
ret_int = return_int()
print(ret_int)
print(type(ret_int))

ret_string = return_string()
print(ret_string)
print(type(ret_string))
"""

y = return_int()
print(type(y).__name__) # This should print "str"
try:
   y = return_string()
   print("shouldn't get here!")
except ValueError:
   print("can't convert that string to an integer!") # This is what should happen
