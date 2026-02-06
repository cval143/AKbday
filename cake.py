import streamlit as st

# # Stage 0: Setup
st.set_page_config(page_title="AK's Birthday Bakery 🎂", page_icon="🍰")

# Refined CSS for infinite stacking
st.markdown("""
    <style>
    .cake-container {
        position: relative;
        height: 450px; /* Base height for the cake stand */
        width: 100%;
        display: flex;
        justify-content: center;
        margin-bottom: 20px;
    }
    .cake-layer {
        position: absolute;
        bottom: 10px; /* Changed to bottom alignment for better stacking look */
        width: 100%;
        max-width: 400px;
        transition: all 0.3s ease; /* Adds a smooth appearance effect */
    }
    </style>
""", unsafe_allow_html=True)

if 'cake_layers' not in st.session_state:
    st.session_state.cake_layers = []
if 'page' not in st.session_state:
    st.session_state.page = "intro"

# # Stage 1: Intro
if st.session_state.page == "intro":
    st.title("It's our bestie's birthday! 🎉")
    st.image("https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExaGRmNXIyNmQ5bTQzOHdheTk1M2w0aHRtZXdnemkzaDZyMjZqajZrdSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/n3KZaXLYLuyNSHEvbm/giphy.gif")
    if st.button("Let's Bake a Cake! 👩‍🍳", use_container_width=True):
        st.session_state.page = "build"
        st.rerun()

# # Stage 2: The Bakery
elif st.session_state.page == "build":
    st.title("Purble Place Studio 🧁")
    
    # --- LIVE PREVIEW ---
    st.subheader("🎂 Your Creation")
    if not st.session_state.cake_layers:
        st.info("The cake stand is waiting for its first layer!")
    else:
        html_code = '<div class="cake-container">'
        for layer in st.session_state.cake_layers:
            # Pulls images directly from your AKbday main branch
            html_code += f'<img src="https://raw.githubusercontent.com/cval143/AKbday/main/{layer}" class="cake-layer">'
        html_code += '</div>'
        st.markdown(html_code, unsafe_allow_html=True)
    
    st.write("---")

    # --- INGREDIENTS ---
    tabs = st.tabs(["Sponges", "Frosting Drips", "Toppings"])
    
    with tabs[0]:
        st.write("Click to add a layer (you can stack as many as you want!):")
        cols = st.columns(3)
        if cols[0].button("Vanilla"): st.session_state.cake_layers.append("vanilla_base.png")
        if cols[1].button("Chocolate"): st.session_state.cake_layers.append("chocolate_base.png")
        if cols[2].button("Strawberry"): st.session_state.cake_layers.append("strawberry_base.png")
        if cols[0].button("Red Velvet"): st.session_state.cake_layers.append("redvelvet_base.png")
        if cols[1].button("Butterscotch"): st.session_state.cake_layers.append("butterscotch_base.png")
        if cols[2].button("Karela 🥒"): st.session_state.cake_layers.append("karela_base.png")
        
    with tabs[1]:
        st.write("Add some drips on top of the current layer:")
        dcols = st.columns(3)
        if dcols[0].button("Vanilla Drip"): st.session_state.cake_layers.append("vanilla_drip.png")
        if dcols[1].button("Chocolate Drip"): st.session_state.cake_layers.append("chocolate_drip.png")
        if dcols[2].button("Strawberry Drip"): st.session_state.cake_layers.append("strawberry_drip.png")
        if dcols[0].button("Blueberry Drip"): st.session_state.cake_layers.append("blueberry_drip.png")
        if dcols[1].button("Mango Drip"): st.session_state.cake_layers.append("mango_drip.png")

    with tabs[2]:
        st.write("Final toppings:")
        if st.button("Sprinkles"): st.session_state.cake_layers.append("sprinkles.png")
        if st.button("Candles"): st.session_state.cake_layers.append("candles.png")

    st.write("---")
    
    # --- CONTROLS ---
    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button("⏪ Undo Layer", use_container_width=True):
            if st.session_state.cake_layers:
                st.session_state.cake_layers.pop() # Removes the very last item added
                st.rerun()
    with c2:
        if st.button("🗑️ Start Over", use_container_width=True):
            st.session_state.cake_layers = []
            st.rerun()
    with c3:
        if st.button("✅ READY!", type="primary", use_container_width=True):
            st.session_state.page = "final"
            st.rerun()

# # Stage 3: Final Page
elif st.session_state.page == "final":
    st.balloons()
    st.header("IT'S GORGEOUS! 🎂✨")
    
    html_code = '<div class="cake-container">'
    for layer in st.session_state.cake_layers:
        html_code += f'<img src="https://raw.githubusercontent.com/cval143/AKbday/main/{layer}" class="cake-layer">'
    html_code += '</div>'
    st.markdown(html_code, unsafe_allow_html=True)
    
    st.write("Take a screenshot of your masterpiece!")
    if st.button("Make Another? 🔄"):
        st.session_state.cake_layers = []
        st.session_state.page = "intro"
        st.rerun()
