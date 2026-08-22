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

    print("\nBusiness model types:")
    print(df['business_model'].apply(type).value_counts())

    print("\nTarget markets types:")
    print(df['target_markets'].apply(type).value_counts())

    print("\nCore offerings types:")
    print(df['core_offerings'].apply(type).value_counts())

    print("\nSecondary NAICS types:")
    print(df['secondary_naics'].apply(type).value_counts())

    secondary_naics_values = df["secondary_naics"].dropna()
    print("\nSecondary NAICS values:")
    print(secondary_naics_values.head())

    print("\nSecondary NAICS keys:")
    for value in secondary_naics_values:
        print(value.keys())

    print ("\nYear founded missing values:")
    print(df['year_founded'].isna().sum())

    years = df['year_founded'].dropna()

    print("\nAre all existing years whole numbers?")
    print((years % 1 == 0).all())

    print("\nEmployee count missing values:")
    print(df['employee_count'].isna().sum())

    employees = df['employee_count'].dropna()

    print("\nAre all existing employee counts whole numbers?")
    print((employees % 1 == 0).all())

    print("\nRevenue missing values:")
    print(df['revenue'].isna().sum())

    revenue = df['revenue'].dropna()

    print("\nAre all existing revenue values whole numbers?")
    print((revenue % 1 == 0).all())
          

if __name__ == "__main__":
    main()