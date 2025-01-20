from fetchdata import fetch_fred_data
import os
import subprocess # For running scripts from main

def main():
    # Define paths
    data_dir = os.path.join(os.path.dirname(__file__), "..", "data")
    fetchdata_path = os.path.join(os.path.dirname(__file__), "fetchdata.py")
    graph_path = os.path.join(os.path.dirname(__file__), "graph.py")
    # Fetch data
    subprocess.run(["python", fetchdata_path], check=True)
    subprocess.run(["python", graph_path], check=True)

if __name__ == "__main__":
    main()