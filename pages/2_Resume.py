import streamlit as st

from components import (
    bullet_list_card,
    configure_page,
    education_card,
    embed_pdf,
    experience_card,
    inject_css,
    project_card,
    render_sidebar,
    section_header,
)
from data import (
    AWARDS,
    EDUCATION,
    EXPERIENCE,
    LANGUAGES,
    PROJECTS,
    PUBLICATIONS,
)

configure_page("Résumé · Hamid Jahani")
inject_css()
render_sidebar()

st.markdown('<h1 class="hero-name" style="font-size:2.6rem;">Résumé</h1>', unsafe_allow_html=True)

tab_view, tab_pdf = st.tabs(["📄  Structured", "🗎  PDF"])

with tab_view:
    section_header("💼", "Experience")
    for exp in EXPERIENCE:
        experience_card(exp)

    section_header("🚀", "Projects")
    for proj in PROJECTS:
        project_card(proj)

    section_header("🎓", "Education")
    for edu in EDUCATION:
        education_card(edu)
    st.markdown(f'<div class="card"><b>Languages:</b> {LANGUAGES}</div>', unsafe_allow_html=True)

    section_header("📚", "Publications")
    bullet_list_card(PUBLICATIONS)

    section_header("🏆", "Awards")
    bullet_list_card(AWARDS)

with tab_pdf:
    st.caption(
        "Trouble viewing inline? "
        "[Open in Google Drive](https://drive.google.com/file/d/1ivPjW7ubM2ryyJVcoWdz-VOkyWyM-aXi/view?usp=sharing) "
        "or use **Download Résumé** in the sidebar."
    )
    embed_pdf(height=900)
