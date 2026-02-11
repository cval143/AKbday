import streamlit as st
import random
import time

# # Stage 0: Setup
st.set_page_config(page_title="AK's Birthday Bakery 🎂", page_icon="🍰")

# RESPONSIVE CSS + Satirical Styling
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
    st.image("https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExaGRmNXIyNmQ5bTQzOHdheTk1M2w0aHRtZXdnemkzaDZyMjZqajZrdSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/n3KZaXLYLuyNSHEvbm/giphy.gif")
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
            st.session_state.page = "final"
            st.rerun()

    tabs = st.tabs(["Sponges", "Frosting"])
    
    with tabs[0]:
        st.markdown("<p class='tiny-text'>*Please click twice to select</p>", unsafe_allow_html=True)
        cols = st.columns(3)
        if cols[0].button("Vanilla"): st.session_state.cake_layers.append("vanilla_base.png")
        if cols[1].button("Chocolate"): st.session_state.cake_layers.append("chocolate_base.png")
        if cols[2].button("Strawberry"): st.session_state.cake_layers.append("strawberry_base.png")
        if cols[0].button("Red Velvet"): st.session_state.cake_layers.append("redvelvet_base.png")
        if cols[1].button("Butterscotch"): st.session_state.cake_layers.append("butterscotch_base.png")
        if cols[2].button("Karela🤤"): st.session_state.cake_layers.append("karela_base.png")
        
    with tabs[1]:
        st.markdown("<p class='tiny-text'>*Please click twice to select</p>", unsafe_allow_html=True)
        dcols = st.columns(3)
        if dcols[0].button("Vanilla"): st.session_state.cake_layers.append("vanilla_drip.png")
        if dcols[1].button("Chocolate"): st.session_state.cake_layers.append("chocolate_drip.png")
        if dcols[2].button("Strawberry"): st.session_state.cake_layers.append("strawberry_drip.png")
        if dcols[0].button("Blueberry"): st.session_state.cake_layers.append("blueberry_drip.png")
        if dcols[1].button("Mango"): st.session_state.cake_layers.append("mango_drip.png")

    st.subheader("🎂 Your Creation")
    if not st.session_state.cake_layers:
        st.info("Cake stand empty!")
    else:
        html_code = '<div class="cake-container">'
        for layer in st.session_state.cake_layers:
            html_code += f'<img src="https://raw.githubusercontent.com/cval143/AKbday/main/{layer}" class="cake-layer">'
        html_code += '</div>'
        st.markdown(html_code, unsafe_allow_html=True)

# # Stage 3: Satirical Final Page
elif st.session_state.page == "final":
    st.title("Beautiful! Just like the Birthday Girl🌚")
    age = st.number_input("Enter your age:", min_value=1, max_value=100, step=1, value=1)
    
    html_code = '<div class="cake-container">'
    for layer in st.session_state.cake_layers:
        html_code += f'<img src="https://raw.githubusercontent.com/cval143/AKbday/main/{layer}" class="cake-layer">'
    
    random.seed(42) 
    for _ in range(age):
        left_pos = random.randint(35, 62) 
        top_pos = random.randint(35, 50)
        candle_class = "css-candle blown-out" if st.session_state.blown else "css-candle"
        flame_html = '<div class="flame"></div>' if not st.session_state.blown else ''
        html_code += f'<div class="{candle_class}" style="left: {left_pos}%; top: {top_pos}%;">{flame_html}</div>'
    
    html_code += '</div>'
    st.markdown(html_code, unsafe_allow_html=True)

    st.write("---")
    wish = st.text_input("Don't forget to make a wish before you blow the Candles! (It stays a secret🤫):")
    
    if not st.session_state.blown:
        if st.button("Click to Blow the candles", use_container_width=True):
            st.session_state.blown = True
            st.balloons() 
            time.sleep(1)
            st.rerun()
    else:
        st.success("Tathastu, Girl!😙💖")
        if st.button("🎀click here🎀", type="primary", use_container_width=True):
            st.session_state.page = "surprise"
            st.rerun()

# # Stage 4: Surprise Reveal
elif st.session_state.page == "surprise":
    st.title("We have something for you... 🤓")
    st.image("https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExbzE1YmwycTVwazBocm5udDZidzdybGloN2VvMG9pYmlrcTl0cGhodiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/WRL7YgP42OKns22wRD/giphy.gif")
    
    st.write("---")
    drive_link = "https://drive.google.com/file/d/1YCfcnWZX3a-xk3YPrnvEFldXzXBcjc7p/view?usp=sharing"
    st.markdown(f'<a href="{drive_link}" target="_blank" class="gift-button">The one where we surprise you 📽️</a>', unsafe_allow_html=True)
    
    st.write("")
    if st.button("Bake another cake? 🔄", use_container_width=True):
        st.session_state.cake_layers = []
        st.session_state.blown = False
        st.session_state.page = "intro"
        st.rerun()
