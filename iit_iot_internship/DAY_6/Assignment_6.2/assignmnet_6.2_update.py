import mysql.connector
connection= mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="root",
    database="smart_agriculture_",
    use_pure=True
)
sensor_id = int(input("Enter Sensor ID to be update: "))
moisture_level = float(input("Enter Moisture Level to be updated: "))

query = f"update soil_moisture_ SET moisture_level={moisture_level} where sensor_id={sensor_id}"
cursor = connection.cursor()
cursor.execute(query)
connection.commit()

print("Data updated successfully")

cursor.close()
connection.close()