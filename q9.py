import mysql.connector

conn = mysql.connector.connect(
    user='serra',      
    password='1234',  
    host='127.0.0.1',            
    database='Devices' 
)

cursor = conn.cursor()
query = """ SELECT Device_Type, REGEXP_SUBSTR(Stats_Access_Link, 'https?://[^<]+')
FROM Devices_Table; """

cursor.execute(query)
results = cursor.fetchall()

cursor.close()
conn.close()
