import mysql.connector
import time

def db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="Mnrpswrd1234",
        database="credential"
    )

def get_user(email,password):
    db=db_connection()
    cursor=db.cursor()
    start_time = time.time()
    query = "SELECT * FROM USER WHERE email = %s AND password = %s"
    cursor.execute(query, (email, password))
    result = cursor.fetchone()
    query_time = time.time() - start_time
    cursor.close()
    db.close()
