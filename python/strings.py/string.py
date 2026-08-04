# A String is a group of charachters.str represents string datatype.
# name = 'raju'
#name2 = "raju".  There is no difference between these two.
str = ''' welcome to python. it is the fastest growing programming language across the globe.
           it is esay to learn '''
print(str)
# the above str tells us the para's can be written using triple single quotes.
# strings are nothing but names,places etc which are enclosed inside quotes.


#access each character usinh while loop
name = "vara Prasad"
n = len(name)
i = 0
while i < n:
    print(name[i],end = "")
    i+=1
print()

#access each charachter in reverse order
i = -1
while i >= -n:
    print(name[i])
    i -= 1
print()

#access each charachter in reverse order using negative string
i = -1
while i < n:
    print(name[-i],end ="")
    i+=1
print()

name = 'varaprasad is a "good" guy'
print(name)

a1 = "welome to core python \n 'it is easy to learn' "
print(a1) # taking it to next line

a2 = "welocme to \b python"
print(a2) # \b represents backspace

a3 = "welcome to python.\t fastest growing language "
print(a3) # \t represents horizontal tab space

#length of  a string . it tells us number of characters in a string
name = "vara prasad"
print(len(name))

#indexing in strings
#indexing represents the position number of characters. it is written using []
#example
word = "Hello"

print(word[0])    # H
print(word[1])    # e
print(word[-1])   # o
print(word[-5])   # H

word = "Hello"

print(word[0])    # H
print(word[1])    # e
print(word[-1])   # o
print(word[-5])   # H


#slicing the string. slicing is nothing but it represents step or part of a given string
#slicing format = [start:stop:size]
# Complete String Slicing Example

text = "PythonProgramming"

print("String:", text)
print("-----------------------------------------")

# Basic Slicing (start:stop)
print("1. text[0:6]        →", text[0:6])         # Python

#  From Middle
print("2. text[6:17]       →", text[6:17])       # Programming

# Start Omitted
print("3. text[:6]         →", text[:6])         # Python

# Stop Omitted
print("4. text[6:]         →", text[6:])         # Programming

# Full String
print("5. text[:]          →", text[:])          # PythonProgramming

#  Using Step
print("6. text[0:17:2]     →", text[0:17:2])     # Pto rgamn

#  Only Step
print("7. text[::3]        →", text[::3])        # PhPrgm

# Negative Index Slicing
print("8. text[-11:-1]     →", text[-11:-1])     # rogrammin

#  Reverse String
print("9. text[::-1]       →", text[::-1])       # gnimmargorPnohtyP

# Reverse with Step
print("10. text[::-2]       →", text[::-2])      # gimagrPohy

#Repeatig the strings. Repetition operator is denoted by *. it is used to repeat the string for several times.
#example
name = "vikram rathode"
print(name*2)
#repeating part of a string by slicing
name = "python"
name2 = name[2:3]*2
print(name2)

#adding strings by + symbol
name1 ="hello"
name2 = "world"
print(name1 + "|" + name2)

#program to check whether a sub string exists in main string or not
pro = " python is very easy to learn"
pr = "very"
if pr in pro:
    print(pr+' found in pro')
else:
    print(pr+'not found in pro')





#exampless

ori = 2008

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