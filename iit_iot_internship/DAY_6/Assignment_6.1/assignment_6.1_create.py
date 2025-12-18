import mysql.connector
connection= mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="root",
    database="iot_data_1",
    use_pure=True
)
id=int(input("Enter id:"))
temperature=float(input("enter temperature"))
humidity=float(input("enter humidity:"))
timestamp=(input("enter timestamp:",))

query=f"insert into sensor_readings values ({id},{temperature},{humidity},'{timestamp}');"
    
cursor=connection.cursor()
cursor.execute(query)
connection.commit()
cursor.close()
connection.close()
    