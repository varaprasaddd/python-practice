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
'''

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










