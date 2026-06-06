import streamlit as st
import pandas as pd

st.title("CEP Projects Overview")

# Sample CEP-style dataset
data = pd.DataFrame({
    "Project": ["Preston College", "School A", "Community Hall", "Library Roof"],
    "Type": ["Solar PV", "Solar PV", "Solar PV", "Solar PV"],
    "Capacity (kWp)": [467, 120, 80, 150],
    "Status": ["Active", "Planned", "Feasibility", "Active"],
    "Annual Generation (kWh)": [420000, 110000, 70000, 135000]
})

st.subheader("Project Table")
st.dataframe(data)

st.subheader("Quick Insights")

st.metric("Total Projects", len(data))
st.metric("Total Capacity (kWp)", data["Capacity (kWp)"].sum())
st.metric("Total Generation (kWh)", data["Annual Generation (kWh)"].sum())