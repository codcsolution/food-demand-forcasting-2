import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import gc
import catboost as cb
from sklearn.metrics import mean_squared_log_error, mean_squared_error
from sklearn.model_selection import train_test_split, KFold

import gc
import catboost as cb
from sklearn.metrics import mean_squared_log_error, mean_squared_error
from sklearn.model_selection import train_test_split, KFold

import os

def show_all(df, nrow, ncol):
    with pd.option_context('display.max_rows', nrow, 'display.max_columns', ncol):
        display(df)

os.chdir(r"C:\Users\user\Desktop\fdf")
fci_df = pd.read_csv("fulfilment_center_info.csv")
mi_df = pd.read_csv("meal_info.csv")
train_df = pd.read_csv(f"train.csv")
test_df = pd.read_csv("food_Demand_test.csv")

fci_df.head()
