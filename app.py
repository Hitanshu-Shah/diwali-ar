import streamlit as st

# Set up Streamlit page configuration
st.set_page_config(page_title="Diwali AR Greeting", layout="centered")

st.title("Diwali AR Greeting")

st.write("""
         Scan the QR code or click the link below to experience an AR Diwali greeting!
         """)

# Link to the hosted AR file
html_file = open("DiwaliAR.html", 'r', encoding='utf-8').read()

# Embed the HTML file inside the Streamlit app
st.components.v1.html(html_file, height=600, scrolling=True)

# Provide a clickable link to the AR experience if needed
st.markdown(f"[View AR Experience](./ar_greeting.html)")
