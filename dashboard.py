import streamlit as st
import requests
import pandas as pd
import folium
from streamlit_folium import st_folium

# Backend URL
BACKEND_URL = "https://resvi.onrender.com"  # replace with your actual backend URL

st.set_page_config(page_title="ResQ Vision Dashboard", page_icon="🚨", layout="wide")

# Logo + title
st.markdown("""
<div style="text-align: center;">
    <img src="https://cdn-icons-png.flaticon.com/512/565/565547.png" alt="Accident Logo" width="80"/>
    <h1 style="color: white;">🚨 ResQ Vision Dashboard</h1>
</div>
""", unsafe_allow_html=True)

st.write("View live reports, trends and accident locations below:")

# Show reports table and chart
st.subheader("📊 Accident Reports Table & Chart")
if st.button("📋 Show All Reports"):
    r = requests.get(f"{BACKEND_URL}/get-reports")
    reports = r.json().get("reports", [])

    if reports:
        df = pd.DataFrame(reports)
        st.table(df)

        # Convert timestamp
        if 'timestamp' in df.columns:
            df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
            if not df['timestamp'].isna().all():
                df = df.set_index('timestamp')
                numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
                if len(numeric_cols):
                    st.line_chart(df[numeric_cols[0]])
                else:
                    st.info("No numeric data to plot.")
            else:
                st.info("Timestamps could not be parsed.")
        else:
            st.info("No 'timestamp' column found.")
    else:
        st.info("No reports found.")

# Show map
st.subheader("🗺 Accident Locations Map")

# Create sample map with sample marker (replace with real data)
m = folium.Map(location=[17.385044, 78.486671], zoom_start=12)
folium.Marker([17.385044, 78.486671], popup="Sample Accident").add_to(m)

st_folium(m, width=700, height=500)

# Footer
st.markdown("---")
st.caption("© 2025 ResQ Vision")
