username = str(input("")).strip()
password = str(input("")).strip()
is_empty = not username and not password  # True if both are empty
print("both are empty" if is_empty else "both are not empty")