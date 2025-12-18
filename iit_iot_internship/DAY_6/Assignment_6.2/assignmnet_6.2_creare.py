import mysql.connector
connection= mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="root",
    database="smart_agriculture_",
    use_pure=True
)
sensor_id = int(input("Enter Sensor ID: "))
moisture_level = float(input("Enter Moisture Level: "))
reading_time = input("Enter Date and Time: ")

query = f"insert into soil_moisture_ values({sensor_id},{moisture_level},'{reading_time}');"

cursor = connection.cursor()
cursor.execute(query)
connection.commit()

print("Data inserted successfully")

cursor.close()
connection.close()