# import Flask class from flask module
from flask import Flask, request

from utils.executeQuery import executeQuery
from utils.executeSelectQuery import executeSelectQuery

# create a server usinf Flask
server = Flask(__name__)

@server.get('/')
def homepage():
    return "<html><body><h1>This is home page</h1></body></html>"

@server.route('/sensor_readings', methods=['POST'])
def create_sensor_readings():
    # extract data form form
    id = request.form.get('id')
    temp = request.form.get('temp')
    humidity = request.form.get('humidity')
    timestamp = request.form.get('timestamp')

    query = f"insert into sensor_readings values({id}, '{temp}', '{humidity}', '{timestamp}');"

    #print(query)
    #execute the query 
    executeQuery(query=query)

    return "sensor_readings is added successfully"

@server.route('/sensor_readings', methods=['GET'])
def retrieve_sensor_readings():
    query = "select * from sensor_readings;"

    data = executeSelectQuery(query=query)

    return f"sensor_readings : {data}"

@server.route('/sensor_readings', methods=['PUT'])
def update_sensor_readings():

    id = request.form.get('id')
    temp = request.form.get('temp')

    query = f"update sensor_readings SET temp = '{temp}' where id = '{id}';"

    executeQuery(query=query)

    return "temp is updated successfully"

@server.route('/sensor_readings', methods=['DELETE'])
def delete_sensor_readings():

    id = request.form.get('id')
    query = f"delete from sensor_readings where id = '{id}';"

    executeQuery(query=query)

    return "sensor_readings is deleted successfully"

if __name__ == '__main__':
    server.run(host='0.0.0.0', port=4000, debug=True)