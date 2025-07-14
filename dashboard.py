import streamlit as st
import requests
import pandas as pd

BACKEND_URL = "https://resvi.onrender.com"

st.set_page_config(page_title="🚨 ResQ Vision Dashboard", page_icon="🚀", layout="centered")

st.title("🚨 ResQ Vision Dashboard")
st.markdown("AI-powered accident detection & reporting")

st.sidebar.title("⚙️ Controls")

if st.sidebar.button("✅ Check Service Status"):
    r = requests.get(f"{BACKEND_URL}/status")
    st.success(r.json())

if st.sidebar.button("🎲 Run Fake AI Detection"):
    r = requests.get(f"{BACKEND_URL}/detect")
    st.info(r.json())

st.subheader("📡 Send Sensor Data")
sensor_id = st.text_input("Sensor ID", value="LP-01")
data = st.number_input("Sensor Data", step=0.1, value=0.0)
if st.button("📤 Send"):
    r = requests.post(f"{BACKEND_URL}/report?sensor_id={sensor_id}&data={data}")
    st.success(r.json())

st.subheader("🚨 Send Manual Alert")
location = st.text_input("Location for Alert", value="Main Road, City")
if st.button("⚠️ Send Alert"):
    r = requests.post(f"{BACKEND_URL}/alert?location={location}")
    st.warning(r.json())

st.subheader("📊 Accident Reports Table")
if st.button("📋 Show All Reports"):
    r = requests.get(f"{BACKEND_URL}/get-reports")
    reports = r.json().get("reports", [])
    if reports:
        df = pd.DataFrame(reports)
        st.table(df)
    else:
        st.info("No reports found yet.")
