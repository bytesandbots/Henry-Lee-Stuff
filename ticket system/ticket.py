import sqlite3 as sql
from pathlib import Path
DATABASE_PATH = Path(__file__).parent.joinpath("ticket.db")

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
        with sql.connect("ticket.db") as conn:
            cursor = conn.cursor()
            #The issue is with the value with type list. The database excepts string. NEED TO BE FIXED NEXT TIME.
            cursor.execute(f"""INSERT INTO tickets("{title}", "{description}", "{asignee}", "{label}", "{priority}", "{comment}")""")
    
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