from teacher import Teacher
from student import Student
class School:
    courses = {}
    name = ""
    def __init__(self, name):
        self.name = name
    def addTeacher(self, teacher):
        teacherName = teacher.getName()
        for course in teacher.courses:
            self.courses[course] = teacherName
    def findTeacherPlan(self, teacher):
        
        teacherName = teacher.getName()
        coursestaught = []
        for item in self.courses:
            if self.courses[item] == teacherName:
                coursestaught.append(item)
        return coursestaught


rancho = School("Ranch San Joaquin")

Gastelum = Teacher("Elizabeth", "Gastelum", 529039, 14, "Math")
Gilpin = Teacher("Ava", "Gilpin", 250964, 17, "Orchestra")
Homma = Teacher("Bob", "Homma", 253006, 15, "English")

John = Student("John", "Streets", 12, 4, "Physics")
Ryan = Student("Ryan", "Chung", 14, 4, "Photography")
Carter = Student("Carter", "Lee", 14, 4, "Math")
Gastelum.addCourse("Math 1")
Gastelum.addCourse("Math 2")
Gastelum.addCourse("Math 3")
Homma.addCourse("English 1")
Homma.addCourse("English 2")
Homma.addCourse("English 3")
Gilpin.addCourse("Chamber Orchestra")
Gilpin.addCourse("Symphonic Orchestra")
Gilpin.addCourse("Beginner Orchestra")
rancho.addTeacher(Gastelum)
rancho.addTeacher(Gilpin)
rancho.addTeacher(Homma)

print(rancho.findTeacherPlan(Homma))
print(rancho.findTeacherPlan(Gastelum))
print(rancho.findTeacherPlan(Gilpin))
print(Homma)



        
        
        
