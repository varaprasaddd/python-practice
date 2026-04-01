#program to execute a set of statements as long as a condition is true.A statement is executed only once from top to bottom.


#to display number betwwn m and n
m = int(input("num1"))
n = int(input("num2"))
x = m

if x % 2 !=0 :
   x = x+1
while x>=m and x<=n:
   print(x)
   x += 2
 