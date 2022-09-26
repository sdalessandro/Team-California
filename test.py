import pytest
import userMenu
import main

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
