 # Nested loops is nothing but a loop inside another loop
#syntax
# outer_loop
#      inner_loop
#            statements for inner_loop
#      statements for outer_loop

#print 1 to 3 for 3 times for for loop in while loop
i = 1
while i <4:
    print("iter no",i)
    for j in range (1,4):
        print(j)
    print("---")
    i += 1

#print for loop inside for loop to obtain 1 to 3 numbers for 3 times
for i in range (3):
    print("for in for iteration",i )
    for j in range(1,4):
        print(j)
    print("---")

# print prime numbers between 2 and 10
for num in range(2,10):
    for j in range(2,num):
       if num % j == 0:
        break
    else :
        print(num)

# display stars as a right angle triangular form


n = int(input("enter a number"))
for i in range (n):
    for j in range (1,i+1):
        print("*",end="")
    print()


#print equalateral program
n = int(input("Enter number of rows: "))

for i in range(n):
    # Print spaces
    for j in range(n - i - 1):
        print(" ", end="")
    #for odd  
    for j in range(2*i+1):
        print("*",end = "")
    print()

