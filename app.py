import streamlit as st

# Set up Streamlit page configuration
st.set_page_config(page_title="Diwali AR Greeting", layout="centered")

st.title("Diwali AR Greeting")

st.write("""
         Scan the QR code or click the link below to experience an AR Diwali greeting!
         """)

# Provide a clickable link to the hosted AR experience (this opens directly to the AR page)
ar_url = "https://your-github-username.github.io/your-repo-name/ar_greeting.html"
st.markdown(f"[Click here to view the AR greeting]({ar_url})")

# # Optionally, show an image of the QR code
# qr_code_image = "qr_code.png"  # If you generated a QR code image, ensure it's in the folder
# st.image(qr_code_image, caption='Scan to view the AR greeting!')
