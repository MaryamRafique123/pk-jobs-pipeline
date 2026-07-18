import json
import pandas as pd

def clean_jobs(jobs):
    df = pd.DataFrame(jobs)

    df = df[["id", "title", "company_name", "category", "job_type",
              "candidate_required_location", "publication_date", "url"]]

    df = df.rename(columns={
        "company_name": "company",
        "candidate_required_location": "location",
        "publication_date": "posted_date"
    })

    df = df.drop_duplicates(subset="id")
    df["posted_date"] = pd.to_datetime(df["posted_date"], errors="coerce")
    df = df.dropna(subset=["title", "company"])
    df["title"] = df["title"].str.strip()
    df["company"] = df["company"].str.strip()

    return df

if __name__ == "__main__":
    with open("raw_jobs.json") as f:
        jobs = json.load(f)
    df = clean_jobs(jobs)
    print(df.head())
    print(f"Cleaned dataset: {len(df)} rows")
    df.to_csv("cleaned_jobs.csv", index=False)