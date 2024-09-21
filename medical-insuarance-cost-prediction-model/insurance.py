import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Lasso
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn import metrics

insurance_dataset = pd.read_csv('insurance.csv')
print(insurance_dataset.head())
print(insurance_dataset.shape)
print(insurance_dataset.info())

#Categorical Features
#- Sex
#- Smoker
#- Region

def countplot_distribution(column_name, title , data_set):
    plt.figure(figsize=(6,6))
    sns.countplot(x = column_name, data = data_set)
    plt.title(title)
    print(insurance_dataset[column_name].value_counts())
    plt.show()
    
def histplot_distribution(column_name,title):
    plt.figure(figsize=(6,6))
    sns.histplot (insurance_dataset[column_name])
    plt.title(title)
    plt.show()


print(insurance_dataset.isnull().sum())

#data analysis
print(insurance_dataset.describe())

sns.set_theme()

#age distribution
histplot_distribution('age','Age distribution')

#sex distribution
countplot_distribution('region','Region distribution',insurance_dataset)

#BMI distribution
histplot_distribution('bmi','BMI distribution')

#children distribution
countplot_distribution('children','Children distribution',insurance_dataset)

#smoker distribution
countplot_distribution('smoker','Smoker distribution',insurance_dataset)

#region distribution
countplot_distribution('sex','Sex distribution',insurance_dataset)

#charges distribution
histplot_distribution('charges','Charge distribution')


#encoding categorical col
insurance_dataset.replace({'sex':{ 'male': 0 , 'female': 1 }},inplace=True)

#encoding smoker col
insurance_dataset.replace({'smoker':{ 'yes': 0 , 'no': 1 }},inplace=True)

#encoding region col

insurance_dataset.replace({'region':{'southwest': 0, 'southeast': 1, 'northwest': 2, 'northeast': 3}}, inplace=True)