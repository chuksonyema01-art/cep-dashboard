import streamlit as st
import pandas as pd
st.sidebar.title("Filters")

selected_project = st.sidebar.selectbox(
    "Select Project",
    ["All", "Preston College", "School A", "Community Hall"]
)

selected_year = st.sidebar.selectbox(
    "Select Year",
    ["2024", "2025", "2026"]
)

st.set_page_config(page_title="CEP Dashboard", layout="wide")

# Title
st.title("Community Energy Preston Impact Dashboard")

st.write("Real-time overview of energy, carbon, funding, and projects")

# Dummy KPI data
energy = 211000
carbon = 49
investment = 185000
projects = 3

# KPI Cards
col1, col2, col3, col4 = st.columns(4)

col1.metric("Energy Generated", f"{energy:,} kWh", "+12%")
col2.metric("Carbon Saved", f"{carbon} tCO₂", "+8%")
col3.metric("Investment Raised", f"£{investment:,}", "+5%")
col4.metric("Active Projects", projects, "Stable")
import plotly.express as px

# Sample data (energy generation trend)
df = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr", "May"],
    "Energy": [28000, 32000, 45000, 51000, 55000]
})

st.subheader("Energy Generation Trend")

fig = px.line(df, x="Month", y="Energy", markers=True)
st.plotly_chart(fig, use_container_width=True)
st.subheader("Carbon Impact")

carbon_df = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr", "May"],
    "Carbon Saved": [6, 7, 10, 12, 14]
})

fig2 = px.bar(carbon_df, x="Month", y="Carbon Saved")
st.plotly_chart(fig2, use_container_width=True)
st.subheader("Project Portfolio")

projects = pd.DataFrame({
    "Project": ["Preston College", "School A", "Community Hall"],
    "Status": ["Active", "Planned", "Feasibility"],
    "Capacity (kWp)": [467, 120, 80]
})

st.dataframe(projects)
st.subheader("Environmental Impact Equivalent")

st.info("🌳 49 tCO₂ saved ≈ Removing ~10 cars from the road annually")
st.info("🏠 Energy generated ≈ Powering ~60 homes per year")