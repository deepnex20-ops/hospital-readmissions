# hospital_dashboard.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

st.set_page_config(page_title="Hospital Data Dashboard", layout="wide")
st.title("🏥 Hospital Data Dashboard")

np.random.seed(42)
hospital = pd.DataFrame({
    'age_num': np.random.randint(20, 90, size=100),
    'n_emergency_log': np.random.randint(0, 10, size=100),
    'change': np.random.choice([0,1], size=100),
    'diabetes_med': np.random.choice([0,1], size=100),
    'readmitted': np.random.choice([0,1], size=100)
})

st.sidebar.header("Filters")
age_range = st.sidebar.slider("Select Age Range", int(hospital['age_num'].min()), int(hospital['age_num'].max()), (30, 70))
hospital_filtered = hospital[(hospital['age_num'] >= age_range[0]) & (hospital['age_num'] <= age_range[1])]

st.subheader("Distribution of Age")
fig, ax = plt.subplots()
ax.hist(hospital_filtered['age_num'], bins=10, color='skyblue', edgecolor='black')
ax.set_xlabel("Age")
ax.set_ylabel("Count")
ax.set_title("Distribution of Age")
st.pyplot(fig)

st.subheader("Distribution of Number of Emergency Visits (Log)")
fig, ax = plt.subplots()
log_emergency = np.log1p(hospital_filtered['n_emergency_log'])
ax.hist(log_emergency, bins=10, color='salmon', edgecolor='black')
ax.set_xlabel("Log(1 + n_emergency)")
ax.set_ylabel("Count")
ax.set_title("Distribution of n_emergency_log")
st.pyplot(fig)

st.subheader("Correlation Heatmap")
fig, ax = plt.subplots(figsize=(8,6))
sns.heatmap(hospital_filtered.corr(), annot=True, fmt=".2f", cmap='coolwarm', ax=ax)
st.pyplot(fig)

st.subheader("Quick Statistics")
st.write(hospital_filtered.describe())

st.subheader("Key Metrics")
col1, col2, col3 = st.columns(3)
col1.metric("Average Age", f"{hospital_filtered['age_num'].mean():.1f}")
col2.metric("Total Emergency Visits", f"{hospital_filtered['n_emergency_log'].sum()}")
col3.metric("Readmitted Patients", f"{hospital_filtered['readmitted'].sum()}")
