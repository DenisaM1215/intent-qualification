import pandas as pd

DATASET_PATH = "data/companies.jsonl"

def load_dataset():
    return pd.read_json(DATASET_PATH, lines=True)
def main():
    df=load_dataset()

if __name__ == "__main__":
    main()