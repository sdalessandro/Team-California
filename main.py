import loginMenu, User

print("Welcome to InCollege!\n")
loginMenu.successStory()

userList = User.loadUsers("userList.txt")
loginMenu.mainMenu(userList)