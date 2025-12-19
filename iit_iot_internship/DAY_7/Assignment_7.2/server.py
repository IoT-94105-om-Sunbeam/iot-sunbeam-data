from flask import Flask, request
from utils.executeQuery import executeQuery
from utils.executeSelectQuery import executeSelectQuery

server = Flask(__name__)

@server.get('/')
def homepage():
    return "<html><body><h1>Moisture Sensor</h1></body></html>"

@server.post('/sensor')
def create_sensor():
    sensor_id = request.get_json().get('sensor_id')
    moisture_level = request.get_json().get('moisture_level')
    reading_time = request.get_json().get('reading_time')

    query = f"insert into soil_moisture_ values ({sensor_id}, {moisture_level}, '{reading_time}');"
    executeQuery(query=query)

    return "Sensor record added successfully"

@server.get('/sensor')
def retrieve_sensors():
    query = "select * from soil_moisture_;"
    data = executeSelectQuery(query=query)

    return f"Sensor Records: {data}"

@server.put('/sensor')
def update_sensor():
    sensor_id = request.get_json().get('sensor_id')
    moisture_level = request.get_json().get('moisture_level')

    query = f"update soil_moisture_ SET moisture_level = {moisture_level} where sensor_id = {sensor_id};"
    executeQuery(query=query)

    return "Moisture level updated successfully"

@server.delete('/sensor')
def delete_sensor():
    sensor_id = request.get_json().get('sensor_id')

    query = f"delete from soil_moisture_ where sensor_id = {sensor_id};"
    executeQuery(query=query)

    return "Sensor record deleted successfully"

@server.get('/sensor/below')
def moisture_below_threshold():
    threshold = request.args.get('threshold')

    query = f"select * from soil_moisture_ where moisture_level < {threshold};"
    data = executeSelectQuery(query=query)

    return f"Moisture below threshold {threshold}: {data}"

if __name__ == '__main__':
    server.run(host='0.0.0.0', port=4000, debug=True)