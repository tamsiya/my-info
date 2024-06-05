import streamlit as st

# Set the title of the app
st.title("Simple Streamlit App")

# Create a text input box for the user to enter their name
name = st.text_input("Enter your name:")

# Create a button that, when clicked, displays the user's input
if st.button("Submit"):
    st.write(f"Hello, {name}!")
    st.text ("this is the simple script to how create streamlit app in python ")