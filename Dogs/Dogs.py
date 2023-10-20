import os
import sqlite3

def main():
    add_dog() 
    list_dog()

#add_dog------------------------
def add_dog():
    #print("Hund")
    os.system("cls" if os.name == "nt" else "clear" )
    hundnamn = input("Mata in namnet på hunden: ")
    hundras = input("Mata in rasen på hunden: ")

    sqliteConnection = sqlite3.connect("Dogs.db")
    cursor = sqliteConnection.cursor()
    sqlite_insert_query = f""" INSERT INTO dogs(namn, ras) Values ('{hundnamn}', '{hundras}')"""

    cursor.execute(sqlite_insert_query)
    sqliteConnection.commit()
    print("La till BYRACKA")

    cursor.close()
    sqliteConnection.close()

#show list---------------------------
def list_dog():
    sqliteConnection = sqlite3.connect("Dogs.db")
    cursor = sqliteConnection.cursor()
    sqlite_select = """SELECT * FROM Dogs ORDER by namn"""
    cursor.execute(sqlite_select)
    records = cursor.fetchall()

    for myDog in records:
        print(f"\t ID: {myDog[0]}, \tNAMN: {myDog[1]}, \tRAS: {myDog[2]}")

    cursor.close()
    sqliteConnection.close()
    print("The SQLite connection is closed")


        
    
    


#-----------------------
main()