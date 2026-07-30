import pandas as pd
import numpy as np
import logging

logger = logging.getLogger(__name__)



def data_summary(data):
    logging.basicConfig(level=logging.INFO)
    logger.info('Started')

def clean_meal_plan(data: pd.Series) -> pd.Series:
    data = data.replace("Not Selected", np.nan)
    return data


def drop_rare_meal_plan(data: pd.Series) -> pd.Series:
    loaded_data = data
    logger.info(f'Shape of dataset before cleaning is {loaded_data.shape} and row {len(loaded_data)}')
    data = loaded_data[data != "Meal Plan 3"]
    logger.warning(f'Shape of data after cleaning is {data.shape} and row {len(data)}, a total of {len(loaded_data) - len(data) } was removed')
    

    return data
    


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    df = pd.read_csv("~/Desktop/Mlops/Datasets/Hotel_Reservation.csv")["type_of_meal_plan"]
    # print(df.value_counts(dropna=False))
    df = drop_rare_meal_plan(df)
    # print(df)
    # df = clean_meal_plan(df)
    # print(df.value_counts(dropna=False))