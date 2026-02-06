import streamlit as st
import random

# # Stage 0: Initial App Configuration
st.set_page_config(page_title="Akshata's Birthday Bakery 🎂", page_icon="🍰")

# Custom CSS for the "Purble Place" Layering & Random Candle Placement
st.markdown("""
    <style>
    .cake-container {
        position: relative;
        height: 450px;
        width: 100%;
        display: flex;
        justify-content: center;
        background-color: #1e1e1e; /* Dark theme to make the cake pop */
        border-radius: 15px;
        overflow: hidden;
    }
    .cake-layer {
        position: absolute;
        bottom: 50px;
        width: 90%;
        max-width: 450px;
    }
    .candle {
        position: absolute;
        width: 25px; /* Size of the candle */
        z-index: 100;
        transition: opacity 0.8s ease;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize memory for the cake layers and the app stage
if 'cake_layers' not in st.session_state:
    st.session_state.cake_layers = []
if 'page' not in st.session_state:
    st.session_state.page = "intro"
if 'candles_blown' not in st.session_state:
    st.session_state.candles_blown = False

# # Stage 1: The Intro Page
if st.session_state.page == "intro":
    st.title("It's our bestie's birthday! 🎉")
    st.image("https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExaGRmNXIyNmQ5bTQzOHdheTk1M2w0aHRtZXdnemkzaDZyMjZqajZrdSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/n3KZaXLYLuyNSHEvbm/giphy.gif")
    if st.button("Let's Bake a Cake! 👩‍🍳", use_container_width=True):
        st.session_state.page = "build"
        st.rerun()

# # Stage 2: The Custom Cake Studio
elif st.session_state.page == "build":
    st.title("Akshata's Cake Studio 🧁")
    
    # Live Preview (Visualizing the cake formation in real-time)
    st.subheader("🎂 Your Creation")
    if not st.session_state.cake_layers:
        st.info("Your cake stand is empty! Pick a base to start.")
    else:
        # Layering logic: Sponges and Drips get stacked via CSS
        html_code = '<div class="cake-container">'
        for layer in st.session_state.cake_layers:
            html_code += f'<img src="https://raw.githubusercontent.com/cval143/AKbday/main/{layer}" class="cake-layer">'
        html_code += '</div>'
        st.markdown(html_code, unsafe_allow_html=True)
    
    st.write("---")
    st.write("### 🥣 Ingredients")
    tabs = st.tabs(["Sponges", "Frosting Drips"])
    
    with tabs[0]:
        st.write("Choose your bases (you can stack them!):")
        cols = st.columns(3)
        if cols[0].button("Vanilla"): st.session_state.cake_layers.append("vanilla_base.png")
        if cols[1].button("Chocolate"): st.session_state.cake_layers.append("chocolate_base.png")
        if cols[2].button("Strawberry"): st.session_state.cake_layers.append("strawberry_base.png")
        if cols[0].button("Red Velvet"): st.session_state.cake_layers.append("redvelvet_base.png")
        if cols[1].button("Butterscotch"): st.session_state.cake_layers.append("butterscotch_base.png")
        if cols[2].button("Karela 🥒"): st.session_state.cake_layers.append("karela_base.png")
        
    with tabs[1]:
        st.write("Add your drips:")
        dcols = st.columns(3)
        if dcols[0].button("Vanilla Drip"): st.session_state.cake_layers.append("vanilla_drip.png")
        if dcols[1].button("Chocolate Drip"): st.session_state.cake_layers.append("chocolate_drip.png")
        if dcols[2].button("Strawberry Drip"): st.session_state.cake_layers.append("strawberry_drip.png")
        if dcols[0].button("Blueberry Drip"): st.session_state.cake_layers.append("blueberry_drip.png")
        if dcols[1].button("Mango Drip"): st.session_state.cake_layers.append("mango_drip.png")

    st.write("---")
    # Control Panel
    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button("⏪ Undo", use_container_width=True):
            if st.session_state.cake_layers:
                st.session_state.cake_layers.pop()
                st.rerun()
    with c2:
        if st.button("🗑️ Start Over", use_container_width=True):
            st.session_state.cake_layers = []
            st.rerun()
    with c3:
        if st.button("✅ READY!", type="primary", use_container_width=True):
            st.session_state.page = "final"
            st.rerun()

# # Stage 3: The Birthday Reveal & Candle Blowing
elif st.session_state.page == "final":
    st.header("MAKE A WISH! 🎂✨")
    
    # 1. Interactive Age Input
    age = st.number_input("Enter your age to light the candles:", min_value=1, max_value=100, step=1, value=1)

    # 2. The Interactive Cake Container
    html_code = '<div class="cake-container">'
    
    # Draw Cake Bases
    for layer in st.session_state.cake_layers:
        html_code += f'<img src="https://raw.githubusercontent.com/cval143/AKbday/main/{layer}" class="cake-layer">'
    
    # Draw Candles (Scattered randomly across the cake surface if they aren't blown out)
    if not st.session_state.candles_blown:
        # Use a fixed seed so the candles don't move every time she types her age
        random.seed(42) 
        for i in range(age):
            left_pos = random.randint(25, 65) # Horizontal spread
            top_pos = random.randint(35, 55)  # Vertical spread on top of cake
            html_code += f'<img src="https://raw.githubusercontent.com/cval143/AKbday/main/candles.png" class="candle" style="left: {left_pos}%; top: {top_pos}%;">'
    
    html_code += '</div>'
    st.markdown(html_code, unsafe_allow_html=True)

    st.write("---")
    
    # 3. The Blowing Mechanic
    if not st.session_state.candles_blown:
        st.subheader("Now, blow them out! 🌬️")
        if st.button("💨 BLOW OUT THE CANDLES", use_container_width=True):
            st.session_state.candles_blown = True
            st.rerun()
    else:
        st.balloons()
        st.success("🎂 HAPPY BIRTHDAY, AKSHATA! 🎂")
        st.markdown("### All your wishes are coming true! ✨")
        if st.button("Start Over? 🔄"):
            st.session_state.cake_layers = []
            st.session_state.page = "intro"
            st.session_state.candles_blown = False
            st.rerun()
