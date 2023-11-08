
# User data is stored in a dictionary
user_data = {}

#Login function
def login():
    while True:
        username = input("\nEnter your username: ")
        password = input("Enter your password: ")

        if username and password in user_data:
            print("\nLogin successful")
            break
        else:
            print("\nIncorrect username or password.")

          
#Register function
def register():
    username = input("\nEnter a username to register: ")
    
    if username in user_data:
        print("\nUsername already exists.")
    else:
        password = input("Enter a password: ")
        user_data[username] = password
        print("\nRegistration successful.")

#Main menu
while True:
    print("\nWelcome to the Login Page")
    print("1. Login") #Login with the current username and password
    print("2. Register") #Enter new usename and passowrd to register
    print("3. Exit") #Exit the login page

    choice = input("\nEnter your choice (1/2/3): ")

    if choice == "1":
        login()
    elif choice == "2":
        register()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("\nPlease select a valid option (1/2/3).")
