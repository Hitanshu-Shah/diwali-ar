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
      body {
        margin: 0;
        overflow: hidden;
      }
      .arjs-loader {
        height: 100%;
        width: 100%;
        position: absolute;
        top: 0;
        left: 0;
        background-color: rgba(0, 0, 0, 0.8);
        z-index: 9999;
        display: flex;
        justify-content: center;
        align-items: center;
      }
      .arjs-loader div {
        text-align: center;
        font-size: 1.25em;
        color: white;
      }
    </style>
  </head>
  <body style="margin: 0px; overflow: hidden;">
    <div class="arjs-loader">
      <div>Loading, please wait...</div>
    </div>
    <a-scene
      vr-mode-ui="enabled: false"
      embedded
      arjs="sourceType: webcam; debugUIEnabled: false; detectionMode: mono_and_matrix; matrixCodeType: 3x3;">
      <a-assets>
        <img id="access-logo" src="https://raw.githubusercontent.com/Hitanshu-Shah/diwali-ar/main/access-logo.png">
        <a-asset-item id="candle-model" src="https://raw.githubusercontent.com/Hitanshu-Shah/diwali-ar/main/Candle.glb"></a-asset-item>
        <a-asset-item id="rangoli-model" src="https://raw.githubusercontent.com/Hitanshu-Shah/diwali-ar/blob/main/Oriental%20rug.glb"></a-asset-item>
      </a-assets>

      <a-entity id="diwaliScene" position="0 0 -3">
        <!-- Access logo -->
        <a-image src="#access-logo" position="0 1.5 0" scale="1 1 1" look-at="[camera]"></a-image>
        
        <!-- Diwali message -->
        <a-text value="Thank you for being with us!\nHappy Diwali!" position="0 1 0" scale="0.5 0.5 0.5" color="#FFD700" align="center" look-at="[camera]"></a-text>
        
        <!-- Rangoli 3D model on the ground -->
        <a-entity gltf-model="#rangoli-model" position="0 0.01 0" rotation="-90 0 0" scale="2 2 2"></a-entity>

        <!-- Candle arrangement in a circle -->
        <a-entity>
          <a-entity gltf-model="#candle-model" position="1 0 0" scale="0.5 0.5 0.5"></a-entity>
          <a-entity gltf-model="#candle-model" position="-1 0 0" scale="0.5 0.5 0.5"></a-entity>
          <a-entity gltf-model="#candle-model" position="0 0 1" scale="0.5 0.5 0.5"></a-entity>
          <a-entity gltf-model="#candle-model" position="0 0 -1" scale="0.5 0.5 0.5"></a-entity>
          <a-entity gltf-model="#candle-model" position="0.7 0 0.7" scale="0.5 0.5 0.5"></a-entity>
          <a-entity gltf-model="#candle-model" position="0.7 0 -0.7" scale="0.5 0.5 0.5"></a-entity>
          <a-entity gltf-model="#candle-model" position="-0.7 0 0.7" scale="0.5 0.5 0.5"></a-entity>
          <a-entity gltf-model="#candle-model" position="-0.7 0 -0.7" scale="0.5 0.5 0.5"></a-entity>
        </a-entity>

        <!-- Animated fireworks -->
        <a-entity id="fireworks"></a-entity>
      </a-entity>

      <!-- Reactive movement -->
      <a-entity camera look-controls wasd-controls position="0 1.6 0" id="camera">
      </a-entity>
    </a-scene>

    <script>
      window.onload = function() {
        const scene = document.querySelector('a-scene');
        const fireworksContainer = document.querySelector('#fireworks');
        const camera = document.querySelector('#camera');

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

        // Control the camera movement based on device position
        window.addEventListener('deviceorientation', (event) => {
          const alpha = event.alpha;  // rotation around z-axis
          const beta = event.beta;    // tilt front-back
          const gamma = event.gamma;  // tilt left-right
          
          // Adjust camera position based on beta (front-back tilt)
          const distance = Math.max(0, 3 - beta / 90);  // Move closer/further based on beta
          camera.setAttribute('position', `0 ${distance + 1.6} ${-distance}`);
        });

        scene.addEventListener('loaded', () => {
          const loader = document.querySelector('.arjs-loader');
          loader.style.display = 'none';
          launchFireworks();
        });
      };
    </script>
  </body>
</html>
"""

# Display the HTML content in Streamlit
st.components.v1.html(ar_html, height=600, scrolling=False)
