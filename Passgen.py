import random
import string

print("===== PASSWORD GENERATOR =====")

length = int(input("Enter password length: "))

# Characters for password
characters = string.ascii_letters + string.digits + string.punctuation

# Generate password
password = ""

for i in range(length):
    password += random.choice(characters)

print("Your Password is:", password)