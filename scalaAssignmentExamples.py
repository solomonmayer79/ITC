print("-------------init concept ----------------")
class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

# Creating an instance of MyClass
obj = MyClass("solomon", 30)

# Accessing attributes and calling methods
obj.display_info()

print("-----------polymorphism---------------")
class Teacher:
    def __init__(self, *args):

        # Naming the teacher when a single string is passed
        if len(args)==1 & isinstance(args[0], str):
            self.name = args[0]

        # Naming the teacher as well as the subject
        elif len(args)==2:
            self.name = args[0]
            self.sub = args[1]

        # Storing the strength of the class in case of a single int argument
        elif isinstance(args[0], int):
            self.strength = args[0]
        # Storing the name and sub and strength of the class in case of a two str arg and single int argument
        elif len(args) == 3:
            self.name = args[0]
            self.sub = args[1]
            self.strength = args[2]

t1 = Teacher("Solomon Mayer")
print('Name of the teacher is ', t1.name)

t2 = Teacher("Renil Mayer", "Computer Science")
print(t2.name, ' teaches ', t2.sub)

t3 = Teacher(32)
print("Strength of the class is ", t3.strength)

t4 = Teacher('Denilia','IT',43)
print( 'Teacher Name : ',t4.name ,'\nTeacher Sub : ',t4.sub, '\n Strength : ',t4.strength)

# default constructor:
print("-----------Default Constructor------------------")
class Default():

    #defining default constructor
    def __init__(self):
        self.var1 = 56
        self.var2 = 27

    #class function for addition
    def add(self):
        print("Sum is ", self.var1 + self.var2)

obj = Default()     # since default constructor doesn’t take any argument
obj.add()

print("------------------parameterized---------------")

class Default():

    #defining parameterised constructor
    def __init__(self, n1, n2):
        self.var1 = n1
        self.var2 = n2

    #class function for addition
    def add(self):
        print("Sum is ", self.var1 + self.var2)

obj = Default(121, 136)              #Creating object for a class with parameterised init
obj.add()

print("-------------------self parameter---------------")

class mynumber:
    def __init__(self, value):
        self.value = value

    def print_value(self):
        print(self.value)

obj1 = mynumber(17)
obj1.print_value()

print("------------------pointer to current object---------------")

class check:
    def __init__(self):
        print("Address of self = ",id(self))

obj = check()
print("Address of class object = ",id(obj))

print("-----------------------create class with attributes and method----------")
class car():

    # init method or constructor
    def __init__(self, model, color):
        self.model = model
        self.color = color

    def show(self):
        print("Model is", self.model )
        print("color is", self.color )

# both objects have different self which contain their attributes
audi = car("audi a4", "blue")
ferrari = car("ferrari 488", "green")

audi.show()	 # same output as car.show(audi)
ferrari.show() # same output as car.show(ferrari)

print("Model for audi is ",audi.model)
print("Colour for ferrari is ",ferrari.color)

print("-----------------lambda-----------------------")
x = 2
print(lambda x: x + 1)# object
print("Lambda answer: ",(lambda x: x + x + x +  1)(2))
print("Lambda answer: ",(lambda x,y,z: x + y + z +  1)(2,3,4))
print("-------------if statement-----------------")
print((lambda x: x if(x > 10) else 10 * 2)(9))
print((lambda x: x * 10 if x > 10 else (x * 5 if x < 5 else x))(4))
print("----------------------increment-----------------")
increment = lambda x: x + 1
print(increment(2))
print("--------------lambda fn with filter()-------------------")
lst = [33, 3, 22, 2, 11, 1]
print(filter(lambda x: x > 10, lst))#return object
lst = [33, 3, 22, 2, 11, 1]
print(sorted(filter(lambda x: x > 10, lst)))#object pass to sorted fn return ascending order list
lst = [33, 3, 22, 2, 11, 1]
tpl = tuple(filter(lambda x: x > 10, lst))
print(tpl)#tuple
print("-----------------lambda fn with map()-----------------")
lst = [1, 2, 3, 4, 5]
print(sorted(map(lambda x: x * 10, lst)))#object pass to sorted function
tpl = tuple(map(lambda x: x * 10, lst))#object pass to tuple function
print(tpl)
print("------------------lambda with reduce()-----------------")
from functools import reduce
lst = [1, 2, 3, 4, 5]
print(reduce(lambda x, y: x + y, lst))
print("-----------------generator--------------------------")
def my_generator(n):
    # initialize counter
    value = 0
    # loop until counter is less than n
    while value < n:
        # produce the current value of the counter
        yield value
        # increment the counter
        value += 1
# iterate over the generator object produced by my_generator
for value in my_generator(3):
    # print each value produced by generator
    print(value)
print("-----------------list mutability------------------")
# Creating a List with
# the use of Numbers
# code to test that tuples are mutable
List = [1, 2, 4, 4, 3, 3, 3, 6, 5]
print("Original list ", List)

List[3] = 77
print("Example to show mutability ", List)
print("---------------------tuple immutability---------------")
import sys
a_list = []
a_tuple = ()
a_list = ["Geeks", "For", "Geeks"]
a_tuple = ("Geeks", "For", "Geeks")
print(sys.getsizeof(a_list))
print(sys.getsizeof(a_tuple))

print("-------------------execute timing-------------------")

# import sys, platform
# import time
#
# l=list(range(100000001))
# t=tuple(range(100000001))
#
# start = time.time_ns()
# for i in range(len(t)):
#     a = t[i]
# end = time.time_ns()
# print("Total lookup time for Tuple: ", end - start)
#
# start = time.time_ns()
# for i in range(len(l)):
#     a = l[i]
# end = time.time_ns()
# print("Total lookup time for LIST: ", end - start)

my_list = [1, 2, 3]
my_tuple = (4, 5, 6)

print(my_list[0]) # Output: 1
print(my_tuple[1]) # Output: 5
print("--------------------function decorator-------------------")
def simple_decorator(func):
    def wrapper():
        print("Before function execution")
    func()
    print("After function execution")
    return wrapper
@simple_decorator
def greet():
    print("Hello, world!")
greet()
print("-------------------class decorator-------------------")
def class_decorator(cls):
    class NewClass(cls):
        def new_method(self):
            print("This is a new method added by the decorator")
    return NewClass
@class_decorator
class MyClass:
    def original_method(self):
        print("This is the original method")
obj = MyClass()
obj.original_method()
obj.new_method()
print("-----------------Decorators with arguments---------------")
def decorator_with_args(arg1, arg2):
    def actual_decorator(func):
        def wrapper( * args, ** kwargs):
            print("Decorator argument 1:", arg1)
            print("Decorator argument 2:", arg2)
            func( * args, ** kwargs)
        return wrapper
    return actual_decorator
@decorator_with_args("Hello", "World")
def greet(name):
    print('Hi', name,'!')
greet("solomon")
print("---------------execution time of function-----------")
import time
def timer_decorator(func):
    def wrapper( * args, ** kwargs):
        start_time = time.time()
        result = func( * args, ** kwargs)
        end_time = time.time()
        print(func.__name__, 'executed in', end_time, start_time,':.5f seconds')
    return result
    return wrapper
@timer_decorator
def slow_function():
    time.sleep(2)
print("Slow function executed")
slow_function()
