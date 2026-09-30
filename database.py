import json
import sqlite3 as sql

def getConn():
        return sql.connect("database.db")

#database migration scrip called once to create the Database
def migrate( ):
        con = getConn()
        cur = con.cursor()
        cur.execute("""
                    CREATE TABLE IF NOT EXISTS PROJECTS( 
                     ID INTEGER PRIMARY KEY AUTOINCREMENT, 
                     TITLE TEXT NOT NULL, 
                     DIFFICULTY INTEGER NOT NULL, 
                     DESCRIPTION TEXT NOT NULL UNIQUE, 
                     TECHSTACK TEXT NOT NULL,
                     ROADMAP TEXT NOT NULL)
                       """)
        con.commit()
        con.close()

def addProject(title, difficulty, description, techstack,roadmap):
         con = getConn()
         cur = con.cursor()
        # print("values are...")
        # print(title,difficulty,description,techstack,roadmap)
         cur.execute("""
                     INSERT INTO PROJECTS (TITLE,DIFFICULTY,DESCRIPTION,TECHSTACK,ROADMAP)
                     VALUES (?,?,?,?,?)
                     """,(title,difficulty,description,json.dumps(techstack),json.dumps(roadmap)))
         con.commit()
         con.close()