import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def load_csv_data(filepath):
    """Load data from a CSV file into a pandas DataFrame."""
    return pd.read_csv(filepath)

def plot_normalized_overlay_csvs(filepaths, labels, title, ylabel):
    """
    Plot multiple datasets on the same graph with normalized y-values.
    Args:
        filepaths (list): List of CSV file paths.
        labels (list): List of labels for each dataset.
        title (str): Title of the graph.
        ylabel (str): Label for the y-axis.
    """
    plt.figure(figsize=(10, 6))

    for filepath, label in zip(filepaths, labels):
        # Load the data
        df = load_csv_data(filepath)
        df["date"] = pd.to_datetime(df["date"])  # Convert date to datetime format

        # Normalize the 'value' column
        df["normalized_value"] = (df["value"] - df["value"].min()) / (df["value"].max() - df["value"].min())

        # Plot the normalized data
        sns.lineplot(x="date", y="normalized_value", data=df, label=label)

    # Add labels, title, and grid
    plt.title(title)
    plt.xlabel("Date")
    plt.ylabel(f"Normalized {ylabel}")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def main():
    # Define the paths to your data
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(script_dir, "..", "data")

    federal_funds_path = os.path.join(data_dir, "federal_funds_rate.csv")
    ppi_path = os.path.join(data_dir, "ppi_software.csv")
    job_postings_path = os.path.join(data_dir, "software_job_postings.csv")

    # Overlay both datasets in a single graph with normalization
    plot_normalized_overlay_csvs(
        [federal_funds_path, ppi_path, job_postings_path],
        ["Federal Funds Rate", "PPI for Software", "Software Job Postings"],
        "Economic Indicators Over Time (Normalized)",
        "Value"
    )

if __name__ == "__main__":
    main()
