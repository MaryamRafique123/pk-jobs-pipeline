import pandas as pd
import streamlit as st
from sqlalchemy import create_engine
import plotly.express as px

st.set_page_config(page_title="Jobs Market Pipeline", layout="wide")
st.title("Tech Jobs Market Dashboard")

engine = create_engine(st.secrets["DATABASE_URL"])
df = pd.read_sql("SELECT * FROM jobs", engine)

st.metric("Total jobs tracked", len(df))

col1, col2 = st.columns(2)
with col1:
    top_categories = df["category"].value_counts().head(10)
    fig = px.bar(top_categories, title="Top Job Categories")
    st.plotly_chart(fig, use_container_width=True)

with col2:
    top_companies = df["company"].value_counts().head(10)
    fig2 = px.bar(top_companies, title="Top Hiring Companies")
    st.plotly_chart(fig2, use_container_width=True)

st.subheader("Raw Data")
st.dataframe(df)