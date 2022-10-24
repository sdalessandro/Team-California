import User, ast
import sqlite3
# ---------------------------------------------------------------------------------- #
# additional options on whether the user is searching for a job, learning a skill, or communicating with others 

def mainMenu(curUser, userList, friendDic):

    baseMenu = "    1. Job Listings\n\
    2. Learn a skill\n\
    3. Student search\n\
    4. Show my network\n\
    5. Communicate with others\n\
    6. Important Links\n\
    7. Create Profile\n\
    8. View Profile\n\
    9. Logout\n"
  
    pendingFriendList = []
    for user, userFriends in friendDic.items():
        if curUser.username != user:
            continue

        curFriendLog = ast.literal_eval(userFriends)
        
        for friend, status in curFriendLog.items():
            if status == "pending":
                pendingFriendList.append(friend)

    if pendingFriendList:
        option = input(baseMenu + 
            "\nYou have new pending friend request!\n\
Enter 'f' to view them or enter an option 1-9: ")
    else: 
        option = input(baseMenu + "Please select an option 1-9: ")
    
    if option == '1':
        jobListings()
    elif option == '2':
        learnSkill()
    elif option == '3':
        studentSearch(curUser, userList, friendDic)
    elif option == '4':
        showMyNetwork(curUser, userList, friendDic, curFriendLog)
    elif option == '5':
        communicateOthers()
    elif option == '6':
        importantLinksUser()
    elif option == "7":
        createProfile(curUser, userList, friendDic)
    elif option == "8":
        name = curUser.username
        viewProfile(curUser, userList, friendDic, name)
    elif option == '9':
        exit(0)
    elif option == 'f':
        listFriendReqs(curUser, userList, friendDic, pendingFriendList)
    else:
        print("Invalid input. Please select an option 1-9\n")
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

def studentSearch(curUser, userList, friendDic):
    resultList = []
    choice = input("Search for a student by:\n\
    1. Last name\n\
    2. University\n\
    3. Major\nEnter your choice: ")

    if int(choice) == 1:
        lastName = input("Enter the last name of the student you are looking for: ")
        for user in userList:
            if user.lastName == lastName + '\n':
                resultList.append(user)

        if resultList:
            print("The following users match your search:\n")
            for user in resultList:
                print("\t{}\n".format(user.username))
                
            choice = input("Enter the username you want to send a friend request;\n\
otherwise, press q to go back to the main menu: ")
            if choice == 'q':
                mainMenu(curUser, userList, friendDic)
            for user in resultList:
                if choice == user.username:
                    curUser.modFriendReq(choice, friendDic, "pending")
                    mainMenu(curUser, userList, friendDic)
                
            print("Error: Invalid input\n")
            studentSearch(curUser, userList, friendDic)
        else:
            print("A user with the last name {} was not found.".format(lastName))
            mainMenu(curUser, userList, friendDic)
    elif int(choice) == 2:
        print("Under construction")
        studentSearch(curUser, userList, friendDic)
    elif int(choice) == 3:
        print("Under construction")
        studentSearch(curUser, userList, friendDic)
    else:
        print("Error: Invalid input\n\
            Please enter a number 1-3.")
        studentSearch(curUser, userList, friendDic)
    # return "studentSearch"
      
