import streamlit as st
import requests
import pandas as pd

# Backend URL
BACKEND_URL = "https://resvi.onrender.com"  # replace with actual

st.set_page_config(page_title="ResQ Vision Dashboard", page_icon="🚨", layout="wide")

# Logo + title
st.markdown("""
<div style="text-align: center;">
    <img src="https://cdn-icons-png.flaticon.com/512/565/565547.png" alt="Accident Logo" width="80"/>
    <h1 style="color: white;">🚨 ResQ Vision Dashboard</h1>
</div>
""", unsafe_allow_html=True)

st.write("View live reports, trends and search recent accidents:")

# Load reports button
if st.button("📋 Show All Reports"):
    try:
        r = requests.get(f"{BACKEND_URL}/get-reports")
        reports = r.json().get("reports", [])

        if reports:
            df = pd.DataFrame(reports)
            st.subheader("📌 Accident Reports Table")
            st.table(df)

            # Chart
            if 'timestamp' in df.columns:
                df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
                if not df['timestamp'].isna().all():
                    df = df.set_index('timestamp')
                    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
                    if len(numeric_cols):
                        st.subheader("📈 Number of Reports Over Time")
                        st.line_chart(df[numeric_cols[0]])

            # 🔍 Top accident locations
            if 'location' in df.columns:
                st.subheader("📍 Top Locations with Most Accidents")
                top_locations = df['location'].value_counts().head(5)
                st.table(top_locations)

            # 🔍 Search box to filter
            search_term = st.text_input("🔎 Enter Location or Camera ID to see recent accidents:")

            if search_term:
                filtered = df[
                    df['location'].astype(str).str.contains(search_term, case=False, na=False) |
                    df['cam_id'].astype(str).str.contains(search_term, case=False, na=False)
                ]

                if not filtered.empty:
                    st.subheader(f"📝 Recent accidents for '{search_term}':")
                    st.table(filtered.sort_values(by='timestamp', ascending=False).head(10))
                else:
                    st.info("No recent accidents found for this search.")

        else:
            st.info("No reports found yet.")

    except Exception as e:
        st.error(f"Error loading data: {e}")

else:
    st.info("Click the button above to load reports.")

# Footer
st.markdown("---")
st.caption("© 2025 ResQ Vision")
