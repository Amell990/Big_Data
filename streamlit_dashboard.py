import streamlit as st
import pandas as pd
import json
from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'temperature_topic',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='latest',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

st.title("RotorWind Temperature Monitoring Dashboard")

temperature_data = []

for message in consumer:
    data = message.value
    temperature_data.append(data)

    df = pd.DataFrame(temperature_data)
    st.line_chart(df['temperature'])

    if df['temperature'].iloc[-1] > 85:
        st.error(f"ALERT: High temperature ({df['temperature'].iloc[-1]}°C) detected!")

    if len(temperature_data) > 100:
        temperature_data.pop(0)
