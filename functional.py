from variables import *

print("\nFunctional Programming")

# map(list) -> list
lengths = map(len, myTuple)
print(lengths)

# Function
def greater_than_three(x):
    return x > 3


# Multiple return values
def multi_return(x):
    return x, x*2, x*3

print(multi_return(5))

single, double, triple = multi_return(100)
print(single, double, triple)

# Ignoring return values
_, _, triple = multi_return(1000)
print(triple)

# Variable number of arguments
def variadic_function(first, second, third, *args):
    print(first, second, third)
    print("Extra positional arguments: " + str.join(", ", map(str, args)))


variadic_function(1, 2, 3, 9, 8, 7)


# Keyword arguments
def kwargs_function(first, second, third, **kwargs):
    print(first, second, third)
    print("Extra keyword arguments: " + str.join(", ", map(str, kwargs.iteritems())))

kwargs_function(second="5", third="6", first="1", fifth="10", valid=True, another_argument="Yes")


# filter
lengths = filter(greater_than_three, myTuple)
print(lengths)

# filter using lambda instead
lengths = filter(lambda x: x > 3, myTuple)
print(lengths)

# zipping two lists into a list of tuples, optionally into a dict
zipped = zip(myTuple, map(len, myTuple))
print(zipped)
