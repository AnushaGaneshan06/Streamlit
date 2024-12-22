# dont know
import streamlit as st

# Initialize session state variables
if "step" not in st.session_state:
    st.session_state.step = 1

if "info" not in st.session_state:
    st.session_state.info = {}

# Step 1: Input information
if st.session_state.step == 1:
    st.header("Part 1: Information Form")

    # Input field for name
    name = st.text_input("Enter your name:", value=st.session_state.info.get("name", ""))

    # Proceed to next step
    if st.button("Next"):
        if name.strip():  # Ensure the name is not empty
            st.session_state.info["name"] = name
            st.session_state.step = 2
        else:
            st.warning("Please enter a valid name!")

# Step 2: Review and confirm information
elif st.session_state.step == 2:
    st.header("Part 2: Review Your Information")

    # Display collected information
    st.write(f"**Name**: {st.session_state.info.get('name')}")

    # Buttons to go back or confirm
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Back"):
            st.session_state.step = 1
    with col2:
        if st.button("Confirm"):
            st.success("Information submitted successfully!")
