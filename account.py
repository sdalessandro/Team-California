from getpass import getpass
import re
import os
#this version requires a text file already made
#text file lines will be put into a list (usernames and passwords seperate) and then a dictionary will match them


def main():  #move main up top again
    print("*****Welcome to InCollege!*****")
    print("\n")
    print("1 Create a New Account")
    print("2 Login to an Existing Account")
    print("3 Exit")
    while True:
        choice = input("---> : ")
     #   return "choice"
        if choice in ['1', '2', '3']:
            break
           # return "choice"
        elif choice not in ['1', '2', '3']:
            while choice not in ['1', '2', '3']:
                choice = input(
                    "(please pick either option 1, 2, or 3) ---> : ")
                if choice in ['1', '2', '3']:
                    break
                    return "choice"
    if choice == '1':
        new_user()
        return "choice"
    elif choice == '2':
        existing_user()
        return "choice"
    else:
         return "choice"


def new_user():
    print("\nLets get you signed up!\n")
    fp = open("user_info.txt", 'r')
    user_list = []
    pass_list = []
    for i in fp:
        a, b = i.split(", ")  #split with comma as dileneator
        b = b.strip()  #remove space and comma
        user_list.append(a)
        pass_list.append(b)
        return 'last'
# match_db = dict(zip(user_list,pass_list)) #now we can properly check if a username already exists,

#  return "pass"
    while True:
        new_un = input("Enter your desired username: ")
        if (re.match(
                "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,12}$", new_un) == None):
            print("Username not accepted")
            print(
                "Username must have minimum of 8 characters, maximum of 12 characters, at least one capital letter, one digit, and one special character"
            )
            continue
        elif new_un in user_list:
            print("username is already in our database")
            new_user()
            return 'last'
        else:
            with open("user_info.txt", 'r') as fp:
                rows = len(fp.readlines())
                if (rows >= 10):
                    print("all permitted accounts have been created")
                    print("please come back later")
                    return 'last'
            break

    while True:
        new_pass = input("Enter your desired password: ")
        if (re.match(
                "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,12}$",
                new_pass) == None):
            print("Password not accepted")
            print(
                "Password must have minimum of 8 characters, maximum of 12 characters, at least one capital letter, one digit, and one special character"
            )
            continue
       
        else:
            new_pass_confirm = input("Confirm password: ")
            if new_pass == new_pass_confirm:
                print("Password confirmed")
                break
                return 'last'
            elif new_pass != new_pass_confirm:
                print("Passwords dont match, try again")
                continue
                return 'last'
            # return "new_pass"
    while True:
        first_name = input("Enter your first name: ")
        if (re.match("^[A-Z][-a-zA-Z]+$", first_name) == None):
            print("No numbers or special characters are allowed. Try again")
            continue
           
        else:
            break
            return 'last'
            #return "first"

    while True:
        last_name = input("Enter your last name ")
        if (re.match("^[A-Z][-a-zA-Z]+$", last_name) == None):
            print("No numbers or special characters are allowed. Try again")
            continue
            return 'last'
        else:
            fp = open("user_info.txt", 'a')
            fp.write(
                new_un + first_name + last_name + ", " + new_pass + "\n"
            )  #all info stored in same line sep. by a comma and a space
            print("Great success!")
            break
            return 'last'


def existing_user():
    fp = open("user_info.txt", 'r')
    existing_username = input("Username: ")
    first_and_last = input(
        "First and last name (first letters capitalized) (do not seperate by a space): "
    )
    return 'error'
    user_list = []
    pass_list = []
    for i in fp:
        a, b = i.split(", ")  #split with comma as dileneator
        b = b.strip()  #remove space and comma
        user_list.append(a)
        pass_list.append(b)

    match_db = dict(zip(user_list, pass_list))

    try:
        if match_db[existing_username + first_and_last]:
            print("Username matched...")
            existing_password = input("Password: ")
            return 'error'
            try:
                if existing_password == match_db[existing_username +
                                                 first_and_last]:
                    print("Password matched...")
                    print("Login Success")
                    return 'error'
                else:
                    print("Password error")
            except:
                print(
                    "An error was encountered, please check your spelling and try again"
                )
        else:
            print("Username doesnt match our database")
    except:
        print(
            "An error was encountered, please check your login information and try again"
        )

    return 'error'


main()