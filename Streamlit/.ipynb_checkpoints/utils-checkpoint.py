import pandas as pd
import streamlit as st

def load_data():
    df = pd.read_csv(r"C:\Users\ACER\OneDrive\Documents\jupyter\Streamlit\Cleaned_Enquiry_Dataset.csv")

    df.columns = (df.columns
                  .str.strip()
                  .str.lower()
                  .str.replace(" ", "_"))

    df['date'] = pd.to_datetime(df['date'], errors='coerce')

    return df


def apply_global_filters(df):
    st.sidebar.header("🔍 Global Filters")

    # Session state (persists across pages)
    if "location" not in st.session_state:
        st.session_state.location = []
    if "technology" not in st.session_state:
        st.session_state.technology = []

    location = st.sidebar.multiselect(
        "Location",
        df['location'].dropna().unique(),
        default=st.session_state.location
    )

    technology = st.sidebar.multiselect(
        "Technology",
        df['technology'].dropna().unique(),
        default=st.session_state.technology
    )

    date_range = st.sidebar.date_input(
        "Date Range",
        [df['date'].min(), df['date'].max()]
    )

    # Save state
    st.session_state.location = location
    st.session_state.technology = technology

    filtered_df = df.copy()

    if location:
        filtered_df = filtered_df[filtered_df['location'].isin(location)]

    if technology:
        filtered_df = filtered_df[filtered_df['technology'].isin(technology)]

    if len(date_range) == 2:
        start = pd.to_datetime(date_range[0])
        end = pd.to_datetime(date_range[1])

        filtered_df = filtered_df[
            (filtered_df['date'] >= start) &
            (filtered_df['date'] <= end)
        ]

    return filtered_df
