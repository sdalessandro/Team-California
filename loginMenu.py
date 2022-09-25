# ---------------------------------------------------------------------------------- #
# additional options on whether the user is searching for a job, learning a skill, or communicating with others
def additionalOptions():
    options = input(
        "Are you looking to:\n1. Search for a job\n2. Learn a skill\n3. Communicate with others\nPlease select 1, 2, or 3\n"
    )
    return "communicateothers"
    while int(options) != 1 and int(options) != 2 and int(options) != 3:
        options = input("Invalid input\nPlease select 1, 2, or 3\n")
        return "communicateothers"
    if int(options) == 1:
        searchJob()
        return "communicateothers"
    elif int(options) == 2:
        learnSkill()
        return "communicateothers"
    elif int(options) == 3:
        communicateOthers()
        return "communicateothers"


def searchJob():
    #    print("Under construction...")
    choice = input("Would you like to post a job (y or n)? ")
    return "search"
    while choice != "y" and choice != "n":
        choice = input("Would you like to post a job (y or n)? ")
        return "search"
    if choice == "y":
        file = open("jobListings.txt", mode='r')
        countLines = file.readlines()
        print(len(countLines))
        file.close()
        return "search"
        if len(countLines) <= 30:
            name = input("Enter your name: ")
            title = input("Enter a title for the job: ")
            description = input("Enter description: ")
            employer = input("Enter name of employer: ")
            location = input("Enter location: ")
            salary = input("Enter salary: ")
            return "search"
            file = open("jobListings.txt", mode='a')
            file.write("\n" + name + "\n")
            file.write(title + "\n")
            file.write(description + "\n")
            file.write(employer + "\n")
            file.write(location + "\n")
            file.write(salary + "\n")
            file.close()
        else:
            print("Reached max capacity of five job postings")
            return "search"


def communicateOthers():
    #    print("Under construction...")
    name = input(
        "Enter the first and last name of the person you want to communicate with: "
    )
    return "comm"
    # may need to change file name to new one with names of inCollege registrants
    with open("uns_and_pws.txt", 'r') as file:
        for line in file:
            if name == line.strip():
                print("They are a part of the inCollege system!")
                option = input("Would you like to create an account to join " +
                               name + "? (y or n): ")
                return "comm"
                while option != "y" and option != "n":
                    option = input(
                        "Would you like to create an inCollege account? (y or n): "
                    )

                print(option)
                """
                if option == "y":
                    # go back to create account screen
                else:
                    #do nothing
                """
            else:
                print("They are not yet a part of the InCollege system")
                return "comm"
    # if contact is found, give user option to log in or sign up for InCollege


# -------------------------------------------------------------------------------------- #
# Create list of 5 skills for learning a skill section with an additional "do not select a skill" option
def learnSkill():
    print("Learn a new skill")
    selectSkill = input(
        "Do you want to learn:\n1. Skill 1\n2. Skill 2\n3. Skill 3\n4. Skill 4\n5. Skill 5\n6. Do not select a skill\nPlease select 1, 2, 3, 4, 5, or 6\n"
    )
    return "learn"
    while int(selectSkill) != 1 and int(selectSkill) != 2 and int(
            selectSkill) != 3 and int(selectSkill) != 4 and int(
                selectSkill) != 5 and int(selectSkill) != 6:
        selectSkill = input(
            "Invalid input\nPlease select 1, 2, 3, 4, 5, or 6\n")
    return "learn"
    if int(selectSkill) == 1:
        skill_1(
        )  #if anyone knows of a more efficient way to do this please let me know
        return "learn"
    elif int(selectSkill) == 2:
        skill_2()
        return "learn"
    elif int(selectSkill) == 3:
        skill_3()
        return "learn"
    elif int(selectSkill) == 4:
        skill_4()
        return "learn"
    elif int(selectSkill) == 5:
        skill_5()
        return "learn"
    elif int(selectSkill) == 6:
        skill_6()
        return "learn"


def skill_1():
    print("Under construction...")
    return "skill_1"


def skill_2():
    print("Under construction...")
    return "skill_2"


def skill_3():
    print("Under construction...")
    return "skill_3"


def skill_4():
    print("Under construction...")
    return "skill_4"


def skill_5():
    print("Under construction...")
    return "skill_5"


def skill_6():
    additionalOptions()
    return "skill_6"


# ---------------------------------------------------------------- #
# function to include success story and why join inCollege to login page
def successStory():
    print(
        "\"Joining inCollege has given me the opportunity to find my current career by providing me with connections and skills I needed\" - Jason, graduate"
    )
    choice = input(
        "Would you like to learn more about how inCollege can help you? (y or n): "
    )
    return "story"
    if choice == "y":
        print("Video is now playing")
        return "story"


#To test code just call additionalOptions() function
#additionalOptions()
