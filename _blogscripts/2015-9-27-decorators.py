# ##Decorators

# Let's start off easy. This will be both an introduction to this blog's style
# and an introduction to a cool tool that every python programmer should know.
# I'm a huge fan of literate programming and all that, so this blog post will
# be available in two forms, a markdown form like this, as well as an inverted
# form, a runnable python file with the code and the commentary in comments.
# I'm writing this post with python 3 in mind (and generally I use python 3),
# but for this post specifically, there shouldn't be any python 2
# incompatibilities.

# With that disclaimer, let's get started. Python has functions. Functions are
# great tools for doing things. Decorators allow a programmer to modify the way
# functions work, which can be extremely powerful. That said, both the syntax
# and ideas can be rather mind-bending, especially the more complex examples.
# [This is nothing new](http://simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps/),
# and there are a lot of good resources out there to learn how decorators work,
# I just think mine is better.

# So python can have functions

def f(x):  # adds one
    return x + 1

# Functions can obviously be vastly more complex than something that simply
# increments a value, but this will already get confusing, so we start simple.

# We also want to verify that our function actually *works*. 

assert f(2) == 3  # True
# Functions can call other functions within them, mathematically speaking, 
# this would be "function composition".

def g(x):  # adds two
    return f(x) + 1

assert g(2) == 4  # True

# Importantly, functions are just data that we can pass into another function.
# A function can take another function as an argument. At first this seems a
# little silly, but it can be useful.

from collections.abc import Callable, Iterable
# if you aren't familiar with this, don't worry, Callable just means that you
# can treat the object like a function, and Iterable means that you can loop
# over the object

def apply_function(f: Callable, arg):
    return f(arg)  # this just calls the function on the argument


def my_map(f: Callable, l: Iterable):
    new_list = []
    for item in l:
        new_list.append(f(item))
    return new_list


assert apply_function(g, 3) == 5
assert my_map(f, [1,2,3,4,5]) == [2,3,4,5,6]

# The act of iterating over a list and applying a function to each member is so
# common that python provides a builtin to do just that (the map function),
# although often list comprehensions (`[f(item) for item in l]`) are the more
# "pythonic" solution.

# The next, and arguably hardest cognitive leap is that functions can return
# functions. That is, we can create a function within another function.

def function_builder():
    def child_function():
        return "hello world"
    return child_function

assert function_builder()() == "hello world"

# That's some strange syntax, this weird double parenthesis. It looks wrong,
# unnatural, unholy. Its dark magic. We're getting somewhere. What's occurring
# here is *strange*. The result of `function_builder` isn't a string, its a
# function that returns a string. Function builder gives you a function that
# can then be executed to give you a useful result. At first this seems really
# useless, but there is a second, much more important part to this.


def add_n_factory(n: int):
    def add_n(val: int):
        return n + val
    return add_n

add_4 = add_n_factory(4)
assert add_4(3) == 7

add_6 = add_n_factory(6)
assert add_6(4) == 10

# for more weird syntax:
assert add_n_factory(3)(3) == 6
# Here we take advantage of something called a 
# [closure](https://en.wikipedia.org/wiki/Closure_(computer_programming)). 
# In computer science, a closure is the idea of a computation bound to its 
# environment. This goes along with the idea of scope. A function can see 
# what is inside of it.

# global scope
def func(x):
    pass
    # inner scope, I can see 'x'
# back to the global scope
func("hello world")
try:
    print(x)
    # this will fail because x isn't defined in this scope
except:
    pass

# But with nested functions, the inner functions have access to the variables
# in the scope of the outer functions, as we could see with `add_n_factory`.
# The newly created functions could access the value of n. What variables the
# innermost function can see is defined by a set of scoping rules, generally
# speaking a function can access anything in its scope or any enclosing scope
# (this include the global scope) and in the case of conflicts the most
# specific value (which is also the most recently defined) is used.

# Its vital to note that the inner function is bound to the values used when
# defining that function, thus if you run `add_n_factory` again later, it won't
# change the value of n in a previously created scoped function. In other
# words, you can't mutate a previously created inner function.

# So we have a few ideas ideas:

# 1. you can pass a function into another function
# 2. we can dynamically construct a new function within a function
# 3. we can bind a dynamically built function to some values in a closure

# Combining them all leads to a decorator.

def decorate_add_one_more(f: Callable):
    def add_one_more(x: int):
        return f(x) + 1
    return add_one_more

add_5 = decorate_add_one_more(add_4)
assert add_5(10) == 15

# and for more syntactical shenanigans
assert decorate_add_one_more(add_n_factory(5))(3) == 9

# This merits an explanation. `decorate_add_one_more` is a function. You pass a
# function into it, and it returns a different function. The function you give
# it should ideally take in and return an integer, otherwise weird things might
# happen. That function is then bound to a new function, `add_one_more` and
# `add_one_more` calls the old function, does some additional processing and
# returns a different value. This is the basic idea of a decorator.

