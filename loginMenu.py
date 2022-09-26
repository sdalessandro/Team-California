import User, userMenu

def mainMenu(userList):
    
    options = input("\nSelect an option below:\n\
        1. Login\n\
        2. Sign up\n\
        3. Why join InCollege? (video)\n\
        4. Find a friend\n")
    
    if int(options) == 1:
        login(userList)
    elif int(options) == 2:
        User.createUser(userList)
    elif int(options) == 3:
        whyJoin()
    elif int(options) == 4:
        findFriends(userList)
    else:
        print("Error: Invalid input\n\
            Please select 1, 2, 3, or 4\n")
        mainMenu(userList)

def login(userList):
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    for user in userList:
        if user.username == username and user.password == password:
            print("Login successful!")
            userMenu.mainMenu()
            return
            
    print("Error: Login unsuccessful. Please try again")
    mainMenu(userList)

def whyJoin():
    choice = input("Would you like to learn more about how inCollege can help you? (y or n): ")
    if choice == "y":
        print("Video is now playing")

    mainMenu(userList)

def findFriends(userList):
    firstName = input("Enter your friend's first name: ")
    lastName = input("Enter your friend's last name: ")

    for user in userList:
        print(user.firstName)
        print(user.lastName)
        if user.firstName == firstName and user.lastName == (lastName + "\n"):
            print("Your friend is part of the InCollege system!")
            option = input("Would you like to create an account to join " + firstName + "? (y or n): ")
            if option == 'y':
                User.createUser(userList)

    print("{0} {1} is not a member of InCollege.".format(firstName, lastName))

def successStory():
    print("\"Joining inCollege has given me the opportunity to find my current career by providing me with connections and skills I needed\" - Jason, graduate")