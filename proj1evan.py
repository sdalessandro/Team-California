from getpass import getpass
import re

#good version :)

print("Welcome to InCollege!\n")

member = ""
member = input("Are you already a member? (y or n): ")

while member not in ['y', 'Y', 'n', 'N']:
    print("Please input 'y' for (yes) or 'n' for (no)")
    member = input("Are you an existing member? (y or n): ")

if(member == 'y' or member == 'Y'):
    print("Great! Log in below using existing account credentials: \n")
    
    existing_un = input("Username: ")

    with open("uns_and_pws.txt", 'r') as f:
        content = f.read()
        if existing_un in content:
            #print("usernmame exists...")
            existing_pass = getpass("Password: ")
            
    with open("uns_and_pws.txt", 'r') as f:
        content = f.read()
        if existing_pass in content:
            print("you have successfully logged in")
            

else:
    print("\nLets get you signed up!\n")
    taken = None
    while True:
        taken = False
        new_un = input("Enter your desired username: ")
        if(re.match ("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,12}$", new_un) == None):
              print("Username not accepted")
              print("Username must have minimum of 8 characters, maximum of 12 characters, at least one capital letter, one digit, and one special character")
              continue
        else:
            #print("Username accepted") last mode here :)
            with open("uns_and_pws.txt", 'r+') as f:   
                lines = len(f.readlines())
                if(lines > 10):
                    print("all permitted accounts have been created")
                    print("please come back later")
                    break
                else:
                    content = f.read()
                    if new_un in content:
                        print("This username is already taken...")
                        taken = True
                        continue
                if(taken == False):
                    f.write(new_un)
                    f.write("\n")
                    print("Username accepted")
                    break
            
  
    while True:
        new_pass = input("Enter your desired password: ")
        if(re.match ("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,12}$", new_pass) == None):
            print("Password not accepted")
            print("Password must have minimum of 8 characters, maximum of 12 characters, at least one capital letter, one digit, and one special character")
            continue
        else:
            with open("uns_and_pws.txt", 'r+') as f:   
                lines = len(f.readlines())
                if(lines > 10):
                    print("all permitted accounts have been created")
                    print("please come back later")
                    break
                else:
                    f.write(new_pass)
                    f.write("\n")
                    print("Password accepted")
                    break


    

#use f.readlines and save the numbered output to a list ? or directly parse through the file... f.seek(0) start at beg each time (save username then password so as to only need one txt file....)

#t. In this epic, support for up to 5 unique student accounts (unique user name and
#secure password: minimum of 8 characters, maximum of 12 characters, at least one capital letter, one
#digit, one special character) will be provided