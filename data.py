"""Single source of truth for the portfolio.

All resume content lives here and is imported by the Streamlit pages.
Transcribed from D:/Resume/Technical Resume/Latex/resume.tex (updated 2026-06).
Update this file when the resume changes; the whole site follows.
"""

# ---------------------------------------------------------------- profile ----
PROFILE = {
    "name": "Hamid Jahani",
    "title": "Data Scientist | Machine Learning Engineer",
    "tagline": "I ship production ML — NER, RAG, LLM agents, real-time IoT anomaly detection, and large-scale MLOps.",
    "location": "Iran · Remote",
    "email": "hamidjahani999@gmail.com",
    "phone": "+98 930 505 4619",
    "links": {
        "LinkedIn": "https://linkedin.com/in/hamid-jahani/",
        "GitHub": "https://github.com/sheperd007",
        "Portfolio": "https://hamid-resume.streamlit.app/",
    },
    # short, punchy hero metrics drawn from real resume outcomes
    "metrics": [
        {"value": "5+", "label": "Years in Data / ML"},
        {"value": "10+", "label": "ML pipelines shipped"},
        {"value": "60+", "label": "Experiments & A/B tests"},
        {"value": "98%", "label": "RAG factual accuracy"},
    ],
}

ABOUT = (
    "Data Scientist and Machine Learning Engineer with 5+ years taking models from notebook "
    "to production — named-entity recognition, retrieval-augmented generation, LLM agents, "
    "real-time IoT anomaly detection, and large-scale MLOps. M.S. in Statistics (Data Science), "
    "first in class, with published research in EEG deep learning for childhood ADHD. "
    "I build systems that move real metrics: revenue, retention, and time-to-production."
)

# ----------------------------------------------------------------- skills ----
# Each entry: (label, simple-icons slug or None). Icons load from
# https://cdn.simpleicons.org/<slug>; a missing icon falls back to a text chip,
# so the app never shows broken images even if a slug is wrong/offline.
SKILLS = {
    "Programming & Scripting": [
        ("Python", "python"),
        ("R", "r"),
        ("PySpark", "apachespark"),
        ("T-SQL", "microsoftsqlserver"),
        ("pytest", "pytest"),
        ("OOP", None),
    ],
    "Machine Learning & AI": [
        ("PyTorch", "pytorch"),
        ("TensorFlow", "tensorflow"),
        ("scikit-learn", "scikitlearn"),
        ("Pandas", "pandas"),
        ("NumPy", "numpy"),
        ("Statistics", None),
        ("Generative AI", None),
        ("RAG", None),
    ],
    "Deployment & Production": [
        ("Git", "git"),
        ("GitLab CI", "gitlab"),
        ("Docker", "docker"),
        ("AWS SageMaker", "amazonwebservices"),
        ("Flask", "flask"),
        ("FastAPI", "fastapi"),
        ("gRPC", None),
        ("Celery", "celery"),
    ],
    "Data Engineering": [
        ("Linux", "linux"),
        ("Airflow", "apacheairflow"),
        ("Kafka", "apachekafka"),
        ("Hadoop", "apachehadoop"),
        ("MongoDB", "mongodb"),
        ("MLflow", "mlflow"),
        ("Trino", "trino"),
        ("Qdrant", "qdrant"),
        ("Traefik", "traefikproxy"),
        ("Grafana", "grafana"),
        ("Power BI", None),
    ],
}

