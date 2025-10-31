import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta

st.set_page_config(page_title="CU Thermal Twin", layout="wide")

st.markdown("# 🏆 Chandigarh University Thermal Digital Twin")
st.markdown("### Real-time Campus Thermal Analysis & Smart Recommendations")

# Hardcoded dataset (works without backend)
zones_data = [
    {"zone": "Main Parking Lot", "temp": 44.1, "uv": 9.9, "status": "🔴 Hotspot"},
    {"zone": "Academic Block A", "temp": 37.6, "uv": 8.2, "status": "🟡 Medium"},
    {"zone": "Academic Block B", "temp": 36.8, "uv": 8.0, "status": "🟡 Medium"},
    {"zone": "Boys Hostel 1", "temp": 35.9, "uv": 7.8, "status": "🟢 Safe"},
    {"zone": "Boys Hostel 2", "temp": 36.3, "uv": 7.9, "status": "🟡 Medium"},
    {"zone": "Girls Hostel", "temp": 35.4, "uv": 7.5, "status": "🟢 Safe"},
    {"zone": "Sports Stadium", "temp": 41.1, "uv": 10.2, "status": "🔴 Hotspot"},
    {"zone": "Central Library", "temp": 34.0, "uv": 6.2, "status": "🟢 Safe"},
    {"zone": "Green Quad", "temp": 30.2, "uv": 7.6, "status": "🟢 Safe"},
    {"zone": "Food Court", "temp": 37.9, "uv": 8.5, "status": "🟡 Medium"},
    {"zone": "Bus Stop", "temp": 37.4, "uv": 9.1, "status": "🟡 Medium"},
    {"zone": "Admin Block", "temp": 35.2, "uv": 7.7, "status": "🟢 Safe"},
]

# Sidebar Navigation
with st.sidebar:
    st.header("🎯 Navigation")
    page = st.radio("Go to:", ["📊 Dashboard", "❓ Q&A", "🌡️ Zones", "📈 Forecast", "💰 ROI", "🔬 Analytics"])

# ---- Dashboard ----
if page == "📊 Dashboard":
    st.subheader("Campus Thermal Status")
    df = pd.DataFrame(zones_data)
    st.dataframe(df)

# ---- Zones ----
elif page == "🌡️ Zones":
    st.subheader("Zone Details")
    selected = st.selectbox("Select Zone:", [z["zone"] for z in zones_data])
    zone = next(z for z in zones_data if z["zone"] == selected)
    st.metric("Temperature", f"{zone['temp']}°C")
    st.metric("UV Index", zone["uv"])
    st.metric("Status", zone["status"])

st.markdown("---")
st.caption("Chandigarh University Thermal Digital Twin | 2025")
