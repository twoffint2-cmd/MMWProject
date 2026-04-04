import streamlit as st
import random

st.title("⚡ Electricity Tracker")

rate = st.number_input("Rate per kWh (₱)", value=10.5)

st.write("---")
st.write("How do you want to input your usage?")
mode = st.radio("Pick one:", ["By appliance (watts + hours)", "By meter reading (start and end)"])

st.write("---")

total = 0

if mode == "By appliance (watts + hours)":
    st.write("add your appliances below:")
    num_appliances = st.number_input("How many appliances?", min_value=1, max_value=20, value=1)
    days = st.number_input("How many days?", min_value=1, max_value=31, value=7)

    for i in range(1, int(num_appliances) + 1):
        st.write("appliance " + str(i))
        watts = st.number_input("Watts", min_value=0.0, key="watts" + str(i))
        hours = st.number_input("Hours used per day", min_value=0.0, key="hours" + str(i))
        kwh = (watts * hours / 1000) * days
        total += kwh

else:
    st.write("enter your meter readings:")
    start = st.number_input("Previous Reading (kWh)", min_value=0.0)
    end = st.number_input("Current Reading (kWh)", min_value=0.0)
    days = st.number_input("How many days in between?", min_value=1, max_value=31, value=7)
    total = end - start
    if total < 0:
        st.error("end reading cant be lower than start reading 😅")
        total = 0

tips = [
    "try unplugging appliances you're not using, they still consume power on standby 😬",
    "if you're using aircon, try setting it to 26°C instead of lower, saves a lot 😅",
    "check if any lights or electric fans were left on somewhere in the house 👀",
]

st.write("---")

if st.button("Calculate"):
    if days > 0:
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
