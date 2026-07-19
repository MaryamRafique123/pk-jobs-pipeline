# Tech Jobs Market Pipeline

A real end-to-end ETL (Extract, Transform, Load) data pipeline that pulls live remote job
listings, cleans and structures the data, stores it in a cloud PostgreSQL database, and
visualizes it through an interactive live dashboard.

**Live Demo:** https://pk-jobs-pipeline-khezwfvwmnsc8qvxfw7ax9.streamlit.app/

## What it does

- **Extract:** Pulls live job listing data from the Remotive public API
- **Transform:** Cleans and structures the raw data using Pandas — removes duplicates, handles missing values, standardizes formatting, parses dates
- **Load:** Loads the cleaned dataset into a PostgreSQL database (hosted on Neon)
- **Visualize:** An interactive Streamlit dashboard displays job counts, top categories, and top hiring companies through live charts

## Tech Stack

- **Python** — core language
- **Pandas** — data cleaning and transformation
- **PostgreSQL** (via Neon) — cloud database storage
- **SQLAlchemy** — database connection and querying
- **Streamlit** — interactive dashboard/frontend
- **Plotly** — data visualization
- **Git/GitHub** — version control

## How to run it locally

1. Clone this repo
2. Create a virtual environment and install dependencies: `pip install -r requirements.txt`
3. Create a `.env` file with your own database connection string: `DATABASE_URL=your_postgres_connection_string`
4. Run the pipeline: `python pipeline.py`
5. Launch the dashboard: `streamlit run app.py`

## Project Structure

- `extract.py` — pulls raw job data from the API
- `transform.py` — cleans the data with Pandas
- `load.py` — loads cleaned data into PostgreSQL
- `pipeline.py` — runs extract → transform → load in sequence
- `app.py` — Streamlit dashboard

## What this project demonstrates

This reflects the core structure of real-world data engineering work: pulling data from an external source, applying transformation and validation logic, persisting it in a relational database, and serving it through a live, queryable dashboard.