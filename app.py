import streamlit as st

st.title("Electricity Tracker")

days = st.number_input("Number of days", min_value=1, max_value=31, value=7)
rate = st.number_input("Rate per kWh (₱)", value=10.5)

total = 0
for i in range(1, days + 1):
    kwh = st.number_input(f"Day {i} consumption (kWh)", min_value=0.0, key=f"day{i}")
    total += kwh

if st.button("Calculate"):
    avg = total / days
    bill = total * rate
    st.metric("Total Consumption", f"{total:.2f} kWh")
    st.metric("Daily Average", f"{avg:.2f} kWh")
    st.metric("Estimated Bill", f"₱{bill:.2f}")
    if avg > 20:
        st.warning("High usage! Try to reduce appliance usage.")
    else:
        st.success("Good job! Your usage is efficient.")
