#array contains consecutive numbers and in which one number is missing. find the missing value
arr = list(map(int, input().split()))
sum_arr = 0
n = arr[-1]
sum_n = (n*(n+1))/2
for i in arr:
    sum_arr += i
    if(sum_n == sum_arr):
         print("no missing")
    else:
        r = sum_n - sum_arr
print(int(r))

#occurencies of numbers in arrays.
l = [1,2,2,3,4,4]
d = {}
for i in l:
    if i not in d:
        d[i] = 1
    else:
        d[i] = d[i] + 1
print(d)

#occurencies of numbers in arrays.using predifined function
l = [1,2,2,3,4,4]
d = {}
for i in l:
    d[i]=d.get(i,0)+1
    
print(d)
