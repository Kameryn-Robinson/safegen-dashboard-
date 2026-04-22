import streamlit as st
import pandas as pd
import json

st.title("AI Observability Dashboard")

LOG_FILE = "../safegen-api/ai_usage_logs.jsonl"

# Load logs
data = []
try:
    with open(LOG_FILE, "r") as f:
        for line in f:
            line = line.strip()
            if line:
                data.append(json.loads(line))
except FileNotFoundError:
    st.info("Waiting for first API request... no logs found yet.")
    st.stop()

if not data:
    st.info("Log file exists, but no requests have been recorded yet.")
    st.stop()

df = pd.DataFrame(data)

# KPIs
total = len(df)
allowed = len(df[df["decision"] == "allowed"])
blocked = len(df[df["decision"] == "blocked"])

st.metric("Total Requests", total)
st.metric("Allowed", allowed)
st.metric("Blocked", blocked)

# Filters
user_filter = st.selectbox("Filter by User", ["All"] + sorted(df["user"].dropna().unique().tolist()))

if user_filter != "All":
    df = df[df["user"] == user_filter]

# Charts
st.subheader("Requests Over Time")
df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
df = df.dropna(subset=["timestamp"])

if not df.empty:
    requests_over_time = df.set_index("timestamp").resample("1min").count()["prompt"]
    st.line_chart(requests_over_time)

st.subheader("Blocked Reasons")
blocked_df = df[df["decision"] == "blocked"]
if not blocked_df.empty:
    st.bar_chart(blocked_df["reason"].fillna("Unknown").value_counts())

# Table
st.subheader("Recent Requests")
st.dataframe(df.tail(10), use_container_width=True)
