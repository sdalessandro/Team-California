from os.path import exists
import User, userMenu, sqlite3

def inputAccounts():
    fileName = "studentAccounts.txt"

    if(exists(fileName)):
        file = open(fileName)
        accounts = file.read().split("=====\n")
        file.close()
        
        for acc in accounts:
            accList = acc.split('\n')

            for item in accList:
                if item == '' or item == "=====":
                    accList.remove(item)

            if accList == []: continue
            username, firstName, lastName = accList[0].split(' ')
            password = accList[1]

            with open("userList.txt", 'r') as file:
                if len(file.readlines()) > 9:
                    print("\nAPI Input Failed: Max account limit reached.")
                    return
            
            User.saveUser(username, password, firstName, lastName, "False")

def outputUsers(userList):
    fileName = "MyCollege_users.txt"
    try:
        file = open(fileName, 'w')
    except IOError:
        file = open(fileName, 'w+')

    for user in userList:
        status = user.plusMember.strip()
        if status == "True":
            status = "plus"
        else:
            status = "standard"
        file.write("{} {}\n".format(user.username, status))

def inputJobListings():
    fileName = "newJobs.txt"

    if(exists(fileName)):
        file = open(fileName)
        jobs = file.read().split("=====\n")
        file.close()
        
        for job in jobs:
            job = job.replace("&&&\n", " ")
            jobList = job.split('\n')

            for item in jobList:
                if item == '' or item == "=====":
                    jobList.remove(item)
                
            title, desc, poster, employer, loc, salary = jobList
            userMenu.createJobListing(title, desc, poster, employer, loc, salary)

def outputJobListings():

    fileName = "MyCollege_jobs.txt"
    try:
        file = open(fileName, 'w')
    except IOError:
        file = open(fileName, 'w+')
    
    db = sqlite3.connect("jobListings.db")
    cur = db.cursor()
    query = cur.execute("SELECT * FROM jobListings")
    jobs = query.fetchall()

    for job in jobs:
        file.write("Poster: {}\nTitle: {}\nDescription: {}\nEmployer: {}\nLocation: {}\
\nSalary: {}\n=====\n".format(job[0], job[1], job[2], job[3], job[4], job[5]))

def outputAppliedJobs():

    fileName = "MyCollege_appliedJobs.txt"
    try:
        file = open(fileName, 'w')
    except IOError:
        file = open(fileName, 'w+')
    
    db = sqlite3.connect("jobApplications.db")
    cur = db.cursor()
    query = cur.execute("SELECT * FROM jobApplications")
    apps = query.fetchall()

    for app in apps:
        file.write("Title: {}\nApplicant: {}\nWhy Good Fit?: {}\n=====\n"
            .format(app[2], app[0], app[5]))

def outputSavedJobs():

    fileName = "MyCollege_savedJobs.txt"
    try:
        file = open(fileName, 'w')
    except IOError:
        file = open(fileName, 'w+')
    
    db = sqlite3.connect("jobListings.db")
    cur = db.cursor()
    query = cur.execute("SELECT DISTINCT user FROM savedJobs")
    users = query.fetchall()
    for user in users:
        file.write("User: {}\nTitle(s): ".format(user[0]))
        query = cur.execute("SELECT DISTINCT title FROM savedJobs")
        titles = query.fetchall()
        for title in titles:
            file.write("{}, ".format(title[0]))
        file.write("\n=====\n")

def outputProfiles():
    fileName = "MyCollege_profiles.txt"
    try:
        file = open(fileName, 'w')
    except IOError:
        file = open(fileName, 'w+')

    db = sqlite3.connect("profile.db")
    cur = db.cursor()
    db2 = sqlite3.connect("education.db")
    cur2 = db2.cursor()
    
    profiles = open("userProfile.txt", "r")
    preferenceList = [tuple(line.split('/')) for line in profiles.readlines()]
    num_lines = sum(1 for line in open('userProfile.txt'))

    for x in range(num_lines):
        username = preferenceList[x][0]
        file.write("Username: {}\n".format(username))
        file.write("Title: {}\n".format(preferenceList[x][1]))
        file.write("Major: {}\n".format(preferenceList[x][2]))
        file.write("University: {}\n".format(preferenceList[x][3]))
        file.write("Description: {}".format(preferenceList[x][4]))
    
        exp = cur.execute("SELECT * FROM experience WHERE username=?",
                        (username, ))
        expList = exp.fetchall()
    
        for num, exp in enumerate(expList):
            file.write("Experience {}\n".format(num+1))
            file.write("Title: {}\n".format(exp[1]))
            file.write("Employer: {}\n".format(exp[2]))
            file.write("Date started: {}\n".format(exp[3]))
            file.write("Date ended: {}\n".format(exp[4]))
            file.write("Location: {}\n".format(exp[5]))
            file.write("Description: {}\n".format(exp[6]))
        
        exp2 = cur2.execute("SELECT * FROM education WHERE username=?",
                (username, ))
        exp2List = exp2.fetchall()
        if exp2:
            for exp in exp2List:
                file.write(exp[1]+'\n')
                file.write(exp[2]+'\n')
                file.write(exp[3]+'\n')

        file.write("====\n")