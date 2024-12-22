import streamlit as st
import os


st.title("Simple titlt")
st.header("This the header")
st.header("Subheader")
st.markdown("This the **STREAMLIT** ")
st.markdown("This the __STREAMLIT__  ")
st.caption("small text")

code_example = """
def greet(name):
print("hello this the code inside the markdown", name)
"""
st.code(code_example, language="python")

st.divider() #line

# IMAGE INSERTION

st.image(os.path.join(os.getcwd(), "static", "2.png"), width=200)



