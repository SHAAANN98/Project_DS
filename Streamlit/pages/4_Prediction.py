import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from utils import load_data

# ═══════════════════════════════════════════════════════════
# PREMIUM CSS — Dark luxury editorial aesthetic
# ═══════════════════════════════════════════════════════════
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=DM+Sans:wght@300;400;500&display=swap');

/* ── Base reset ─────────────────────────────────────────── */
[data-testid="stAppViewContainer"] {
    background: #0a0a0f !important;
    font-family: 'DM Sans', sans-serif !important;
}
[data-testid="stAppViewContainer"] * { color: #e8e6e0 !important; }
[data-testid="stHeader"] { background: transparent !important; }
.block-container {
    padding: 2.5rem 3rem !important;
    max-width: 1100px !important;
}

/* ── Hero title ─────────────────────────────────────────── */
.hero-wrap {
    position: relative;
    padding: 3rem 0 2rem 0;
    margin-bottom: 0.5rem;
}
.hero-tag {
    font-family: 'DM Sans', sans-serif;
    font-size: 0.72rem;
    font-weight: 500;
    letter-spacing: 0.25em;
    text-transform: uppercase;
    color: #c9a96e !important;
    margin-bottom: 0.6rem;
}
.hero-title {
    font-family: 'Playfair Display', serif;
    font-size: 3.4rem;
    font-weight: 900;
    line-height: 1.05;
    color: #f5f0e8 !important;
    margin: 0 0 0.8rem 0;
}
.hero-title span { color: #c9a96e !important; }
.hero-sub {
    font-family: 'DM Sans', sans-serif;
    font-size: 0.95rem;
    font-weight: 300;
    color: #8a8780 !important;
    letter-spacing: 0.02em;
}
.hero-rule {
    width: 48px; height: 2px;
    background: #c9a96e;
    border: none; margin: 1.5rem 0 0 0;
}

/* ── Model badge ────────────────────────────────────────── */
.model-badge {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    background: rgba(201,169,110,0.10);
    border: 1px solid rgba(201,169,110,0.30);
    border-radius: 2px;
    padding: 0.45rem 1rem;
    font-size: 0.78rem;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: #c9a96e !important;
    margin-bottom: 2rem;
}

/* ── Section label ──────────────────────────────────────── */
.section-label {
    font-size: 0.68rem;
    font-weight: 500;
    letter-spacing: 0.22em;
    text-transform: uppercase;
    color: #5a5855 !important;
    margin-bottom: 1.2rem;
    padding-bottom: 0.5rem;
    border-bottom: 1px solid #1e1e26;
}

/* ── Input cards ────────────────────────────────────────── */
div[data-testid="stSelectbox"] > div > div {
    background: #111118 !important;
    border: 1px solid #1e1e26 !important;
    border-radius: 2px !important;
    color: #e8e6e0 !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 0.9rem !important;
    transition: border-color 0.2s ease !important;
}
div[data-testid="stSelectbox"] > div > div:hover {
    border-color: #c9a96e !important;
}
div[data-testid="stSelectbox"] label {
    font-size: 0.75rem !important;
    letter-spacing: 0.1em !important;
    text-transform: uppercase !important;
    color: #6b6965 !important;
    font-weight: 500 !important;
    margin-bottom: 0.3rem !important;
}

/* ── Predict button ─────────────────────────────────────── */
div[data-testid="stButton"] > button {
    background: #c9a96e !important;
    color: #0a0a0f !important;
    border: none !important;
    border-radius: 2px !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 0.8rem !important;
    font-weight: 600 !important;
    letter-spacing: 0.18em !important;
    text-transform: uppercase !important;
    padding: 0.75rem 2.5rem !important;
    width: 100% !important;
    margin-top: 1rem !important;
    transition: all 0.2s ease !important;
    cursor: pointer !important;
}
div[data-testid="stButton"] > button:hover {
    background: #e0c08a !important;
    transform: translateY(-1px) !important;
}

/* ── Metric cards ───────────────────────────────────────── */
.metric-card {
    background: #111118;
    border: 1px solid #1e1e26;
    border-radius: 2px;
    padding: 1.4rem 1.6rem;
    margin-bottom: 1rem;
}
.metric-card-gold { border-left: 3px solid #c9a96e; }
.metric-card-red  { border-left: 3px solid #e05c5c; }
.metric-label {
    font-size: 0.68rem;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: #5a5855 !important;
    margin-bottom: 0.4rem;
}
.metric-value {
    font-family: 'Playfair Display', serif;
    font-size: 2.8rem;
    font-weight: 700;
    line-height: 1;
    color: #f5f0e8 !important;
}
.metric-value-sm {
    font-family: 'Playfair Display', serif;
    font-size: 1.8rem;
    font-weight: 700;
    color: #f5f0e8 !important;
}
.metric-sub {
    font-size: 0.78rem;
    color: #5a5855 !important;
    margin-top: 0.3rem;
}
.verdict-join    { color: #c9a96e !important; }
.verdict-no-join { color: #e05c5c !important; }

/* ── Progress bar custom ────────────────────────────────── */
div[data-testid="stProgress"] > div > div > div {
    background: linear-gradient(90deg, #c9a96e, #e0c08a) !important;
    border-radius: 0 !important;
}
div[data-testid="stProgress"] > div > div {
    background: #1e1e26 !important;
    border-radius: 0 !important;
    height: 4px !important;
}

/* ── Stat grid ──────────────────────────────────────────── */
.stat-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 1px;
    background: #1e1e26;
    border: 1px solid #1e1e26;
    border-radius: 2px;
    overflow: hidden;
    margin-bottom: 2rem;
}
.stat-cell {
    background: #111118;
    padding: 1.2rem 1rem;
    text-align: center;
}
.stat-cell-num {
    font-family: 'Playfair Display', serif;
    font-size: 1.6rem;
    font-weight: 700;
    color: #c9a96e !important;
}
.stat-cell-lbl {
    font-size: 0.65rem;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    color: #5a5855 !important;
    margin-top: 0.2rem;
}

/* ── Summary panel ──────────────────────────────────────── */
.summary-panel {
    background: #111118;
    border: 1px solid #1e1e26;
    border-radius: 2px;
    padding: 1.6rem;
}
.summary-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0.6rem 0;
    border-bottom: 1px solid #1a1a20;
}
.summary-row:last-child { border-bottom: none; }
.summary-key {
    font-size: 0.72rem;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: #5a5855 !important;
}
.summary-val {
    font-size: 0.85rem;
    color: #c9a96e !important;
    font-weight: 500;
    text-align: right;
}

/* ── Insight box ────────────────────────────────────────── */
.insight-box {
    border: 1px solid #1e1e26;
    border-radius: 2px;
    padding: 1.2rem 1.4rem;
    margin-top: 1rem;
    background: #0d0d14;
    font-size: 0.85rem;
    line-height: 1.6;
    color: #8a8780 !important;
}
.insight-box strong { color: #c9a96e !important; }

/* ── Expander ───────────────────────────────────────────── */
details { background: #111118 !important; border: 1px solid #1e1e26 !important; border-radius: 2px !important; }
details summary { font-size: 0.78rem !important; letter-spacing: 0.1em !important; color: #6b6965 !important; padding: 0.8rem 1rem !important; }

/* ── Divider ────────────────────────────────────────────── */
hr { border-color: #1e1e26 !important; margin: 2rem 0 !important; }

/* ── Sidebar ─────────────────────────────────────────────  */
[data-testid="stSidebar"] { background: #080810 !important; }
[data-testid="stSidebar"] * { color: #6b6965 !important; }
</style>
""", unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════
# DATA + MODEL
# ═══════════════════════════════════════════════════════════
@st.cache_data
def get_data():
    df = load_data()
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
    for col in df.columns:
        if df[col].dtype == "object":
            df[col] = df[col].astype(str).str.strip().str.lower()
    # Normalize status
    df["status"] = df["status"].replace({
        "joined": "yes", "not joined": "no", "1": "yes", "0": "no"
    })
    return df.dropna()

FEATURES = [
    'location', 'find_us', 'qualification', 'branch',
    'career_issue', 'looking_for', 'technology', 'mode',
    'time_slot', 'attended_by',
]

@st.cache_resource
def train_lr(df):
    model_df = df[FEATURES + ["status"]].copy()
    model_df["status"] = model_df["status"].map({"yes": 1, "no": 0})
    model_df = model_df.dropna(subset=["status"])
    model_df["status"] = model_df["status"].astype(int)

    if model_df["status"].nunique() < 2 or len(model_df) < 30:
        return None, {}

    X = model_df[FEATURES]
    y = model_df["status"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    preprocessor = ColumnTransformer([
        ("cat", OneHotEncoder(handle_unknown="ignore", sparse_output=False), FEATURES)
    ])

    pipeline = Pipeline([
        ("pre", preprocessor),
        ("clf", LogisticRegression(
            max_iter=1000,
            class_weight="balanced",
            solver="lbfgs",
            C=1.0,
            random_state=42,
        ))
    ])

    pipeline.fit(X_train, y_train)
    report = classification_report(y_test, pipeline.predict(X_test), output_dict=True)

    metrics = {
        "accuracy":   round(report["accuracy"] * 100, 1),
        "precision":  round(report["1"]["precision"] * 100, 1),
        "recall":     round(report["1"]["recall"] * 100, 1),
        "f1":         round(report["1"]["f1-score"] * 100, 1),
        "train_n":    len(X_train),
        "test_n":     len(X_test),
    }
    return pipeline, metrics


df = get_data()
model, metrics = train_lr(df)


# ═══════════════════════════════════════════════════════════
# HERO HEADER
# ═══════════════════════════════════════════════════════════
st.markdown("""
<div class="hero-wrap">
    <div class="hero-tag">Cybersquare · Intelligence Engine</div>
    <h1 class="hero-title">Lead <span>Conversion</span><br>Predictor</h1>
    <p class="hero-sub">Logistic Regression model trained on historical enquiry data</p>
    <hr class="hero-rule">
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="model-badge">⬡ &nbsp; Logistic Regression &nbsp;·&nbsp; lbfgs solver &nbsp;·&nbsp; balanced classes</div>', unsafe_allow_html=True)


# ── Model performance stat bar ────────────────────────────
if metrics:
    st.markdown(f"""
    <div class="stat-grid">
        <div class="stat-cell">
            <div class="stat-cell-num">{metrics['accuracy']}%</div>
            <div class="stat-cell-lbl">Accuracy</div>
        </div>
        <div class="stat-cell">
            <div class="stat-cell-num">{metrics['precision']}%</div>
            <div class="stat-cell-lbl">Precision</div>
        </div>
        <div class="stat-cell">
            <div class="stat-cell-num">{metrics['recall']}%</div>
            <div class="stat-cell-lbl">Recall</div>
        </div>
        <div class="stat-cell">
            <div class="stat-cell-num">{metrics['f1']}%</div>
            <div class="stat-cell-lbl">F1 Score</div>
        </div>
    </div>
    """, unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════
# INPUT FORM
# ═══════════════════════════════════════════════════════════
st.markdown('<div class="section-label">01 — Student Profile</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2, gap="large")

with col1:
    tech      = st.selectbox("💻 Technology",      sorted(df['technology'].dropna().unique()))
    loc       = st.selectbox("📍 Location",         sorted(df['location'].dropna().unique()))
    mode      = st.selectbox("📡 Mode",             sorted(df['mode'].dropna().unique()))
    find      = st.selectbox("🔍 Find Us",          sorted(df['find_us'].dropna().unique()))
    time_slot = st.selectbox("⏰ Time Slot",        sorted(df['time_slot'].dropna().unique()))

with col2:
    branch   = st.selectbox("🏢 Branch",            sorted(df['branch'].dropna().unique()))
    career   = st.selectbox("🎯 Career Issue",      sorted(df['career_issue'].dropna().unique()))
    looking  = st.selectbox("🔍 Looking For",       sorted(df['looking_for'].dropna().unique()))
    attended = st.selectbox("👤 Attended By",       sorted(df['attended_by'].dropna().unique()))
    qual     = st.selectbox("🎓 Qualification",     sorted(df['qualification'].dropna().unique()))

st.markdown("")
predict_btn = st.button("⬡  Run Prediction Engine")


# ═══════════════════════════════════════════════════════════
# PREDICTION OUTPUT
# ═══════════════════════════════════════════════════════════
if predict_btn:
    input_dict = {
        "technology": tech, "location": loc, "mode": mode,
        "find_us": find, "time_slot": time_slot, "branch": branch,
        "career_issue": career, "looking_for": looking,
        "attended_by": attended, "qualification": qual,
    }
    input_df = pd.DataFrame([input_dict])

    try:
        if model is not None:
            proba_arr = model.predict_proba(input_df)[0]
            conversion_prob = float(proba_arr[1])
        else:
            # Lightweight fallback
            score = 0.30
            if tech in ["python","data science","mern","java"]:   score += 0.15
            if mode == "offline":                                   score += 0.12
            if find in ["reference","social media"]:               score += 0.10
            if career == "no issue":                               score += 0.15
            if time_slot in ["morning","afternoon"]:               score += 0.08
            if looking in ["it internship","it work experience"]:  score += 0.10
            if qual in ["ug","pg"]:                                score += 0.05
            if career == "backpapers":                             score -= 0.12
            conversion_prob = max(0.05, min(0.95, score))

        prediction = int(conversion_prob >= 0.50)
        prob_pct   = conversion_prob * 100
        prob_safe  = float(np.clip(conversion_prob, 0.01, 0.99))

        st.markdown("---")
        st.markdown('<div class="section-label">02 — Prediction Result</div>', unsafe_allow_html=True)

        left, right = st.columns([3, 2], gap="large")

        with left:
            # ── Main verdict card ─────────────────────────────
            if prediction == 1:
                st.markdown(f"""
                <div class="metric-card metric-card-gold">
                    <div class="metric-label">Conversion Verdict</div>
                    <div class="metric-value verdict-join">Likely<br>to Join</div>
                    <div class="metric-sub">Confidence score above threshold</div>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div class="metric-card metric-card-red">
                    <div class="metric-label">Conversion Verdict</div>
                    <div class="metric-value verdict-no-join">Unlikely<br>to Join</div>
                    <div class="metric-sub">Confidence score below threshold</div>
                </div>
                """, unsafe_allow_html=True)

            # ── Probability display ───────────────────────────
            prob_col1, prob_col2 = st.columns(2)
            with prob_col1:
                st.markdown(f"""
                <div class="metric-card" style="margin-bottom:0">
                    <div class="metric-label">Join Probability</div>
                    <div class="metric-value-sm" style="color:#c9a96e !important">{prob_pct:.1f}%</div>
                </div>
                """, unsafe_allow_html=True)
            with prob_col2:
                st.markdown(f"""
                <div class="metric-card" style="margin-bottom:0">
                    <div class="metric-label">Drop Probability</div>
                    <div class="metric-value-sm" style="color:#e05c5c !important">{100 - prob_pct:.1f}%</div>
                </div>
                """, unsafe_allow_html=True)

            # ── Probability bar ───────────────────────────────
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown('<div class="metric-label">Conversion Likelihood Bar</div>', unsafe_allow_html=True)
            st.progress(prob_safe)
            st.markdown(f'<div class="metric-sub" style="margin-top:0.3rem">Threshold: 50.0% &nbsp;|&nbsp; Score: {prob_pct:.1f}%</div>', unsafe_allow_html=True)

            # ── Recommendation ────────────────────────────────
            if conversion_prob >= 0.75:
                insight = "<strong>🔥 High Priority Lead.</strong> Strong conversion signals across multiple factors. Recommend immediate personal follow-up within 24 hours."
            elif conversion_prob >= 0.60:
                insight = "<strong>🟡 Warm Lead.</strong> Good probability of joining. A targeted follow-up call with a tailored pitch is advised."
            elif conversion_prob >= 0.45:
                insight = "<strong>🟠 Borderline Lead.</strong> Score is near the threshold. Consider offering a trial session or fee concession to tip the balance."
            else:
                insight = "<strong>🔵 Low Priority Lead.</strong> Several deterring factors detected. Long-term nurturing campaign recommended over direct push."

            st.markdown(f'<div class="insight-box">{insight}</div>', unsafe_allow_html=True)

        with right:
            # ── Input Summary panel ───────────────────────────
            st.markdown("""
            <div class="metric-label" style="margin-bottom:1rem">Input Summary</div>
            """, unsafe_allow_html=True)

            rows = [
                ("Technology",   tech.title()),
                ("Location",     loc.title()),
                ("Mode",         mode.title()),
                ("Find Us",      find.title()),
                ("Time Slot",    time_slot.title()),
                ("Branch",       branch.title()),
                ("Career Issue", career.title()),
                ("Looking For",  looking.title()),
                ("Attended By",  attended.title()),
                ("Qualification",qual.upper()),
            ]
            rows_html = "".join([
                f'<div class="summary-row"><span class="summary-key">{k}</span><span class="summary-val">{v}</span></div>'
                for k, v in rows
            ])
            st.markdown(f'<div class="summary-panel">{rows_html}</div>', unsafe_allow_html=True)

        # ── Model info expander ───────────────────────────────
        if metrics:
            st.markdown("<br>", unsafe_allow_html=True)
            with st.expander("📐 Model Technical Details"):
                st.markdown(f"""
                **Algorithm:** Logistic Regression (sklearn)  
                **Solver:** lbfgs &nbsp;|&nbsp; **Regularization C:** 1.0 &nbsp;|&nbsp; **Max Iterations:** 1000  
                **Class Weight:** balanced &nbsp;|&nbsp; **Features:** {len(FEATURES)} categorical  
                **Encoding:** OneHotEncoder (handle_unknown=ignore)  
                **Train samples:** {metrics['train_n']} &nbsp;|&nbsp; **Test samples:** {metrics['test_n']}  
                **Test Accuracy:** {metrics['accuracy']}% &nbsp;|&nbsp;
                **Precision:** {metrics['precision']}% &nbsp;|&nbsp;
                **Recall:** {metrics['recall']}% &nbsp;|&nbsp;
                **F1:** {metrics['f1']}%
                """)

    except Exception as e:
        st.error(f"Prediction error: {e}")
        st.exception(e)