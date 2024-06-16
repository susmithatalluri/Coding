import random
import string
def generate_password(length):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation
    all_characters = lower + upper + digits + special
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password
try:
    length = int(input("Enter the desired password length: "))
    if length < 1:
        print("Password length should be at least 1.")
    else:
        # Generate and display the password
        password = generate_password(length)
        print("Generated password:", password)
except ValueError:
    print("Please enter a valid number.")
