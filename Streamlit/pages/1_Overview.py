import streamlit as st
import plotly.express as px
import pandas as pd
from utils import load_data

# -----------------------------
# 🎨 Page Styling
# -----------------------------
st.markdown("""
<style>
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

/* KPI Cards */
.stMetric {
    background-color: #1c1f26;
    padding: 15px;
    border-radius: 10px;
    text-align: center;
}

/* Column spacing */
div[data-testid="column"] {
    padding: 0 15px;
}
</style>
""", unsafe_allow_html=True)

st.title("📊 Overview Dashboard")

# -----------------------------
# 📥 Load Data
# -----------------------------
df = load_data()

# -----------------------------
# 🔍 Sidebar Filters
# -----------------------------
st.sidebar.header("🔍 Filters")

location = st.sidebar.multiselect(
    "Location", df['location'].dropna().unique()
)

technology = st.sidebar.multiselect(
    "Technology", df['technology'].dropna().unique()
)

date_range = st.sidebar.date_input(
    "Select Date Range",
    [df['date'].min(), df['date'].max()]
)

# -----------------------------
# 🔄 Apply Filters
# -----------------------------
filtered_df = df.copy()

if location:
    filtered_df = filtered_df[
        filtered_df['location'].isin(location)
    ]

if technology:
    filtered_df = filtered_df[
        filtered_df['technology'].isin(technology)
    ]

if len(date_range) == 2:
    start_date = pd.to_datetime(date_range[0])
    end_date = pd.to_datetime(date_range[1])

    filtered_df = filtered_df[
        (filtered_df['date'] >= start_date) &
        (filtered_df['date'] <= end_date)
    ]

# -----------------------------
# 📊 KPI SECTION
# -----------------------------
with st.container():
    col1, col2, col3, col4 = st.columns(4, gap="medium")

    total = len(filtered_df)
    joined = len(filtered_df[filtered_df['status'] == 'joined'])
    conversion = (joined / total * 100) if total > 0 else 0

    col1.metric("Total Enquiries", total)
    col2.metric("Conversions", joined)
    col3.metric("Conversion Rate", f"{conversion:.2f}%")
    col4.metric("Locations", filtered_df['location'].nunique())

# Divider
st.markdown("---")

# -----------------------------
# 📈 CHART SECTION 1
# -----------------------------
with st.container():
    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.subheader("📅 Enquiries Over Time")
        st.markdown("<div style='margin-top:15px;'></div>", unsafe_allow_html=True)

        time_data = filtered_df.groupby(
            filtered_df['date'].dt.date
        ).size().reset_index(name='count')

        fig1 = px.line(time_data, x='date', y='count')
        st.plotly_chart(fig1, use_container_width=True)

    with col2:
        st.subheader("💻 Technology Distribution")
        st.markdown("<div style='margin-top:15px;'></div>", unsafe_allow_html=True)

        fig2 = px.pie(filtered_df, names='technology')
        st.plotly_chart(fig2, use_container_width=True)

# Divider
st.markdown("---")

# -----------------------------
# 📍 CHART SECTION 2
# -----------------------------
with st.container():
    st.subheader("📍 Enquiries by Location")
    st.markdown("<div style='margin-top:15px;'></div>", unsafe_allow_html=True)

    loc_data = filtered_df['location'].value_counts().reset_index()
    loc_data.columns = ['location', 'count']

    fig3 = px.bar(loc_data, x='location', y='count')
    st.plotly_chart(fig3, use_container_width=True)