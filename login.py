def login():

    users = {
        "vignesh": "password123",
        "admin": "admin@123",
        "user": "user2025"
    }

    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Authentication
    if username in users and users[username] == password:
        print("Login successful!")
    else:
        print("Invalid username or password.")

login()