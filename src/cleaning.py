import pandas as pd
import numpy as np



def clean_meal_plan(data: pd.Series) -> pd.Series:
    data = data.replace("Not Selected", np.nan)
    return data



if __name__ == "__main__":
    
    df = pd.read_csv("~/Desktop/Mlops/Datasets/Hotel_Reservation.csv")["type_of_meal_plan"]
    print(df.value_counts(dropna=False))
    df = clean_meal_plan(df)
    print(df.value_counts(dropna=False))