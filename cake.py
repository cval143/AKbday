import streamlit as st
import random

# # Stage 0: Setup
st.set_page_config(page_title="AK's Birthday Bakery 🎂", page_icon="🍰")

# RESPONSIVE CSS
st.markdown("""
    <style>
    .cake-container {
        position: relative;
        width: 100%;
        max-width: 500px; /* Limits size on laptop */
        aspect-ratio: 1 / 1; /* Keeps it a perfect square on all devices */
        margin: auto;
        background-color: #1a1a1a;
        border-radius: 15px;
        overflow: hidden;
    }
    .cake-layer {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        object-fit: contain; /* Ensures layers don't stretch weirdly */
    }
    .css-candle {
        position: absolute;
        width: 2%; /* Scale width relative to container */
        height: 10%; /* Scale height relative to container */
        background: linear-gradient(to bottom, #ffee58, #fbc02d);
        border-radius: 2px;
        z-index: 100;
    }
    .flame {
        position: absolute;
        top: -40%;
        left: 50%;
        transform: translateX(-50%);
        width: 150%;
        height: 50%;
        background: radial-gradient(circle, #ffeb3b, #ff9800, #f44336);
        border-radius: 50% 50% 20% 20%;
        box-shadow: 0 0 8px #ff9800;
        animation: flicker 0.1s infinite alternate;
    }
    @keyframes flicker {
        from { transform: translateX(-50%) scale(1); }
        to { transform: translateX(-50%) scale(1.1) rotate(2deg); }
    }
    </style>
""", unsafe_allow_html=True)

# ... (Keep your existing session_state and Page 1/2 logic exactly as is)

# # Stage 3: Updated Final Page for Mobile
elif st.session_state.page == "final":
    st.header("MAKE A WISH! 🎂✨")
    
    age = st.number_input("Enter your age:", min_value=1, max_value=100, step=1, value=1)

    html_code = '<div class="cake-container">'
    # Draw Cake
    for layer in st.session_state.cake_layers:
        html_code += f'<img src="https://raw.githubusercontent.com/cval143/AKbday/main/{layer}" class="cake-layer">'
    
    # Draw CSS Candles with Mobile-Safe Coordinates
    if not st.session_state.blown:
        random.seed(42) 
        for _ in range(age):
            # We narrow the range (40-60 instead of 30-70) so they stay on top 
            # of the frosting even on narrow phone screens.
            left_pos = random.randint(35, 62) 
            top_pos = random.randint(35, 50)
            html_code += f'<div class="css-candle" style="left: {left_pos}%; top: {top_pos}%;"><div class="flame"></div></div>'
    
    html_code += '</div>'
    st.markdown(html_code, unsafe_allow_html=True)

    st.write("---")
    if not st.session_state.blown:
        if st.button("💨 BLOW OUT THE CANDLES", use_container_width=True):
            st.session_state.blown = True
            st.rerun()
    else:
        st.balloons()
        st.success(f"🎂 HAPPY {age}th BIRTHDAY, AKSHATA! 🎂")
        if st.button("Bake another?"):
            st.session_state.cake_layers = []
            st.session_state.page = "intro"
            st.session_state.blown = False
            st.rerun()
