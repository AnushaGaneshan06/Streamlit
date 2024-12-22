import streamlit as st
from datetime import datetime

# Title for the app
st.title("User Information Form")

# Initialize form values
form_values = {
    "name": None,
    "height": None,
    "gender": None,
    "dob": None,
    "location": None
}

# Define minimum and maximum date for date of birth
min_date = datetime(1990, 1, 1)
max_date = datetime.now()

# Create the form
with st.form(key="user_info_form"):
    form_values["name"] = st.text_input("Enter your name:")
    form_values["height"] = st.number_input("Enter your height (in cm):", min_value=0)
    form_values["gender"] = st.selectbox("Select your gender:", ["Male", "Female", "Other"])
    form_values["dob"] = st.date_input("Enter your birthdate:", min_value=min_date, max_value=max_date)
    form_values["location"] = st.text_input("Enter your location:")

    # Submit button
    submit_button = st.form_submit_button(label="Submit")

    # Handle form submission
    if submit_button:
        # Check if any field is empty or None
        if None in form_values.values() or any(str(value).strip() == "" for value in form_values.values()):
            st.warning("Please fill in all the fields!")
        else:
            st.balloons()
            st.write("### Submitted Information:")
            for key, value in form_values.items():
                st.write(f"**{key.capitalize()}**: {value}")
