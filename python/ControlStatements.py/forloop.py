char = 'name'
for ch in char:
   print(ch)

# to display nummbers in reverse using for loop
for i in range (50,9,-2):
    print(i)

#odd num between 1 and 99
for i in range (1,99,2):
    print(i)

#sum of list
list = [10,20,30,40,50]
sum = 0

for i in list:
    sum+=i

print(sum)

#sum of numbers in list
list = [20,30,40,50,60]
total = 0
while i < len(list):
     total+=len(list)
     i+=1
     print("sum",sum)

# prime numbers
num = int(input("enter a number"))
if num <=1 :
    print("not prime")
    

for i in range(2,num):
    num % i == 0
    print("not prime")
    break
  

else:
    print("prime")