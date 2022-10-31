import User, ast
import sqlite3
import datetime

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
        jobListings(curUser, userList, friendDic)
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
    
def jobListings(curUser, userList, friendDic):
    db = sqlite3.connect("jobListings.db")
    cur = db.cursor()  
    cur.execute("CREATE TABLE IF NOT EXISTS jobListings('poster' TEXT NOT NULL, 'title' TEXT, 'description' TEXT, 'employer' TEXT, 'location' TEXT, 'salary' TEXT)")
    print("Current user: ", curUser.username)
    sm1_query3 = sqlite3.connect("jobListings.db")
    curz = sm1_query3.cursor()
    curz.execute("CREATE TABLE IF NOT EXISTS savedJobs('user' TEXT NOT NULL, 'title' TEXT)")
  #prnt = cur.execute("SELECT * FROM jobApplications")
    d1 = sqlite3.connect("jobApplications.db")
    cur1 = d1.cursor()
    prnt = cur1.execute("SELECT * FROM jobApplications WHERE user=?",(curUser.username,))
        
    x = prnt.fetchall()
    d2 = sqlite3.connect("jobListings.db")
    cur2 = d2.cursor()

    for i in x:
      cur2.execute("SELECT * FROM jobListings WHERE poster = ? AND title = ?", (i[1], i[2]))
      ex1 = cur2.fetchall()
      if ex1:
        pass
        #print("This job " + i[2] + "has not been deleted") 
      else:
        print("The job you applied for: " + "(" + i[2] + ")" + " has been deleted*") 

    options = input("What are you looking to do?\n\
      1. Generate lists\n\
      2. Post a job\n\
      3. Apply to a job\n\
      4. Delete a job you posted\n\
Please select one of the options above:\n")

    while options != "1" and options != "2" and options != "3" and options != "4":
      options = input("Invalid input")
    
    if options == "1":
        sub_menu_1 = input("What are you looking to do?\n\
        1. Browse all job listings\n\
        2. Browse jobs that you applied for\n\
        3. Browse jobs that you have not applied for\n\
        4. Browse jobs that you have saved\n")

        while sub_menu_1 != "1" and sub_menu_1 != "2" and sub_menu_1 != "3" and sub_menu_1 != "4":
          sub_menu_1 = input("Invalid input")

        if sub_menu_1 == "1":
        # file = open("jobListings.txt", mode = 'r')
        # for line in file:
        #     print(line.strip())
          
          prnt = cur.execute("SELECT * FROM jobListings") #should this not be cur?
          x = prnt.fetchall()
      
          for i in x:
            print()
            print("Poster: " + i[0]) #poster
            print("Title: " + i[1]) #title
            print("Description: " + i[2]) #description
            print("Employer: " + i[3]) #employer
            print("Location: " + i[4]) #location
            print("Salary: " + i[5]) #salary
      
            d = sqlite3.connect("jobApplications.db")
            curd = d.cursor() 
            curd.execute("SELECT * FROM jobApplications WHERE user = ? AND poster = ? AND title = ?",(curUser.username, i[0], i[1],))
            exe = curd.fetchall()
            if exe:
              print("You have applied for this job!")

            
          saved_job = input("If you would like to save a job enter its title, otherwise press 'q' to quit:")
          if(saved_job == 'q'):
            exit(-1)
          sm1_query4 = sqlite3.connect("jobListings.db")
          sm1_cur4 = sm1_query4.cursor()
          sm1_cur4.execute("SELECT * FROM jobListings")
          exe4 = sm1_cur4.fetchall()
          if exe4:
            sm1_query4.execute("INSERT INTO savedJobs(user,title) VALUES(?,?)", (curUser.username, saved_job))
            sm1_query4.commit()
          else:
            print("job name not listed")
            exit(-1)
          print("\n")
        elif sub_menu_1 == "2":
          prnt2 = cur.execute("SELECT * FROM jobListings")
          c = prnt2.fetchall()

          for i in c:
            sm1_query = sqlite3.connect("jobApplications.db")
            sm1_cur = sm1_query.cursor()
            sm1_cur.execute("SELECT * FROM jobApplications WHERE user = ? AND poster = ? AND title = ?", (curUser.username, i[0], i[1]))
            ex2 = sm1_cur.fetchall()
            if ex2:
              print()
              print("Poster: " + i[0]) #poster
              print("Title: " + i[1]) #title
              print("Description: " + i[2]) #description
              print("Employer: " + i[3]) #employer
              print("Location: " + i[4]) #location
              print("Salary: " + i[5]) #salary
              print()
        
        elif sub_menu_1 == "3":
          prnt3 = cur.execute("SELECT * FROM jobListings")
          c1 = prnt3.fetchall()

          for i in c1:
            sm1_query2 = sqlite3.connect("jobApplications.db")
            sm1_cur2 = sm1_query2.cursor()
            sm1_cur2.execute("SELECT * FROM jobApplications WHERE user = ? AND poster = ? AND title = ?", (curUser.username, i[0], i[1]))
            ex3 = sm1_cur2.fetchall()
            if not ex3: #if not something youve already applied for
              print()
              print("Poster: " + i[0]) #poster
              print("Title: " + i[1]) #title
              print("Description: " + i[2]) #description
              print("Employer: " + i[3]) #employer
              print("Location: " + i[4]) #location
              print("Salary: " + i[5]) #salary
              print()
        elif sub_menu_1 == "4":
          sm1_query5 = sqlite3.connect("jobListings.db")
          sm1_cur5 = sm1_query5.cursor()
          prnt4 = sm1_cur5.execute("SELECT * FROM savedJobs")
          #for row in prnt4.fetchall():
            #print(row)
          
          for i in prnt4:
            print("Job: " + i[1])
            print()

          save_or_nah = input("If you would like to unsave any of these jobs enter 'u', otherwise enter 'q' to quit: ")
          if(save_or_nah == 'u'):
            donzo = input("Which job would you like to delete?:")
            sm1_query6 = sqlite3.connect("jobListings.db")
            sm1_cur6 = sm1_query6.cursor()
            query_delete_2= sm1_cur6.execute("DELETE FROM savedJobs WHERE title = ?", (donzo,))
            sm1_query6.commit()
            print("You have deleted " + donzo + " from the saved jobs list\n")
          elif(save_or_nah == 'q'):
            exit(-2)
        mainMenu(curUser, userList, friendDic)
          
    elif options == "2":
        prnt = cur.execute("SELECT * FROM jobListings")
        x = prnt.fetchall()
      
        if len(x) <= 10:
            # name = input("Enter your name: ")
            title = input("Enter a title for the job: ")
            description = input("Enter description: ")
            employer = input("Enter name of employer: ")
            location = input("Enter location: ")
            salary = input("Enter salary: ")

            cur.execute("INSERT INTO jobListings(poster, title, description, employer, location, salary) VALUES (?, ?, ?, ?, ?, ?)", (curUser.username, title, description, employer, location, salary))
            db.commit()
        else: 
            print("Reached max capacity of ten job postings")
    elif options == "3":    
 
      poster = input("Input poster: ")
      title = input("Input title: ")
      
      if poster == curUser.username:
        print("You cannot apply to a job you posted!")
        mainMenu(curUser, userList, friendDic)
      else:
        exe = cur.execute("SELECT * FROM jobListings WHERE poster=? AND title=?", (poster, title,))
        tmp = exe.fetchall() # check if specific jobposting exists
        if tmp: #if it does exist...

          d = sqlite3.connect("jobApplications.db")
          curd = d.cursor()  
          curd.execute("CREATE TABLE IF NOT EXISTS jobApplications('user' TEXT NOT NULL, 'poster' TEXT, 'title' TEXT, 'graduationDate' TEXT, 'startDate' TEXT, 'goodFit' TEXT)")

          tempexe = curd.execute("SELECT * FROM jobApplications WHERE user=? AND poster=? AND title=?", (curUser.username, poster, title,))
          x = tempexe.fetchall()
          if x: #check if user has already applied to the job 
            print("You have already applied to this job!\n")
            mainMenu(curUser, userList, friendDic)
          else:    
            graduationDate = input("When do you graduate (mm/dd/yyyy)? ")
            startDate = input("When can you start working (mm/dd/yyyy)? ")
            goodFit = input("Why do you think you would be a good fit for this job? ")
          
            curd.execute("INSERT INTO jobApplications(user, poster, title, graduationDate, startDate, goodFit) VALUES (?, ?, ?, ?, ?, ?)", (curUser.username, poster, title, graduationDate, startDate, goodFit))
            #poster and title identify the jobListing that curUser is applying t
            d.commit()
            mainMenu(curUser, userList, friendDic)
        else:
          print("Job not found\n")
          mainMenu(curUser, userList, friendDic)
    elif options == "4":
      #make another poster variable inside option 4
      #print("Which job would you like to delete?: ")
      #list jobs associated with that login
      poster = input("Poster: ")
      con = sqlite3.connect("jobListings.db")
      cur = con.cursor()
      #tempexe = cur.execute("SELECT * FROM jobApplications WHERE poster=? ", (curUser.username,)) 
      query = cur.execute("SELECT * FROM jobListings WHERE poster = ? ", (poster,)) #currUser.username
      #x = tempexe.fetchall() #
      #print(x)
      i = 1
      for row in query.fetchall():
        print(i, " : ", row)
        i = i + 1

      job_to_delete = input("Which job would you like to delete? ")
      #make sure to include option to back out
      #input validation (must be a valid job name) 
      #(job can only be deleted by poster)
      #should it be con.execute or cur.execute?
      query_delete = cur.execute("DELETE FROM jobListings WHERE title = ?", (job_to_delete,))
            
      query_post_deletion = cur.execute("SELECT * FROM jobListings WHERE poster = ?", (poster,))
      i = 1
      for row in query_post_deletion.fetchall():
        print(i, " : ", row)
        i = i + 1

      con.commit()
      
      #job_to_delete = input("")
      
      #ask enduser which one
      #user picks one
      #find the notifications related to that job
      #delete them all
      #delete the actual job record
      
      #dont forget to commit when necessary (when to commit
      #table has same name as db..
      
      
      #cur = 
      
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
    print("Under construction...")
    #mainMenu(curUser, userList, friendDic)
    
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

def viewProfile(curUser, userList, friendDic, username):
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
  
