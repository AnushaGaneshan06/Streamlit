import streamlit as st

# Fragment 1: Header Section
def header_section():
    """This fragment displays the header and subheader of the app."""
    st.title("Streamlit Fragments Example")
    st.subheader("Breaking a Streamlit app into reusable sections (fragments)")

# Fragment 2: User Input Section
def user_input_section():
    """This fragment collects user input."""
    st.header("User Input Section")
    name = st.text_input("Enter your name:")
    age = st.number_input("Enter your age:", min_value=0, step=1)
    submit_button = st.button("Submit")
    return name, age, submit_button

# Fragment 3: Output Section
def display_output(name, age):
    """This fragment displays the output based on user input."""
    if name and age > 0:
        st.write(f"Hello **{name}**, you are **{age}** years old!")
    else:
        st.warning("Please enter valid name and age.")

# Main Function to Combine All Fragments
def main():
    # Call header fragment
    header_section()

    # Call user input fragment
    name, age, submit_button = user_input_section()

    # If submit button is pressed, display the output
    if submit_button:
        display_output(name, age)

# Run the Streamlit app
if __name__ == "__main__":
    main()
