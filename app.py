import streamlit as st

# Set up Streamlit page configuration
st.set_page_config(page_title="Diwali AR Greeting", layout="centered")

st.title("Diwali AR Greeting")

st.write("""
         Scan the QR code or click the link below to experience an AR Diwali greeting!
         """)

# Link to the hosted AR file
html_file = open("ar_greeting.html", 'r', encoding='utf-8').read()

# Embed the HTML file inside the Streamlit app
st.components.v1.html(html_file, height=600, scrolling=True)

# Optionally, if you want to show an image of the QR code, include that here
st.write("Use your camera to scan this QR code:")
qr_code_image = "qr_code.png"  # If you generated a QR code image, place it in the folder
st.image(qr_code_image, caption='Scan to view the AR greeting!')

# Provide a clickable link to the AR experience if needed
st.markdown(f"[View AR Experience](./ar_greeting.html)")
