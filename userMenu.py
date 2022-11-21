import User, ast, re, sqlite3, apis
from datetime import datetime

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
    9. Manage Subscription\n\
    10. Logout\n"

  # function to notify of new users
  newUsers(curUser, userList, friendDic)

  # notification reminder to create profile if profile has not been created yet
  prefile = open("userProfile.txt", "r")
  preferenceList = [tuple(line.split('/')) for line in prefile.readlines()]
  num_lines = sum(
    1 for line in open('userProfile.txt'))  #number of lines in file
  # preferenceList[x][0] will iterate through the users in userProfile.txt
  # check if user has already created a profile or not
  flag = 0
  for x in range(num_lines):
    if curUser.username == preferenceList[x][0]:
      # profile has already been created
      flag = 1

  if flag == 0:
    print("Don't forget to create a profile!")

  # check for new friend request
  pendingFriendList = []
  for user, userFriends in friendDic.items():
    if curUser.username != user:
      continue

    curFriendLog = ast.literal_eval(userFriends)

    for friend, status in curFriendLog.items():
      if status == "pending":
        pendingFriendList.append(friend)

  # check for new messages from NEW users (no responses)
  message_db = sqlite3.connect("messages.db")
  cur = message_db.cursor()

  # check table exists for curUser
  cur.execute(
    "SELECT count(name) FROM sqlite_master WHERE type='table' AND name='" +
    curUser.firstName + "'")
  if cur.fetchone()[0] == 1:
    # table exists
    print("\n")
  else:
    query = "CREATE TABLE IF NOT EXISTS " + curUser.firstName + " ('receiver' TEXT NOT NULL, 'sender' TEXT, 'message' TEXT, 'read' TEXT, 'response' TEXT)"
    cur.execute(query)
  # continue checking for messages
  exist2 = cur.execute(
    "SELECT receiver FROM " + curUser.firstName +
    " WHERE receiver=? AND read=? AND response=?",
    (curUser.username, "no", "no"))
  exist = exist2.fetchall()

  # check for messages that are responses to curUser's
  response_exist = cur.execute(
    "SELECT receiver FROM " + curUser.firstName +
    " WHERE receiver=? AND read=? AND response=?",
    (curUser.username, "no", "yes"))
  response_exist2 = response_exist.fetchall()
  if response_exist2:
    print("You have messages waiting for you in your inbox.")


  # Compare current datetime to saved value to check if no new apps in a week
  with open("checkJobApps.txt", "r", encoding = "utf-8") as checkFile:
    lastAppDate = checkFile.read()
    match = re.search(r'\d+-\d+-\d{4}', lastAppDate)
    lastAppDate = datetime.strptime(match.group(), '%m-%d-%Y')
    diff = datetime.now() - lastAppDate
    if diff.days >= 7:
        print("Remember – you're going to want to have a job when you graduate. \
Make sure that you start to apply for jobs today!\n")

      
  if exist and pendingFriendList:
    option = input(
      baseMenu +
      "\n You have new messages and new pending friend requests!\n\ Enter 'i' to view messages, 'f' to view friend requests, or enter an option 1-10: "
    )
  elif exist:
    option = input(baseMenu + "\n You have new messages!\n\
      Enter 'i' to view them or enter an option 1-10: ")
  elif pendingFriendList:
    option = input(baseMenu + "\nYou have new pending friend request!\n\
Enter 'f' to view them or enter an option 1-10: ")
  else:
    option = input(baseMenu + "Please select an option 1-10: ")

  if option == '1':
    jobListings(curUser, userList, friendDic)
  elif option == '2':
    learnSkill()
  elif option == '3':
    studentSearch(curUser, userList, friendDic)
  elif option == '4':
    showMyNetwork(curUser, userList, friendDic, curFriendLog)
  elif option == '5':
    communicateOthers(curUser, userList, friendDic)
  elif option == '6':
    importantLinksUser(curUser, userList, friendDic)
  elif option == "7":
    createProfile(curUser, userList, friendDic)
  elif option == "8":
    name = curUser.username
    viewProfile(curUser, userList, friendDic, name)
  elif option == "9":
    manageSub(curUser, userList, friendDic)
  elif option == '10':
    exit(0)
  elif option == 'f':
    listFriendReqs(curUser, userList, friendDic, pendingFriendList)
  elif option == "i":
    viewMessages(curUser, userList, friendDic)
  else:
    print("Invalid input. Please select an option 1-9\n")
    mainMenu(userList)


