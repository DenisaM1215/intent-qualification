import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

pd.set_option("display.float_format","{:.2f}".format)

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
    print("Histogram saved!")
    plt.close()

    employees = df_unique['employee_count'].dropna()
    print("\nEmployee count statistics:")
    print(employees.describe())

    print("\nMedian:")
    print(employees.median())

    plt.figure(figsize=(10, 5))
    plt.hist(employees, bins=30, rwidth=0.9, color="#f388e7e1", edgecolor='black')
    plt.title("Distribution of Employee Count")
    plt.xlabel("Employee Count")
    plt.ylabel("Number of companies")
    plt.tight_layout()
    plt.savefig("analysis/figures/employee_count_distribution.png")
    print("Histogram saved!")
    plt.close()

    print("\nEmployee count skewness:")
    print(employees.skew())

    print("\nEmployee count percentiles:")
    print(employees.quantile([0.25, 0.5, 0.75, 0.9, 0.95, 0.99]))

    employee_bins = np.logspace(
        np.log10(employees.min()),
        np.log10(employees.max()),
        20
    )

    plt.figure(figsize=(10, 5))
    plt.hist(employees, bins=employee_bins, rwidth=0.9, color="#f388e7e1", edgecolor='black')
    plt.xscale('log')
    plt.title("Distribution of Employee Count (Log Scale)")
    plt.xlabel("Employee Count (Log Scale)")
    plt.ylabel("Number of companies")
    plt.tight_layout()
    plt.savefig("analysis/figures/employee_count_distribution_log_scale.png")
    print("Histogram saved!")
    plt.close()



if __name__ == "__main__":
    main()