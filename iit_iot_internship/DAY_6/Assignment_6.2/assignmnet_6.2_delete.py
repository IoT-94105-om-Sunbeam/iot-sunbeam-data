import mysql.connector
connection= mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="root",
    database="smart_agriculture_",
    use_pure=True
)
sensor_id = int(input("Enter Sensor ID to be deleted: "))


query = f"delete from soil_moisture_ where sensor_id={sensor_id};"
cursor = connection.cursor()
cursor.execute(query)
connection.commit()

print("Data deleted successfully")

cursor.close()
connection.close()