# Relational operators are used to compare two values.They return a boolean value (True or False) based on the comparison.

# Example usage of relational operators in Python 
a = 10
b = 20
print("a =", a)
print("b =", b)

# Equal to (==)
print("a == b:", a == b)  # False

# Not equal to (!=)
print("a != b:", a != b)  # True

# Greater than (>)
print("a > b:", a > b)    # False

# Less than (<)
print("a < b:", a < b)    # True

# Greater than or equal to (>=)
print("a >= b:", a >= b)  # False

# Less than or equal to (<=)
print("a <= b:", a <= b)  # True

# You can also use relational operators in conditional statements
if a < b:
    print("a is less than b")
else:
    print("a is not less than b")

# Example of using relational operators in a function
def compare_numbers(x, y):
    if x == y:
        return "x is equal to y"
    elif x > y:
        return "x is greater than y"
    else:
        return "x is less than y"   
result = compare_numbers(15, 10)
print(result)  # Output: x is greater than y

