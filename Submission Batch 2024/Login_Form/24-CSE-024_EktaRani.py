
stored_username = "student123"
stored_password = "python123"

# User input
username = input("Enter username: ")
password = input("Enter password: ")


if username == stored_username and password == stored_password:
    print("Login Successful!")
else:
    print("Login Failed. Please try again.")