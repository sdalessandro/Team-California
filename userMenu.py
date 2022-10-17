import User
# ---------------------------------------------------------------------------------- #
# additional options on whether the user is searching for a job, learning a skill, or communicating with others 

def mainMenu(curUser, userList, friendDic):

    baseMenu = "\t1. Job Listings\n\
        \t2. Learn a skill\n\
        \t3. Student search\n\
        \t4. Communicate with others\n\
        \t5. Important Links\n"
    pendingFriendList = []
    curFriendLog = {}
    
    for user, userFriends in friendDic:
        if curUser.username != user:
            break
        curFriendLog = userFriends
        for friend, status in userFriends:
            if status == "pending":
                pendingFriendList.append(friend)

    if pendingFriendList:
        friendOptions = input(baseMenu + 
            "\tYou have new pending friend request! Enter f to view them.\n\
            \tEnter 'f' to view them or enter an option 1-5: ")
    else: 
        options = input(baseMenu + 
        "\tPlease select an option 1-5: ")
    
    if int(options) == 1:
        jobListings()
    elif int(options) == 2:
        learnSkill()
    elif int(options) == 3:
        studentSearch(userList, friendDic)
    elif int(options) == 4:
        communicateOthers()
    elif int(options) == 5:
        importantLinksUser()
    elif int(friendOptions) == 'f':
        listFriendReqs(curUser, pendingFriendList, friendDic)
    else:
        options = input("Invalid input. Please select an option 1-5\n")
        mainMenu(userList)
    
def jobListings():

    options = input("What are you looking to do?\n\
        \t1. Browse listings\n\
        \t2. Post a job\n\
        \tPlease select 1 or 2:\n")

    if int(options) == 1:
        file = open("jobListings.txt", mode = 'r')
        for line in file:
            print(line.strip())
    elif int(options) == 2:
        file = open("jobListings.txt", mode = 'r')
        countLines = file.readlines()
        print(len(countLines))
        file.close()
    
        if len(countLines) <= 30:
            name = input("Enter your name: ")
            title = input("Enter a title for the job: ")
            description = input("Enter description: ")
            employer = input("Enter name of employer: ")
            location = input("Enter location: ")
            salary = input("Enter salary: ")

            file = open("jobListings.txt", mode = 'a')
            file.write("\n" + name + "\n")
            file.write(title + "\n")
            file.write(description + "\n")
            file.write(employer + "\n")
            file.write(location + "\n")
            file.write(salary + "\n")
            file.close()
        else: 
            print("Reached max capacity of five job postings")
    else:
        options = input("Invalid input. Please select 1 or 2\n")
        jobListings()
        return

# -------------------------------------------------------------------------------------- #
# Create list of 5 skills for learning a skill section with an additional "do not select a skill" option 
def learnSkill():
    print("Learn a new skill")
    selectSkill = input("Do you want to learn:\n1. Skill 1\n2. Skill 2\n3. Skill 3\n4. Skill 4\
        \n5. Skill 5\n6. Do not select a skill\n\nPlease select 1, 2, 3, 4, 5, or 6:\n")
    
    while int(selectSkill) != 1 and int(selectSkill) != 2 and int(selectSkill) != 3 and int(selectSkill) != 4 and int(selectSkill) != 5 and int(selectSkill) != 6:
        selectSkill = input("Invalid input\nPlease select 1, 2, 3, 4, 5, or 6\n")

    if int(selectSkill) == 1:
        skill_1() #if anyone knows of a more efficient way to do this please let me know 
    elif int(selectSkill) == 2:    
        skill_2()
    elif int(selectSkill) == 3:    
        skill_3()
    elif int(selectSkill) == 4:    
        skill_4()
    elif int(selectSkill) == 5:  
        skill_5()
    elif int(selectSkill) == 6:  
        skill_6()  

def skill_1():
    print("Under construction...")
    
def skill_2():
    print("Under construction...")
    
def skill_3():
    print("Under construction...")
    
def skill_4():
    print("Under construction...")
    
def skill_5():
    print("Under construction...")
    
def skill_6():
    mainMenu(userList)
    
def importantLinksUser():
    choice = input("Select an option:\n\
            1. Copyright Notice\n\
            2. About\n\
            3. Accessibility\n\
            4. User Agreement\n\
            5. Privacy Policy\n\
            6. Cookie Policy\n\
            7. Copyright Policy\n\
            8. Brand Policy\n")


    # create a file that includes all and read file to user

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
            guestControls()
        elif int(choice) == 6:
            print(link_list[15] + '\n' + link_list[16] + '\n' + link_list[17] + '\n' + link_list[18] + '\n' + link_list[19] + '\n' + link_list[20])
        elif int(choice) == 7:
            print(link_list[22] + '\n' + link_list[23])
        elif int(choice) == 8:
            print(link_list[25] + '\n' + link_list[26] + '\n' + link_list[27] + '\n' + link_list[28]);
        else:
            print("Error: Invalid input\n\
                    Please enter a number 1-8.")
            importantLinksUser()

