# this file contains the class definition of the 'Student' class
class Student:
    def __init__(self, name="guest", password="guest", email="", roll="", programme="", courses=[]):
        self.name = name
        self.password = password
        self.email = email
        self.roll = roll
        self.programme = programme
        self.courses = courses

    #setter methods
    def setStudentInfo(self, name, password, email, roll, programme):
        self.name = name
        self.password = password
        self.roll = roll # this is the id for the student
        self.email = email
        self.programme = programme

    def addCourse(self, course):
        self.courses.append(course.getCourseId())

    def removeCourse(self, course):
        self.courses.remove(course.getCourseId())

    #getter methods
    def showInfo(self):
    # displays the student's info
        print('Name:', self.name)
        print('Roll No.', self.roll)
        print('Email:', self.email)
        print('Programme:', self.programme)
        print('Courses Taken:', self.courses)

    def showCoursesTaken(self):
        print(self.courses) # prints a list where each element is a courseId
