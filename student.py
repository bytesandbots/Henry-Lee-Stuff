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




num = 1

def plusOne(number):
    secondNumber = 2
    print(secondNumber)
    return num+1

plusOne(2)


        




        
