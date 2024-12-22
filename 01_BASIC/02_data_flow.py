# DATA FLOW IN STAREMLIT
# Every time reload the page adta are refresh or vanish or run again

# ---------------------------------------------------
import streamlit as st

print("run")
pressed = st.button("Press Me")
print("first", pressed)
# rerun the application of the true or false


pressed2 = st.button("Second Button")
print("Second",pressed)