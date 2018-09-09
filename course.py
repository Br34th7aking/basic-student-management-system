# this file contains the class definition of the Course class

class Course:
    def __init__(self, name="", instructor="", credits=4, preReq="", details = "", teeA=[], textbook="" \
    , evaluation="", numStudents=0, status="", cost=0, courseId=""):
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
        self.courseId = courseId

    #setter methods
    def setBasicInfo(self, name, credits, preReq, textbook, courseId):
        self.name = name
        self.credits = credits
        self.preReq = preReq
        self.textbook = textbook
        self.courseId = courseId

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
    def printCourseInfo(self):
        print("*" * 20 + "\n" + \
        "Course Name:", self.name + "\n" + \
        "_" * 20 + "\n" + \
        "Course ID:", self.courseId + "\n" + \
        "_" * 20 + "\n" + \
        "Instructor:", self.instructor + "\n" + \
        "_" * 20 + "\n" + \
        "Credits:", str(self.credits) + "\n" + \
        "_" * 20 + "\n" + \
        "Pre-requisites:", self.preReq + "\n" + \
        "_" * 20 + "\n" + \
        "Textbook:", self.textbook + "\n" + \
        "_" * 20 + "\n" + \
        "Details:", self.details + "\n" + \
        "_" * 20 + "\n" + \
        "Evaluation:", self.evaluation + "\n" + \
        "_" * 20 + "\n" + \
        "Cost: ", str(self.cost) + "\n" + \
        "*" * 20)

    def getCourseId(self):
        return self.courseId

    def getCourseCost(self):
        return self.cost
