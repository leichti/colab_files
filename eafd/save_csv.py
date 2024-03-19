import pandas as pd

df = pd.read_excel("Grain_Size_Distribution_2V.xlsx")
df.columns = ["mesh", "underflow"]
df.to_csv("grain_size_distribution.csv")
