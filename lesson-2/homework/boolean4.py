a=int(input(""))
b=int(input(""))
c=int(input(""))
all_different = a!=b and b != c and a != c
print("all numbers are different"if all_different else "At least two numbers are the same.")