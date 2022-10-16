import re
from collections import defaultdict

global currentUser

class User(object):

    def __init__(self, username, password, firstName, lastName):
        super(User, self).__init__()
        self.username = username
        self.password = password
        self.firstName = firstName
        self.lastName = lastName
        self.loggedIn = False

def loadUsers(fileName):
    with open(fileName) as userFile:
        userList = [User(*(line.split(' '))) for line in userFile]
    return userList

def loadFriends(fileName):
    friendDict= {}

    with open("userFriends.txt", "r") as friendFile:
        lines = friendFile.read().splitlines()
        for line in lines:
            key, value = line.split(' ', 1)
            friendDict[key] = value

    return friendDict

def createUser(userList):
    username = setUsername(userList)
    password = setPassword()
    firstName = setFirstName()
    lastName = setLastName()

    # Write new user to userList.txt
    file = open("userList.txt", 'a')
    file.write("{0} {1} {2} {3}\n".format(username, password, firstName, lastName))
    file.close()

    #Write new user to userFriends.txt
    file = open("userFriends.txt", 'a')
    file.write(username + " {}\n")
    file.close()
    

def setUsername(userList):
    username = input("Enter your desired username: ")
    if len(userList) > 10:
        print("All permitted accounts have been created. Please come back later.")
        mainMenu()
    if (re.match("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,12}$", 
            username) == None):
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

def getFriends(self, friendDic):

    myFriends = []
    for friend, status in friendDic:
        if status = "accepted":
            myFriends.append(friend)
    
    return myFriends

def sendFriendRequest(user, friendList):
    return
    
# Pass in the user you are asking to be your friend and the friendDic
def addFriend(user, friendDic):

    #if ():
        
    return

# Decline pending friend (user) request and update friend Dic
def delFriend(user, friendList):

    #if ():
        
    return
