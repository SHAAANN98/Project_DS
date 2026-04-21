import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from utils import load_data

st.title("🤖 AI Prediction")

df = load_data()

# -----------------------------
# 📊 Prepare data
# -----------------------------
df = df.dropna()

X = pd.get_dummies(df[
    ['location', 'find_us', 'qualification', 'branch',
     'career_issue', 'looking_for', 'technology', 'mode',
     'time_slot', 'attended_by', 'year_of_pass_out']
])

y = (df['status'] == 'joined').astype(int)

model = RandomForestClassifier()
model.fit(X, y)

# -----------------------------
# 🧾 User Input
# -----------------------------
st.subheader("Enter New Enquiry Details")

col1, col2 = st.columns(2)

with col1:
    tech = st.selectbox("💻 Technology", df['technology'].unique())
    loc = st.selectbox("📍 Location", df['location'].unique())
    mode = st.selectbox("📡 Mode", df['mode'].unique())
    find = st.selectbox("📡 Find Us", df['find_us'].unique())
    time_slot = st.selectbox("⏰ Time Slot", df['time_slot'].unique())

with col2:
    branch = st.selectbox("🏢 Branch", df['branch'].unique())
    career = st.selectbox("🎯 Career Issue", df['career_issue'].unique())
    looking = st.selectbox("🔍 Looking For", df['looking_for'].unique())
    attended = st.selectbox("👤 Attended By", df['attended_by'].unique())
    qual = st.selectbox("🎓 Qualification", df['qualification'].unique())
    yop = st.selectbox("📅 Year of Passout", df['year_of_pass_out'].unique())

# -----------------------------
# 🧠 Create Input Data
# -----------------------------
input_df = pd.DataFrame({
    "technology": [tech],
    "location": [loc],
    "mode": [mode],
    "find_us": [find],
    "time_slot": [time_slot],
    "branch": [branch],
    "career_issue": [career],
    "looking_for": [looking],
    "attended_by": [attended],
    "qualification": [qual],
    "year_of_pass_out": [yop]
})

# Encode
input_encoded = pd.get_dummies(input_df)

# Align with training data
input_encoded = input_encoded.reindex(columns=X.columns, fill_value=0)

# -----------------------------
# 🔮 Prediction
# -----------------------------
if st.button("🚀 Predict"):
    prediction = model.predict(input_encoded)[0]

    if prediction == 1:
        st.success("✅ Likely to Convert")
    else:
        st.error("❌ Not Likely to Convert")