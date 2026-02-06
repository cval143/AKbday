import streamlit as st

# # Stage 0: Setup
st.set_page_config(page_title="AK's Birthday Bakery 🎂", page_icon="🍰")

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
    
    col_opts, col_preview = st.columns([1, 1])

    with col_opts:
        st.write("### 🥣 Ingredients")
        tabs = st.tabs(["Sponges", "Frosting Drips", "Toppings"])
        
        with tabs[0]:
            st.write("Choose your bases:")
            # Matching your uploaded filenames
            if st.button("Vanilla"): st.session_state.cake_layers.append("vanilla_base.png")
            if st.button("Chocolate"): st.session_state.cake_layers.append("chocolate_base.png")
            if st.button("Strawberry"): st.session_state.cake_layers.append("strawberry_base.png")
            if st.button("Red Velvet"): st.session_state.cake_layers.append("redvelvet_base.png")
            if st.button("Butterscotch"): st.session_state.cake_layers.append("butterscotch_base.png")
            if st.button("Karela (Prank!) 🥒"): st.session_state.cake_layers.append("karela_base.png")
            
        with tabs[1]:
            st.write("Add some drips:")
            if st.button("Vanilla Drip"): st.session_state.cake_layers.append("vanilla_drip.png")
            if st.button("Chocolate Drip"): st.session_state.cake_layers.append("chocolate_drip.png")
            if st.button("Strawberry Drip"): st.session_state.cake
