import requests
import streamlit as st
from streamlit.errors import StreamlitSecretNotFoundError
from streamlit_lottie import st_lottie
from streamlit_timeline import timeline

from components import (
    configure_page,
    hero,
    inject_css,
    render_sidebar,
    section_header,
    skill_group,
)
from constant import info
from data import ABOUT, SKILLS

configure_page("Hamid Jahani · Data Scientist")
inject_css()
render_sidebar()

name = info["Name"]
pronoun = info["Pronoun"]


# -----------------  helpers  ----------------- #
@st.cache_data(show_spinner=False, ttl=86400)
def load_lottieurl(url: str):
    """Fetch a Lottie animation; never break the page if it's unreachable."""
    try:
        r = requests.get(url, timeout=4)
        if r.status_code == 200:
            return r.json()
    except requests.RequestException:
        pass
    return None


# -----------------  hero  ----------------- #
with st.container():
    col1, col2 = st.columns([7, 3], vertical_alignment="center")
    with col1:
        hero()
    with col2:
        lottie = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_x17ybolp.json")
        if lottie:
            st_lottie(lottie, height=260, key="hero")

# -----------------  about  ----------------- #
section_header("👨‍💻", "About")
st.write(ABOUT)

# -----------------  skills  ----------------- #
section_header("⚒️", "Tech Stack")
for category, items in SKILLS.items():
    skill_group(category, items)

# -----------------  career timeline  ----------------- #
section_header("📌", "Career Snapshot")
try:
    with open("example.json", "r", encoding="utf-8") as f:
        timeline(f.read(), height=420)
except Exception:
    st.info("Timeline unavailable.")

# -----------------  chatbot  ----------------- #
section_header("🤖", "Chat with Buddy")
st.caption(
    f"Buddy is an AI assistant that answers recruiter questions about {name}. "
    "Powered by OpenAI — add a key in the sidebar or `st.secrets` to enable it."
)

try:
    secret_key = st.secrets.get("OPENAI_API_KEY", "")
except StreamlitSecretNotFoundError:
    secret_key = ""

openai_api_key = st.sidebar.text_input(
    "OpenAI API key (for the chatbot)",
    type="password",
    value=(secret_key or "").strip(),
    help="Only used in your session to answer questions about Hamid. Never stored.",
).strip()


@st.cache_data(show_spinner=False)
def load_documents():
    from llama_index.core import SimpleDirectoryReader

    return SimpleDirectoryReader(input_files=["bio.txt"]).load_data()


@st.cache_resource(show_spinner=False)
def build_index(_openai_api_key: str):
    from llama_index.core import Settings, VectorStoreIndex
    from llama_index.embeddings.openai import OpenAIEmbedding
    from llama_index.llms.openai import OpenAI

    Settings.llm = OpenAI(model="gpt-4o-mini", temperature=0, api_key=_openai_api_key)
    Settings.embed_model = OpenAIEmbedding(model="text-embedding-3-small", api_key=_openai_api_key)
    return VectorStoreIndex.from_documents(load_documents())


def ask_bot(index, question: str) -> str:
    prompt = (
        f"You are Buddy, an AI assistant helping {name} in {pronoun} job search by giving "
        f"recruiters relevant, concise information. If you don't know the answer, say so politely "
        f"and point them to {name}'s contact details. Do not prefix your answer with 'Buddy' or a "
        f"line break.\n\nQuestion: {question}\n"
    )
    return str(index.as_query_engine(similarity_top_k=4).query(prompt))


st.caption("Try: *“What's his experience with LLMs?”* · *“What's his education?”* · *“How do I contact him?”*")
with st.form("buddy_form", clear_on_submit=False):
    user_input = st.text_input("Ask anything about Hamid, then click Submit.", key="input")
    submitted = st.form_submit_button("Submit")

if submitted and user_input:
    if not openai_api_key:
        st.warning("Add your OpenAI API key in the sidebar (or set `OPENAI_API_KEY` in secrets) to chat.")
    else:
        try:
            with st.spinner("Thinking..."):
                st.info(ask_bot(build_index(openai_api_key), user_input))
        except Exception as e:
            st.error(f"Couldn't reach the model: {e}")

# -----------------  contact  ----------------- #
section_header("📨", "Contact Me")
st.markdown(
    f"""
    <form action="https://formsubmit.co/{info['Email']}" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """,
    unsafe_allow_html=True,
)
