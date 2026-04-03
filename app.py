import streamlit as st

st.title("⚡ Electricity Tracker")
st.write("simple lang to, para malaman mo kung magkano kuryente mo 😅")

rate = st.number_input("Rate per kWh (₱)", value=10.5)
days = st.number_input("Ilang days?", min_value=1, max_value=31, value=7)

st.write("---")
st.write("i-enter mo yung daily consumption mo:")

total_kwh = 0
for i in range(1, int(days) + 1):
    daily = st.number_input(f"day {i} (kWh)", min_value=0.0, key=f"day{i}")
    total_kwh += daily

st.write("---")

if st.button("compute na 🔌"):
    average = total_kwh / days
    total_cost = total_kwh * rate

    st.write("### results:")
    st.write(f"📊 total consumption: **{total_kwh:.2f} kWh**")
    st.write(f"📅 average per day: **{average:.2f} kWh**")
    st.write(f"💸 estimated bill: **₱{total_cost:.2f}**")

    st.write("---")

    if average > 20:
        st.warning("grabe naman kuryente mo pre 😬 bawasan mo na yung aircon")
    elif average > 10:
        st.info("medyo mataas, okay lang naman 😐")
    else:
        st.success("ayos! matipid ka 👍")
