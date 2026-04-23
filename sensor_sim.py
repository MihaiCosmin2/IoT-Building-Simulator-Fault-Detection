import paho.mqtt.client as mqtt
import json
import time
import random

# Broker address is the server wich the data is being sent off to
broker_address = "mqtt-broker"
# Topic is a channel which services can listen to
topic = "building/hvac/telemetry"
# TCP/IP connection on 1883
client = mqtt.Client("Simulator_HVAC")
client.connect(broker_address, 1883)

# This while imitates a hardware sensor from a building
while True:
    temp = round(random.uniform(17.0, 27.0), 1)
    status = random.choice(["ON", "ON", "ON", "OFF"])
    # Equipments don't break 33% of time so we got to put weights on the statuses
    fault_code = random.choices([0, 1, 2], weights=[0.95, 0.025, 0.025])[0]
    # Building json data
    payload = {
        "device_id": "HVAC_Unit_1",
        "temperature_c": temp,
        "hvac_status": status,
        "fault_code": fault_code
    }
    msg = json.dumps(payload)

    # Sending the data to MQTT server
    client.publish(topic, msg)
    print(f"Sent message: {msg}")
    time.sleep(3) # 3 sec pause
