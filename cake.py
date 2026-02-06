import streamlit as st

# # Stage 0: Setup
st.set_page_config(page_title="AK's Birthday Bakery 🎂", page_icon="🍰")

# Custom CSS for overlapping layers
st.markdown("""
    <style>
    .cake-container {
        position: relative;
        height: 500px;
        width: 100%;
        display: flex;
        justify-content: center;
        overflow: hidden;
    }
    .cake-layer {
        position: absolute;
        top: 0;
        width: 100%;
        max-width: 500px;
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
    st.title("Akshata's Cake Studio 🧁")
    
    # --- LIVE PREVIEW SECTION ---
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

    st.write("### 🥣 Ingredients")
    # Now only two tabs for a faster, cleaner experience
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
    st.balloons()
    st.header("IT'S GORGEOUS! 🎂✨")
    
    # 1. Ask for her age
    age = st.number_input("How many candles should we light? (Enter your age 🎂)", 
                          min_value=0, max_value=100, value=0)

    # 2. Display the cake with dynamic candles
    html_code = '<div class="cake-container">'
    
    # First, draw the cake layers she built
    for layer in st.session_state.cake_layers:
        html_code += f'<img src="https://raw.githubusercontent.com/cval143/AKbday/main/{layer}" class="cake-layer">'
    
    # Second, add the number of candles she requested
    # We use a loop to add the candle image multiple times
    for _ in range(age):
        html_code += f'<img src="https://raw.githubusercontent.com/cval143/AKbday/main/candles.png" class="cake-layer">'
        
    html_code += '</div>'
    st.markdown(html_code, unsafe_allow_html=True)
    
    st.write("---")
    if age > 0:
        st.subheader(f"Happy {age}th Birthday, Akshata! 🎉")
    
    if st.button("Bake another?"):
        st.session_state.cake_layers = []
        st.session_state.page = "intro"
        st.rerun()
