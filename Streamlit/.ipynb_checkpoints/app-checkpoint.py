import streamlit as st

# -----------------------------
# ⚙️ Page Config (ONLY ONCE)
# -----------------------------
st.set_page_config(
    page_title="Enquiry Dashboard",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------
# 🎨 Custom Styling
# -----------------------------
st.markdown("""
<style>
/* Background */
.stApp {
    background-color: #0e1117;
}

/* Title */
h1 {
    color: #ffffff;
    text-align: center;
}

/* Subtitle */
.subtitle {
    text-align: center;
    font-size: 20px;
    color: #9ca3af;
    margin-bottom: 30px;
}

/* Card Styling */
.card {
    background-color: #1c1f26;
    padding: 25px;
    border-radius: 15px;
    text-align: center;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.3);
}

/* Feature text */
.card h3 {
    color: white;
}
.card p {
    color: #9ca3af;
}

/* Divider */
hr {
    border: 1px solid #2c2f36;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# 🚀 HEADER SECTION
# -----------------------------
st.markdown("<h1>🚀 Enquiry Analytics Dashboard</h1>", unsafe_allow_html=True)

st.markdown(
    "<div class='subtitle'>Professional Data Analytics & AI Insights Platform</div>",
    unsafe_allow_html=True
)

st.markdown("---")

# -----------------------------
# 📊 FEATURE CARDS
# -----------------------------
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
        <h3>📊 Dashboard</h3>
        <p>View real-time enquiry analytics, KPIs, and trends</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <h3>📈 Performance</h3>
        <p>Analyze branch, counselor, and conversion performance</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
        <h3>🤖 AI Prediction</h3>
        <p>Predict which enquiries are likely to convert</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# -----------------------------
# 📌 INSTRUCTIONS SECTION
# -----------------------------
st.subheader("📌 How to Use")

st.markdown("""
- Use the **sidebar** to navigate between pages  
- Apply **filters** to explore data  
- Check **Insights & Performance** pages for deeper analysis  
- Use **AI Prediction** to forecast conversions  
""")

st.markdown("---")

# -----------------------------
# 💡 FOOTER
# -----------------------------
st.markdown(
    "<p style='text-align:center; color:gray;'>Streamlit</p>",
    unsafe_allow_html=True
)
st.sidebar.markdown("---")

st.sidebar.subheader("ℹ️ About")

st.sidebar.info("""
**Enquiry Analytics Dashboard**

This app helps analyze enquiry data with:
- 📊 Interactive dashboards  
- 📈 Performance insights  
- 🔍 Deep analytics  
- 🤖 AI-based predictions  

""")