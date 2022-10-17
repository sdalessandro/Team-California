import pytest
import userMenu
import main
import loginMenu
import User

userList = User.loadUsers("userList.txt")


def test_option1():
  assert loginMenu.mainMenu(userList) == "Login"


def test_option2():
  assert loginMenu.mainMenu(userList) == "Sign up"


def test_option3():
  assert loginMenu.mainMenu(userList) == "Why join"


def test_option4():
  assert loginMenu.mainMenu(userList) == "Find a friend"


def test_option5():
  assert loginMenu.mainMenu(userList) == "Useful links"


def test_option6():
  assert loginMenu.mainMenu(userList) == "Incollege important links"


def test_whyJoin():
  assert loginMenu.whyJoin(userList) == "why Join option success"


def test_findFriends():
  assert loginMenu.findFriends(userList) == "find Friends option success"


def test_general():
  assert loginMenu.usefulLinks(userList) == "General link option success"


def test_goBack():
  assert loginMenu.usefulLinks(userList) == "go back"


def test_browseInCollege():
  assert loginMenu.usefulLinks(userList) == "Browse InCollege option success"


def test_businessSolutions():
  assert loginMenu.usefulLinks(userList) == "under construction"


def test_directories():
  assert loginMenu.usefulLinks(userList) == "under construction"


def test_general():
  assert loginMenu.generalLinks(userList) == "go back"


def test_signup():
  assert loginMenu.generalLinks(userList) == "sign up"


def test_helpCenter():
  assert loginMenu.generalLinks(userList) == "help center"


def test_about():
  assert loginMenu.generalLinks(userList) == "about"


def test_press():
  assert loginMenu.generalLinks(userList) == "press"


def test_blog():
  assert loginMenu.generalLinks(userList) == "blog"


def test_careers():
  assert loginMenu.generalLinks(userList) == "careers"


def test_developers():
  assert loginMenu.generalLinks(userList) == "developers"


def test_userMenu1():
  assert userMenu.mainMenu() == "mainmenu"


def test_userMenu2():
  assert userMenu.jobListings() == "joblist"


def test_userMenu3():
  assert userMenu.skill_1() == "skill1"


def test_userMenu4():
  assert userMenu.skill_2() == "skill2"


def test_userMenu5():
  assert userMenu.skill_3() == "skill3"


def test_userMenu6():
  assert userMenu.skill_4() == "skill4"


def test_userMenu7():
  assert userMenu.skill_5() == "skill5"


def test_userMenu8():
  assert userMenu.skill_6() == "skill6"


def test_userMenu9():
  assert userMenu.importantLinksUser() == "import"


def test_userMenu10():
  assert userMenu.studentSearch() == "studentsearch"


def test_userMenu11():
  assert userMenu.showMyNetwork() == "showmy"


def test_userMenu12():
  assert userMenu.communicateOthers() == "comm"


def test_userMenu13():
  assert userMenu.guestControls() == "guest"


def test_userMenu14():
  assert userMenu.currentPreferences() == "current"


def test_userMenu15():
  assert userMenu.importantLinksUser() == "import"


def test_userMenu16():
  assert userMenu.studentSearch() == "studentsearch"


def test_userMenu17():
  assert userMenu.respondToFriendReq() == "studentsearch"


def test_userMenu18():
  assert userMenu.logout() == "log"

def test_userMenu19():
  assert User.getFriends() == "acc"
def test_userMenu20():
  assert User.sendFriendRequest() == "send"
def test_userMenu21():
  assert User.acceptFriendReq() == "accept"
  
def test_userMenu22():
  assert User.declineFriendReq() == "dec"
def test_userMenu23():
  assert User.loadUsers() == "load"

def test_userMenu24():
  assert User.loadFriends() == "Fr"
def test_userMenu25():
  assert User.createUser(userList) == "create "
  
'''
def test_log_in_1():
    assert userMenu.mainMenu() == "communicateothers"

# assert main.learnSkill()== 1
# assert main.learnSkill()== 2
# assert main.learnSkill()== 3

def test_log_in_2():
    assert userMenu.learnSkill() == "learn"

def test_log_in_3():
    assert userMenu.communicateOthers() == "comm"

def test_log_in_4():
    assert userMenu.searchJob() == "search"

def test_log_in_6():
    assert userMenu.skill_1() == "skill_1"

def test_log_in_7():
    assert userMenu.skill_2() == "skill_2"

def test_log_in_8():
    assert userMenu.skill_3() == "skill_3"

def test_log_in_9():
    assert userMenu.skill_4() == "skill_4"

def test_log_in_10():
    assert userMenu.skill_5() == "skill_5"

def test_log_in_11():
    assert userMenu.skill_6() == "skill_6"

def test_log_in_12():
    assert userMenu.successStory() == "story"

def test1():
    #  assert main.main()== "input"
    assert account.main() == "choice"


def test2():
    assert account.new_user() == 'last'
   # assert main.new_user()=='last2'


def test3():
   # assert main.existing_user()==("exist","error")
   # assert main.existing_user() == "exist"
    assert account.existing_user() == "error"
'''
