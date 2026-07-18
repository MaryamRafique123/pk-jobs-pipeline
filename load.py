import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

def load_to_postgres(df):
    engine = create_engine(os.getenv("DATABASE_URL"))
    df.to_sql("jobs", engine, if_exists="replace", index=False)
    print(f"Loaded {len(df)} rows into the 'jobs' table")

if __name__ == "__main__":
    df = pd.read_csv("cleaned_jobs.csv")
    load_to_postgres(df)