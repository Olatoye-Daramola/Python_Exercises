import mysql.connector as mysql
from mysql.connector import Error as e


def connect_fetch():
    """function to connect and fetch rows in database"""

    # create a variable for the connector object
    conn = None

    # connect using out database parameters
    host = input("Enter host:\n")
    database = input("Enter database:\n")
    user = input("Enter user:\n")
    password = input("Enter password:\n")

    try:
        conn = mysql.connect(host=host, database=database,
                             user=user, password=password)
        print("Connecting to the database server")
        if conn.is_connected:
            print("Connected to database server")

            # select query
            sql_select_query = "select * from Human"
            cursor = conn.cursor()
            cursor.execute(sql_select_query)
            records = cursor.fetchall()
            print("Total number of rows in human is: ", cursor.rowcount)

            # display data from the database
            print("\nPrinting each Human record")
            # records.insert(10, [11, "Shade Ade", "Blue", "Other", "Unknown"])
            for row in records:
                print("Human Id: ", row[0])
                print("Name: ", row[1])
                print("Color: ", row[2])
                print("Gender: ", row[3])
                print("Blood Group: ", row[4], "\n")

    except:
        print("Not connecting due to: ", e)
    finally:
        if conn is not None and conn.is_connected():
            conn.close()
            print("Database shutdown")


connect_fetch()
