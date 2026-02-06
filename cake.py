import streamlit as st

# # Stage 0: Setup
st.set_page_config(page_title="AK's Birthday Bakery 🎂", page_icon="🍰")

# Custom CSS to force images to overlap instead of stack vertically
st.markdown("""
    <style>
    .cake-container {
        position: relative;
        height: 500px;
        width: 100%;
        display: flex;
        justify-content: center;
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
    st.title("Purble Place Studio 🧁")
    
    # --- LIVE PREVIEW SECTION ---
    st.subheader("🎂 Your Creation")
    if not st.session_state.cake_layers:
        st.info("Your cake stand is empty! Pick a base to start.")
    else:
        html_code = '<div class="cake-container">'
        for layer in