# List your friends and allow removal of friends
def showMyNetwork(curUser, userList, friendDic, curFriendLog):
    print("My friend list:")

    prefile = open("userProfile.txt", "r")
    preferenceList = [tuple(line.split('/')) for line in prefile.readlines()]
    num_lines = sum(1 for line in open('userProfile.txt'))
    profileList = []
    for x in range(num_lines):
      profileList.append(preferenceList[x][0])
    
    x = 0
    for friend in curUser.getFriends(curFriendLog):
        if friend in profileList:
          print("\t{} profile".format(friend))
          x += 1
          continue
        print("\t{}".format(friend))
        x += 1

    choice = input("Would you like to remove any friends? (y/n): ")
    if choice == 'y':
        friendInput = input("Enter the username you would like to unfriend: ")
        for friend in curFriendLog:
            if (friendInput == friend):
                curUser.rmFriend(friendInput, friendDic)
                print("You have removed {} as a friend.".format(friendInput))
                break
        else:
            print("Error: Invalid input, Aborting...")
    elif choice != 'n':
        print("Error: Invalid input, Aborting...")

    choiceProfile = input("Would you like to see any friend's profile? (y/n) ")
    while choiceProfile != "y" and choiceProfile != "n":
      choiceProfile = input("Invalid input. (y/n) ")

    if choiceProfile == "y":
      name = input("Type of username of the friend whose profile you want to see: ")
      viewProfile(curUser, userList, friendDic, name)
  
    mainMenu(curUser, userList, friendDic)
    # return "showNetwork"
    return

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
def listFriendReqs(curUser, userList, friendDic, pendingFriendList):
    print("Pending friend requests:")
    for username in pendingFriendList:
        print("\t{} would like to be your friend!".format(username))
    
    choice = input("\nEnter a username above to respond to the request.\n\
Otherwise, press q to quit: ")
    if choice == 'q':
        mainMenu(curUser, userList, friendDic)
        return
    for username in pendingFriendList:
        if choice == username:
            respondToFriendReq(curUser, userList, friendDic, username)

# Accept or decline a friend request
def respondToFriendReq(curUser, userList, friendDic, username):
    choice = input("Do you want to accept the friend request from {}? (y/n): ".format(username))
    if choice == 'y':
        curUser.modFriendReq(username, friendDic, "accepted")
        print("Request accepted! You are now friends with {}".format(username))
    elif choice == 'n':
        curUser.modFriendReq(username, friendDic, "declined")
        print("You have declined the request from {}".format(username))
    else:
        print("Error: Please enter 'y' or 'n'")
        respondToFriendReq(curUser, userList, friendDic, username)

    mainMenu(curUser, userList, friendDic)
    return

  
