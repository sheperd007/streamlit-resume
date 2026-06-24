# Hamid Jahani — Portfolio & Résumé

An interactive Streamlit portfolio for **Hamid Jahani**, Data Scientist & Machine Learning Engineer.
Live: **[hamid-resume.streamlit.app](https://hamid-resume.streamlit.app/)**

## Features

- **Modern dark UI** — glassmorphism cards, gradient hero, Inter typography (custom CSS + theme).
- **Single source of truth** — all résumé content lives in [`data.py`](data.py); every page reads from it.
- **Home** — hero with live metrics, tech-stack grid, career timeline, AI chatbot, contact form.
- **Résumé** — native-rendered Experience / Projects / Education / Publications / Awards + embedded
  and downloadable PDF.
- **Hobbies** — a lighter, personal page.
- **Buddy chatbot** — RAG over a bio file (LlamaIndex + OpenAI), answers recruiter questions.
- **Resilient assets** — skill icons (simple-icons CDN) and animations fail soft; no broken images,
  no blocking network calls on first paint.

## Run locally

```bash
pip install -r requirements.txt
streamlit run 1_Home.py
```

## Configuration

The chatbot uses OpenAI. Provide a key one of two ways (the rest of the site works without it):

- **Local:** copy `.env.example` → `.env` and set `OPENAI_API_KEY`, or paste the key in the sidebar.
- **Streamlit Cloud:** Settings → Secrets → add `OPENAI_API_KEY = "sk-..."`.

> Secrets (`.env`, `.streamlit/secrets.toml`) are gitignored — never commit API keys.

## Updating the résumé

Edit [`data.py`](data.py) (and `bio.txt` for the chatbot), then drop the latest `resume.pdf` into
`images/`. The whole site updates from there.

## Project layout

```
1_Home.py            # hero, skills, timeline, chatbot, contact
pages/2_Resume.py    # structured résumé + PDF
pages/3_Hobbies.py   # personal page
data.py              # all résumé content (edit here)
constant.py          # thin facade over data.py for the chatbot
components.py        # shared UI helpers (sidebar, hero, cards, badges)
style/style.css      # dark theme
bio.txt              # chatbot knowledge base
example.json         # career timeline (TimelineJS)
```

---

Originally based on the [Streamlit portfolio template](https://blog.streamlit.io/land-your-dream-job-build-your-portfolio-with-streamlit/);
substantially redesigned.
