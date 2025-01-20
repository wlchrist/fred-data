import requests
import pandas as pd 
import os


API_KEY = "50557c145ae73786c962fc5ecad124aa"

# FRED API endpoint
BASE_URL = "https://api.stlouisfed.org/fred/series/observations"

# Ensure the /data directory exists
script_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(script_dir, "..", "data")
os.makedirs(data_dir, exist_ok=True)

def fetch_fred_data(series_id, filename, frequency = "m"):
    """
    Fetch data from FRED API and save as a CSV file.
    Args:
        series_id (str): The FRED series ID (e.g., "FEDFUNDS").
        filename (str): Name of the output CSV file.
    """
    print(f"Fetching {series_id} data...")
    url = "https://api.stlouisfed.org/fred/series/observations"
    params = {
        "series_id": series_id,
        "api_key": API_KEY,
        "file_type": "json",
        "frequency" : frequency,
        "observation_start": "2020-02-01",
        "observation_end": "2024-01-01",
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()["observations"]
        df = pd.DataFrame(data)[["date", "value"]]
        df["value"] = pd.to_numeric(df["value"], errors="coerce")
        file_path = os.path.join(data_dir, filename)
        df.to_csv(file_path, index=False)
        print(f"Saved {series_id} data to {file_path}")
    else:
        print(f"Error fetching {series_id}: {response.status_code}")

def main():
    # Fetch Federal Funds Rate
    fetch_fred_data("FEDFUNDS", "federal_funds_rate.csv")
    
    # Fetch Software Development Job Postings on Indeed in the United States
    fetch_fred_data("IHLIDXUSTPSOFTDEVE", "software_job_postings.csv")
    
    # Fetch Producer Price Index by Industry: Software Publishers
    fetch_fred_data("WPU34", "ppi_software.csv")
if __name__ == "__main__":
    main()