def createProfile(curUser,userList,friendDic):
    prefile = open("userProfile.txt", "r")
    preferenceList = [tuple(line.split('/')) for line in prefile.readlines()]

    num_lines = sum(1 for line in open('userProfile.txt')) #number of lines in file
    breaker = 0
    #preferenceList[x][0] will iterate through the users in userProfile.txt
    #check if user has already created a profile or not
    for x in range(num_lines):
      if curUser.username == preferenceList[x][0]:
        print("Profile has already been created!")
        decision = input("Edit profile? (y/n) ")
        while decision != "y" and decision != "n":
          decision = input("Invalid input. Edit profile? (y/n) ")

        if decision == "y":
          edit = input("Which part do you want to edit?\n1. Title\n2. Major\n3. University\n4. About\n5. Experience\n6. Education\n")
          while edit != "1" and edit != "2" and edit != "3" and edit != "4" and edit != "5" and edit != "6":
            edit = input("Invalid input. Please enter 1 - 5: ")

          lineRemove = curUser.username + "/" + preferenceList[x][1] + "/" + preferenceList[x][2] + "/" + preferenceList[x][3] + "/" + preferenceList[x][4]
          
          if edit == "1":
            print(preferenceList[x][1])
            newTitle = input("New title: ")
            breaker = 1
            #finds lineRemove variable in the txt file and deletes it 
            with open("userProfile.txt", "r+") as f:
              d = f.readlines()
              f.seek(0)
              for i in d:
                if i != lineRemove:
                  f.write(i)
              f.truncate()

            #write a new line into the txt file 
            file = open("userProfile.txt", 'a')
            file.write(f"{curUser.username}/{newTitle}/{preferenceList[x][2]}/{preferenceList[x][3]}/{preferenceList[x][4]}\n")
            file.close()
            print("Title updated!")
            mainMenu(curUser, userList, friendDic) #goes back to main menu
          
          elif edit == "2":
            print(preferenceList[x][2])
            newMajor = input("New major: ")
            breaker = 1
            #finds lineRemove variable in the txt file and deletes it 
            with open("userProfile.txt", "r+") as f:
              d = f.readlines()
              f.seek(0)
              for i in d:
                if i != lineRemove:
                  f.write(i)
              f.truncate()

            #write a new line into the txt file 
            file = open("userProfile.txt", 'a')
            file.write(f"{curUser.username}/{preferenceList[x][1]}/{newMajor}/{preferenceList[x][3]}/{preferenceList[x][4]}\n")
            file.close()
            print("Major updated!")
            mainMenu(curUser, userList, friendDic) #goes back to main menu

          elif edit == "3":
            print(preferenceList[x][3])
            new = input("New university: ")
            breaker = 1
            #finds lineRemove variable in the txt file and deletes it 
            with open("userProfile.txt", "r+") as f:
              d = f.readlines()
              f.seek(0)
              for i in d:
                if i != lineRemove:
                  f.write(i)
              f.truncate()

            #write a new line into the txt file 
            file = open("userProfile.txt", 'a')
            file.write(f"{curUser.username}/{preferenceList[x][1]}/{preferenceList[x][2]}/{new}/{preferenceList[x][4]}\n")
            file.close()
            print("University updated!")
            mainMenu(curUser, userList, friendDic) #goes back to main menu
        
          elif edit == "4":
              print(preferenceList[x][4])
              new = input("New about: ")
              breaker = 1
              #finds lineRemove variable in the txt file and deletes it 
              with open("userProfile.txt", "r+") as f:
                d = f.readlines()
                f.seek(0)
                for i in d:
                  if i != lineRemove:
                    f.write(i)
                f.truncate()
  
              #write a new line into the txt file 
              file = open("userProfile.txt", 'a')
              file.write(f"{curUser.username}/{preferenceList[x][1]}/{preferenceList[x][2]}/{preferenceList[x][3]}/{new}\n")
              file.close()
              print("About updated!")
              mainMenu(curUser, userList, friendDic) #goes back to main menu
          elif edit == "5":
              experience(curUser, userList, friendDic)
              breaker = 1
          elif edit == "6":
              education(curUser, userList, friendDic)
              breaker = 1
    
        elif decision == "n":
          breaker = 1
          mainMenu(curUser, userList, friendDic)
          
    if breaker == 0:  
      title = input("Create profile\nPlease enter the title: ")
      major = input("Enter your major: ")
      university = input("Enter your university: ")
      about = input("Tell us about yourself: ")
      print("Profile created!\n")
      exp = input("Add experience? (y/n) ")
      file = open("userProfile.txt", 'a')
      file.write(f"{curUser.username}/{title}/{major}/{university}/{about}\n")
      file.close()
      
      
      while exp != "y" and exp != "n":
        exp = input("Invalid input. Add experience? (y/n) ")
  
      if exp == "y":
        experience(curUser, userList, friendDic)
  


  
    #for choice in userList 

def viewProfile(curUser,userList,friendDic, username):
    db = sqlite3.connect("profile.db")
    cur = db.cursor()  

    db2 = sqlite3.connect("education.db")
    cur2 = db2.cursor()
    
    prefile = open("userProfile.txt", "r")
    preferenceList = [tuple(line.split('/')) for line in prefile.readlines()]

    num_lines = sum(1 for line in open('userProfile.txt')) #number of lines in file
    foundProfile = False
    #preferenceList[x][0] will iterate through the users in userProfile.txt
    #check if user has already created a profile or not
    for x in range(num_lines):
      if username == preferenceList[x][0]:
        #profile has been found 
        print(username)
        print("Title: " + preferenceList[x][1])
        print("Major: " + preferenceList[x][2])
        print("University: " + preferenceList[x][3])
        print("Description: " + preferenceList[x][4])
        foundProfile = True

        exp = cur.execute("SELECT * FROM experience WHERE username=?", (username,))
        expList = exp.fetchall()

        for num, exp in enumerate(expList):
          print(f"Experience {num + 1}")
          print("Title: " + exp[1])
          print("Employer: " + exp[2])
          print("Date started: " + exp[3])
          print("Date ended: " + exp[4])
          print("Location: " + exp[5])
          print("Description: " + exp[6] + "\n")

        exp2 = cur2.execute("SELECT * FROM education WHERE username=?", (username,))
        exp2List = exp2.fetchall()
        if exp2:  
          for exp in exp2List: 
            print(exp[1])
            print(exp[2])
            print(exp[3])
            
        mainMenu(curUser, userList, friendDic)
                 
    if foundProfile == False:
      print("Profile not found.")
      mainMenu(curUser, userList, friendDic)

    #return "createdProfile"

