import mysql.connector
from mysql.connector import Error

mydb = mysql.connector.connect(host = "localhost" , user = "root" , password = "28868755", database = "abcd")

def student(stid,stname,stgender):
    try :
        ptr = mydb.cursor()
        query = "insert into student values (%s,%s,%s)"
        parameters = (stid,stname,stgender)
        ptr.execute(query,parameters)
        mydb.commit()
    except Error as error:
        print("Failed to execute insertion: {}".format(error))
    finally:
        if (mydb.is_connected()):
            ptr.close()

student('1001','Roma Mishra','Female')

def display():
    try :
        ptr = mydb.cursor()
        query = 'Select *from student'
        ptr.execute(query)
        result = ptr.fetchall()
        print(result)
    except Error as error:
        print("Failed to execute insertion: {}".format(error))
    finally:
        if (mydb.is_connected()):
            ptr.close()

display()


''' 
OUTPUT :- 
[(1001, 'Roma Mishra', 'Female')]
'''
