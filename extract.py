import requests
import json

def fetch_jobs():
    url = "https://remotive.com/api/remote-jobs"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    jobs = data["jobs"]
    print(f"Fetched {len(jobs)} jobs")
    return jobs

if __name__ == "__main__":
    jobs = fetch_jobs()
    with open("raw_jobs.json", "w") as f:
        json.dump(jobs, f)