def experience(curUser, userList, friendDic):  
  db = sqlite3.connect("profile.db")
  cur = db.cursor()  
  cur.execute("CREATE TABLE IF NOT EXISTS experience('username' TEXT NOT NULL, 'title' TEXT, 'employer' TEXT, 'dateStarted' TEXT, 'dateEnded' TEXT, 'location' TEXT, 'description' TEXT)")
  flag = 0 
  ask = input("Would you like to edit an experience? (y/n) ")
  while ask != "y" and ask != "n":
    ask = input("Invalid input. (y/n) ")
    
  if ask == "y":
    expNum = input("Which experience would you like to edit? (Insert title of experience) ")
    
    exist2 = cur.execute("SELECT title FROM experience WHERE title=?", (expNum,))
    exist = exist2.fetchall()
    
    if exist:
      expTitle = input("New Experience 1\nTitle: ")
      expEmployer = input("New Employer: ")
      expDateStarted = input("New Date started: ")
      expDateEnded = input("New Date ended: ")
      expLocation = input("New Location: ")
      expDescription = input("New Description: ")
      cur.execute("UPDATE experience SET title=?, employer=?, dateStarted=?, dateEnded=?, location=?, description=? WHERE title=?", (expTitle, expEmployer, expDateStarted, expDateEnded, expLocation, expDescription, expNum,))
      db.commit()
      print("Experience updated")
      flag = 1
      mainMenu(curUser, userList, friendDic)
    else:
      print("Experience title not found")

  
  experienceCount = cur.execute("SELECT username FROM experience WHERE username=?", (curUser.username,))
  expCount = (len(experienceCount.fetchall()))
  
  if expCount == 3 and flag == 0:
    print("Maximum number of experiences reached\n")
    mainMenu(curUser, userList, friendDic)
  else:
    expTitle = input("Experience 1\nTitle: ")
    expEmployer = input("Employer: ")
    expDateStarted = input("Date started: ")
    expDateEnded = input("Date ended: ")
    expLocation = input("Location: ")
    expDescription = input("Description: ")
  
    
    cur.execute("INSERT INTO experience (username, title, employer, dateStarted, dateEnded, location, description) VALUES (?, ?, ?, ?, ?, ?, ?)", (curUser.username, expTitle, expEmployer, expDateStarted, expDateEnded, expLocation, expDescription))
    db.commit()
    mainMenu(curUser, userList, friendDic)

def education(curUser, userList, friendDic):
  db = sqlite3.connect("education.db")
  cur = db.cursor()  
  cur.execute("CREATE TABLE IF NOT EXISTS education('username' TEXT NOT NULL, 'schoolName' TEXT, 'degree' TEXT, 'yearsAttended' TEXT)")

  nameCheck = cur.execute("SELECT username FROM education WHERE username=?", (curUser.username,))

  if nameCheck:
    print("Education section already found.")
  else:
    schoolName = input("School name: ")
    degree = input("Degree: ")
    yearsAttended = input("Years attended: ")
    
    cur.execute("INSERT INTO education (username, schoolName, degree, yearsAttended) VALUES (?, ?, ?, ?)", (curUser.username, schoolName, degree, yearsAttended))
    db.commit()
    print("Education added!\n")
    mainMenu(curUser, userList, friendDic)

  # return "education"
  
