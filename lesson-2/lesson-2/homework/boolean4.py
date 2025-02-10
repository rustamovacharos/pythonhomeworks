a=int(input(""))
b=int(input(""))
c=int(input(""))
print(f"a is {a},b is {b} and c is {c}"*(a!=b and a!=c and b!=c) or "same")