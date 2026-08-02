from dataclasses import dataclass
import pandas as pd

@dataclass
class ColumnConfig:
    column: str
    strategy: str 


avg_price_per_room = ColumnConfig(
    column="avg_price_per_room",
    strategy="median"
)

market_segment_type = ColumnConfig(
    column="market_segment_type",
    strategy="mode"
)

arrival_year = ColumnConfig(
    column="arrival_year",
    strategy="mode"
)

def fill_missing(df, config):
    col = df[config.column]

    if config.strategy == "median":
        value = col.median()
    else:  # mode
        value = col.mode().iloc[0]

    df[config.column] = col.fillna(value)
    return df

if __name__ == "__main__":
    columns = ["avg_price_per_room", "market_segment_type", "arrival_year"]
    df = pd.read_csv("~/Desktop/Mlops/Datasets/Hotel_Reservation.csv")[columns]
    print(df.isnull().sum())
    fill_missing(df, avg_price_per_room)
    fill_missing(df, market_segment_type)
    fill_missing(df, arrival_year)
    print(df.isnull().sum())
