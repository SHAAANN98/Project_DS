import streamlit as st
import plotly.express as px
from utils import load_data

st.title("📈 Performance Analysis")

df = load_data()

# Divider
st.markdown("---")

# -----------------------------
# 📍 TOP 10 LOCATIONS
# -----------------------------
st.subheader("🏆 Top 10 Locations")

top_locations = (
    df['location']
    .value_counts()
    .head(10)
    .reset_index()
)

top_locations.columns = ['location', 'count']

fig = px.bar(
    top_locations,
    x='location',
    y='count',
    text='count'
)

st.plotly_chart(fig, use_container_width=True)


# Divider
st.markdown("---")

# -----------------------------
# 🎓 Qualification Performance
# -----------------------------
st.subheader("🎓 Qualification-wise Student Count")

qual_data = (
    df['qualification']
    .value_counts()
    .reset_index()
)

qual_data.columns = ['qualification', 'count']

# Horizontal bar (clean UI)
fig = px.bar(
    qual_data,
    x='count',
    y='qualification',
    orientation='h',
    text='count'
)

st.plotly_chart(fig, use_container_width=True)

# Branch performance
st.subheader("🏢 Branch Performance")
branch = df['branch'].value_counts().reset_index()
fig = px.bar(branch, x='branch', y='count', color='branch')
st.plotly_chart(fig, use_container_width=True)

# Divider
st.markdown("---")

# 🎓 Year of Passout Distribution

st.subheader("🎓 Year of Passout Distribution")

yop_data = (
    df['year_of_pass_out']
    .value_counts()
    .sort_index()
    .reset_index()
)

yop_data.columns = ['year_of_pass_out', 'count']

fig = px.bar(
    yop_data,
    x='year_of_pass_out',
    y='count',
    text='count'
)

st.plotly_chart(fig, use_container_width=True)

# Career issues
st.subheader("💼 Career Issues")
career = df['career_issue'].value_counts().reset_index()
fig = px.bar(career, x='career_issue', y='count')
st.plotly_chart(fig, use_container_width=True)

# Time slot
st.subheader("🕒 Preferred Time Slot")
fig = px.pie(df, names='time_slot')
st.plotly_chart(fig, use_container_width=True)


# Looking For
st.subheader("🔍Looking for")
looking_count = df['looking_for'].value_counts().reset_index()
fig = px.bar(looking_count, x='looking_for',y='count')
st.plotly_chart(fig, use_container_width=True)

# Mode analysis
st.subheader("📡 Mode of Training")
fig = px.pie(df, names='mode')
st.plotly_chart(fig, use_container_width=True)

# Counselor performance
if 'attended_by' in df.columns:
    st.subheader("👤 Counselor Performance")
    counselor = df['attended_by'].value_counts().reset_index()
    fig = px.bar(counselor, x='attended_by', y='count', color='attended_by')
    st.plotly_chart(fig, use_container_width=True)

# Divider
st.markdown("---")

# -----------------------------
# 📡 Find Us Source Distribution
# -----------------------------
st.subheader("📡 Find Us")

source_data = (
    df['find_us']
    .value_counts()
    .reset_index()
)

source_data.columns = ['source', 'count']

fig = px.pie(
    source_data,
    names='source',
    values='count'
)

st.plotly_chart(fig, use_container_width=True)

# Conversion by branch
st.subheader("🔥 Conversion by Branch")
conv = df[df['status'] == 'joined']['branch'].value_counts().reset_index()
fig = px.bar(conv, x='branch', y='count', color='branch')
st.plotly_chart(fig, use_container_width=True)

#Top10 Remarks
# Divider
st.markdown("---")

# -----------------------------
# 💬 Top 10 Remarks
# -----------------------------
st.subheader("💬 Top 10 Remarks")

remarks_data = (
    df['remarks']
    .dropna()
    .value_counts()
    .head(10)
    .reset_index()
)

remarks_data.columns = ['remark', 'count']

fig = px.bar(
    remarks_data,
    x='count',
    y='remark',
    orientation='h',
    text='count'
)

st.plotly_chart(fig, use_container_width=True)

# Divider
st.markdown("---")

# -----------------------------
# 📈 Year-wise Enquiry Trend
# -----------------------------
st.subheader("📈 Year-wise Enquiry Trend")

# Extract year from date
df['year'] = df['date'].dt.year

yearly_data = (
    df.groupby('year')
    .size()
    .reset_index(name='count')
)

fig = px.line(
    yearly_data,
    x='year',
    y='count',
    markers=True
)

st.plotly_chart(fig, use_container_width=True)

# Divider
st.markdown("---")

# -----------------------------
# 📅 Month-wise Trend by Year
# -----------------------------
st.subheader("📅 Month-wise Trend (Year Comparison)")

# Extract Year & Month
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month

monthly_data = (
    df.groupby(['year', 'month'])
    .size()
    .reset_index(name='count')
)

fig = px.line(
    monthly_data,
    x='month',
    y='count',
    color='year',
    markers=True
)

st.plotly_chart(fig, use_container_width=True)

# Divider
st.markdown("---")

# -----------------------------
# 💻 Top Technologies per Year
# -----------------------------
st.subheader("💻 Top Technologies per Year Trend")

tech_year = (
    df.groupby(['year', 'technology'])
    .size()
    .reset_index(name='count')
)

fig = px.line(
    tech_year,
    x='year',
    y='count',
    color='technology',
    markers=True
)

st.plotly_chart(fig, use_container_width=True)