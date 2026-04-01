# Boolean operators in Python
# Boolean operators are used to perform logical operations on boolean values (True and False).
# The three main boolean operators are AND, OR, and NOT.
# Example usage of boolean operators in Python
a = True
b = False
print("a =", a)
print("b =", b)

# Boolean AND operator
print("a and b:", a and b)  # False
print("a and True:", a and True)  # True
print("b and False:", b and False)  # False

# Boolean OR operator
print("a or b:", a or b)   # True
print("a or False:", a or False)  # True
print("b or True:", b or True)  # True

# Boolean NOT operator
print("not a:", not a)  # False
print("not b:", not b)  # True

# You can also use boolean operators in conditional statements
if a and not b:
    print("Condition met: a is True and b is False")
else:
    print("Condition not met")