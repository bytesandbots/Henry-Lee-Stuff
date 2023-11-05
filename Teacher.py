class Teacher:
    firstName = ""
    lastName = ""
    identityNum = 0
    roomNum = 0
    department = ""
    students = []
    courses = []

    def __init__(self, firstName, lastName, identityNum, roomNum, department):
        self.firstName = firstName
        self.lastName = lastName
        self.identityNum = identityNum
        self.roomNum = roomNum
        self.department = department
        self.courses= []
    def __str__(self):
        return f"{self.firstName}, {self.lastName}, {self.identityNum}, {self.roomNum}, {self.department}"
    def addCourse(self, course):
        self.courses.append(course)
    def removeCourse(self, course):
        try:
            self.courses.pop(course)
        except ValueError:
            print("Cannot be removed since not in course")
    def getName(self):
        return self.firstName + self.lastName
        
    