# Importantly though, python provides some very special syntax for decorators.
# Its common to want to immediately decorate a function in some manner. Often
# when using a library, the designers will have done something to abstract away
# a set of processing, and the library's API will involve decorators to keep
# the abstractions clean (see Flask). Other times, a decorator can be used to
# modify a function to provide a common functionality (such as `staticmethod`,
# `lru_cache` and family from the standard library). In such cases, there is a
# common pattern to immediately define a function and then decorate it, python
# provides a syntax for this using the @ symbol.

def add_7(x):
    return 6 + x

add_7 = decorate_add_one_more(add_7)

@decorate_add_one_more
def add_9(x):
    return 8 + x

assert add_7(2) == add_9(0) == 9  # it works!

# The above two methods are implemented in essentially the same way. A function
# is defined and immediately passed into another function, which modifies it
# and returns a new function under the name of the old function. That means
# that the versions that adds 8 is never really accessible (it is if you try
# really hard, but that's another post). And the version that adds 6 is only
# accessible until it is wrapped a few lines later. After that, the "old"
# functions essentially disappear and its only possible to work with the
# wrapped function. The result being that the function works "correctly" is
# the only accessible one.

# So that's how decorators work. There are a few more complex topics to cover.
# The first is decorators that take arguments. As an example, in flask, you use
# `@app.route('/')` to denote the url at which a certain page will be
# accessible. This isn't the same kind of decorator as what we were using.
# Instead, we need to create a decorator factory.

def do_nothing(f): # a decorator
    return f

def do_nothing_wrapper(): # a decorator factory
    def do_nothing_2(f):
        return f
    return do_nothing_2

@do_nothing  # do nothing is called on func
def func():
    return 10

@do_nothing_wrapper()  # the result of do_nothing_wrapper is called on func
def func_2():
    return 10

assert func() == 10
assert func_2() == 10

# In essence, the result of the @ line is what is called on the function, so
# once you evaluate what follow @, you should have a function that is then
# called on the decorated function. This is still mind bending and leads to
# some convoluted code.

def add_n_more(n: int):
    def add_n_decorator(f: Callable):
        def new_adder(m: int):
            return f(m) + n
        return new_adder
    return add_n_decorator

@add_n_more(3)
def add_15(n):
    return n + 12

@add_n_more(5)
def add_3(n):
    return n - 2  # I was running out of numbers


assert add_3(5) == 8
assert add_15(5) == 20
# now for some horrors
# I'm going to use lambdas for simplicities sake, hopefully you are familiar
assert add_n_more(3)(lambda x: x + 2)(5) == 10

# Here, add_n_more constructs a new decorator at runtime, which then wraps the
# function that is defined. This decorator then adds the value that is passed
# to the function factory, instead of a predefined value. That said, its still
# a terrifying layering of functions 3 deep.

# The second more complex idea is that of generic decorators using variable
# length arguments and variable length keyword arguments. Quickly, lets define
# a sum function in two ways, one with and one without keyword arguments

def my_sum(a_list):
    s = 0
    for item in a_list:
        s += item
    return s

def my_var_sum(*a_list):
    s = 0
    for item in a_list:
        s += item
    return s
# These are...exactly the same, with the exception of an asterisk in the second
# one. So now lets test them.

assert my_sum([1,2,3,4]) == 10
assert my_var_sum(1,2,3,4) == 10
assert my_var_sum(1,2,3,4,5,6,7,8,9) == 45
# Here the difference becomes apparent. With the `*a_list` syntax, you don't
# pass in the list, you pass in a series of single values. Python then forms
# these into a variable length list which can be accessed from the variable
# name preceded by an asterisk. Normally, this variable is named `*args`.
# Similarly, for keyword arguments, `**kwargs` can be used to form a variable
# sized dictionary of keyword arguments.

# Further, there is a syntax for unpcking such lists, called either the splat
# or "unpacking argument lists" operator, using `*list` or `**dict` will unpack
# them into component arguments. This syntax only works within a function call.

# Putting these together, we can create generic decorators that work on any
# function with any set of arguments.

def dynamic_logging_decorator(file="out.log"):
    # lets use a decorator that can optionally take an argument
    def debug_decorator(function):
        def decorated_function(*args, **kwargs):
            with open(file, 'a') as f:
                f.write("calling function " + str(function) + " with args " + str(args) + 
                "; and keyword args " + str(kwargs))
            return function(*args, **kwargs)
        return decorated_function
    return debug_decorator

# I leave testing this as an exercise to the reader. 

@dynamic_logging_decorator()
def fanc(x, val=0):
    return x+val+1

print(fanc(3))
print(fanc(3, val=4))
