users = {
    "digvijay": "12345",
    "admin": "admin123"
}

username = input("Enter username: ")
password = input("Enter password: ")

if username in users and users[username] == password:
    print("Login successful!")
    print("Welcome", username)
else:
    print("Invalid username or password")