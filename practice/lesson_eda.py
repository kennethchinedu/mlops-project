import pandas as pd
df = pd.read_csv("~/Desktop/Mlops/Datasets/Hotel_Reservation.csv")

print(df["booking_status"].value_counts())
print(df["type_of_meal_plan"].value_counts())
print(df["lead_time"].value_counts())
print(df["booking_status"].describe())
print(df["no_of_week_nights"].describe())
print(df["market_segment_type"].value_counts())
print("---------------")
print(df["market_segment_type"].value_counts(dropna=False))