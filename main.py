# Assignment 2 - Student Management System
# Written by - Abhijit Raj
# Roll No - MT18231

import coursedata
from course import Course

# student class
class Student:
    def __init__(self, name="guest", password="guest", email="", roll="", programme="", courses=[]):
        self.name = name
        self.password = password
        self.email = email
        self.roll = roll
        self.programme = programme
        self.courses = courses

# make a list of available courses
availableCourses = [] # contains the list of all available courses
for i in range(len(coursedata.courseList)):
    course = Course()
    # set the basic info
    course.setBasicInfo(coursedata.courseList[i]['name'], coursedata.courseList[i]['credits'], \
    coursedata.courseList[i]['preReq'], coursedata.courseList[i]['textbook'], coursedata.courseList[i]['courseId'])
    #set the instructor and TA
    course.setInstTA(coursedata.courseList[i]['instructor'], coursedata.courseList[i]['teeA'])
    #set the Details
    course.setDetails(coursedata.courseList[i]['details'])
    #set Evaluation
    course.setEvaluation(coursedata.courseList[i]['evaluation'])
    #set Cost
    course.setCost(coursedata.courseList[i]['cost'])
    availableCourses.append(course)


# uncomment below code to see the starter information of all the available courses
for i in range(len(availableCourses)):
    availableCourses[i].getCourseInfo()
