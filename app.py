import streamlit as st

# Set up Streamlit page configuration
st.set_page_config(page_title="Diwali AR Greeting", layout="centered")

st.title("Diwali AR Greeting")

st.write("""
 Please allow camera Access to see this greeting in Augmented Reality
 """)

# Embed the updated markerless AR HTML directly into the Streamlit app
ar_html = """
<!DOCTYPE html>
<html>
  <head>
    <title>AR Diwali Greeting (Markerless)</title>
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
    <!-- AR.js Scene without markers -->
    <a-scene embedded arjs="sourceType: webcam; debugUIEnabled: false;" vr-mode-ui="enabled: false">
      
      <!-- Place AR objects in front of the camera at a specific distance -->
      <a-entity position="0 1 -4" rotation="0 180 0" scale="1 1 1">
        <!-- Add the Access logo floating in space -->
        <a-image src="https://raw.githubusercontent.com/Hitanshu-Shah/diwali-ar/main/access-logo.png" position="0 1 0" scale="1.5 1.5 1.5"></a-image>

        <!-- Thank You Message positioned above the logo -->
        <a-text value="Thank you for being with us! Happy Diwali!" position="0 2 0" scale="3 3 3" color="#FFD700"></a-text>

        <!-- Add a rotating box for better 3D depth perception -->
        <a-box color="orange" position="0 -1 0" scale="0.5 0.5 0.5" rotation="0 45 0" animation="property: rotation; to: 0 360 0; loop: true; dur: 3000"></a-box>
      </a-entity>

      <!-- AR.js Camera for the webcam feed -->
      <a-entity camera look-controls></a-entity>

    </a-scene>
  </body>
</html>
"""

# Display the HTML content in Streamlit
st.components.v1.html(ar_html, height=600, scrolling=False)
