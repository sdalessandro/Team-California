import User
import userMenu
import loginMenu
import main
import sqlite3

def setup():
  # create test files for users
  file = open("testStudentAccounts.txt", "w")
  for i in range(11):
    file.write("Username{}!\n".format(i))
    file.write("Password1!\n")
    file.write("fName{}".format(i))
    file.write("lName{}".format(i))
    file.write("=====\n")

  # create test files for job input
  file = open("testNewJobs.txt", "w")
  for i in range(11):
    file.write("title{}\n".format(i))
    file.write("Description of\njob listing\n&&&\n")
    file.write("posterName{}\n".format(i))
    file.write("employerName{}\n".format(i))
    file.write("location{}\n".format(i))
    file.write("{}\n".format(i*100))
    file.write("=====\n")

def test_student_accounts():
  # test num of students created
  file = open("userList.txt", 'r')
  lines = file.readlines()
  for line in lines:
    count = count + 1
    
  assert count == 10

def test_job_input():
  db = sqlite3.connect("jobListings.db")
  cur = db.cursor()

  jobs = cur.execute('SELECT * FROM jobs')
  assert len(jobs) == 10

  for i, job in enumerate(jobs):
    expected = (
            i+1,
            "employerName{}".format(i),
            "title{}".format(i),
            "Description of job listing",
            "posterName{}".format(i),
            "location{}".format(i),
            i*1000
    )

    assert job[0] == expected[0]
    assert job[1] == expected[1]
    assert job[2] == expected[2]
    assert job[3] == expected[3]
    assert job[4] == expected[4]
    assert job[5] == expected[5]
