import streamlit as st

st.sidebar.title("This is the sidebar")
st.sidebar.write("You can have the place eleemnt like slider, button and text here")
sidebar_input = st.sidebar.text_input("Enter the something in side bar")



# TABS LAYOUTS

tab1, tab2 , tab3 = st.tabs(["Tab1", "Tab2", "Tab3"])

with tab1:
    st.write("You are in tab 1")

with tab2:
    st.write("You are in tab 2")

with tab3:
    st.write("You are in tab 3")


#columns
col1, col2, col3 = st.columns(3)

with col1:
    st.header("column 1")
    st.write("content for column 1")

with col2:
    st.header("column 2")
    st.write("content for column 2")

with col3:
    st.header("column 3")
    st.write("content for column 3")

#conatiner example

with st.container(border=True):
    st.write("This is inside the container")
    st.write("This is inside the container as a grouping for a element")
    st.write("container help manage section of the page")



# EMPTY PLACEHOLDER

placeholder = st.empty()
placeholder.write("This is the empty placeholder useful for dynamic content")

if st.button("update placeholder"):
    placeholder.write("The content is updated")


# EXPANDER
with st.expander("Expand for more deatils"):
    st.write("This the additional information hidden by default")
    st.write("You can expander to keep your inter fcae cleaner")


# POPOVER 

st.write("hover over this button for the tooltip")
st.button("Button with tooltip ", help="This the tooltio or popover on hover")


#side bar input handling
if sidebar_input:
    st.write(f"you have entered in sidebar : {sidebar_input}")






