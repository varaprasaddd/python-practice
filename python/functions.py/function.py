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










