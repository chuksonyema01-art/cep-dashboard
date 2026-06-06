import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Environmental Impact Dashboard")

# Sample CEP-style data
df = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Energy (kWh)": [28000, 32000, 45000, 51000, 55000, 60000],
    "Carbon Saved (tCO₂)": [6, 7, 10, 12, 14, 15]
})

# Energy trend
st.subheader("Energy Generation Trend")
fig1 = px.line(df, x="Month", y="Energy (kWh)", markers=True)
st.plotly_chart(fig1, use_container_width=True)

# Carbon trend
st.subheader("Carbon Savings Trend")
fig2 = px.bar(df, x="Month", y="Carbon Saved (tCO₂)")
st.plotly_chart(fig2, use_container_width=True)

# Insights
st.subheader("Key Insights")

st.info("📈 Energy generation is steadily increasing month-on-month.")
st.info("🌍 Carbon savings are improving, indicating stronger renewable impact.")
st.info("⚡ Strong alignment with community sustainability goals.")