import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 1. Title and Description
st.title("My First Streamlit App")
st.write("This is a simple app to demonstrate Streamlit syntax.")

# 2. User Input
name = st.text_input("Enter your name:")
age = st.slider("Select your age", 0, 100, 25)

st.write(f"Hello, {name}! You are {age} years old.")

# 3. Display Data
data = pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar', 'Apr'],
    'Sales': [100, 200, 150, 300]
})

if st.checkbox("Show Sales Data"):
    st.dataframe(data)

# 4. Chart
st.subheader("Sales Chart")
st.line_chart(data['Sales'])

# 5. Matplotlib Example
st.subheader("Sales Bar Chart (Matplotlib)")
fig, ax = plt.subplots()
ax.bar(data['Month'], data['Sales'], color='skyblue')
st.pyplot(fig)

# 6. Selectbox Example
color = st.selectbox("Choose a color", ["Red", "Green", "Blue"])
st.write("You selected:", color)
