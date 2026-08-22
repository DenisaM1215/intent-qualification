import pandas as pd

DATA_PATH = "data/companies.jsonl"

def load_dataset():
    return pd.read_json(DATA_PATH, lines=True)

def main():
    df = load_dataset()

    print ("Dataset shape: ", df.shape)
    print ("\nColumns: ")
    print (df.columns.to_list())

    print("\nFirst 5 rows: ")
    print(df.head())

    print("\nFirst complete record: ")
    print(df.iloc[0].to_dict())

    print("\nData types:")
    print(df.dtypes)

    print("\nActual Python types:")
    for col in df.columns:
        print(f"{col}: {type(df[col].iloc[0])}")

    print("\nAddress types:")
    print(df['address'].apply(type).value_counts())

if __name__ == "__main__":
    main()