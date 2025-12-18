import mysql.connector

connection = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="root",
    database="smart_agriculture_",
    use_pure=True
)

threshold = float(input("Enter moisture level threshold: "))

query = f"select * from soil_moisture_ where moisture_level < {threshold};"


cursor = connection.cursor()
cursor.execute(query)

soil_moisture_ = cursor.fetchall()
for i in soil_moisture_:
    print(i)

cursor.close()

connection.close()