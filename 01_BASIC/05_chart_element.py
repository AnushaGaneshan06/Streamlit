import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px


st.title("Stramlit chart demo")

# sample data
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["a", "b", "c"]
)

st.subheader("area chart")
st.area_chart(chart_data)

#bar chart
st.subheader("bar chart")
st.bar_chart(chart_data)

#line chart
st.subheader("line chart")
st.line_chart(chart_data)


#line chart
st.subheader("Scatter chart")
scatter_data = pd.DataFrame({
    "x" :np.random.randn(100),
    "y" :np.random.randn(100),
})
st.scatter_chart(chart_data)



#map 
st.subheader("map")
map_data = pd.DataFrame(
    np.random.randn(100, 2) / [50, 50] + [37.76, -122.4],
    columns=["lat", "lon"]
)
st.map(map_data)




# pyplot

st.title("Simple Plotly Chart with Streamlit")

# Sample data
data = {
    "Category": ["A", "B", "C", "D"],
    "Values": [10, 23, 15, 8]
}
df = pd.DataFrame(data)

# Create a Plotly bar chart
fig = px.bar(df, x="Category", y="Values", title="Bar Chart Example")

# Display the chart in Streamlit
st.plotly_chart(fig)