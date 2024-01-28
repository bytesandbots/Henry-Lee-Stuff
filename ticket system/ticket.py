# READ THE COMMENT IN LINE 42
# Start with implementing the database connection in your 

import sqlite3 as sql
from pathlib import Path
DATABASE_PATH = Path(__file__).parent.joinpath("ticket.db")

def listToString(list) -> str:
    str = ""
    for item in list:
        str = str + item + ","
    str[:-1] #removes the last comma
    return str    

class Ticket:

    def __init__(self, title, description="", asignee=[], label=[], priority="normal", comment=[]):
        try:
            conn = sql.connect(DATABASE_PATH)
            cursor = conn.cursor()
            cursor.execute("""CREATE TABLE tickets(
                        title STRING,
                        description STRING,
                        asignees STRING,
                        label STRING,
                        priority STRING,
                        comment STRING
            )
            """)
        except(sql.OperationalError):
            pass
            conn.close()
        self.title = title
        self.description = description
        self.asignee = asignee
        self.label = label
        self.priority = priority
        self.comment = comment
        self.closed = False
        with sql.connect(DATABASE_PATH) as conn:
            cursor = conn.cursor()
            # Please note the function listToString(). It takes a list and returns a string with all of the list items separated with a comma
            cursor.execute(f"""INSERT INTO tickets VALUES("{self.title}", "{self.description}", "{listToString(self.asignee)}", "{listToString(self.label)}", "{self.priority}", "{listToString(self.comment)}")""")
    
    def add_assignee(self, asignee):
        self.asignee.append(asignee)
        #what if there is more than one asignee

    def add_label(self, label):
        self.label.append(label)
    
    def add_comment(self, comment):
        self.comment.append(comment)

    def close(self):
        self.closed = True
    
    def __str__(self):
        ticketString = f"""
        title: {self.title}\n
        description: {self.description}\n
        asignee: {self.asignee}\n
        label: {self.label}\n
        priority: {self.priority}\n
        Is closed: {self.closed}\n
        """
        return ticketString

ticket = Ticket("dog")

ticket.add_assignee("henry")
ticket.add_label("dogissues")
ticket.add_comment("doe")
ticket.close()
print(ticket)