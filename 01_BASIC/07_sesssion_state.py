import streamlit as st

# counter = 0

# st.write(f"Counter value : {counter}" )

# # BUTTON TO INCREMENT COUNTER

# if st.button("Increement Counter"):
#     counter += 1
#     st.write(f"Counter is increement to {counter}")
# else:
#     st.write(f"Counter stays at {counter}")




if "counter" not in st.session_state:
    st.session_state.counter = 0

if st.button("Increement button"):
    st.session_state.counter += 1
    st.write(f"counter increment to {st.session_state.counter}")

if st.button("Reset"):
    st.session_state.counter = 0
else:
    st.write(F"counter did not reset")

st.write(f"counter value : {st.session_state.counter}")