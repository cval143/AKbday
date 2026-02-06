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
        max-width: 500px;
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
        width: 2%;
        height: 10%;
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

if 'cake_layers' not in st.session_state:
    st.session_state.cake_layers = []
if 'page' not in st.session_state:
    st.session_state.page = "intro"
if 'blown' not in st.session_state:
    st.session_state.blown = False

# # Stage 1: Intro
if st.session_state.page == "intro":
    st.title("It's our bestie's birthday! 🎉")
    st.image("https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExaGRmNXIyNmQ5bTQzOHdheTk1M2w0aHRtZXdnemkzaDZyMjZqajZrdSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/n3KZaXLYLuyNSHEvbm/giphy.gif")
    if st.button("Let's Bake a Cake! 👩‍🍳", use_container_width=True):
        st.session_state.page = "build"
        st.rerun()

# # Stage 2: The Bakery
elif st.session_state.page == "build":
    st.title("Akshata's Cake Studio 🧁")
    
    st.subheader("🎂 Your Creation")
    if not st.session_state.cake_layers:
        st.info("Your cake stand is empty! Pick a base to start.")
    else:
        html_code = '<div class="cake-container">'
        for layer in st.session_state.cake_layers:
            html_code += f'<img src="https://raw.githubusercontent.com/cval143/AKbday/main/{layer}" class="cake-layer">'
        html_code += '</div>'
        st.markdown(html_code, unsafe_allow_html=True)
    
    st.write("---")
    tabs = st.tabs(["Sponges", "Frosting Drips"])
    
    with tabs[0]:
        st.write("Choose your bases:")
        cols = st.columns(3)
        if cols[0].button("Vanilla"): st.session_state.cake_layers.append("vanilla_base.png")
        if cols[1].button("Chocolate"): st.session_state.cake_layers.append("chocolate_base.png")
        if cols[2].button("Strawberry"): st.session_state.cake_layers.append("strawberry_base.png")
        if cols[0].button("Red Velvet"): st.session_state.cake_layers.append("redvelvet_base.png")
        if cols[1].button("Butterscotch"): st.session_state.cake_layers.append("butterscotch_base.png")
        if cols[2].button("Karela 🥒"): st.session_state.cake_layers.append("karela_base.png")
        
    with tabs[1]:
        st.write("Add some drips:")
        dcols = st.columns(3)
        if dcols[0].button("Vanilla Drip"): st.session_state.cake_layers.append("vanilla_drip.png")
        if dcols[1].button("Chocolate Drip"): st.session_state.cake_layers.append("chocolate_drip.png")
        if dcols[2].button("Strawberry Drip"): st.session_state.cake_layers.append("strawberry_drip.png")
        if dcols[0].button("Blueberry Drip"): st.session_state.cake_layers.append("blueberry_drip.png")
        if dcols[1].button("Mango Drip"): st.session_state.cake_layers.append("mango_drip.png")

    st.write("---")
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("⏪ Undo", use_container_width=True):
            if st.session_state.cake_layers:
                st.session_state.cake_layers.pop()
                st.rerun()
    with col2:
        if st.button("🗑️ Start Over", use_container_width=True):
            st.session_state.cake_layers = []
            st.rerun()
    with col3:
        if st.button("✅ READY!", type="primary", use_container_width=True):
            st.session_state.page = "final"
            st.rerun()

# # Stage 3: Final Page
elif st.session_state.page == "final":
    st.header("MAKE A WISH! 🎂✨")
    age = st.number_input("Enter your age:", min_value=1, max_value=100, step=1, value=1)
    
    html_code = '<div class="cake-container">'
    for layer in st.session_state.cake_layers:
        html_code += f'<img src="https://raw.githubusercontent.com/cval143/AKbday/main/{layer}" class="cake-layer">'
    
    if not st.session_state.blown:
        random.seed(42) 
        for _ in range(age):
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
