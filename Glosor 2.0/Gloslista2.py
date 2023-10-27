
import sqlite3 as list

def connect():

    sqList = list.connect("Gloslista2.db")
    cursor = sqList.cursor()
    return sqList, cursor

def addList(native, trans, sqList, cursor):
    cursor.execute(f"""INSERT INTO Gloslista (Na, Tr)
                   VALUES ("{native}","{trans}") """)
    sqList.commit()

def showList(cursor):
    words = []

    cursor.execute("""SELECT * FROM Gloslista""")
    for obj in cursor:
        words.append(obj)
        
    return words

def delete(sqList, cursor):
    cursor.execute("""DELETE FROM Gloslista""")
    #cursor.execute("""""")
    sqList.commit()







