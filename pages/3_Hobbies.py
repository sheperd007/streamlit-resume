import streamlit as st
from PIL import Image

from components import configure_page, inject_css, render_sidebar, section_header

configure_page("Hobbies · Hamid Jahani")
inject_css()
render_sidebar()

st.markdown('<h1 class="hero-name" style="font-size:2.6rem;">Hobbies</h1>', unsafe_allow_html=True)
section_header("🫶", "Beyond the keyboard")
st.write(
    "Outside of data and ML, I'm drawn to astronomy and cosmology, financial markets, "
    "psychology, and continuous self-improvement."
)

cols = st.columns(3)
for col, path in zip(cols, ["images/1.jpg", "images/2.png", "images/3.png"]):
    with col:
        try:
            st.image(Image.open(path), width="stretch")
        except Exception:
            st.empty()
