MINIMUM_LENGTH = 8
password = input(f"Enter a password (minimum {MINIMUM_LENGTH} characters): ")
while len(password) < MINIMUM_LENGTH:
    print(f"Password is too short! It must be at least {MINIMUM_LENGTH} characters.")
    password = input(f"Enter a password (minimum {MINIMUM_LENGTH} characters): ")
print('*' * len(password))
