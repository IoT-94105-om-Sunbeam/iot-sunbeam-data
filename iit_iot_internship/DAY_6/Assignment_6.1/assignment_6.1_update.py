import mysql.connector
connection= mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="root",
    database="iot_data_1",
    use_pure=True
)
id=int(input("Enter id whose temp to be updated:"))
temperature=float(input("enter temperature whose temperature to be updated"))


query=f"update sensor_readings SET temperature ={temperature} where id={id}"
    
cursor=connection.cursor()
cursor.execute(query)
connection.commit()
cursor.close()
connection.close()