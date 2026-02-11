import streamlit as st
import random
import time

# Stage 0: Setup
# Fixed Line 9: Added standard quotes and ensured no invisible characters
st.set_page_config(page_title="AK's Birthday Bakery 🎂", page_icon="🍰")

# RESPONSIVE CSS + New Satirical Styling
# Fixed Line 14: Used triple quotes (""") to properly wrap the multi-line CSS block
st.markdown("""
    <style>
    .cake-container {
        position: relative;
        width: 100%;
        max-width: 400px;
        aspect-ratio: 1 / 1;
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
        object-fit: contain;
    }
    .css-candle {
        position: absolute;
        width: 2.5%;
        height: 12%;
        background: linear-gradient(to bottom, #ffee58, #fbc02d);
        border-radius: 2px;
        z-index: 100;
        transition: opacity 1.2s ease-out;
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
        box-shadow: 0 0 10px #ff9800;
        animation: flicker 0.1s infinite alternate;
    }
    .blown-out {
        opacity: 0;
    }
    @keyframes flicker {
        from { transform: translateX(-50%) scale(1); }
        to { transform: translateX(-50%) scale(1.1) rotate(1deg); }
    }
    .tiny-text {
        font-size: 10px;
        color: #888;
        margin-top: -10px;
        margin-bottom: 10px;
    }
    .gift-button {
        display: inline-block;
        padding: 0.6em 1.2em;
        color: white;
        background-color: #ff4b4b;
        border-radius: 10px;
        text-decoration: none;
        font-weight: bold;
        text-align: center;
        width: 100%;
        border: 2px solid #ff4b4b;
    }
    </style>
""", unsafe_allow_html=True)

if 'cake_layers' not in st.session_state:
    st.session_state.cake_layers = []
if 'page' not in st.session_state:
    st.session_state.page = "intro"
if 'blown' not in st.session_state:
    st.session_state.blown = False

# # Stage 1: Intro
if st.session_state.page == "intro":
    st.title("It's our bestie's birthday! 🎉")
    st.image("https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExaGRmNXIyNmQ5TQzOHdheTk1M2w0aHRtZXdnemkzaDZyMjZqajZrdSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/n3KZaXLYLuyNSHEvbm/giphy.gif")
    if st.button("Let's Bake a Cake! 👩‍🍳", use_container_width=True):
        st.session_state.page = "build"
        st.rerun()

# # Stage 2: The Bakery
elif st.session_state.page == "build":
    st.title("Akshata's Cake Studio 🧁")
    
    st.write("### 🥣 Ingredients")
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("⏪ Undo", use_container_width=True):
            if st.session_state.cake_layers:
                st.session_state.cake_layers.pop()
                st.rerun()
    with col2:
        if st.button("🗑️ Reset", use_container_width=True):
            st.session_state.cake_layers = []
            st.rerun()
    with col3:
        if st.button("Next ➡️", type="primary", use_container_width=True):
            # Added Confetti burst here as requested
            st.balloons() 
            st.session_state.page = "final"
            time.sleep(1)
            st.rerun()

    tabs = st.tabs(["Sponges", "Frosting Drips"])
    
    with tabs[0]:
        st.markdown("<p class='tiny-text'>*Please click twice to select</p>", unsafe_allow_html=True)
        cols = st.columns(3)
        if cols[0].button("Vanilla"): st.session_state.cake_layers.append("vanilla_base.png")
        if cols[1].button("Chocolate"): st.session_state.cake_layers.append("chocolate_base.png")
