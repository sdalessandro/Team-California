import User, userMenu

def mainMenu(userList):
    
    options = input("\nSelect an option:\n\
        1. Login\n\
        2. Sign up\n\
        3. Why join InCollege? (video)\n\
        4. Find a friend\n\
        5. Useful Links\n\
        6. InCollege Important Links\n")
    
    if int(options) == 1:
        login(userList)
        return
    elif int(options) == 2:
        User.createUser(userList)
        return
    elif int(options) == 3:
        whyJoin()
        return
    elif int(options) == 4:
        findFriends(userList)
        return
    elif int(options) == 5:
        usefulLinks(userList)
        return
    elif int(options) == 6:
        importantLinks()
        return
    else:
        print("Error: Invalid input\n\
            Please select a choice 1-6\n")
        mainMenu(userList)

def login(userList):
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    for user in userList:
        if user.username == username and user.password == password:
            User.currentUser = user.username
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


def usefulLinks(userList):
    
    options = input("\nSelect an option:\n\
        1. General\n\
        2. Browse InCollege\n\
        3. Business Solutions\n\
        4. Directories\n\
        \n\
        0. Go Back\n")

    if int(options) == 0:
        mainMenu(userList)
        return
    elif int(options) == 1:
        generalLinks(userList)
        return
    elif int(options) == 2:
        print("Under construction")
    elif int(options) == 3:
        print("Under construction")
    elif int(options) == 4:
        print("Under construction")
    else:
        print("Error: Invalid input\n\
            Please select a choice 1-4\n")

def generalLinks(userList):

    options = input("\nSelect an option:\n\
        1. Sign Up\n\
        2. Help Center\n\
        3. About\n\
        4. Press\n\
        5. Blog\n\
        6. Careers\n\
        7. Developers\n\
        \n\
        0. Go Back\n")

    if int(options) == 0:
        usefulLinks()
        return
    if int(options) == 1:
        User.createUser(userList)
        return
    elif int(options) == 2:
        print("We're here to help")
        return
    elif int(options) == 3:
        print("In College: Welcome to In College, the world's largest college student network with many users in many countries and territories worldwide")
        return
    elif int(options) == 4:
        print("In College Pressroom: Stay on top of the latest news, updates, and reports")
        return
    elif int(options) == 5:
        print("Under construction")
        return
    elif int(options) == 6:
        print("Under construction")
        return
    elif int(options) == 7:
        print("Under construction")
        return
    else:
        print("Error: Invalid input\n\
	    Please select a choice 1-7\n")
        generalLinks(userList)

def importantLinks():

    choice = input("Select an option:\n\
            1. Copyright Notice\n\
            2. About\n\
            3. Accessibility\n\
            4. User Agreement\n\
            5. Privacy Policy\n\
            6. Cookie Policy\n\
            7. Copyright Policy\n\
            8. Brand Policy\n")
    
    with open("importantLinks.txt") as file:
        data = file.readlines()
        link_list = [x.strip() for x in data]

        if int(choice) == 1:
            print(link_list[0] + '\n' + link_list[1])
        elif int(choice) == 2:
            print(link_list[3] + '\n' + link_list[4])
        elif int(choice) == 3:
            print(link_list[6] + '\n' + link_list[7])
        elif int(choice) == 4:
            print(link_list[9] + '\n' + link_list[10])
        elif int(choice) == 5:
            print(link_list[12] + '\n' + link_list[13])
        elif int(choice) == 6:
            print(link_list[15] + '\n' + link_list[16] + '\n' + link_list[17] + '\n' + link_list[18] + '\n' + link_list[19] + '\n' + link_list[20])
        elif int(choice) == 7:
            print(link_list[22] + '\n' + link_list[23])
        elif int(choice) == 8:
            print(link_list[25] + '\n' + link_list[26] + '\n' + link_list[27] + '\n' + link_list[28]);
        else: 
            print("Error: Invalid input\n\
                    Please enter a number 1-8.")
            importantLinks()

