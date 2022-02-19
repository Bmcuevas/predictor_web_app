import numpy as np
import pandas as pd

import pickle
import warnings
warnings.filterwarnings("ignore")

from sklearn.ensemble import RandomForestRegressor

rf=RandomForestRegressor(max_depth=20, random_state=0, n_estimators=100)

df =  pd.read_csv('/Users/brunocuevas/Desktop/ana_datos/prueba_python/df.csv', index_col=0)

# Modelo de Regresión lineal
y = df[["price"]]
x = df.drop(columns=["price"])

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = .2)

rf.fit(x_train,y_train)


pickle.dump(rf, open("model.pkl", "wb"))

model=pickle.load(open('model.pkl','rb'))