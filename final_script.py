import xml.etree.ElementTree as ET

tree = ET.parse('cus.xml')
root = tree.getroot()

MSISDN=[]
for x in root.iter('MSISDN'):
    MSISDN.append(x.text)
    
values=[]    
for z in root.iter('TextblockParameter'):
        if(z[0].text=='CONTACTINFO_MSISDN'):
            values.append(z[1].text)


"""SQL FIEL """

import mysql.connector as my
db = my.connect(host="localhost",user="root",passwd="",database="customer")
cursor=db.cursor()

all_c_no=cursor.execute("SELECT C_no FROM cust_details")

c_no=cursor.fetchall()
cust_no=[]
for c in c_no:
    cust_no.append(c)
    
    
list_len=len(cust_no)    
for i in range(list_len):
    if MSISDN[i]!=cust_no[i]:
        upd="UPDATE cust_details SET C_no={} WHERE C_no={}".format(MSISDN[i],cust_no[i][0])
        cursor.execute(upd)
        db.commit()
        
for i in range(list_len):
    if values[i]!=cust_no[i]:
        upd="UPDATE cust_details SET C_no={} WHERE C_no={}".format(values[i],cust_no[i][0])
        cursor.execute(upd)
        db.commit()
 
db.close()