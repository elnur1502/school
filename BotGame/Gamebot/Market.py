import sqlite3
import os.path


class Market:
    def __init__(self):
        self.DB = "market.db"
        isExistsMarketDB = os.path.exists(self.DB)

        self.conn = sqlite3.connect(self.DB)  # Connect to DB
        self.cursor = self.conn.cursor()

        if not isExistsMarketDB:
            with open(self.DB, 'a'):
                os.utime(self.DB, None)

            # Creating table
            self.cursor.execute("""CREATE TABLE Market
                              (user text, name text, priceRU text, priceAU text, linkRU text, linkAU text)
                           """)
            self.conn.commit()

    def getUser(self, userID):
        self.cursor.execute("SELECT * FROM Market WHERE user='{}'".format(userID))
        return self.cursor.fetchone()

    def getName(self, userID):
        self.cursor.execute("SELECT * FROM Market WHERE user='{}'".format(userID))
        return self.cursor.fetchone()[1]

    def getPriceRU(self, userID):
        self.cursor.execute("SELECT * FROM Market WHERE user='{}'".format(userID))
        return self.cursor.fetchone()[2]

    def getPriceAU(self, userID):
        self.cursor.execute("SELECT * FROM Market WHERE user='{}'".format(userID))
        return self.cursor.fetchone()[3]

    def getLinkRU(self, userID):
        self.cursor.execute("SELECT * FROM Market WHERE user='{}'".format(userID))
        return self.cursor.fetchone()[4]

    def getLinkAU(self, userID):
        self.cursor.execute("SELECT * FROM Market WHERE user='{}'".format(userID))
        return self.cursor.fetchone()[5]

    def addUser(self, userID, shop):
        for i in range(list(shop)):
            name = str(shop[i]).split("|")[0]
            priceRU = str(shop[i]).split("|")[1]
            priceAU = str(shop[i]).split("|")[2]
            linkRU = str(shop[i]).split("|")[3]
            linkAU = str(shop[i]).split("|")[4]
            self.cursor.execute("INSERT INTO Market VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(userID, name, priceRU, priceAU, linkRU, linkAU))
            self.conn.commit()

    def delUser(self, userID):
        self.cursor.execute("DELETE FROM Market WHERE user='{}'".format(userID))
        self.conn.commit()
