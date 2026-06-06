import streamlit as st
import pandas as pd

st.title("Financial Overview")

# Sample CEP financial model
df = pd.DataFrame({
    "Project": ["Preston College", "School A", "Community Hall"],
    "Investment (£)": [500000, 120000, 80000],
    "Annual Savings (£)": [65000, 18000, 12000],
})

df["Payback (Years)"] = df["Investment (£)"] / df["Annual Savings (£)"]

st.subheader("Project Financials")
st.dataframe(df)

# KPIs
st.subheader("Portfolio Summary")

total_investment = df["Investment (£)"].sum()
total_savings = df["Annual Savings (£)"].sum()
avg_payback = df["Payback (Years)"].mean()

col1, col2, col3 = st.columns(3)

col1.metric("Total Investment", f"£{total_investment:,}")
col2.metric("Annual Savings", f"£{total_savings:,}")
col3.metric("Avg Payback (Years)", f"{avg_payback:.1f}")