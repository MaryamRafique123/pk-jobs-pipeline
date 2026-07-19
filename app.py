import os
import pandas as pd
import streamlit as st
from sqlalchemy import create_engine
from dotenv import load_dotenv
import plotly.express as px
import google.generativeai as genai

load_dotenv()

def get_secret(key):
    try:
        return st.secrets[key]
    except Exception:
        return os.getenv(key)

st.set_page_config(page_title="Jobs Market Pipeline", layout="wide")
st.title("Tech Jobs Market Dashboard")

engine = create_engine(get_secret("DATABASE_URL"))
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

st.subheader("Ask AI about this data")
user_question = st.text_input("e.g. 'Summarise the top trends in this data'")

if user_question:
    api_key = get_secret("GEMINI_API_KEY")
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-3.5-flash")

    summary_stats = df.describe(include="all").to_string()
    prompt = f"You are a data analyst. Based only on this summary stats table:\n{summary_stats}\n\nAnswer this question: {user_question}"

    with st.spinner("Thinking..."):
        response = model.generate_content(prompt)
    st.write(response.text)
