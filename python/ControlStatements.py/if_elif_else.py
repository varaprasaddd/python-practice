#program for if-elif-else statement.The programmer has to test multiple conditions and execute statements depending on those conditions.
a = 33
b = 200
if b > a:
    print("b is greater than a")   
elif a == b:
    print("a is equal to b")
else:
    print("a is greater than b")
    
#example
ori = 2008

n = int(input("Enter the PIN: "))

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