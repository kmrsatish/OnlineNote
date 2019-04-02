import xml.etree.ElementTree as ET

tree = ET.parse('cus.xml')
root = tree.getroot()

MSISDN=[]
for x in root.iter('MSISDN'):
    MSISDN.append(x.text)
    
for i in MSISDN:
    print(i)
    
"""ls=[]
for y in root.iter('value'):
    ls.append(y.text)

for i in ls:
    print(i)"""
 
values=[]    
for z in root.iter('TextblockParameter'):
        if(z[0].text=='CONTACTINFO_MSISDN'):
            values.append(z[1].text)
            

for i in values:
    print(i)

import mysql.connector as my
db = my.connect(host="localhost",user="root",passwd="",database="customer")
cursor=db.cursor()
print(db)

cursor.execute("SHOW TABLES")
tables = cursor.fetchall() 
for table in tables:
    print(table)
    
cursor.execute("DESC cust_details")
print(cursor.fetchall())


sql=cursor.execute("SELECT * FROM cust_details")
records = cursor.fetchall()
for record in records:
    print(record)
    
    
"""fet=cursor.execute("SELECT C_no FROM cust_details where Task_id='B0007959920'")"""
all_c_no=cursor.execute("SELECT C_no FROM cust_details")

c_no=cursor.fetchall()
cust_no=[]
for c in c_no:
    cust_no.append(c)

for i in cust_no:
    print(i[0])
    
"""    
if MSISDN[1]!=v[3]:
   upd="UPDATE cust_details SET C_no={} WHERE C_no={}".format(MSISDN[1],v[3][0])
   cursor.execute(upd)
db.commit()   
 """  

"""sql=cursor.execute("SELECT * FROM cust_details")
records = cursor.fetchall()
for record in records:
    print(record) """
    
db.close()