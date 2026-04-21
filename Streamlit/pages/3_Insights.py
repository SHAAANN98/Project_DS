import streamlit as st
import plotly.express as px
import pandas as pd
from utils import load_data

st.title("🔍 Insights")

df = load_data()


# Qualification vs Status
st.subheader("🎓 Qualification vs Status")
cross = pd.crosstab(df['qualification'], df['status'])
st.dataframe(cross)

#Branch-wise status distribution
st.subheader("🏢 Branch-wise Status Distribution")
cross = pd.crosstab(df['branch'],df['status'])
st.dataframe(cross)

#Career issue vs status
st.subheader("💼 Career Issues vs Status")
cross =pd. crosstab(df['career_issue'],df['status'])
st.dataframe(cross)

#Looking-for vs status
st.subheader("🔍 Looking-for vs Status")
cross = pd.crosstab(df['looking_for'],df['status'])
st.dataframe(cross)

#Technology vs status
st.subheader("💻 Technology vs Status")
cross = pd.crosstab(df['technology'],df['status'])
st.dataframe(cross)

#Timeslot vs status
st.subheader("🕒 Time Slot vs Status")
cross = pd.crosstab(df['time_slot'],df['status'])
st.dataframe(cross)

#Enquiry-sources vs status
st.subheader("📡 Find Us vs Status")
cross = pd.crosstab(df['find_us'],df['status'])
st.dataframe(cross)

#Attended-by vs status
st.subheader("👤 Counselor vs Status")
cross = pd.crosstab(df['attended_by'],df['status'])
st.dataframe(cross)

#Enquiry vs status
st.subheader("📩 Enquiry vs Status")
cross = pd.crosstab(df['status'], columns="Count")
st.dataframe(cross)