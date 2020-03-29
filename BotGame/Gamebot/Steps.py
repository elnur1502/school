import sqlite3
import os.path


class Steps:
    def __init__(self):
        self.DB = "steps.db"
        isExistsStepsDB = os.path.exists(self.DB)

        self.conn = sqlite3.connect(self.DB)  # Connect to DB
        self.cursor = self.conn.cursor()

        if not isExistsStepsDB:
            with open(self.DB, 'a'):
                os.utime(self.DB, None)

            # Creating table
            self.cursor.execute("""CREATE TABLE stepsDB
                              (user text, step integer)
                           """)
            self.conn.commit()

    def getUser(self, userID):
        self.cursor.execute("SELECT * FROM stepsDB WHERE user='{}'".format(userID))
        return self.cursor.fetchone()

    def isExistsUser(self, userID):
        self.cursor.execute("SELECT step FROM stepsDB WHERE user='{}'".format(userID))
        if self.cursor.fetchone() == None:
            return False
        else:
            return True

    def addUser(self, userID):
        self.cursor.execute("INSERT INTO stepsDB VALUES ('{}', 0)".format(userID))
        self.conn.commit()

    def setStep(self, userID, step):
        self.cursor.execute("UPDATE stepsDB SET step={} WHERE user='{}'".format(step, userID))
        self.conn.commit()

    def getStep(self, userID):
        self.cursor.execute("SELECT * FROM stepsDB WHERE user='{}'".format(userID))
        return self.cursor.fetchone()[1]
