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
    <title>Immersive AR Diwali Greeting</title>
    <script src="https://aframe.io/releases/1.2.0/aframe.min.js"></script>
    <script src="https://raw.githack.com/AR-js-org/AR.js/master/aframe/build/aframe-ar-nft.js"></script>
    <script src="https://raw.githack.com/donmccurdy/aframe-extras/master/dist/aframe-extras.loaders.min.js"></script>
    <style>
      body { margin: 0; overflow: hidden; }
    </style>
  </head>
  <body style="margin: 0px; overflow: hidden;">

    <a-scene
      vr-mode-ui="enabled: false"
      embedded
      arjs="sourceType: webcam; debugUIEnabled: false; detectionMode: mono_and_matrix; matrixCodeType: 3x3;">
      <a-assets>
        <video id="diwaliVideo" autoplay loop="true" crossorigin="anonymous" webkit-playsinline playsinline>
          <source src="https://github.com/Hitanshu-Shah/diwali-ar/raw/main/Happy%20Diwali%20_%20Diwali%20Greeting%20Video%20_%20Diwali%20Wishes%20_%20Deepavali%202021.mp4" type="video/mp4">
        </video>
        <a-asset-item id="candle-model" src="https://raw.githubusercontent.com/Hitanshu-Shah/diwali-ar/main/Candle.glb"></a-asset-item>
      </a-assets>

      <a-entity id="diwaliScene" position="0 0 -3">
        <!-- Video texture on a plane (5% smaller) -->
        <a-plane src="#diwaliVideo" width="3.42" height="2.565" position="0 1.5 0" look-at="[camera]"></a-plane>
        
        <!-- Diwali message in 3D font -->
        <a-entity
          text="value: Happy Diwali and a Prosperous New Year!; 
                font: exo2bold; 
                color: #FFD700; 
                align: center; 
                width: 4; 
                baseline: center"
          position="0 0.5 0"
          scale="1 1 1"
          look-at="[camera]"
        ></a-entity>
        
        <a-entity
          text="value: - Chandresh Shah & The Access Team; 
                font: exo2bold; 
                color: #FFD700; 
                align: center; 
                width: 4; 
                baseline: center"
          position="0 0.2 0"
          scale="0.8 0.8 0.8"
          look-at="[camera]"
        ></a-entity>

        <!-- Candle arrangement in a circle -->
        <a-entity>
          <a-entity gltf-model="#candle-model" position="1 0 0" scale="0.5 0.5 0.5"></a-entity>
          <a-entity gltf-model="#candle-model" position="-1 0 0" scale="0.5 0.5 0.5"></a-entity>
          <a-entity gltf-model="#candle-model" position="0 0 1" scale="0.5 0.5 0.5"></a-entity>
          <a-entity gltf-model="#candle-model" position="0 0 -1" scale="0.5 0.5 0.5"></a-entity>
          <a-entity gltf-model="#candle-model" position="0.7 0 0.7" scale="0.5 0.5 0.5"></a-entity>
          <a-entity gltf-model="#candle-model" position="0.7 0 -0.7" scale="0.5 0.5 0.5"></a-entity>
          <a-entity gltf-model="#candle-model" position="0.7 0 0.7" scale="0.5 0.5 0.5"></a-entity>
          <a-entity gltf-model="#candle-model" position="-0.7 0 -0.7" scale="0.5 0.5 0.5"></a-entity>
        </a-entity>

        <!-- Animated fireworks -->
        <a-entity id="fireworks"></a-entity>
      </a-entity>

      <!-- Camera with look-controls to allow user movement -->
      <a-entity camera look-controls wasd-controls position="0 1.6 0"></a-entity>

    </a-scene>

    <script>
      window.onload = function() {
        const scene = document.querySelector('a-scene');
        const fireworksContainer = document.querySelector('#fireworks');

        function createFirework(x, y, z, color) {
          const firework = document.createElement('a-sphere');
          firework.setAttribute('color', color);
          firework.setAttribute('position', `${x} ${y} ${z}`);
          firework.setAttribute('radius', '0.05');
          
          const animPosition = document.createElement('a-animation');
          animPosition.setAttribute('attribute', 'position');
          animPosition.setAttribute('to', `${x} ${y + 2} ${z}`);
          animPosition.setAttribute('dur', '1500');
          animPosition.setAttribute('easing', 'ease-out');
          
          const animScale = document.createElement('a-animation');
          animScale.setAttribute('attribute', 'scale');
          animScale.setAttribute('to', '2 2 2');
          animScale.setAttribute('dur', '1500');
          
          const animOpacity = document.createElement('a-animation');
          animOpacity.setAttribute('attribute', 'opacity');
          animOpacity.setAttribute('to', '0');
          animOpacity.setAttribute('dur', '1500');
          
          firework.appendChild(animPosition);
          firework.appendChild(animScale);
          firework.appendChild(animOpacity);
          
          fireworksContainer.appendChild(firework);
          
          setTimeout(() => {
            fireworksContainer.removeChild(firework);
          }, 1500);
        }

        function launchFireworks() {
          const colors = ['#ff0000', '#00ff00', '#0000ff', '#ffff00', '#ff00ff'];
          setInterval(() => {
            const x = Math.random() * 4 - 2;
            const z = Math.random() * 4 - 2;
            const color = colors[Math.floor(Math.random() * colors.length)];
            createFirework(x, 0, z, color);
          }, 500);
        }

        scene.addEventListener('loaded', () => {
          launchFireworks();
        });
      };
    </script>
  </body>
</html>
"""

# Display the HTML content in Streamlit
st.components.v1.html(ar_html, height=600, scrolling=False)
