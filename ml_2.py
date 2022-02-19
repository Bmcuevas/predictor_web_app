import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn import datasets, linear_model
import pandas as pd

import pickle
import warnings
warnings.filterwarnings("ignore")

linear_reg = linear_model.LinearRegression()

df_depto_ba_lr =  pd.read_csv('/Users/brunocuevas/Desktop/ana_datos/prueba_python/df_depto_ba_lr.csv', index_col=0)

# Modelo de Regresión lineal
y = df_depto_ba_lr[["price"]]
x = df_depto_ba_lr[["covered_area"]]

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = .2)
linear_reg.fit(x_train, y_train)






pickle.dump(linear_reg, open("model.pkl", "wb"))

model=pickle.load(open('model.pkl','rb'))