# Assignment 2 - Student Management System
# Written by - Abhijit Raj
# Roll No - MT18231

import coursedata
from course import Course
from student import Student
from cart import Cart


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
# for i in range(len(availableCourses)):
#     availableCourses[i].printCourseInfo()

newStudent = Student()
name = "Abhijit"
password = "recycled_fiber"
email = "subwayip@iiitd.ac.in"
roll = "MT18231"
programme = "MTECH"

newStudent.setStudentInfo(name, password, email, roll, programme)
newStudent.showInfo()
print('\n\n')
#uncomment below code to see how courses are added to the student's course list
# for i in range(len(availableCourses)):
#     newStudent.addCourse(availableCourses[i])
# newStudent.showInfo()
# print('\n\n')
#
# #uncomment below code to see how courses are removed from the student's course list
# for i in range(len(availableCourses)):
#     newStudent.removeCourse(availableCourses[i])
# newStudent.showInfo()
# print('\n\n')

# building a cart
courseCart = Cart()
# added all courses to cart
#there are 3 courses in the coursedata.py. There total cost is 80,000
for i in range(len(availableCourses)):
    courseCart.addItem(newStudent, availableCourses[i])

print('Current Courses in cart: ')
courseCart.displayCart()
print('Total course cost is{}'.format(courseCart.totalCourseCost()))

# to see the description of a course uncomment the corresponding line below
# courseCart.printItemInfo(courseCart.currentCartContent()[0]) # the first course
# courseCart.printItemInfo(courseCart.currentCartContent()[1]) # the second course
# courseCart.printItemInfo(courseCart.currentCartContent()[2]) # the third course


# below code removes all courses except the last one, i.e. OOPD
courseCart.removeItem(newStudent, availableCourses[0])
print('Current Courses in cart: ')
courseCart.displayCart()
print('Total course cost is{}'.format(courseCart.totalCourseCost()))


courseCart.removeItem(newStudent, availableCourses[1])
print('Current Courses in cart: ')
courseCart.displayCart()
print('Total course cost is{}'.format(courseCart.totalCourseCost()))



# show the contents of student one last time
newStudent.showInfo()
