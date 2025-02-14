def check_password():
    while True:
        password = input("Enter your password: ")

        if len(password) < 8:
            print("Password is too short.")
        elif not any(char.isupper() for char in password):
            print("Password must contain an uppercase letter.")
        else:
            print("Password is strong.")
            break  # Exit the loop when a strong password is entered

# Run the password checker
check_password()