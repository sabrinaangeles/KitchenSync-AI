import streamlit as st
import pandas as pd
import datetime

# Set page config
st.set_page_config(page_title="KitchenSync AI", layout="wide")

# Header
st.title("🍔 KitchenSync AI – Live Kitchen Dashboard")
st.subheader("BurgerPlus – Singapore Branch")

# Current time
st.markdown(f"**Current Time:** {datetime.datetime.now().strftime('%I:%M %p')} (Lunch Rush)")

# Kitchen Status Table
st.markdown("### 🍟 Kitchen Live Status")
kitchen_status = pd.DataFrame({
    "Station": ["Grill", "Fryer", "Prep Station", "Assembly"],
    "Status": ["⚠️ Delayed", "⚠️ Overloaded", "✅ On Schedule", "✅ On Schedule"],
    "Wait Time": ["4 mins", "3 mins", "-", "-"],
    "Notes": [
        "Backlog of 12 burger orders",
        "Fries queue growing fast",
        "",
        ""
    ]
})
st.dataframe(kitchen_status, use_container_width=True)

# Predictive Insights
st.markdown("### 🔮 Predictive Insights (Next 15 Minutes)")
st.markdown("""
- 📈 **Order Surge Predicted:** +35% volume in next 8 minutes  
  → Suggest **pre-starting 10 burger patties**  
- 🕒 **Staff Shortage Detected**  
  → Suggest **reallocating 1 prep worker to fryer**  
- ❗ **Potential Waste Warning:** Chicken patties over-prepped  
  → Estimated waste: 14%  
  → Suggest **reducing prep batch size by 25%**
""")

# Staff Suggestions
st.markdown("### 👷 Staff Reallocation Suggestions")
staff_suggestions = pd.DataFrame({
    "Name": ["Aisha", "Kumar", "Mei"],
    "Current Station": ["Prep", "Grill", "Assembly"],
    "Suggested Move": ["→ Fryer", "Stay", "Stay"],
    "Reason": [
        "Fryer overload; Aisha cross-trained",
        "Grill under pressure",
        "Flow is stable"
    ]
})
st.dataframe(staff_suggestions, use_container_width=True)

# KPI Table
st.markdown("### 📊 Kitchen Performance KPIs (Today)")
kpi_data = pd.DataFrame({
    "Metric": [
        "Avg. Order Completion Time", 
        "Prep Waste Rate", 
        "Staff Utilization Rate", 
        "On-Time Orders"
    ],
    "Value": ["9.4 mins", "6.2%", "92%", "81%"],
    "Benchmark": ["≤ 8 mins", "≤ 4%", "85–95%", "≥ 90%"],
    "Status": ["⚠️ Behind", "⚠️ High", "✅ Good", "⚠️ Needs Attention"]
})
st.dataframe(kpi_data, use_container_width=True)

# AI Recommendations
st.markdown("### 🔄 Live Recommendations (From KitchenSync AI)")
st.markdown("""
1. **Reassign Aisha to Fryer for 20 mins**
2. **Pre-cook 10 burger patties immediately**
3. **Pause chicken patty prep – projected waste too high**
4. **Send alert to front-of-house: Slight delay expected on burger orders**
""")
