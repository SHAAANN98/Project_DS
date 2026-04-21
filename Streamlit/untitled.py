import streamlit as st
import pandas as pd
import plotly.express as px

# Page config
st.set_page_config(page_title="Enquiry Dashboard", layout="wide")

st.title("📊 Enquiry Analytics Dashboard")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv(r"C:\Users\ACER\OneDrive\Documents\jupyter\Streamlit\Cleaned_Enquiry_Dataset.csv")
    
    # Clean column names
    df.columns = (df.columns
                  .str.strip()
                  .str.lower()
                  .str.replace(" ", "_"))
    
    # Convert date
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    
    return df

df = load_data()

# Sidebar filters
st.sidebar.header("🔍 Filters")

# Date filter
date_range = st.sidebar.date_input(
    "Select Date Range",
    [df['date'].min(), df['date'].max()]
)

# Dropdown filters
location = st.sidebar.multiselect("Location", df['location'].dropna().unique())
technology = st.sidebar.multiselect("Technology", df['technology'].dropna().unique())
status = st.sidebar.multiselect("Status", df['status'].dropna().unique())

# Apply filters
filtered_df = df.copy()

if len(date_range) == 2:
    filtered_df = filtered_df[
        (filtered_df['date'] >= pd.to_datetime(date_range[0])) &
        (filtered_df['date'] <= pd.to_datetime(date_range[1]))
    ]

if location:
    filtered_df = filtered_df[filtered_df['location'].isin(location)]

if technology:
    filtered_df = filtered_df[filtered_df['technology'].isin(technology)]

if status:
    filtered_df = filtered_df[filtered_df['status'].isin(status)]

# KPIs
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Enquiries", len(filtered_df))
col2.metric("Unique Locations", filtered_df['location'].nunique())
col3.metric("Technologies", filtered_df['technology'].nunique())
col4.metric("Conversions", filtered_df[filtered_df['status'] == 'joined'].shape[0])

# Charts Row 1
col1, col2 = st.columns(2)

with col1:
    st.subheader("📍 Enquiries by Location")
    fig = px.bar(filtered_df['location'].value_counts().reset_index(),
                 x='count', y='location',
                 orientation='h')
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("💻 Technology Interest")
    fig = px.pie(filtered_df, names='technology')
    st.plotly_chart(fig, use_container_width=True)

# Charts Row 2
col1, col2 = st.columns(2)

with col1:
    st.subheader("📅 Enquiries Over Time")
    time_data = filtered_df.groupby(filtered_df['date'].dt.date).size()
    fig = px.line(x=time_data.index, y=time_data.values)
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("📊 Status Distribution")
    fig = px.bar(filtered_df['status'].value_counts().reset_index(),
                 x='status', y='count')
    st.plotly_chart(fig, use_container_width=True)