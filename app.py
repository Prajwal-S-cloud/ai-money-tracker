import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from analyzer import extract_data
from advisor import analyze_spending, financial_advice

st.set_page_config(page_title="AI Money Tracker", layout="wide")

st.title("💰 AI Money Tracker & Advisor")
st.markdown("Smart expense analysis powered by AI")

# Load data
data = pd.read_csv("sms_data.csv")

records = []
for msg in data["message"]:
    amount, category = extract_data(msg)
    records.append({
        "message": msg,
        "amount": amount,
        "category": category
    })

df = pd.DataFrame(records)

# 🔹 ADD THIS HERE
st.sidebar.header("Filters")
category_filter = st.sidebar.selectbox(
    "Select Category",
    ["All"] + list(df["category"].unique())
)

if category_filter != "All":
    df = df[df["category"] == category_filter]

# Layout columns
col1, col2 = st.columns(2)

total, summary = analyze_spending(df)

with col1:
    st.subheader("📊 Total Spending")
    st.metric("Total", f"₹ {total}")

with col2:
    st.subheader("📁 Transactions")
    st.dataframe(df)

st.subheader("📈 Category Breakdown")

fig, ax = plt.subplots()
ax.pie(summary, labels=summary.index, autopct='%1.1f%%')
st.pyplot(fig)

st.subheader("🧠 AI Financial Advice")
advice = financial_advice(summary)

for a in advice:
    st.success(a)