def jobListings(curUser, userList, friendDic):
  db = sqlite3.connect("jobListings.db")
  cur = db.cursor()
  cur.execute(
    "CREATE TABLE IF NOT EXISTS jobListings('poster' TEXT NOT NULL, 'title' TEXT, 'description' TEXT, 'employer' TEXT, 'location' TEXT, 'salary' TEXT)"
  )
  sm1_query3 = sqlite3.connect("jobListings.db")
  curz = sm1_query3.cursor()
  curz.execute(
    "CREATE TABLE IF NOT EXISTS savedJobs('user' TEXT NOT NULL, 'title' TEXT)")
  #prnt = cur.execute("SELECT * FROM jobApplications")
  d1 = sqlite3.connect("jobApplications.db")
  cur1 = d1.cursor()
  prnt = cur1.execute("SELECT * FROM jobApplications WHERE user=?",
                      (curUser.username, ))
  x = prnt.fetchall()
  d2 = sqlite3.connect("jobListings.db")
  cur2 = d2.cursor()

  # Print number of jobs applied for
  print("\nYou have currently applied for {} jobs".format(len(x)))
    
  for i in x:
    cur2.execute("SELECT * FROM jobListings WHERE poster = ? AND title = ?",
                 (i[1], i[2]))
    ex1 = cur2.fetchall()
    if ex1:
      pass
      #print("This job " + i[2] + "has not been deleted")
    else:
      print("The job you applied for: " + "(" + i[2] + ")" +
            " has been deleted*")

        
  # Check for new job listings compared to last time
  jobListingCheck = 0
  checkNewListings = sqlite3.connect("jobListings.db")
  curCheckNewListings = checkNewListings.cursor()
  curCheckNewListings.execute("SELECT rowid, * FROM jobListings")
  rowsAndListings = curCheckNewListings.fetchall()
  # Set check to max value to know if any new rows have been added
  for i in rowsAndListings:
    if i[0] > jobListingCheck:
      jobListingCheck = i[0]
  # Compare to last value to see if there are new listings
  with open("checkJobListings.txt", "r", encoding = "utf-8") as checkFile:
    value = checkFile.readlines()
    # If there is a new max row, save it to check file
    if jobListingCheck > int(value[0]):
      value[0] = jobListingCheck
      checkFile.close()
      with open("checkJobListings.txt", "w", encoding = "utf-8") as checkFile:
        checkFile.writelines(str(value[0]))
        print("A new job has been posted.")

          
  options = input("\nWhat are you looking to do?\n\
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

      prnt = cur.execute("SELECT * FROM jobListings")  #should this not be cur?
      x = prnt.fetchall()

      for i in x:
        print()
        print("Poster: " + i[0])  #poster
        print("Title: " + i[1])  #title
        print("Description: " + i[2])  #description
        print("Employer: " + i[3])  #employer
        print("Location: " + i[4])  #location
        print("Salary: " + i[5])  #salary

        d = sqlite3.connect("jobApplications.db")
        curd = d.cursor()
        curd.execute(
          "SELECT * FROM jobApplications WHERE user = ? AND poster = ? AND title = ?",
          (
            curUser.username,
            i[0],
            i[1],
          ))
        exe = curd.fetchall()
        if exe:
          print("You have applied for this job!")

      saved_job = input(
        "If you would like to save a job enter its title, otherwise press 'q' to quit:"
      )
      if (saved_job == 'q'):
        exit(-1)
      sm1_query4 = sqlite3.connect("jobListings.db")
      sm1_cur4 = sm1_query4.cursor()
      sm1_cur4.execute("SELECT * FROM jobListings")
      exe4 = sm1_cur4.fetchall()
      if exe4:
        sm1_query4.execute("INSERT INTO savedJobs(user,title) VALUES(?,?)",
                           (curUser.username, saved_job))
        sm1_query4.commit()
        # Update output api
        apis.outputSavedJobs()
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
        sm1_cur.execute(
          "SELECT * FROM jobApplications WHERE user = ? AND poster = ? AND title = ?",
          (curUser.username, i[0], i[1]))
        ex2 = sm1_cur.fetchall()
        if ex2:
          print()
          print("Poster: " + i[0])  #poster
          print("Title: " + i[1])  #title
          print("Description: " + i[2])  #description
          print("Employer: " + i[3])  #employer
          print("Location: " + i[4])  #location
          print("Salary: " + i[5])  #salary
          print()

    elif sub_menu_1 == "3":
      prnt3 = cur.execute("SELECT * FROM jobListings")
      c1 = prnt3.fetchall()

      for i in c1:
        sm1_query2 = sqlite3.connect("jobApplications.db")
        sm1_cur2 = sm1_query2.cursor()
        sm1_cur2.execute(
          "SELECT * FROM jobApplications WHERE user = ? AND poster = ? AND title = ?",
          (curUser.username, i[0], i[1]))
        ex3 = sm1_cur2.fetchall()
        if not ex3:  #if not something youve already applied for
          print()
          print("Poster: " + i[0])  #poster
          print("Title: " + i[1])  #title
          print("Description: " + i[2])  #description
          print("Employer: " + i[3])  #employer
          print("Location: " + i[4])  #location
          print("Salary: " + i[5])  #salary
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

      save_or_nah = input(
        "If you would like to unsave any of these jobs enter 'u', otherwise enter 'q' to quit: "
      )
      if (save_or_nah == 'u'):
        donzo = input("Which job would you like to delete?:")
        sm1_query6 = sqlite3.connect("jobListings.db")
        sm1_cur6 = sm1_query6.cursor()
        query_delete_2 = sm1_cur6.execute(
          "DELETE FROM savedJobs WHERE title = ?", (donzo, ))
        sm1_query6.commit()
        print("You have deleted " + donzo + " from the saved jobs list\n")
        # Update output api
        apis.outputSavedJobs()
      elif (save_or_nah == 'q'):
        exit(-2)
    mainMenu(curUser, userList, friendDic)

  elif options == "2":

    if len(x) <= 10:
      # name = input("Enter your name: ")
      title = input("Enter a title for the job: ")
      desc = input("Enter description: ")
      employer = input("Enter name of employer: ")
      loc = input("Enter location: ")
      salary = input("Enter salary: ")
      poster = curUser.username

      createJobListing(title, desc, poster, employer, loc, salary)
      apis.outputJobListings()

    else:
      print("Reached max capacity of ten job postings")
  elif options == "3":

    poster = input("Input poster: ")
    title = input("Input title: ")

    if poster == curUser.username:
      print("You cannot apply to a job you posted!")
      mainMenu(curUser, userList, friendDic)
    else:
      exe = cur.execute("SELECT * FROM jobListings WHERE poster=? AND title=?",
                        (
                          poster,
                          title,
                        ))
      tmp = exe.fetchall()  # check if specific jobposting exists
      if tmp:  #if it does exist...

        d = sqlite3.connect("jobApplications.db")
        curd = d.cursor()
        curd.execute(
          "CREATE TABLE IF NOT EXISTS jobApplications('user' TEXT NOT NULL, 'poster' TEXT, 'title' TEXT, 'graduationDate' TEXT, 'startDate' TEXT, 'goodFit' TEXT)"
        )

        tempexe = curd.execute(
          "SELECT * FROM jobApplications WHERE user=? AND poster=? AND title=?",
          (
            curUser.username,
            poster,
            title,
          ))
        x = tempexe.fetchall()
        if x:  #check if user has already applied to the job
          print("You have already applied to this job!\n")
          mainMenu(curUser, userList, friendDic)
        else:
          graduationDate = input("When do you graduate (mm/dd/yyyy)? ")
          startDate = input("When can you start working (mm/dd/yyyy)? ")
          goodFit = input(
            "Why do you think you would be a good fit for this job? ")

          curd.execute(
            "INSERT INTO jobApplications(user, poster, title, graduationDate, startDate, goodFit) VALUES (?, ?, ?, ?, ?, ?)",
            (curUser.username, poster, title, graduationDate, startDate,
             goodFit))
          #poster and title identify the jobListing that curUser is applying to
          d.commit()

          # Update api output file
          apis.outputAppliedJobs()
            
          # Update latest job app in checkJobsApps.txt
          with open("checkJobApps.txt", "r", encoding = "utf-8") as checkFile:
            value = checkFile.readlines()
            value = datetime.now().strftime("%m-%d-%Y")
          with open("checkJobApps.txt", "w", encoding = "utf-8") as checkFile:
            checkFile.writelines(value)

            
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
    query = cur.execute("SELECT * FROM jobListings WHERE poster = ? ",
                        (poster, ))  #currUser.username
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
    query_delete = cur.execute("DELETE FROM jobListings WHERE title = ?",
                               (job_to_delete, ))

    query_post_deletion = cur.execute(
      "SELECT * FROM jobListings WHERE poster = ?", (poster, ))
    i = 1
    for row in query_post_deletion.fetchall():
      print(i, " : ", row)
      i = i + 1

    con.commit()
    apis.outputJobListings()
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

def createJobListing(title, desc, poster, employer, loc, salary):
    db = sqlite3.connect("jobListings.db")
    cur = db.cursor()
    prnt = cur.execute("SELECT * FROM jobListings")
    x = prnt.fetchall()
    cur.execute(
        "INSERT INTO jobListings(poster, title, description, employer, location, salary) VALUES (?, ?, ?, ?, ?, ?)",
        (poster, title, desc, employer, loc, salary))
    db.commit()

def learnSkill():
  print("Learn a new skill")
  selectSkill = input(
    "Do you want to learn:\n1. Skill 1\n2. Skill 2\n3. Skill 3\n4. Skill 4\
        \n5. Skill 5\n6. Do not select a skill\n\nPlease select 1, 2, 3, 4, 5, or 6:\n"
  )

  while int(selectSkill) != 1 and int(selectSkill) != 2 and int(
      selectSkill) != 3 and int(selectSkill) != 4 and int(
        selectSkill) != 5 and int(selectSkill) != 6:
    selectSkill = input("Invalid input\nPlease select 1, 2, 3, 4, 5, or 6\n")

  if int(selectSkill) == 1:
    skill_1(
    )  #if anyone knows of a more efficient way to do this please let me know
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


def importantLinksUser(curUser, userList, friendDic):
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
      print(link_list[15] + '\n' + link_list[16] + '\n' + link_list[17] +
            '\n' + link_list[18] + '\n' + link_list[19] + '\n' + link_list[20])
    elif int(choice) == 7:
      print(link_list[22] + '\n' + link_list[23])
    elif int(choice) == 8:
      print(link_list[25] + '\n' + link_list[26] + '\n' + link_list[27] +
            '\n' + link_list[28])
    else:
      print("Error: Invalid input\n\
                    Please enter a number 1-8.")
      importantLinksUser()
  mainMenu(curUser, userList, friendDic)


def studentSearch(curUser, userList, friendDic):
  resultList = []
  choice = input("Search for a student by:\n\
    1. Last name\n\
    2. University\n\
    3. Major\nEnter your choice: ")

  if int(choice) == 1:
    lastName = input(
      "Enter the last name of the student you are looking for: ")
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
    name = input(
      "Type of username of the friend whose profile you want to see: ")
    viewProfile(curUser, userList, friendDic, name)

  mainMenu(curUser, userList, friendDic)
  # return "showNetwork"
  return


# function used to communicate with friends (standard) or everyone (plus)
def communicateOthers(curUser, userList, friendDic):
  # table created for curUser to send/receive messages
  #return "communicateOthers"
  message_db = sqlite3.connect("messages.db")
  cur = message_db.cursor()

  subscription = curUser.plusMember.strip()

  option = input("Select an option:\n\
  1. Generate List of Friends\n\
  2. Message Friends\n\
  3. Message Everyone\n\
  4. View Inbox\n\
  \n\
  0. Go back\n")

  if int(option) == 0:
    mainMenu(curUser, userList, friendDic)
  elif int(option) == 1:
    # generate list of friends - DONE
    for user, userFriends in friendDic.items():
      if curUser.username != user:
        continue
      curFriendLog = ast.literal_eval(userFriends)
    print("Friends: ")
    for user, status in curFriendLog.items():
      print(user)
    communicateOthers(curUser, userList, friendDic)
  elif int(option) == 2:
    # message friends ( available to standard and plus) -- DONE
    for user, userFriends in friendDic.items():
      if user == curUser.username:
        if len(userFriends) > 2:
          print("Send a message to a friend!")
        else:
          print("You have no friends!")
          mainMenu(curUser, userList, friendDic)

    choice = input("Who would you like to send a message to:\n")
    flag = 0
    for user, userFriends in friendDic.items():
      if user == choice:
        flag = 1
        for User1 in userList:
          if user == User1.username:
            username1 = User1.firstName
        message = input("What message would you like to send: ")
        # now to add messages to database to table of receiver (title = user's firstName)
        query = "CREATE TABLE IF NOT EXISTS " + username1 + " ('receiver' TEXT NOT NULL, 'sender' TEXT, 'message' TEXT, 'read' TEXT, 'response' TEXT)"
        cur.execute(query)
        cur.execute(
          "INSERT INTO " + username1 +
          "(receiver, sender, message, read, response) VALUES (?, ?, ?, ?, ?)",
          (user, curUser.username, message, "no", "no"))
        message_db.commit()
        print("Message sent!")
    if flag == 0:
      print("I'm sorry, you are not friends with this person. ")

  elif int(option) == 3:
    # message others (available only to plus) -- DONE
    if subscription == "False":
      print(
        "Only Plus users are allowed to communicate with those outside of their friend list, upgrade today!"
      )
      communicateOthers(curUser, userList, friendDic)
    f = open('userList.txt', 'r')
    # continue for messaging every user
    #display all users in the system
    p_flag = False
    with open('userList.txt', 'r') as f:
      for line in f:
        words = line.split()
        if words:
          if not p_flag:
            print()
            print("User List:\n")
            p_flag = True
          print(words[0])
          print()
    choice = input("Who would you like to send a message to:\n")
    flag = 0
    for user in userList:
      if user.username == choice:
        flag = 1
        message = input("What message would you like to send:\n")
        # table created with title of receiver's firstName
        query = "CREATE TABLE IF NOT EXISTS " + user.firstName + " ('receiver' TEXT NOT NULL, 'sender' TEXT, 'message' TEXT, 'read' TEXT, 'response' TEXT)"
        cur.execute(query)
        cur.execute(
          "INSERT INTO " + user.firstName +
          "(receiver, sender, message, read, response) VALUES (?, ?, ?, ?, ?)",
          (user.username, curUser.username, message, "no", "no"))
        message_db.commit()
        print("Message sent!")
    if flag == 0:
      print("This user is not in our system!")
      communicateOthers(curUser, userList, friendDic)

  elif int(option) == 4:
    # view inbox -> parsing messages db
    exist2 = cur.execute(
      "SELECT receiver FROM " + curUser.firstName +
      " WHERE receiver=? AND read=?", (curUser.username, "no"))
    exist = exist2.fetchall()

    if exist:
      print("Messages found!")
      received = cur.execute(
        "SELECT * FROM " + curUser.firstName + " WHERE receiver=? AND read=?",
        (curUser.username, "no"))
      messageList = received.fetchall()

      print("Unread messages: ")
      for num, exp in enumerate(messageList):
        print(f"Message {num + 1}")
        print("Sender: " + exp[1])
        print("Message: " + exp[2] + "\n")

      read_messages = cur.execute(
        "SELECT * FROM " + curUser.firstName + " WHERE receiver=? AND read=?",
        (curUser.username, "yes"))
      read = read_messages.fetchall()

      print("Read messages: ")
      for num, exp in enumerate(read):
        print(f"Message {num + 1}")
        print("Sender: " + exp[1])
        print("Message: " + exp[2] + "\n")

      choice = input("Would you like to mark any as read (y or n): ")
      while choice != "y" and choice != "n":
        choice = input("Enter a valid value (y or n): ")

      if choice == 'y':
        message_read = input(
          "Enter username of messages you would like to mark as read: ")
        flag = 0
        for user in userList:
          if user.username != message_read:
            continue
          elif user.username == message_read:  #changed to add conditional...
            flag = 1
            cur.execute("UPDATE " + curUser.firstName + " SET read=?",
                        ("yes", ))
            message_db.commit()
            print("Messages are now marked as read")
        if flag == 0:
          print("There are no messages associated with that username")

      delete_choice = input("Would you like to delete any message (y or n)? ")
      while delete_choice != "y" and delete_choice != "n":
        delete_choice = input("Enter a valid value (y or n): ")

      if delete_choice == "y":
        message_delete = input(
          "Enter username of messages you would like to delete: ")
        for user in userList:
          if user.username == message_delete:
            cur.execute("DELETE FROM " + curUser.firstName + " WHERE sender=?",
                        (user.username, ))
            message_db.commit()
            print("Messages are now deleted.")

      respond_choice = input(
        "Would you like to respond to a message (y or n)?")
      while respond_choice != "y" and respond_choice != "n":
        respond_choice = input("Enter a valid value (y or n): ")

      if respond_choice == "y":
        response_message = input("Which user would you like to respond to: ")
        flag = 0
        for user in userList:
          if user.username == response_message:
            flag = 1
            message = input("What message would you like to send:\n")
            # table created with title of receiver's firstName
            query = "CREATE TABLE IF NOT EXISTS " + user.firstName + " ('receiver' TEXT NOT NULL, 'sender' TEXT, 'message' TEXT, 'read' TEXT, 'response' TEXT)"
            cur.execute(query)
            cur.execute(
              "INSERT INTO " + user.firstName +
              "(receiver, sender, message, read, response) VALUES (?, ?, ?, ?, ?)",
              (user.username, curUser.username, message, "no", "yes"))
            message_db.commit()
            print("Message sent!")
    else:
      print("No messages")
  else:
    print("Enter a valid input value between 0-4\n")
    communicateOthers(curUser, userList, friendDic)
  communicateOthers(curUser, userList, friendDic)


# function allows you to view messages from NEW users(no responses)
def viewMessages(curUser, userList, friendDic):
  message_db = sqlite3.connect("messages.db")
  cur = message_db.cursor()
  exist2 = cur.execute(
    "SELECT receiver FROM " + curUser.firstName +
    " WHERE receiver=? AND read=?", (curUser.username, "no"))
  exist = exist2.fetchall()

  if exist:
    print("Messages found!")
    print()
    received = cur.execute(
      "SELECT * FROM " + curUser.firstName +
      " WHERE receiver=? AND read=? AND response=?",
      (curUser.username, "no", "no"))
    messageList = received.fetchall()

    for num, exp in enumerate(messageList):
      print("Sender: " + exp[1])
      print("Message: " + exp[2] + "\n")
      with open('userList.txt', 'r') as f2:
        for line in f2:
          u_names = line.split()
          if u_names:
            if (u_names[0] == exp[1] and u_names[4] == "True"):
              print("(The user" + " " + "(" + u_names[0] + ")" + " " +
                    "is a plus member)" + "\n")

    #choice = input("Would you like to mark as read or delete any message (y or n)? ")
    choice = input("Would you like to respond to a message (y or n)?")
    while choice != "y" and choice != "n":
      choice = input("Enter a valid value (y or n): ")

    if choice == "y":
      respond_user = input("Which user would you like to respond to: ")
      flag2 = 0
      for user in userList:
        if user.username == respond_user:
          flag2 = 1
          message = input("What message would you like to send:\n")
          # table created with title of receiver's firstName
          query = "CREATE TABLE IF NOT EXISTS " + user.firstName + " ('receiver' TEXT NOT NULL, 'sender' TEXT, 'message' TEXT, 'read' TEXT, 'response' TEXT)"
          cur.execute(query)
          cur.execute(
            "INSERT INTO " + user.firstName +
            "(receiver, sender, message, read, response) VALUES (?, ?, ?, ?, ?)",
            (user.username, curUser.username, message, "no", "yes"))
          message_db.commit()
          print("Message sent!")
  else:
    print("No messages")
  while choice != "y" and choice != "n":
    choice = input("Enter a valid value (y or n): ")

  if choice == "y":
    communicateOthers(curUser, userList, friendDic)
  else:
    mainMenu(curUser, userList, friendDic)


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
        print("Enter a valid value between 0-3")
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
  choice = input(
    "Do you want to accept the friend request from {}? (y/n): ".format(
      username))
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


# function allows a user to add to profile db
def createProfile(curUser, userList, friendDic):
  prefile = open("userProfile.txt", "r")
  preferenceList = [tuple(line.split('/')) for line in prefile.readlines()]

  num_lines = sum(
    1 for line in open('userProfile.txt'))  #number of lines in file
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
        edit = input(
          "Which part do you want to edit?\n1. Title\n2. Major\n3. University\n4. About\n5. Experience\n6. Education\n"
        )
        while edit != "1" and edit != "2" and edit != "3" and edit != "4" and edit != "5" and edit != "6":
          edit = input("Invalid input. Please enter 1 - 5: ")

        lineRemove = curUser.username + "/" + preferenceList[x][
          1] + "/" + preferenceList[x][2] + "/" + preferenceList[x][
            3] + "/" + preferenceList[x][4]

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
          file.write(
            f"{curUser.username}/{newTitle}/{preferenceList[x][2]}/{preferenceList[x][3]}/{preferenceList[x][4]}\n"
          )
          file.close()
          print("Title updated!")
          mainMenu(curUser, userList, friendDic)  #goes back to main menu

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
          file.write(
            f"{curUser.username}/{preferenceList[x][1]}/{newMajor}/{preferenceList[x][3]}/{preferenceList[x][4]}\n"
          )
          file.close()
          print("Major updated!")
          mainMenu(curUser, userList, friendDic)  #goes back to main menu

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
          file.write(
            f"{curUser.username}/{preferenceList[x][1]}/{preferenceList[x][2]}/{new}/{preferenceList[x][4]}\n"
          )
          file.close()
          print("University updated!")
          mainMenu(curUser, userList, friendDic)  #goes back to main menu

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
          file.write(
            f"{curUser.username}/{preferenceList[x][1]}/{preferenceList[x][2]}/{preferenceList[x][3]}/{new}\n"
          )
          file.close()
          print("About updated!")
          mainMenu(curUser, userList, friendDic)  #goes back to main menu
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

  num_lines = sum(
    1 for line in open('userProfile.txt'))  #number of lines in file
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

      exp = cur.execute("SELECT * FROM experience WHERE username=?",
                        (username, ))
      expList = exp.fetchall()

      for num, exp in enumerate(expList):
        print(f"Experience {num + 1}")
        print("Title: " + exp[1])
        print("Employer: " + exp[2])
        print("Date started: " + exp[3])
        print("Date ended: " + exp[4])
        print("Location: " + exp[5])
        print("Description: " + exp[6] + "\n")

      exp2 = cur2.execute("SELECT * FROM education WHERE username=?",
                          (username, ))
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
  cur.execute(
    "CREATE TABLE IF NOT EXISTS experience('username' TEXT NOT NULL, 'title' TEXT, 'employer' TEXT, 'dateStarted' TEXT, 'dateEnded' TEXT, 'location' TEXT, 'description' TEXT)"
  )
  flag = 0
  ask = input("Would you like to edit an experience? (y/n) ")
  while ask != "y" and ask != "n":
    ask = input("Invalid input. (y/n) ")

  if ask == "y":
    expNum = input(
      "Which experience would you like to edit? (Insert title of experience) ")

    exist2 = cur.execute("SELECT title FROM experience WHERE title=?",
                         (expNum, ))
    exist = exist2.fetchall()

    if exist:
      expTitle = input("New Experience 1\nTitle: ")
      expEmployer = input("New Employer: ")
      expDateStarted = input("New Date started: ")
      expDateEnded = input("New Date ended: ")
      expLocation = input("New Location: ")
      expDescription = input("New Description: ")
      cur.execute(
        "UPDATE experience SET title=?, employer=?, dateStarted=?, dateEnded=?, location=?, description=? WHERE title=?",
        (
          expTitle,
          expEmployer,
          expDateStarted,
          expDateEnded,
          expLocation,
          expDescription,
          expNum,
        ))
      db.commit()
      print("Experience updated")
      flag = 1
      mainMenu(curUser, userList, friendDic)
    else:
      print("Experience title not found")

  experienceCount = cur.execute(
    "SELECT username FROM experience WHERE username=?", (curUser.username, ))
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

    cur.execute(
      "INSERT INTO experience (username, title, employer, dateStarted, dateEnded, location, description) VALUES (?, ?, ?, ?, ?, ?, ?)",
      (curUser.username, expTitle, expEmployer, expDateStarted, expDateEnded,
       expLocation, expDescription))
    db.commit()
    mainMenu(curUser, userList, friendDic)


def education(curUser, userList, friendDic):
  db = sqlite3.connect("education.db")
  cur = db.cursor()
  cur.execute(
    "CREATE TABLE IF NOT EXISTS education('username' TEXT NOT NULL, 'schoolName' TEXT, 'degree' TEXT, 'yearsAttended' TEXT)"
  )

  nameCheck = cur.execute("SELECT username FROM education WHERE username=?",
                          (curUser.username, ))

  if nameCheck:
    print("Education section already found.")
  else:
    schoolName = input("School name: ")
    degree = input("Degree: ")
    yearsAttended = input("Years attended: ")

    cur.execute(
      "INSERT INTO education (username, schoolName, degree, yearsAttended) VALUES (?, ?, ?, ?)",
      (curUser.username, schoolName, degree, yearsAttended))
    db.commit()
    print("Education added!\n")
    mainMenu(curUser, userList, friendDic)

  # return "education"


# --- function for managing Standard or Plus subscription ---- #
def manageSub(curUser, userList, friendDic):
  print("Current subscription: ")
  subscription = curUser.plusMember.strip()

  # open file to copy data and replace curUser line with True/False if they choose to change subscription
  fin = open("userList.txt", 'r')
  data = fin.readlines()
  newString = ''

  if subscription == "False":
    print("Standard")
    print("Upgrade to Plus to send messages to everyone!")
    choice = input("Would you like to change your subscription (y or n)? ")
    if choice == "y":
      subscription = "True"
      print(
        "You are now a Plus member! This change will be reflected the next time you login. A charge of $10 will be added to your account each month."
      )
      for userLine in data:
        if curUser.username in userLine:
          userLine = userLine.replace("False\n", "True\n")
        newString += userLine
    elif choice == "n":
      subscription = "False"
      for userLine in data:
        newString += userLine
    else:
      print("Invalid input")
      manageSub(curUser, userList, friendDic)

  elif subscription == "True":
    print("Plus")
    choice = input("Would you like to change your subscription (y or n)? ")
    if choice == "y":
      subscription = "False"
      print(
        "You are no longer a Plus member! This change will be reflected next time you login. You will no longer be charged after this months billing cycle is complete."
      )
      for userLine in data:
        if curUser.username in userLine:
          userLine = userLine.replace("True\n", "False\n")
        newString += userLine
    elif choice == "n":
      subscription = "True"
      for userLine in data:
        newString += userLine
    else:
      print("Invalid input")
      manageSub(curUser, userList, friendDic)

  fin.close()

  # write data with replaced string back into userList
  fin = open("userList.txt", 'w')
  fin.write(newString)
  fin.close()

  # update userList to grab new True/False
  userList = User.loadUsers("userList.txt")

  mainMenu(curUser, userList, friendDic)


# method for notifying a new user has joined inCollege
def newUsers(curUser, userList, friendDic):
  newUserDic = {}

  # used to read from file and create newUserDic
  with open("newUsers.txt", 'r') as newUserFile:
    lines = newUserFile.read().splitlines()
    for line in lines:
      key, value = line.split(' ', 1)
      newUserDic[key] = value

  #print(newUserDic)

  # used to modify the status to yes or no
  for user, userNotif in newUserDic.items():
    #print(newUser)
    #print(userNotif)
    tmpDic = ast.literal_eval(userNotif)
    #print(tmpDic)
    #print(tmpDic.keys())
    # != curUser
    if curUser.username in tmpDic.keys():
      continue
      #print('Ismarieu1! has been notified of ' + user)
    else:
      tmpDic[curUser.username] = "yes"
      for user2 in userList:
        if user2.username == user and user2.username != curUser.username:
          print("{0} {1} has joined inCollege".format(user2.firstName, user2.lastName))

    newUserDic[user] = str(tmpDic)

  #print(newUserDic)
  # used to update newFriends.txt with new information
  newUsersFile = open("newUsers.txt", "w")
  newUsersFile.truncate()
  for user, userNotif in newUserDic.items():
      newUsersFile.write("{0} {1}\n".format(user, userNotif))
              
  newUsersFile.close()