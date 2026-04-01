# Logical operators are used to combine conditional statements in Python.
# The three main logical operators are AND, OR, and NOT.

# Example usage of logical operators in Python
a = 10
b = 5
c = 15
print("a =", a)
print("b =", b)
print("c =", c)

# Logical AND (and)
print("a > b and a < c:", a > b and a < c)  # True
print("a < b and a < c:", a < b and a < c)  # False

# Logical OR (or)
print("a > b or a < c:", a > b or a < c)   # True
print("a < b or a > c:", a < b or a > c)   # False

# Logical NOT (not)
print("not(a > b):", not(a > b))  # False
print("not(a < b):", not(a < b))  # True

# You can also use logical operators in conditional statements
if a > b and a < c:
    print("a is greater than b and less than c")
else:
    print("Condition not met")