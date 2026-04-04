import streamlit as st
import random

st.title("⚡ Electricity Tracker")

days = st.number_input("Number of days", min_value=1, max_value=31, value=7)
rate = st.number_input("Rate per kWh (₱)", value=10.5)

total = 0
for i in range(1, int(days) + 1):
    kwh = st.number_input("Day " + str(i) + " consumption (kWh)", min_value=0.0, key="day" + str(i))
    total += kwh

tips = [
    "try unplugging appliances you're not using, they still consume power on standby 😬",
    "if you're using aircon, try setting it to 26°C instead of lower, saves a lot 😅",
    "check if any lights or electric fans were left on somewhere in the house 👀",
]

if st.button("Calculate"):
    avg = total / days
    bill = total * rate

    st.metric("Total Consumption", str(round(total, 2)) + " kWh")
    st.metric("Daily Average", str(round(avg, 2)) + " kWh")
    st.metric("Estimated Bill", "₱" + str(round(bill, 2)))

    if avg > 20:
        st.warning("High usage! Try to reduce appliance usage.")
        st.write("💡 tip:", random.choice(tips))
    else:
        st.success("Good job! Your usage is efficient.")
