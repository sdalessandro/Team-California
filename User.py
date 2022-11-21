import re, ast

global currentUser

class User(object):

    def __init__(self, username, password, firstName, lastName, plusMember):
        super(User, self).__init__()
        self.username = username
        self.password = password
        self.firstName = firstName
        self.lastName = lastName
        self.loggedIn = False
        self.plusMember = plusMember

    # Takes in the entire friend log and checks which are "accepted"
    def getFriends(self, friendLog):
        myFriends = []
        for friend, status in friendLog.items():
            if status == "accepted":
                myFriends.append(friend)
        
        return myFriends
        
    # Takes in the username to modify friend status, updates friendDic, and saves changes
    def modFriendReq(self, username, friendDic, status):
        for user, userFriends in friendDic.items():
            tmpDic = ast.literal_eval(userFriends)
            if user == self.username:
                # Only sending pending req to recipient 
                if status == "pending":
                    tmpDic[username] = "waiting"
                else:
                    tmpDic[username] = status
            if user == username:
                tmpDic[self.username] = status
            friendDic[user] = str(tmpDic)
    
        saveFriends(friendDic)
        return friendDic

    # Unfriend yourself and the passed username by updating friendDic and saves the changes
    def rmFriend(self, username, friendDic):
        for user, userFriends in friendDic.items():
            tmpDic = ast.literal_eval(userFriends)
            if self.username == user:
                tmpDic.pop(username, "Error: {0} not friends with {1}".
                    format(self.username, username))
            if username == user:
                tmpDic.pop(self.username, "Error: {0} is not friends with {1}".
                    format(username, self.username))
            friendDic[user] = str(tmpDic)
    
        saveFriends(friendDic)
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

def saveUser(username, password, firstName, lastName, plusMember):
    # Write new user to userList.txt
    file = open("userList.txt", 'a')
    file.write("{0} {1} {2} {3} {4}\n".format(username, password, firstName, lastName, plusMember))
    file.close()

    #Write new user to userFriends.txt
    file = open("userFriends.txt", 'a')
    file.write(username + " {}\n")
    file.close()

    # write new user to newUsers.txt
    file = open("newUsers.txt", 'a')
    file.write(username + " {}\n")
    file.close()

def createUser(userList):
    username = setUsername(userList)
    password = setPassword()
    firstName = setFirstName()
    lastName = setLastName()
    plusMember = setSubscription()

    saveUser(username, password, firstName, lastName, plusMember)
    
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

def setSubscription():
    choice = input("Would you like to subscribe to Plus membership for $10 a month (y or n): ")

    if choice == "y":
      return True
    elif choice == "n":
      return False
    else:
      print("Invalid choice, pick y or n")
      setSubscription()