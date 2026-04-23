import streamlit
import psycopg2
import pandas
import os
import time


DB_HOST = os.getenv("DB_HOST", "localhost")
DB_NAME = "iot_data"
DB_USER = "admin"
DB_PASS = "database_pass"

streamlit.set_page_config(page_title="BMS Dashboard", layout="wide")
streamlit.title("Building Management System - Dashboard")
streamlit.markdown("Real time monitoring for temperature and HVAC status.")


def get_data():
    try:
        conn = psycopg2.connect(host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASS)
        query = "SELECT timestamp, device_id, temperature, status, fault_code FROM hvac_telemetry ORDER BY timestamp DESC LIMIT 50"
        df = pandas.read_sql_query(query, conn)
        conn.close()
        return df
    except Exception as e:
        streamlit.error(f"Could not connect to Database: {e}")
        return pandas.DataFrame()
    
df = get_data()


if not df.empty:
    latest_temp = df['temperature'].iloc[0]
    latest_status = df['status'].iloc[0]

    col1, col2, col3 = streamlit.columns(3)
    col1.metric("Current Temperature", f"{latest_temp} C")
    col2.metric("HVAC Status", latest_status)
    col3.metric("Active Alerts", "0" if df['fault_code'].iloc[0] == 0 else "! ERROR")

    streamlit.divider()

    streamlit.subheader("Temperature history (last 50 readings)")
    chart_data = df.set_index('timestamp')['temperature']
    streamlit.line_chart(chart_data)

    streamlit.subheader("Data Logs")
    streamlit.dataframe(df, use_container_width=True)


else:
    streamlit.warning("Waiting on sensors data...")

time.sleep(3)
streamlit.rerun()
