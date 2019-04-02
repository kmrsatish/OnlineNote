import mysql.connector as my
db = my.connect(host="localhost",user="root",passwd="",database="customer")
cursor=db.cursor()

    

"""cursor.execute("CREATE TABLE cust_details (Task_id VARCHAR(255) NOT NULL PRIMARY KEY,B_acc BIGINT,C_no BIGINT,SSN VARCHAR(255))")"""
cursor.execute("SHOW TABLES")
print(cursor.fetchall())

cursor.execute("DESC cust_details")
print(cursor.fetchall())


query = "INSERT INTO cust_details (Task_id, B_acc,C_no,SSN) VALUES ('123',21154356,31582674717,'321')"
query1 = "INSERT INTO cust_details (Task_id, B_acc,C_no,SSN) VALUES ('124',12543562,367125232911,'421')"
query2 = "INSERT INTO cust_details (Task_id, B_acc,C_no,SSN) VALUES ('125',15725894,31636091204,'521')"
query3 = "INSERT INTO cust_details (Task_id, B_acc,C_no,SSN) VALUES ('126',75842123,316309120,'621')"

cursor.execute(query3)
cursor.execute(query2)
cursor.execute(query1)
cursor.execute(query)

db.commit()

sql=cursor.execute("SELECT * FROM cust_details")
records = cursor.fetchall()
for record in records:
    print(record)
    