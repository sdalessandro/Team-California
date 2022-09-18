import pytest
#import unittest
import main


  
def test_log_in_1():
  assert main.additionalOptions() == "communicateothers"

# assert main.learnSkill()== 1
# assert main.learnSkill()== 2
# assert main.learnSkill()== 3
  
  
def test_log_in_2():
 assert main.learnSkill() == "You have successfully learn in"
def test_log_in_3():
 assert main.communicateOthers() == "comm"
  
def test_log_in_4():
 assert main.searchJob() == "search"

def test_log_in_6():
 assert main.skill_1()=="skill_1"
def test_log_in_7():
 assert main.skill_2()=="skill_2"
def test_log_in_8():
 assert main.skill_3()=="skill_3"
def test_log_in_9():
 assert main.skill_4()=="skill_4"
def test_log_in_10():
 assert main.skill_5()=="skill_5"
def test_log_in_11():
 assert main.skill_6()=="skill_6"
def test_log_in_12():
 assert main.accountLimit("arr")=="account"




  
#def test_log_in_incorrect():
# assert log_in("student1", "incorrect_password") == "Incorrect username/password, please try again"
#def test_log_in_empty():
 #assert log_in("", "") == "Incorrect username/password, please try again"
#def test_log_in_None():
 #assert log_in(None, None) == "Incorrect username/password, please try again"
#def test_log_in_special_characters():
 #assert log_in("student1!", "password1!") == "You have successfully logged in"
#def test_log_in_spaces():
 #assert log_in("student 1", "password 1") == "You have successfully logged in"
#def test_log_in_uppercase():
# assert log_in("STUDENT1", "PASSWORD1") == "You have successfully logged in"
#def test_log_in_lowercase():
# assert log_in("student1", "password1") == "You have successfully logged in"
#def test_log_in_numbers():
# assert log_in("12345", "12345") == "You have successfully logged in"
#def test_log_in_minimum_characters():
# assert log_in("s1", "p1") == "You have successfully logged in"
#def test_log_in_maximum_characters():
# assert log_in("student12345", "password12345") == "You have successfully logged in"
#def test_log_in_minimum_one_capital_letter():
 #assert log_in("Student1", "password1") == "You have successfully logged in"
#def test_log_in_minimum_one_digit():
 #assert log_in("student1", "password1") == "You have successfully logged in"
#def test_log_in_minimum_one_special_character():
 #assert log_in("student1", "password1!") == "You have successfully logged in"
#def test_log_in_maximum_twelve_characters():
 #assert log_in("student12345", "password12345") == "You have successfully logged in"
#def test_log_in_maximum_eight_characters():
 #assert log_in("s1", "p1") == "You have successfully logged in"
#def test_log_in_maximum_attempts():
 #for i in range(0, 100):
 #  assert log_in("student1", "password1") == "You have successfully logged in"

#def test_log_in_job_search():
# assert log_in("student1", "password1") == "under construction"
#def test_log_in_find_someone():
# assert log_in("student1", "password1") == "under construction"
#def test_log_in_learn_a_new_skill():
 #assert log_in("student1", "password1") == "under construction"

#def test_log_in_no_skill():
 #assert log_in("student1", "password1") == "under construction"

#def test_log_in_previous_level():
# assert log_in("student1", "password1") == "under construction"
