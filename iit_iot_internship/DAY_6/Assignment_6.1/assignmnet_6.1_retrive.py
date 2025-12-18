import mysql.connector
connection= mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="root",
    database="iot_data_1",
    use_pure=True
)


query="select * from sensor_readings where temperature>25" ;
    
cursor=connection.cursor()
cursor.execute(query)
sensor_readings = cursor.fetchall()

# print students data
#print(students)

for i in sensor_readings:
    print(i)
    
# close the cursor
cursor.close()