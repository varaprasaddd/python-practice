# Bitwise operators in Python
# Bitwise operators are used to perform bitwise operations on integers.
# The main bitwise operators are AND (&), OR (|), XOR (^), NOT (~), Left Shift (<<), and Right Shift (>>).
# Example usage of bitwise operators in Python
a = 10  # Binary: 1010
b = 4   # Binary: 0100

print("a =", a)
print("b =", b)

# Bitwise AND operator (&)
print("a & b:", a & b)  # Output: 0 (Binary: 0000)

# Bitwise OR operator (|)
print("a | b:", a | b)  # Output: 14 (Binary: 1110)

# Bitwise XOR operator (^)
print("a ^ b:", a ^ b)  # Output: 14 (Binary: 1110)

# Bitwise NOT operator (~)
print("~a:", ~a)   # Output: -11 (Binary: ...11110101)

# Left shift operator (<<)
print("a << 2:", a << 2)   # Output: 40 (Binary: 1010 followed by two zeros)

# Right shift operator (>>)
print("a >> 2:", a >> 2)   # Output: 2 (Binary: The last two bits are removed)