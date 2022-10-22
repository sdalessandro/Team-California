import re, json
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

    # Takes in the entire friend log and checks which are "accepted"
    def getFriends(self, friendLog):
        myFriends = []
        for friend, status in friendLog:
            if status == "accepted":
                myFriends.append(friend)
        
        return myFriends
        
    # Takes in the username of the person you are wanting to friend and updates friendDic
    def sendFriendRequest(self, username, friendDic):
        #dict = json.loads(friendDic)
        for user, userFriends in friendDic.items():
            if user == self.username:
                friendDic[user] = "pending"
            if user == username:
                friendDic[user] = "pending"
    
        saveFriends(friendDic)
        
    # updates friendDic by making yourself and username friends
    def acceptFriendReq(self, username, friendDic):
        for user, userFriends in friendDic.items():
            if self.username == user:
                userFriends[user] = "accepted"
            if username == user:
                userFriends[user] = "accepted"
    
        return friendDic
    
    # Decline pending friend (user) request and update friendDic
    def declineFriendReq(self, username, friendDic):
        for user, userFriends in friendDic.items():
            if self.username == user:
                userFriends[user] = "declined"
            if username == user:
                userFriends[self.username] = "declined"
    
        return friendDic
    
    # Unfriend yourself and the passed username by updating friendDic
    def rmFriend(self, username, friendDic):
        for user, userFriends in friendDic.items():
            if self.username == user:
                userFriends.pop(username, "Error: {0} not friends with {1}".
                    format(self.username, username))
            if username == user:
                userFriends.pop(self.username, "Error: {0} is not friends with {1}".
                    format(username, self.username))
    
        return friendDic


def loadUsers(fileName):
    with open(fileName) as userFile:
        userList = [User(*(line.split(' '))) for line in userFile]
    return userList

def loadFriends(fileName):
    friendDic = {}

    with open("userFriends.txt", "r") as friendFile:
        lines = friendFile.read().splitlines()
        for line in lines:
            key, value = line.split(' ', 1)
            friendDic[key] = value

    return friendDic

def saveFriends(friendDic):

    friendFile = open("userFriends.txt", "w")
    friendFile.truncate()
    for user, userFriends in friendDic.items():
        friendFile.write("{0} {1}\n".format(user, userFriends))
            
    friendFile.close()

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