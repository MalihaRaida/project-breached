import hashlib
import mysql.connector


def db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="Mnrpswrd1234",
        database="credential"
    )

def insert_db(cursor,value):
    sql = "INSERT INTO USER (EMAIL, PASSWORD) VALUES (%s, %s)"
    cursor.execute(sql,value)
        

def read_credentials(inputfile):
    with open(inputfile, 'r', encoding="utf8") as file:
        for line in file:
            if ':' in line:
                yield line.rstrip('\n').split(":")

def hash_credentials(credential):
    email_hash = hashlib.sha256(credential[0].encode("utf-8")).hexdigest()
    password_hash = hashlib.sha256(credential[1].encode("utf-8")).hexdigest()
    return (email_hash, password_hash)

if __name__ == "__main__":
    input_file1 = "C:\\Users\\User\\Downloads\\data\\credentials1.txt"
    input_file2 = "C:\\Users\\User\\Downloads\\data\\credentials2.txt"
    input_file_short= "C:\\Users\\User\\Downloads\\data\\credentials_short.txt"

    with db_connection() as db:
        with db.cursor() as cursor:
            count=0
            for credential in read_credentials(input_file_short):
                insert_db(cursor,hash_credentials(credential))
                count=count+1
                print(count)
            db.commit()
            


# credentials_list2=read_credentials("C:\\Users\\User\\Downloads\\Project Breached\\data\\credentials2.txt")
# hashed_list=hash_credentials(credentials_list2)
# insert_db(hashed_list)

# db.close()