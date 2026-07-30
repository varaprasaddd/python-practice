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

#Variable Length Arguments (*args)
def total(*numbers):
    print(sum(numbers))

total(10, 20)
total(10, 20, 30, 40)

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








