arr = [1,2,4,5,6,7]
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

    