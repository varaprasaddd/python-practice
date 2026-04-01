#program to display sum of two numbers
x = 5
y = 10
sum = x + y
print("The sum of", x, "and", y, "is:", sum)

#example of float data type
a = 5.5
b = 2.3
product = a * b
print("The product of", a, "and", b, "is:", product)

#example of complex data type
c1 = 2 + 3j
c2 = 1 + 4j
sum_complex = c1 + c2
print("The sum of", c1, "and", c2, "is:", sum_complex)

#coverting data types
num = 10
print(float(num))  # converting integer to float
print(complex(num))    # converting integer to complex

# python program to convert into deciamal system
n1 = 0o17
n2 = 0B1110010
n3 = 0x1c2

n=int(n1)
print("The decimal value of", n1, "is:", n)
n=int(n2)
print("The decimal value of", n2, "is:", n)
n=int(n3)
print("The decimal value of", n3, "is:", n)


#python program to demonstrate boolean data type
a = 10
b = 5
print(a > b)    # True
print(a < b)    # False
print(a == b)   # False
print(a != b)   # True

#python program to demonstrate string data type
str1 = "Hello, "
str2 = "World!"
greeting = str1 + str2
print(greeting)
print("Length of the greeting message is:", len(greeting))


# python program to demonstrate tuple data type
my_tuple = (10, 20, 30, 40)
print("My tuple:", my_tuple)

# Access elements
print("First element:", my_tuple[0])
print("Last element:", my_tuple[-1])

# Tuple unpacking
numbers = (1, 2, 3)
a, b, c = numbers

print("a:", a)
print("b:", b)
print("c:", c)

# Tuple operations
t1 = (1, 2, 3)
t2 = (4, 5)

# Concatenation
t3 = t1 + t2
print("Concatenated tuple:", t3)

# Repetition
t4 = t1 * 2
print("Repeated tuple:", t4)

# Check membership
print("Is 2 in t1?", 2 in t1)
print("Is 6 in t1?", 6 in t1)

# python program to demonstrate set data type
fruits = {"apple", "banana", "cherry", "apple"}  # 'apple' duplicate
print("Fruits set:", fruits)
fruits.add("orange")
print("After adding orange:", fruits)
fruits.remove("banana")
print("After removing banana:", fruits)

# Two sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Union (all unique elements)
print("Union:", set1 | set2)  # or set1.union(set2)

# Intersection (common elements)
print("Intersection:", set1 & set2)  # or set1.intersection(set2)

# Difference (elements in set1 not in set2)
print("Difference:", set1 - set2)  # or set1.difference(set2)

# Symmetric Difference (elements in either set, not both)
print("Symmetric Difference:", set1 ^ set2)  # or set1.symmetric_difference(set2)

# python program to demonistrate list data type
my_list = [1, 2, 3, 4, 5]
print(my_list)          
print(my_list[0])       
print(my_list[-1])   
#common list operators   
my_list.append(6)      
my_list.extend([7, 8]) 
my_list.insert(2, 99) 
print(my_list)
#removing elements
my_list.remove(3)   
popped = my_list.pop()   
del my_list[0]      
print(my_list)
#slicing and indexing
numbers = [10, 20, 30, 40, 50]
print(numbers[1:4])   
print(numbers[:3])     
print(numbers[::2])    
#functions
nums = [5, 2, 9, 1]
print(len(nums))      
print(max(nums))      
print(min(nums))         
nums.sort()          
print(nums)
nums.reverse()        
print(nums)
#loops
fruits = ["apple", "banana", "cherry"]

# Using for loop
for fruit in fruits:
    print(fruit)

# Using while loop
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1 

       