# ------------------------------------------------------------- experience ----
EXPERIENCE = [
    {
        "company": "Great Learning",
        "role": "Mentor and Course Owner",
        "location": "Bengaluru, India (Remote)",
        "period": "Dec 2024 – Present",
        "bullets": [
            "Own data science and machine learning programs (AI in Healthcare; Data-Driven "
            "Decisions) and mentor practitioners on end-to-end deep learning and NLP projects.",
        ],
    },
    {
        "company": "RoomVU",
        "role": "Data Scientist & Machine Learning Engineer",
        "location": "Vancouver, Canada (Remote)",
        "period": "Oct 2023 – Jun 2025",
        "bullets": [
            "Engineered a production named-entity-recognition (NER) service (Python, Celery, gRPC, "
            "Flask) on cloud data pipelines, improving crawling extraction accuracy 50%.",
            "Built voice-cloning and image-enhancement products on AWS SageMaker and serverless "
            "GPUs, contributing +5% revenue.",
            "Deployed NLP summarization and three automated news ML pipelines, cutting manual "
            "editorial workload 20%.",
            "Shipped retrieval-augmented generation (RAG) with LLMs at 98% factual accuracy for "
            "customer support.",
            "Integrated ChatGPT-based agents that saved 20+ agent hours/week, increased daily "
            "inquiry throughput 70%, and automated specialized scheduling.",
        ],
    },
    {
        "company": "Snappfood",
        "role": "Machine Learning Engineer · Data Analyst & Big Data Scientist",
        "location": "Remote",
        "period": "Dec 2021 – Nov 2023",
        "bullets": [
            "Automated training and release data pipelines (GitLab CI, Docker Swarm, Traefik, "
            "MLflow), cutting model time-to-production ~30%.",
            "Standardized MLOps runbooks, reviews, and handoffs across teams, reducing cross-team "
            "delivery friction ~30%.",
            "Fourth data-science hire: built 10+ ML pipelines and dashboards, mentored two analysts "
            "as the team scaled 4 → 15; recovered 10% of churned users, doubled engagement, cut "
            "drop-off 30%.",
            "Grew revenue 5% with a Hadoop/Spark data warehouse powering 60+ experiments, A/B "
            "tests, and Power BI for four teams.",
            "Reduced Hadoop session startup time 60%+ using PySpark on large-scale batch pipelines.",
            "Owned production churn, vendor-recommendation, and query-autocomplete models (MLlib, "
            "scikit-learn, MLflow, Evidently, Streamlit).",
        ],
    },
    {
        "company": "Digikala",
        "role": "Business Data Analyst",
        "location": "Tehran, Iran",
        "period": "Apr 2021 – Dec 2021",
        "bullets": [
            "Cut weekly analyst and sales prep time 20% by automating vendor segmentation and "
            "delivering 10 Power BI dashboards on operational data pipelines.",
            "Deployed a scikit-learn churn model retaining 10,000+ customers, contributing ~$8,000/"
            "month in measurable savings.",
        ],
    },
]

# --------------------------------------------------------------- projects ----
PROJECTS = [
    {
        "name": "Industrial IoT Predictive-Maintenance Platform (SensesIQ)",
        "stack": "Python · Kafka · MongoDB · SQL Server · Grafana · Docker · Linux · MLflow · GitLab CI/CD",
        "period": "2025 – Present",
        "bullets": [
            "Architected an end-to-end real-time platform ingesting data from 40+ industrial "
            "spinning-mill machines into a fault-tolerant streaming pipeline with reliable delivery "
            "and automated source-outage recovery.",
            "Built real-time monitoring dashboards used by operations and maintenance teams to "
            "triage machine health and downtime, decreasing time-to-outage-response 30%.",
            "Applied unsupervised signal processing with a temporal convolutional autoencoder to "
            "detect anomalous machine behavior in real time, preventing 100+ critical failures.",
            "Shipped live machine-failure alarming to operators via Telegram in under 5 seconds, "
            "cutting mean fault-response time and downtime.",
        ],
    },
]

# -------------------------------------------------------------- education ----
EDUCATION = [
    {
        "school": "Tarbiat Modares University",
        "location": "Tehran, Iran",
        "detail": "M.S. Statistics (Data Science) · GPA 4.0/4.0 · 1st/10 · "
                  "Thesis: EEG deep learning for childhood ADHD",
        "period": "2020 – 2022",
    },
    {
        "school": "Allameh Tabataba'i University",
        "location": "Tehran, Iran",
        "detail": "B.S. Statistics · GPA 3.93/4.0 · 1st/60",
        "period": "2016 – 2020",
    },
]

LANGUAGES = "English — TOEFL iBT (Reading 5, Listening 5.5, Writing 4.5, Speaking 5) · Persian — Native"

# ----------------------------------------------------------- certifications --
CERTIFICATIONS = [
    "Linux Foundation Certified System Administrator (LFCS)",
    "LLM Zoomcamp — DataTalksClub, 2025",
    "MLOps Zoomcamp — DataTalksClub, 2023",
    "Data Engineering Zoomcamp — DataTalksClub, 2023",
    "Power BI Data Analyst, 2023",
    "Machine Learning with Big Data — Coursera, 2022",
]

# ----------------------------------------------------------- publications ----
PUBLICATIONS = [
    "Hamid Jahani, A. A. Safaei. “EEG-based deep learning for childhood ADHD diagnosis.” "
    "*Cognitive Computation*, 2024.",
    "A. A. Safaei, Hamid Jahani. Chapter in *Handbook of Neural Engineering*, Vol. 1, Elsevier, 2023.",
    "Hamid Jahani. *Mathematical Statistics with R*. Allameh Tabataba'i University Press, 2020.",
]

# ----------------------------------------------------------------- awards ----
AWARDS = [
    "🥇 First place, Play with Real Data (60 teams), AGNA.co — Feb 2023",
    "🥈 Second place, National Master's Entrance Exam, Iran — Apr 2021",
    "🥈 Silver medal, National Statistics Olympiad (2020, 2019)",
    "🥇 Gold medal, Iran Statistics Competition — Jun 2019",
]
