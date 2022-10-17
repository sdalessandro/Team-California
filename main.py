import loginMenu, User

print("Welcome to InCollege!\n")
loginMenu.successStory()

userList = User.loadUsers("userList.txt")
friendDic = User.loadFriends("userFriends.txt")
loginMenu.mainMenu(userList, friendDic)