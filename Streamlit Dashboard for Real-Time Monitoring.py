# Basic real-time temperature dashboard using Streamlit
import streamlit as st
import pandas as pd
import time, random

st.title("RotorWind Machine Monitoring Dashboard")

placeholder = st.empty()

while True:
    df = pd.DataFrame({
        'timestamp': [pd.Timestamp.now()],
        'temperature': [round(random.uniform(45, 105), 2)]
    })
    with placeholder.container():
        st.line_chart(df.set_index("timestamp"))
    time.sleep(5)
