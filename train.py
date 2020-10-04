import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from os import path
from sklearn.model_selection import train_test_split
import pickle

datapath = path.join("data")
modelpath = path.join("models")

dataset=pd.read_csv(path.join(datapath,"parametros.csv"))
dataset=dataset.iloc[:,0:3]

x=dataset.iloc[:,:2].values
y=dataset.iloc[:,-1].values

x_tarin,x_test,y_train,y_test= train_test_split(x,y, test_size=.10)

from sklearn.ensemble import RandomForestClassifier

reg = RandomForestClassifier(n_estimators=100)
reg.fit(x_tarin,y_train)
y_pred=reg.predict(x_test)

filename = 'model.sav'
pickle.dump(reg, open(path.join(modelpath,filename), 'wb'))

#calidad
dataset2=pd.read_csv(path.join(datapath,"calidad.csv"))
dataset2=dataset2.iloc[:,:4]

x2=dataset2.iloc[:,:-1].values
y2=dataset2.iloc[:,-1].values

x_tarin2,x_test2,y_train2,y_test2= train_test_split(x2,y2, test_size=.2)

reg2 = RandomForestClassifier(n_estimators=100)
reg2.fit(x_tarin2,y_train2)
y_pred2=reg2.predict(x_test2)

filename2 = 'model2.sav'
pickle.dump(reg2, open(path.join(modelpath,filename2), 'wb'))
