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

    string_addresses = df [df["address"].apply(type) == str]
    print("\nAddress strings:")
    print(string_addresses["address"].head())

    print("\nDo all string addresses look like dictionaries?")
    print(string_addresses["address"].str.startswith("{").value_counts())

    print("\nPrimary NAICS types:")
    print(df['primary_naics'].apply(type).value_counts())

    address_is_string = df["address"].apply(type) == str
    naics_is_string = df["primary_naics"].apply(type) == str
    print("\nSame profile with string address and primary_naics:")
    print((address_is_string== naics_is_string).all())

    string_naics = df [df["primary_naics"].apply(type) == str]
    print("\nPrimary NAICS strings:")
    print(string_naics["primary_naics"].head())
    print("\nDo all string primary_naics look like dictionaries?")
    print(string_naics["primary_naics"].str.startswith("{").value_counts())

    

if __name__ == "__main__":
    main()