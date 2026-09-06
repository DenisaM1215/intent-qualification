import pandas as pd
import matplotlib.pyplot as plt

DATASET_PATH = "data/companies.jsonl"

def load_dataset():
    return pd.read_json(DATASET_PATH, lines=True)
def main():
    df=load_dataset()

    duplicate_mask = df.astype(str).duplicated()
    df_unique = df[~duplicate_mask].copy()

    years = df_unique['year_founded'].dropna()
    print("\nYear founded statistics:")
    print(years.describe())

    print("\nMedian:")
    print(years.median())

    plt.figure(figsize=(10, 5))
    plt.hist(years, bins=range(1850, 2031, 10), rwidth=0.9, color="#f388e7e1", edgecolor='black')
    plt.title("Distribution of Year Founded")
    plt.xlabel("Year Founded")
    plt.ylabel("Number of companies")

    plt.tight_layout()
    plt.savefig("analysis/figures/year_founded_distribution.png")
    plt.close()


if __name__ == "__main__":
    main()