import pandas as pd

def load_and_clean_data(filepath, commodity_name, market_name):
    df = pd.read_csv(filepath)

    # Remove extra spaces from column names
    df.columns = df.columns.str.strip()

    # Filter by commodity and market
    df = df[
        (df["Commodity"] == commodity_name) &
        (df["Market"] == market_name)
    ]

    # Keep only required columns
    df = df[["Arrival_Date", "Modal_Price"]]

    # Convert date column
    df["Arrival_Date"] = pd.to_datetime(df["Arrival_Date"], dayfirst=True)


    # Drop missing values
    df = df.dropna()

    # Rename for Prophet
    df = df.rename(columns={
        "Arrival_Date": "ds",
        "Modal_Price": "y"
    })

    # Sort by date
    df = df.sort_values("ds")

    return df
