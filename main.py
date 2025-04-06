from ast import Global
from numpy.ma import maximum_fill_value
import pandas as pd
import numpy as np
import kaggle
from pandas.core.tools.numeric import is_decimal

# Downloads dataset
# kaggle.api.authenticate()
# kaggle.api.dataset_download_files("amansingh0000000/smartphones", path=".", unzip=True)


# read donwloaded csv

df = pd.read_csv("./mobile_phones_2000.csv")


# ask for user what to type a price range
def get_price_range():
    ma_val = int(input("insert max price: ")) or int("1000")
    mi_val = int(input("insert min price: ")) or int("200")

    return ma_val, mi_val


max_val, min_val = get_price_range()

# compares prices and shows between the price range
df_try = df.query(f"{max_val} >= `Price (USD)` > {min_val}")


def ask_refresh_rate():
    rr = int(
        input(
            "insert one of the following available Refresh rates:\n 1.90\n 2.90\n 3.120\n 4.140\n 5.165\n"
        )
    )

    return rr


refresh_rate = ask_refresh_rate()

cont_df = df_try.query(f"{refresh_rate} == `Refresh Rate (Hz)`")

print("test \n")
print(cont_df)
