# ---------------------------------------------------------------------------------- #
# additional options on whether the user is searching for a job, learning a skill, or communicating with others 
def mainMenu():
    
    options = input("Are you looking to:\n\
        \t1. Job Listings\n\
        \t2. Learn a skill\n\
        \t3. Communicate with others\n\
        \tPlease select 1, 2, or 3\n")
    
    
    if int(options) == 1:
        jobListings()
    elif int(options) == 2:
        learnSkill()
    elif int(options) == 3:
        communicateOthers()
    else:
        options = input("Invalid input. Please select 1, 2, or 3\n")
        mainMenu()
    
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

def communicateOthers():
    print("Under construction...") 

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
    mainMenu()
    


#To test code just call additionalOptions() function
#additionalOptions() 