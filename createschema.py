import mysql.connector

def main():
    global db
    try:
        db = mysql.connector.connect(user='combatengine', password='orbusdb',
                                     host='127.0.0.1',
                                     database='ORBUSDB')

        #example
            mycursor = mydb.cursor()
            mycursor.execute("SELECT * FROM customers")
            myresult = mycursor.fetchall()
            for x in myresult:
                print(x)
        #end example


        print(db)
    except Exception as dbe:
        print("************ SOMETHING WENT TRAGICALLY WRONG (EXCEPTION) ****************")
        print(str(dbe))
        print("****************************************")
    finally:
        db.close()


if __name__ == "__main__":
    main()