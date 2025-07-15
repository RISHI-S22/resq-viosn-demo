import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="ResQ Vision Dashboard", layout="wide", page_icon="🚨")

# Dark theme style
st.markdown(
    """
    <style>
    body {background-color: #111; color: #fff;}
    .st-cm {color: #fff;}
    </style>
    """, unsafe_allow_html=True
)

# Title & logo
st.title("🚨 ResQ Vision - Accident Detection Dashboard")

# Dummy accident data
data = {
    "Location": ["NH44 Cam 01", "Ring Road Cam 02", "City Center Cam 03", "Highway Cam 04"],
    "Date": ["2025-07-13", "2025-07-12", "2025-07-12", "2025-07-11"],
    "Time": ["15:30", "20:45", "18:10", "09:25"],
    "Severity": ["High", "Medium", "Low", "High"]
}
df = pd.DataFrame(data)

# Show table
st.subheader("📄 Recent Accident Reports")
st.table(df)

# Accident count chart (dummy data)
st.subheader("📊 Accident Trend - Last 7 Days")
accidents_per_day = [2, 3, 1, 4, 2, 3, 5]
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

fig, ax = plt.subplots()
ax.bar(days, accidents_per_day, color='red')
ax.set_ylabel("Number of Accidents")
ax.set_xlabel("Day")
ax.set_title("Weekly Accident Count")

st.pyplot(fig)
