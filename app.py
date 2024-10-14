import streamlit as st

# Set up Streamlit page configuration
st.set_page_config(page_title="Diwali AR Greeting", layout="centered")

st.title("Diwali AR Greeting")

st.write("""
         Scan the QR code or click the link below to experience an AR Diwali greeting!
         """)

# Embed the AR HTML directly into the Streamlit app
ar_html = """
<!DOCTYPE html>
<html>
  <head>
    <title>AR Diwali Greeting</title>
    <script src="https://aframe.io/releases/1.2.0/aframe.min.js"></script>
    <script src="https://cdn.jsdelivr.net/gh/AR-js-org/AR.js/aframe/build/aframe-ar.min.js"></script>
    <style>
      body, html {
        margin: 0;
        overflow: hidden;
        width: 100%;
        height: 100%;
      }
    </style>
  </head>
  
  <body>
    <!-- AR.js Scene -->
    <a-scene embedded arjs='sourceType: webcam; debugUIEnabled: false;'>
      
      <!-- This will detect the specific image (Access-branded frame) -->
      <a-marker type="pattern" url="https://raw.githubusercontent.com/Hitanshu-Shah/diwali-ar/main/access-marker.patt">
        
        <!-- Add the Access logo -->
        <a-image src="https://raw.githubusercontent.com/Hitanshu-Shah/diwali-ar/main/access-logo.png" position="0 0.5 0" scale="1 1 1"></a-image>

        <!-- Thank You Message -->
        <a-text value="Thank you for being with us! Happy Diwali!" position="0 1.5 0" scale="2 2 2" color="#FFD700"></a-text>

        <!-- Optionally, you can add 3D models like a diya here or animations -->
        <a-box color="orange" position="0 0.5 0" scale="0.5 0.5 0.5"></a-box>
      
      </a-marker>
      
      <!-- AR.js Camera -->
      <a-entity camera></a-entity>
      
    </a-scene>
  </body>
</html>
"""

# Display the HTML content in Streamlit
st.components.v1.html(ar_html, height=600, scrolling=False)
