class Teacher:
    firstName = ""
    lastName = ""
    identityNum = 0
    roomNum = 0
    department = ""

    def __init__(self, firstName, lastName, identityNum, roomNum, department):
        self.firstName = firstName
        self.lastName = lastName
        self.identityNum = identityNum
        self.roomNum = roomNum
        self.department = department
