import loginMenu, User, apis

print("Welcome to InCollege!\n")
loginMenu.successStory()
apis.inputAccounts()
userList = User.loadUsers("userList.txt")
friendDic = User.loadFriends("userFriends.txt")
#apis.inputJobListings()
apis.outputUsers(userList)
apis.outputJobListings()
apis.outputAppliedJobs()
apis.outputSavedJobs()
apis.outputProfiles()
loginMenu.mainMenu(userList, friendDic)