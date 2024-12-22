import streamlit as st

# Initialize the counter in session state if it doesn't exist
if "counter" not in st.session_state:
    st.session_state.counter = 0

# Increment button
if st.button("Increment Counter"):
    st.session_state.counter += 1
    st.write(f"Counter incremented to {st.session_state.counter}")

# Reset button
if st.button("Reset Counter"):
    st.session_state.counter = 0
    st.write("Counter reset to 0")

# Display the current counter value
st.write(f"Current counter value: {st.session_state.counter}")

# Button to increment and update immediately
if st.button("Increment and Update Immediately"):
    st.session_state.counter += 1
    st.experimental_rerun()  # Immediately reruns the app to update the counter
