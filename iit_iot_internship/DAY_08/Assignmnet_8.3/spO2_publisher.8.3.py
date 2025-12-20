import paho.mqtt.client as mqtt

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.connect("localhost")

spo2 = 100        
client.publish("health/spo2", spo2)

print("spO2 sent:", spo2)
client.disconnect()