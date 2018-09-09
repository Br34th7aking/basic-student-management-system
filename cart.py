# contains code for the cart class

class Cart:
    def __init__(self, itemList=[], cost=0, shippingCost=5000):
        self.itemList = itemList
        self.cost = cost
        self.shippingCost = shippingCost

    #setter methods
    def addItem(self, student, course):
        # adds a course to the cart
        self.itemList.append(course)
        self.cost = self.cost + course.getCourseCost()
        student.addCourse(course)

    def removeItem(self, student, course):
        # removes a course from the cart
        if (len(self.itemList) == 0):
            print ("Cart is empty!")
        else:
            if course in self.itemList:
                self.itemList.remove(course)
                self.cost = self.cost - course.getCourseCost()
                student.removeCourse(course)

    #getter methods
    def displayCart(self):
        # shows the list of all courses currently in cart
        courseList = []
        for i in range(len(self.itemList)):
            courseList.append(self.itemList[i].getCourseId())
        print(courseList)

    def currentCartContent(self):
        #returns the list of items present in cart, but doesn't print them
        return self.itemList

    def printItemInfo(self, course):
        #prints the details of the course present in the cart
        course.printCourseInfo()

    def totalCourseCost(self):
        #returns the total cost of all the courses taken by student
        return self.cost + self.shippingCost
