# ---------------------------------------------------------------------------------- #
# additional options on whether the user is searching for a job, learning a skill, or communicating with others 
def additionalOptions():
    options = input("Are you looking to:\n1. Search for a job\n2. Learn a skill\n3. Communicate with others\nPlease select 1, 2, or 3\n")
    
    while int(options) != 1 and int(options) != 2 and int(options) != 3:
        options = input("Invalid input\nPlease select 1, 2, or 3\n")
    
    if int(options) == 1:
        searchJob()
    elif int(options) == 2:
        learnSkill()
    elif int(options) == 3:
        communicateOthers()
    
def searchJob():
    print("Search for a new Job")
    
def communicateOthers():
    print("Communicate with others")

# -------------------------------------------------------------------------------------- #
# Create list of 5 skills for learning a skill section with an additional "do not select a skill" option 
def learnSkill():
    print("Learn a new skill")
    selectSkill = input("Do you want to learn:\n1. Skill 1\n2. Skill 2\n3. Skill 3\n4. Skill 4\n5. Skill 5\n6. Do not select a skill\nPlease select 1, 2, 3, 4, 5, or 6\n")
    
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
    print("Selected skill 1")
    
def skill_2():
    print("Selected skill 2")
    
def skill_3():
    print("Selected skill 3")
    
def skill_4():
    print("Selected skill 4")
    
def skill_5():
    print("Selected skill 5")
    
def skill_6():
    print("Selected \"do not select skill")
    
# ---------------------------------------------------------------- #
# Creating a 6th account will result in an error 
# Just a prototype, I rely on evan's code for this to work
def accountLimit(arr):
    num = len(arr)
    if num > 5:
        print("Error, too many accounts")
    else:
        print(arr)

#To test code just call additionalOptions() function
#additionalOptions() 