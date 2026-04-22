import streamlit as st
import pandas as pd
import json

st.title("AI Observability Dashboard")

# Load logs
data = []
with open("../safegen-api/ai_usage_logs.jsonl", "r") as f:
    for line in f:
        data.append(json.loads(line))

df = pd.DataFrame(data)

# KPIs
total = len(df)
allowed = len(df[df["decision"] == "allowed"])
blocked = len(df[df["decision"] == "blocked"])

st.metric("Total Requests", total)
st.metric("Allowed", allowed)
st.metric("Blocked", blocked)

# Filters
user_filter = st.selectbox("Filter by User", ["All"] + list(df["user"].unique()))

if user_filter != "All":
    df = df[df["user"] == user_filter]

# Charts
st.subheader("Requests Over Time")
df["timestamp"] = pd.to_datetime(df["timestamp"])
st.line_chart(df.set_index("timestamp").resample("1T").count()["prompt"])

st.subheader("Blocked Reasons")
blocked_df = df[df["decision"] == "blocked"]
if not blocked_df.empty:
    st.bar_chart(blocked_df["reason"].value_counts())

# Table
st.subheader("Recent Requests")
st.dataframe(df.tail(10))
