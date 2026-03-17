import streamlit as st
import base64
import os

st.title("Ship Map Analysis")
st.caption("hover over the decks")

def get_image_as_base64(file_path):
    if not os.path.exists(file_path):
        return "" 
    with open(file_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

top_deck_b64 = get_image_as_base64("titanic_ship_map/Top_deck_Titanic.png")
a_deck_b64 = get_image_as_base64("titanic_ship_map/A_deck_Titanic.png")
b_deck_b64 = get_image_as_base64("titanic_ship_map/b_deck_Titanic.png")
c_deck_b64 = get_image_as_base64("titanic_ship_map/c_deck_Titanic.png")
d_deck_b64 = get_image_as_base64("titanic_ship_map/d_deck_Titanic.png")
e_deck_b64 = get_image_as_base64("titanic_ship_map/e_deck_Titanic.png")
f_deck_b64 = get_image_as_base64("titanic_ship_map/f_deck_Titanic.png")
g_deck_b64 = get_image_as_base64("titanic_ship_map/g_deck_Titanic.png")
bottom_deck_b64 = get_image_as_base64("titanic_ship_map/bottom_deck_Titanic.png")
dialog_bg_b64 = get_image_as_base64("dialog_box.png")

st.html(f"""
<style>

    body .hover_able{{
        transition: transform 0.2s ease;
        padding: 0px;
        margin: 0px;
    }}

    .deck_container {{
        position: relative;
        width: 600px;
        border: 1px solid #ccc; /* Temporary border to see the box */
        margin-bottom: 2px;
    }}
    .dialog-box {{
        height: 220px;
        width: 250px;
        color:black;
        background-image: url("data:image/png;base64,{dialog_bg_b64}");
        background-color: #f0f0f0; /* Fallback color */
        background-size: cover;
        position: absolute;
        top: -150px;
        right: -230px;
        z-index: 999;
        opacity: 0;
        visibility: hidden;
        transition: opacity 0.3s;
        padding:0px 0px 0px 10px;
    }}
    .deck_container:hover .dialog-box {{
        opacity: 1;
        visibility: visible;
    }}
    .hover_able:hover {{
    opacity: 0.6;
    transform: scale(1.2);
    }}
</style>
<body>
<img src="data:image/png;base64,{top_deck_b64}" width="600px">
    
    <div class="deck_container">
        <div class="dialog-box">
            <h2>Deck A</h2>
            <p>
            total p: 468 |
            mean age = 28.82 |
            survival rate = 24.57264957264957 |
            male/female = 406/62
            </p>
        </div>
        <img src="data:image/png;base64,{a_deck_b64}" width="600px" class="hover_able">
    </div>
    
    <div class="deck_container">
        <div class="dialog-box">
            <h2>Deck B</h2>
            <p>
            total p: 76 |
            mean age = 37.61 |
            survival rate = 51.31578947368421 |
            male/female = 45/31
            </p>
        </div>
        <img src="data:image/png;base64,{b_deck_b64}" width="600px" class="hover_able">
    </div>
    
    <div class="deck_container">
        <div class="dialog-box">
            <h2>Deck C</h2>
            <p>
                total p: 181 |
                mean age = 20.35 |
                survival rate = 41.988950276243095 |
                male/female = 39/142
            </p>
        </div>
        <img src="data:image/png;base64,{c_deck_b64}" width="600px" class="hover_able">
    </div>
    
    <div class="deck_container">
        <div class="dialog-box">
            <h2>Deck D</h2>
            <p>
                total p: 43 |
                mean age = 37.69 |
                survival rate = 72.09302325581395 |
                male/female = 22/21
            </p>
        </div>
        <img src="data:image/png;base64,{d_deck_b64}" width="600px" class="hover_able">
    </div>
    
    <div class="deck_container">
        <div class="dialog-box">
            <h2>Deck E</h2>
            <p>
                total p: 51 |
                mean age = 36.4 |
                survival rate = 74.50980392156863 |
                male/female = 21/30
            </p>
        </div>
        <img src="data:image/png;base64,{e_deck_b64}" width="600px" class="hover_able">
    </div>
    
    <div class="deck_container">
        <div class="dialog-box">
            <h2>Deck F</h2>
            <p>
            total p: 25 |
            mean age = 43.18 |
            survival rate = 32.0 |
            male/female = 24/1
            </p>
        </div>
        <img src="data:image/png;base64,{f_deck_b64}" width="600px" class="hover_able">
    </div>
    
    <div class="deck_container">
        <div class="dialog-box">
            <h2>Deck G</h2>
            <p>
            total p: 47 |
            mean age = 34.96 |
            survival rate = 74.46808510638297 |
            male/female = 20/27
            </p>
        </div>
        <img src="data:image/png;base64,{g_deck_b64}" width="600px" class="hover_able">
    </div>
    
    <div class="deck_container">
        <img src="data:image/png;base64,{bottom_deck_b64}" width="600px">
    </div>
</body>
""")