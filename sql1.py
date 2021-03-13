import mysql.connector

if __name__ == "__main__":
    database = mysql.connector.connect(
        host="dct-turtle-uav.cojdookdlkis.us-east-1.rds.amazonaws.com",
        user="admin",
        password="DukeConservationTech1!"
    )
    mycursor = database.cursor()
    sqlCommand = ""
    value = ""
    mycursor.execute(sqlCommand, value)
    database.commit()
    print(database)