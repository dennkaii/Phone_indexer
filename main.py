# ~/.kaggle/kaggle.json

import pandas as pd
import numpy as np
import kaggle

kaggle.api.authenticate()
kaggle.api.dataset_download_files("amansingh0000000/smartphones", path=".", unzip=True)


# read donwloaded csv

df = pd.read_csv("./mobile_phones_2000.csv")
df.head()
