![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white&style=flat-square)
![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white&style=flat-square)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?logo=postgresql&logoColor=white&style=flat-square)
![MQTT](https://img.shields.io/badge/MQTT-660066?logo=mqtt&logoColor=white&style=flat-square)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white&style=flat-square)
![Pandas](https://img.shields.io/badge/Pandas-150458?logo=pandas&logoColor=white&style=flat-square)


# IoT Building Simulator & Fault Detection

A containerized IoT project that simulates a Building Management System (BMS). It generates HVAC telemetry data, sends it via MQTT, and detects system faults in real time.

This project was built to demonstrate fundamental concepts used in Building Automation and IoT cloud platforms, focusing on data collection, remote connectivity and automated fault detection.

<img width="1830" height="953" alt="dashboard" src="https://github.com/user-attachments/assets/b1dcf1c6-c213-4743-a559-be7c6282209b" />


## How it works

The system is split into 5 services that work together:

1. **IoT Sensor Simulator (Python):** Generates sensor data.
2. **MQTT Broker (Mosquitto):** The communication hub.
3. **Fault Monitor (Python):** Logic for real-time error detection.
4. **Database (PostgreSQL):** For data storage.
5. **Web Dashboard (Streamlit):** UI for data visualisation

   
## Stack
* **Python** (paho-mqtt, pandas, streamlit)
* **MQTT** (Eclipse Mosquitto)
* **PostgreSQL**
* **Docker**


## How to run it?

You only need Docker installed.

1. Clone the repository:
   
    ```text
      git clone [https://github.com/MihaiCosmin2/IoT-Building-Simulator-Fault-Detection.git](https://github.com/MihaiCosmin2/IoT-Building-Simulator-Fault-Detection.git)
         cd IoT-Building-Simulator-Fault-Detection
      ```

2. Start the system:
   
    ```text
   sudo docker compose up --build```

4. Open the Live Dashboard in your browser:

   ```bash http://localhost:8501```




