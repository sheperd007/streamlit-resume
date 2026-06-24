"""Reusable UI helpers shared across pages. Keeps each page file focused."""

import base64
from pathlib import Path

import streamlit as st

from constant import info
from data import PROFILE

_ICON_COLOR = "c9d1d9"  # muted light — readable on the dark theme, monochrome look
_RESUME_PDF = "images/resume.pdf"

# Map of social link -> emoji used in the sidebar
_LINK_ICONS = {"LinkedIn": "💼", "GitHub": "🐙", "Portfolio": "🌐"}


def inject_css(file_name: str = "style/style.css") -> None:
    """Load a local stylesheet once per page."""
    css = Path(file_name).read_text(encoding="utf-8")
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)


def configure_page(page_title: str) -> None:
    """First Streamlit call on every page — sets tab title, icon, layout."""
    st.set_page_config(page_title=page_title, layout="wide", page_icon="🧑🏻‍💻")


@st.cache_data(show_spinner=False)
def _resume_bytes() -> bytes | None:
    p = Path(_RESUME_PDF)
    return p.read_bytes() if p.exists() else None


def render_sidebar() -> None:
    """Identity block, social links, and a resume download button."""
    with st.sidebar:
        st.markdown(
            f"""
            <div class="sidebar-card">
                <div class="sidebar-name">{PROFILE['name']}</div>
                <div class="sidebar-title">{PROFILE['title']}</div>
                <div class="sidebar-loc">📍 {PROFILE['location']}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        links = " ".join(
            f'<a class="sidebar-link" href="{url}" target="_blank">{_LINK_ICONS.get(name, "🔗")} {name}</a>'
            for name, url in PROFILE["links"].items()
        )
        st.markdown(
            f'<a class="sidebar-link" href="mailto:{PROFILE["email"]}">✉️ Email</a>{links}',
            unsafe_allow_html=True,
        )
        pdf = _resume_bytes()
        if pdf:
            st.download_button(
                "⬇️  Download Résumé (PDF)",
                data=pdf,
                file_name="Hamid_Jahani_Resume.pdf",
                mime="application/pdf",
                width="stretch",
            )


def section_header(icon: str, title: str) -> None:
    st.markdown(
        f'<h2 class="section-header">{icon}&nbsp; {title}</h2>',
        unsafe_allow_html=True,
    )


def hero() -> None:
    """Gradient name title, tagline, and metric chips."""
    metrics = "".join(
        f'<div class="metric"><div class="metric-val">{m["value"]}</div>'
        f'<div class="metric-lbl">{m["label"]}</div></div>'
        for m in PROFILE["metrics"]
    )
    st.markdown(
        f"""
        <div class="hero">
            <div class="hero-greet">Hi, I'm</div>
            <h1 class="hero-name">{PROFILE['name']} 👋</h1>
            <div class="hero-title">{PROFILE['title']}</div>
            <p class="hero-tagline">{PROFILE['tagline']}</p>
            <div class="metric-row">{metrics}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def _chip(label: str, slug: str | None) -> str:
    if slug:
        img = (
            f'<img class="chip-icon" loading="lazy" '
            f'src="https://cdn.simpleicons.org/{slug}/{_ICON_COLOR}" '
            f"onerror=\"this.style.display='none'\" alt=''>"
        )
        return f'<span class="skill-chip">{img}{label}</span>'
    return f'<span class="skill-chip text-only">{label}</span>'


def skill_group(category: str, items: list) -> None:
    chips = "".join(_chip(label, slug) for label, slug in items)
    st.markdown(
        f'<div class="skill-cat">{category}</div><div class="chip-row">{chips}</div>',
        unsafe_allow_html=True,
    )


def experience_card(exp: dict) -> None:
    bullets = "".join(f"<li>{b}</li>" for b in exp["bullets"])
    st.markdown(
        f"""
        <div class="card">
            <div class="card-top">
                <span class="card-title">{exp['role']}</span>
                <span class="card-period">{exp['period']}</span>
            </div>
            <div class="card-sub">{exp['company']} · {exp['location']}</div>
            <ul class="card-list">{bullets}</ul>
        </div>
        """,
        unsafe_allow_html=True,
    )


def project_card(proj: dict) -> None:
    bullets = "".join(f"<li>{b}</li>" for b in proj["bullets"])
    st.markdown(
        f"""
        <div class="card">
            <div class="card-top">
                <span class="card-title">{proj['name']}</span>
                <span class="card-period">{proj['period']}</span>
            </div>
            <div class="card-stack">{proj['stack']}</div>
            <ul class="card-list">{bullets}</ul>
        </div>
        """,
        unsafe_allow_html=True,
    )


def education_card(edu: dict) -> None:
    st.markdown(
        f"""
        <div class="card">
            <div class="card-top">
                <span class="card-title">{edu['school']}</span>
                <span class="card-period">{edu['period']}</span>
            </div>
            <div class="card-sub">{edu['location']}</div>
            <div class="card-detail">{edu['detail']}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def bullet_list_card(items: list) -> None:
    lis = "".join(f"<li>{i}</li>" for i in items)
    st.markdown(f'<div class="card"><ul class="card-list">{lis}</ul></div>', unsafe_allow_html=True)


def embed_pdf(path: str = _RESUME_PDF, height: int = 900) -> None:
    """Inline PDF preview with graceful fallback."""
    p = Path(path)
    if not p.exists():
        st.warning("Résumé PDF not found.")
        return
    b64 = base64.b64encode(p.read_bytes()).decode("utf-8")
    st.markdown(
        f'<iframe class="pdf-frame" src="data:application/pdf;base64,{b64}" '
        f'width="100%" height="{height}px" type="application/pdf"></iframe>',
        unsafe_allow_html=True,
    )
