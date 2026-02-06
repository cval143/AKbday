import streamlit as st

st.set_page_config(page_title="Bake-a-Cake! 🎂", page_icon="🍰")

# # Stage 0: Initialize Cake Memory
if 'cake_layers' not in st.session_state:
    st.session_state.cake_layers = [] # List to store selected image filenames
if 'page' not in st.session_state:
    st.session_state.page = "intro"

# # Stage 1: Intro
if st.session_state.page == "intro":
    st.title("It's our bestie's birthday! 🎉")
    st.write("We wanted to bake you a cake, but we need your expert help.")
    # Add a cute image of a kitchen or chefs here
    if st.button("Let's Start Baking! 👩‍🍳"):
        st.session_state.page = "build"
        st.rerun()

# # Stage 2: The Bakery
elif st.session_state.page == "build":
    st.title("Custom Cake Studio 🎨")
    
    col_options, col_preview = st.columns([1, 1])

    with col_options:
        st.subheader("Pick your ingredients:")
        
        # Tabs for a clean Purble Place feel
        tab1, tab2, tab3 = st.tabs(["Sponge", "Fillings", "Toppings"])
        
        with tab1:
            st.write("Choose a base:")
            if st.button("Vanilla"): st.session_state.cake_layers.append("vanilla_base.png")
            if st.button("Chocolate"): st.session_state.cake_layers.append("choc_base.png")
            if st.button("Strawberry"): st.session_state.cake_layers.append("pink_base.png")

        with tab2:
            st.write("Add some cream/filling:")
            if st.button("White Frosting"): st.session_state.cake_layers.append("cream.png")
            if st.button("Chocolate Ganache"): st.session_state.cake_layers.append("ganache.png")
            # ... add 2 more here

        with tab3:
            st.write("Final touches:")
            if st.button("Sprinkles"): st.session_state.cake_layers.append("sprinkles.png")
            if st.button("Cherries"): st.session_state.cake_layers.append("cherries.png")
            # ... add 4 more here

        st.write("---")
        if st.button("🗑️ Clear Cake"):
            st.session_state.cake_layers = []
            st.rerun()
            
        if st.button("✅ READY!", use_container_width=True):
            st.session_state.page = "final_reveal"
            st.rerun()

    with col_preview:
        st.subheader("Your Creation:")
        if not st.session_state.cake_layers:
            st.info("Start adding layers to see your cake!")
        else:
            # This loops through and shows all images stacked
            for layer in st.session_state.cake_layers:
                st.image(layer, use_container_width=True)

# # Stage 3: Final Reveal
elif st.session_state.page == "final_reveal":
    st.balloons()
    st.header("IT'S PERFECT! 🎂✨")
    for layer in st.session_state.cake_layers:
        st.image(layer, use_container_width=True)
    st.write("Wait until you see what happens next...")
