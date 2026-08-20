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


#sum of an array
arr = [10,20,30,40]
total = 0
for num in range(len(arr)):
    total = total + arr[num]
print(total)


#taking array as an user input
arr = list(map(int, input().split()))
for i in range(len(arr)):
    print(arr[i])
    
print(arr)


# Create an empty list
n = int(input("enterr num"))
arr = []

# Take 5 inputs from user
for i in range(n):
    num = int(input(f"enter numner {i+1} :"))
    arr.append(num)

# Print each element
print("You entered:")
for i in range(len(arr)):
    print(arr[i])

# Print the whole array
print("Final array:", arr)


#printing max in array
arr = [2,3,4,5]
max = arr[0]
for i in range(len(arr)):
    if arr[i] > max:
        max = arr[i]
print(max)
'
arr = [1,0,2,0,3]
end = 0

for i in range(len(arr)):
    if arr[i] != 0:
        arr[end] = arr[i]
        end += 1

# Fill the rest with zeros
while end < len(arr):
    arr[end] = 0
    end += 1
print(arr)


#getting zereos to another side of array
arr = [1,2,3,0,4,0]
end = len(arr)-1
for i in range(len(arr)-1-1-1) :
    if arr[i] != 0:
        arr[end] = arr[i]
        end-=1
while end >= 0:
    arr[end] = 0
    end -= 1
print(arr)


#using two pointers
arr = [1,2,0,4,0]
l = 0
r = len(arr) - 1

while l < r:
    if arr[l] != 0:
        l += 1
    elif arr[r] == 0:
        r -= 1
    else:
        arr[l], arr[r] = arr[r], arr[l]
        l += 1
        r -= 1

print(arr)



#even or odd using bitwise operations
n = int(input())
if (n & 1):
    print("odd")
else:
    print("even")
    

#find maximum and minimun in an array
arr = [1,2,3,4,7]
maximum = arr[0]
for i in range(len(arr)):
    if arr[i] > maximum:
        maximum = arr[i]
print(maximum)

#min
n = list(map(int, input().split()))
min = n[0]
for i in range(1,len(n)):
    if n[i] < min:
        min = n[i]
print(min)
'''



