import paho.mqtt.client as mqtt
import json
import psycopg2
import os
import time


DB_HOST = os.getenv("DB_HOST", "localhost")
DB_NAME = "iot_data"
DB_USER = "admin"
DB_PASS = "database_pass"


while True:
    try:
        conn = psycopg2.connect(host=DB_HOST,
                                database= DB_NAME,
                                user= DB_USER,
                                password= DB_PASS)
        cur = conn.cursor()
        cur.execute(""" CREATE TABLE IF NOT EXISTS hvac_telemetry (
                            id SERIAL PRIMARY KEY,
                            device_id VARCHAR(50),
                            temperature REAL,
                            status VARCHAR(10),
                            fault_code INTEGER,
                            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP);


                    """)
        conn.commit()
        print("Succesfully connected with PostgreSQL.")
        break
    except Exception as e:
        print(f"Waiting on database... {e}")
        time.sleep(2)


broker_address = "mqtt-broker"
topic = "building/hvac/telemetry"


def on_message(client, userdata, message):
    try:
        payload = json.loads(message.payload.decode("utf-8"))

        cur.execute(""" 
                INSERT INTO hvac_telemetry (device_id, temperature, status, fault_code)
                VAlUES (%s, %s, %s, %s)
        """, (payload['device_id'], payload['temperature_c'], payload['hvac_status'], payload['fault_code']))
        conn.commit()


        if payload['fault_code'] != 0:
            print(f"[ALERT] Error detected on device's id: {payload['device_id']}!")
        else:
            print(f"[DATA_SAVED] Saved Log sucessfully for device's id {payload['device_id']}: {payload['temperature_c']}C")

    except Exception as e:
        print(f"Data processing error: {e}")
    

client = mqtt.Client("Monitor_Sistem")
client.on_message = on_message

client.connect(broker_address, 1883)
client.subscribe(topic)

print("The Monitoring script has started. Waiting on cloud data...")
client.loop_forever()


