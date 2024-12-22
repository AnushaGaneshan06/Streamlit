import streamlit as st
import time

# Define a function to fetch data with caching enabled
@st.cache_data(ttl=60)  # Cache the function's output for 60 seconds
def fetch_data():
    # Simulate a delay to represent data fetching
    time.sleep(3)
    # Return the data that will be cached
    return {"data": "This is cached data!!"}

# Display a message before fetching data
st.write("Fetching data...")

# Call the fetch_data function
# The first call will take 3 seconds (due to the delay), but subsequent calls within 60 seconds will use cached data.
data = fetch_data()

# Display the fetched data
st.write(data)
