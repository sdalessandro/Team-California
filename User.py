import re

class User(object):

    def __init__(self, username, password, firstName, lastName):
        super(User, self).__init__()
        self.username = username
        self.password = password
        self.firstName = firstName
        self.lastName = lastName
        self.loggedIn = True

def loadUsers(fileName):
    with open(fileName) as file:
        userList = [User(*(line.split(' '))) for line in file]
    return userList

def createUser(userList):
    username = setUsername(userList)
    password = setPassword()
    firstName = setFirstName()
    lastName = setLastName()

    file = open("userList.txt", 'a')
    file.write('{0} {1} {2} {3}\n'.format(username, password, firstName, lastName))
    file.close()

def setUsername(userList):
    username = input("Enter your desired username: ")
    if len(userList) >= 10:
        print("All permitted accounts have been created. Please come back later.")
        mainMenu()
    if (re.match("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,12}$", username) == None):
        print("Error: Username not accepted")
        print("Username must have minimum of 8 characters, maximum of 12 characters, \
            at least one capital letter, one digit, and one special character\n")
        setUsername(userList)
    if username in userList:
        print("Error: Username is already in our database\n")
        setUsername(userList)
        
    return username

def setPassword():
    password = input("Enter your desired password: ")
    if (re.match("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,12}$",
            password) == None):
        print("Error: Password not accepted")
        print("Password must have minimum of 8 characters, maximum of 12 characters, \
            at least one capital letter, one digit, and one special character")
        setPassword()
   
    confirmPassword = input("Confirm password: ")
    if password == confirmPassword:
        print("Password confirmed")
    else:
        print("Passwords do not match, try again.")
        setPassword()
            
    return password

def setFirstName():
    firstName = input("Enter your first name: ")
    if (re.match("^[A-Z][-a-zA-Z]+$", firstName) == None):
        print("No numbers or special characters are allowed. Try again")
        setFirstName()

    return firstName

def setLastName():
    lastName = input("Enter your last name: ")
    if (re.match("^[A-Z][-a-zA-Z]+$", lastName) == None):
        print("No numbers or special characters are allowed. Try again")
        setLastName()

    return lastName