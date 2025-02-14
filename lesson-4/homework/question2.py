def print_squares(n):
    for i in range(1, n):
        print(i * i)  # Bitwise equivalent: (i << log2(i)) when i is a power of 2

# Test case
print_squares(5)