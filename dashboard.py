import streamlit as st
import requests

BACKEND_URL = "https://resvi.onrender.com"

st.title("🚨 ResQ Vision Dashboard")

if st.button("Check Service Status"):
    r = requests.get(f"{BACKEND_URL}/status")
    st.write(r.json())

if st.button("Run Fake AI Detection"):
    r = requests.get(f"{BACKEND_URL}/detect")
    st.write(r.json())

sensor_id = st.text_input("Sensor ID")
data = st.number_input("Sensor Data", step=0.1)
if st.button("Send Sensor Data"):
    r = requests.post(f"{BACKEND_URL}/report?sensor_id={sensor_id}&data={data}")
    st.write(r.json())

location = st.text_input("Location for Alert")
if st.button("Send Alert"):
    r = requests.post(f"{BACKEND_URL}/alert?location={location}")
    st.write(r.json())

if st.button("Show All Reports"):
    r = requests.get(f"{BACKEND_URL}/get-reports")
    reports = r.json().get("reports", [])
    st.write(reports)
