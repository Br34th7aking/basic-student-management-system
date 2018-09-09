# Assignment 2 - Student Management System
# Written by - Abhijit Raj
# Roll No - MT18231

import coursedata

class Student:
    def __init__(self, name="guest", password="guest", email="", roll="", programme="", courses=[]):
        self.name = name
        self.password = password
        self.email = email
        self.roll = roll
        self.programme = programme
        self.courses = courses


class Course:
    def __init__(self, name="", instructor="", credits=4, preReq="", details = "", teeA=[], textbook="" \
    , evaluation="", numStudents=0, status="", cost=0):
        self.name = name
        self.instructor = instructor
        self.credits = credits
        self.preReq = preReq
        self.teeA = teeA
        self.textbook = textbook
        self.evaluation = evaluation
        self.numStudents = numStudents
        self.status = status
        self.details = details
        self.cost = cost

    #setter methods
    def setBasicInfo(self, name, credits, preReq, textbook):
        self.name = name
        self.credits = credits
        self.preReq = preReq
        self.textbook = textbook

    def setInstTA(self, inst, teeA):
        self.instructor = inst
        self.teeA = teeA

    def setDetails(self, details):
        self.details = details

    def setEvaluation(self, evaluation):
        self.evaluation = evaluation

    def setCost(self, cost):
        self.cost = cost
    # getter methods
    def getCourseInfo(self):
        print("*" * 20)
        print("Course Name:", self.name)
        print("_" * 20)
        print("Instructor:", self.instructor)
        print("_" * 20)
        print("Credits:", self.credits)
        print("_" * 20)
        print("Pre-requisites:", self.preReq)
        print("_" * 20)
        print("Textbook:", self.textbook)
        print("_" * 20)
        print("Details:", self.details)
        print("_" * 20)
        print("Evaluation:", self.evaluation)
        print("_" * 20)
        print("Cost", self.cost)
        print("*" * 20)

# test code
# make a list of available courses
availableCourses = [] # contains the list of all available courses
for i in range(len(coursedata.courseList)):
    course = Course()
    # set the basic info
    course.setBasicInfo(coursedata.courseList[i]['name'], coursedata.courseList[i]['credits'], \
    coursedata.courseList[i]['preReq'], coursedata.courseList[i]['textbook'])
    #set the instructor and TA
    course.setInstTA(coursedata.courseList[i]['instructor'], coursedata.courseList[i]['teeA'])
    #set the Details
    course.setDetails(coursedata.courseList[i]['details'])
    #set Evaluation
    course.setEvaluation(coursedata.courseList[i]['evaluation'])
    #set Cost
    course.setCost(coursedata.courseList[i]['cost'])
    availableCourses.append(course)
