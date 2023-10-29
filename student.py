class Student:

    firstName = ""
    lastName = ""
    age = 0
    gpa = 4.0
    course = []



    def __init__(self, firstName, lastName, age, gpa, course):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.gpa = gpa
        self.course = course
        
    def changeFirstName(self, firstName):
        self.firstName = firstName
    def changeLastName(self, lastName):
        self.lastName = lastName

    def checkClass(self, course):
        
        try:
            self.course.index(course)
            print(f"{self.firstName} is taking {course}")
        except ValueError:
            print(f"{self.firstName} is not taking {course}")

    ## Work on try and exceptions with Henry
            
    def __str__(self):
        return f"{self.firstName}, {self.lastName}, {self.age}, {self.gpa}, {self.course}"

##    def outputInfo(self):
##        print(self.firstName, self.lastName, self.age, self.gpa, self.course)
    def addClass(self, course):
        self.course.append(course)

    def removeClass(self, course):
        try:
            index = self.course.index(course)
            self.course.pop(index)
        except ValueError:
            print("Cannot be removed since not taking class")

    def changeGPA(self, gpa):
        self.gpa = gpa
        
    def changeAge(self):
        self.age += 1
        


henry = Student("Henry", "Lee", 12, 4.0, ["ELA", "ComputerScience", "Math", "Spanish"])
jack = Student("Jack", "Lee", 12, 4.0, ["Art", "Soccer", "Chemistry", "Physics"])
henry.changeAge()
jack.changeAge()
henry.addClass("English 1")
henry.removeClass("ELA")
henry.checkClass("chemistry")
jack.removeClass("Math")
jack.checkClass("Math")
##henry.outputInfo()
####henry.changeGPA(4.1)
####henry.outputInfo()
##jack.outputInfo()
print(henry)
print(jack)

        
