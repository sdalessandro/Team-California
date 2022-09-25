import pytest
#import unittest
import loginMenu
import account

def test_log_in_1():
    assert loginMenu.additionalOptions() == "communicateothers"


# assert main.learnSkill()== 1
# assert main.learnSkill()== 2
# assert main.learnSkill()== 3


def test_log_in_2():
    assert loginMenu.learnSkill() == "learn"


def test_log_in_3():
    assert loginMenu.communicateOthers() == "comm"


def test_log_in_4():
    assert loginMenu.searchJob() == "search"


def test_log_in_6():
    assert loginMenu.skill_1() == "skill_1"


def test_log_in_7():
    assert loginMenu.skill_2() == "skill_2"


def test_log_in_8():
    assert loginMenu.skill_3() == "skill_3"


def test_log_in_9():
    assert loginMenu.skill_4() == "skill_4"


def test_log_in_10():
    assert loginMenu.skill_5() == "skill_5"


def test_log_in_11():
    assert loginMenu.skill_6() == "skill_6"


def test_log_in_12():
    assert loginMenu.successStory() == "story"

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
  
