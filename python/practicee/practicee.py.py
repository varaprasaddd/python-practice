'''ori = 2008

n = 2008

if n == ori:
    print("PIN accepted")
    
    balance = 5000
    amount = int(input("Enter withdrawal amount: "))

    if amount <= balance:
        balance = balance - amount
        print("Withdrawal successful")
        print("Remaining balance:", balance)
    else:
        print("Insufficient balance")

else:
    print("Incorrect PIN")


#palindrome without loops
n = int(input("enter a number"))
temp = n
#for the last digit
a = n%10
n = n//10
#for second last digit 
b = n%10
n = n//10
#for third last digit
c = n%10

reversed = a*100+b*10+c
print(reversed)


if reversed == temp:
    print("palindrome")
else:
    print("not a paindrome")
    


name = [1,2,3]
print(len(name)) 

name = "raj"
print(name.lower())


ch = str(input("enter a name"))
count = 0
for i in ch:
    if i in "aeiou":
        count+=1
        print(i)
print(count)

ch = str(input("enter a name"))
count = 0
for i in ch:
    if i not in "aeiou":
        count+=1
        print(i)
print(count)


ch = str(input("enter a name"))
count = 0
for i in ch:
    if  i  in " ":
        count+=1
        print(i)
print(count)


chr = str(input("enter a  number"))
print(chr[:-1])


# removing space

name = "hello world"
count = 0
for i in name:
    if i not in " ":
        print(i,end ="")

name = "hello world"
count = {}

for i in name:
    if i != " ":   # skip spaces
        if i in count:
            count[i] += 1
        else:
            count[i] = 1

for key, value in count.items():
    print(key, "=", value, end=", ")


#replace one ch with other
n = "rajuuuun"
n1 = " "
for ch in n:
    if ch == "u":
        n1+="a"
    else:
        n1+=ch
    
print(n1)



text = "hello world"
char = "d"

for i in range(len(text)-1,-1,-1):
    if text[i] == char:
        print("Last occurrence of", char, "is at index", i)
        break
    
#
text = "hello world"
char = "o"

for i in range(len(text)):
    if text[i] == char:
        print("First occurrence of", char, "is at index", i)
        break


str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

if str1 == str2:
    print("Same strings")
else:
    print("Not same")



#captalize
text = "i am good boy"
# Method 1: Using split and loop
words = text.split()
capitalized_words = [word.capitalize() for word in words]
result = " ".join(capitalized_words)
print("Capitalized:", result)

# Method 2: Shortcut using title()
print("Capitalized (shortcut):", text.title())

#remove duplicates
name = "reddy"
raj = ""
for ch in name:
    if ch  not in raj:
        raj+=ch
print(raj)


#longest length of word
name = "i am python programing"

words = name.split()
largest = words[0]

for w in words:
    if len(w)>len(largest):
        largest = w
print(largest)

def fiboLastDigit(n):
    a = 1
    b = 1

    if n == 1 or n == 2:
        return 1

    for i in range(3, n + 1):
        c = (a + b) % 10
        a = b
        b = c

    return b

n = int(input())
print(fiboLastDigit(n))
'''


#lucky number
MOD = 1000000007

t = int(input())

for _ in range(t):
    n = int(input())
    
    ans = 0
    
    # 2^i + 2^j gives exactly two set bits
    for i in range(60):
        for j in range(i + 1, 60):
            
            lucky = (1 << i) + (1 << j)
            
            if lucky <= n:
                ans = (ans + lucky) % MOD
    
    print(ans)