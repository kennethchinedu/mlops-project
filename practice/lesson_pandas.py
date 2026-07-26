import pandas as pd


df = pd.read_csv("~/Desktop/Mlops/Datasets/Hotel_Reservation.csv")
df.info()
print(df.isnull().sum())
print(df.shape)