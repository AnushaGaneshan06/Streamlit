import streamlit as st

#streamlit wont support same name so we use key
st.button("ok")
st.button("ok", key="btn") #unquie identifer

# ---------------SLIDER VALUE------------
# identify by parameter

if "slider" not in st.session_state:
    st.session_state.slider = 25

min_value = st.slider("set min value ", 0, 50, 25)

st.session_state.slider = st.slider("slider", min_value, 100, st.session_state.slider)



# ------------checkbox------------


