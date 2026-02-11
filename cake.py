import streamlit as st
import random
import time

# # Stage 0: Setup
st.set_page_config(page_title="AK's Birthday Bakery 🎂", page_icon="🍰")

# RESPONSIVE CSS + New Satirical Styling
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
