num = int(input("enter a number :"))
original = num
reversed = 0
while num > 0:
    digit = num%10
    reversed = reversed*10 + digit
    num = num//10

if (original== reversed):
    print("palindrome")
else :
    print("not a palindrome")


#reverse a number
num = int(input("enter a number :"))
reversed = 0
while num>0:
    digit = num%10
    reversed = reversed*10 + digit
    num = num//10
print(reversed)


#armstrong number
num = int(input("enter a number :"))                               
reversed = 0
power = len(str(num))
original = num
while num>0:
    digit = num%10
    reversed +=  digit**power
    num = num//10
if reversed == original:
    print("armstrong")
else :
    print("not a armstrong")       

#factorial
n = int(input("enter a number"))
factorial = 1
for i in range(1,n+1):
    factorial *= i
print(factorial)


#prime number
n = int(input("Enter a number: "))
if n <= 1:
    print("Not a prime")
else:
    for i in range(2, n):
        if n % i == 0:
             print("Not a prime")
             break
    else:
       print("Prime")

#prime numbers between 1 to 10
for i in range(1,11):
    if i <= 1:
        continue
    for n in range(2,i):
     if i % n== 0:
             break
    else:
        print(i)

#perfect number
n = int(input("enter a number"))
sum = 0
for i in range(1,n):
    if n % i == 0:
        sum+=i
print("sum of divisiors of n",sum) 
if sum == n:
    print("perfect number")
else:
    print("not a perfect number")


#strong number
n = int(input("enter a number :"))
total = n
sum = 0
while total > 0:
    digit =  total%10
    fact = 1
    for i in range(1,digit+1):
        fact *=i

    sum += fact
    total = total//10
print(sum)
    
if sum == n:
    print("strg num")
else:
    print("not strg num")


a = [1,2,3,4,5]
b = a.sort()
print(b)