def studentSearch(userList, friendDic):
    resultList = []
    choice = input("Search for a student by:\n\
        \t1. Last name\n\
        \t2. University\n\
        \t3. Major\n\
        Enter your choice: ")

    if int(choice) == 1:
        lastName = input("Enter the last name of the student you are looking for: ")
        for user in userList:
            if user[3] == lastName:
                resultList.append(user)

        if resultList:
            print("The following users match your search:\n")
            for user in resultList:
                print("\t{}\n".format(user[0]))
                
            choice = input("Enter the username you want to send a friend request;\n\
                otherwise, press q to go back to the main menu: ")
            if choice in resultList:
                User.sendFriendRequest(choice, friendDic)
            elif choice == 'q':
                mainMenu(userList)
            else:
                print("Error: Invalid input\n")
                studentSearch(userList)
        else:
            print("A user with the last name {} was not found.".format(lastName))
            mainMenu(userList)
    elif int(choice) == 2:
        print("Under construction")
        studentSearch(userList)
    elif int(choice) == 3:
        print("Under construction")
        studentSearch(userList)
    else:
        print("Error: Invalid input\n\
            Please enter a number 1-3.")
        studentSearch(userList)

def communicateOthers():
    print("Under construction...") 

def guestControls():
    option = input("Select an option:\n\
            1. Guest Controls\n\
            2. Language\n\
            \n\
            0. Go back\n")

    with open("userPreferences.txt", 'a') as file:
        if int(option) == 0:
            importantLinksUser()
        elif int(option) == 1:
            currentPreferences()
            method = input("What would you like to turn off:\n\
                    1. Email\n\
                    2. SMS\n\
                    3. Targeted Advertising\n\
                    \n\
                    0. Go back\n")
            if int(method) == 0:
                guestControls()
            elif int(method) == 1:
                print("Email option turned off")
                file.write("{0} Email: {1} \n".format(User.currentUser, "off"))
            elif int(method) == 2:
                print("SMS option turned off")
                file.write("{0} SMS: {1} \n".format(User.currentUser, "off"))
            elif int(method) == 3:
                print("Targeted advertising turned off")
                file.write("{0} Advertising: {1} \n".format(User.currentUser, "off"))
            else:
                print("Enter a valid value between 0-3");
                guestControls()
        elif int(option) == 2:
            currentPreferences()
            language = input("Which language would you like:\n\
                    1. English\n\
                    2. Spanish\n")
            if int(language) == 1:
                print("English language saved")
                file.write("{0} English: {1} \n".format(User.currentUser, "on"))
            elif int(language) == 2:
                print("Spanish language saved")
                file.write("{0} Spanish: {1} \n".format(User.currentUser, "on"))
            else:
                print("Enter a valid value between 0-2")
                guestControls()
        else:
            print("Enter a valid value between 0-2")
            guestControls()

def currentPreferences():
    i = 0
    with open("userPreferences.txt", 'r') as file:
        preferenceList = [tuple(line.split(' ')) for line in file.readlines()]
        while i < len(preferenceList):
            if preferenceList[i][0] == User.currentUser:
                print(preferenceList[i][1] + preferenceList[i][2])
            i = i + 1

# Prints list of pending friend requests and let's you accept them
def listFriendReqs(curUser, pendingFriendList, friendDic):
    print("Pending friend requests:")
    for username in pendingFriendList):
        print("\t{} would like to be your friend!".format(username))
    
    choice = input("Enter a username above to respond to the request.\n\
        Otherwise, press q to quit")
    if choice == 'q':
        return
    for username in pendingFriendList:
        if choice == username:
            respondToFriendReq(curUser, username, friendDic)
            
# Accept or decline a friend request
def respondToFriendReq(curUser, username, friendDic):
    choice = input("Do you want to accept the friend request from {}? (y/n)".format(username))
    if choice == 'y':
        curUser.acceptFriendReq(username, friendDic)
        print("Request accepted! You are now friends with {}".format(username))
    elif choice == 'n':
        curUser.declineFriendReq(username, friendDic)
        print("You have declined the request from {}".format(username))
    else:
        print("Error: Please enter 'y' or 'n'")
        respondToFriendReq(curUser, username, friendDic)