import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn import metrics

gold_data = pd.read_csv("gold_price_data.csv")
print(gold_data.head())
print(gold_data.tail())
print(gold_data.shape)
print(gold_data.info())

print(gold_data.isnull().sum())
print(gold_data.describe())

correlation = gold_data.corr(
    method='kendall',
    numeric_only=False,
    )

plt.figure(figsize=(8,8))
sns.heatmap(correlation, cbar=True, fmt='.1f',annot=True,annot_kws={'size':8},cmap='Blue')
regressor = RandomForestRegressor(n_estimators=100)
