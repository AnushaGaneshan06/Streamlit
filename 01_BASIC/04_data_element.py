import streamlit as st
import pandas as pd

st.title("Streamlit Element Demo")


st.subheader("Dataframe")
df = pd.DataFrame({
    "name" : ["alice", "bob", "david", "shinchan"],
    "age":[2, 3 , 45, 6],
    "occupation": ["engineer", "doctor", "artist", "dancer"]
})
st.dataframe(df)

# DATA EDITOR SECTION (EDITABLE DATAFRAME)
st.subheader("data editor")
editable_df = st.data_editor(df)



# STATIC TABLE DATA

st.subheader("static table")
st.table(df)


# METERIC SECTION

st.subheader("Metrics")
st.metric(label="Total ROW", value = len(df))
st.metric(label="Average age", value = round(df["age"].mean(), 1)) # 1 is the point


#JSON AND DICT SECTION
st.write("JSON")
sample_dict = {
    "name" : ["alice", "bob", "david", "shinchan"],
    "age":[2, 3 , 45, 6],
    "occupation": ["engineer", "doctor", "artist", "dancer"]

}
st.json(sample_dict)
st.write(sample_dict)
st.write("dictionary view", sample_dict)