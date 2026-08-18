'''
#Arrays are nothing but a collection of elements of same datatype 
names = ["ravi","reddy","saran","jaswanth","arun"]
for i in names:
    print(i)

#accessing array
arr = ["ravi","reddy","saran","jaswanth","arun"]
print(arr[0])
print(arr[-1])

#updating array
num = [1,2,3,4,5]
num[2] = 5
print(num)

#adding and removing elements
arr = [1,2,3,4,5]
arr.append(4)
arr.insert(2,7)
arr.remove(1)
print(arr)


#slicing arrays
arr = [1,2,3,4,5]
print(arr[0:2])
print(arr[::-1])
print(arr[:-1])
print(arr[0:5])
print(arr[-2:])

#Find Maximum and Minimum
arr = [12, 45, 7, 23, 89, 3]
print("Max:", max(arr))
print("Min:", min(arr))

#Linear Search

arr = [5, 10, 15, 20, 25]
target = 20

if target in arr:
    print("Found at index:", arr.index(target))
else:
    print("Not found")
    
# Take input as list of strings
words = input("Enter strings separated by space: ").split()

# Print the list
print("List of strings:", words)

# Print elements one by one
for w in words:
    print(w)

name = ["bubby","vinay","pramod","madhu","jaswanth"]
print("bubby" in name)
print(name.append("reddy"))
print(name[::-1])


numbers=[10,20,30]
print(sum(numbers))
print(max(numbers))
print(min(numbers))
print(sorted(numbers))
print(any(numbers))
print(all(numbers))
r = numbers.copy()
r = numbers[:2]
print(r)

#join arrays3
a=[1,2]
b=[3,4]
print(a+b)



#looping
numbers = ["1","2","3"]
for num in numbers:
    print(num)

for i in range(len(numbers)):
    print(i,numbers[i])
'''

# 2D Arrays
matrix=[
[1,2,3],
[4,5,6],
[7,8,9]
]
print(matrix[1][2])
for i in matrix:
    for j in i:
        print(j, end =" ")
print()
for row in matrix:
    print(row[2])


