#function contains group of statements that are intended to perform a certain task
#The below is example program of function
def sum(a,b):
    c = a+b
    print(c)
sum(1.0,2.5)

#returning results from a function
#example1
def sum(a,b):
    c = a-b
    return c
m = sum(10,15)
print(m)
y = sum(2,3.4)
print(y)

#example2
#test whether number is odd or even
def even_odd(num):
    if num %2 == 0:
        print(num,"\neven")
    else:
        print(num,"\nodd")

even_odd(10)

#a function to calculate factorial valuee
def fact(n):
    prod = 1
    while n>1:
        prod*=n
        n-=1
    return prod
for i in range(1,11):
    print('factorial of {} is {}'.format(i,fact(i)))


#default arguments
def greet(name = "hii"):
    print("hello",name)

greet()
greet("reddyy")


#check whether number is prime or not
def is_prime(n):
    if n <= 1:
        return False
    
    for i in range (2, n) :
        if n % i == 0:
         return False
    

    return True
n = int(input("enter a num"))
if is_prime(n):
       
    print("prime")
else:
    print("not a prime")

#first 10 prime numbers
def is_prime(num):
    if num <= 1:
        return False

    for i in range(2,num):
        if num %i == 0:
             return False
    return True

count = 0
num = 2
n = int(input("enter a numbber"))
while count < n:
    if is_prime(num):
        print(num)
        count+=1
    num+=1



#Keyword Variable Length Arguments (**kwargs)
def details(**data):
    for key, value in data.items():
        print(key, value)

details(name="Vara", age=20, city="Chennai")



#Local Variable          	                     Global Variable
#Declared inside a function	                     Declared outside all functions
#Can be used only inside that function	         Can be used throughout the program
#Exists only while the function is running	     Exists until the program ends

#9. Local Variables
def test():
    x = 10
    print(x)

test()


# Global Variables
x = 100

def show():
    print(x)

show()


#Recursive Function
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))

#exchanging of global variable
x = 10

def change():
    global x
    x = 50

change()
print(x)

#lamda function
square = lambda x: x * x

print(square(6))

#Map Function
numbers = [1,2,3,4,5]

result = list(map(lambda x:x*x, numbers))

print(result)


#Filter Function

numbers = [1,2,3,4,5,6]

even = list(filter(lambda x:x%2==0, numbers))

print(even)

#Reduce Function
from functools import reduce

numbers = [1,2,3,4]

result = reduce(lambda x,y:x+y, numbers)

print(result)

#Nested Functions
def outer():
    print("Outer Function")

    def inner():
        print("Inner Function")

    inner()

outer()


# Function Calling Another Function
def add(a,b):
    return a+b

def display():
    result = add(10,20)
    print(result)

display()


# Anonymous Function
cube = lambda x:x**3

print(cube(3))


# Pass Statement
def future():
    pass

print("Program continues")

# Docstrings
def add(a,b):
    """Returns the addition of two numbers."""
    return a+b

print(add.__doc__)


# Function Annotations
def add(a:int,b:int)->int:
    return a+b

print(add(5,6))


# Multiple Return Values
def calculate(a,b):
    return a+b,a-b,a*b

x,y,z=calculate(10,5)

print(x)
print(y)
print(z)

# Returning Lists
def numbers():
    return [10,20,30]

print(numbers())


#Returning Dictionaries
def student():
    return {
        "name":"Vara",
        "age":20
    }

print(student())


# Returning Tuples
def values():
    return 10,20,30

print(values())








