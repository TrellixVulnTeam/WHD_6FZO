import pickle
from os import path
import joblib
import numpy as np

datapath=path.join("data")
modelpath = path.join("models")

model1 = 'model.sav'
model2= 'model2.sav'

# with open(path.join(datapath,"sleep.txt"), "r") as f:
#     y_test=f.readlines()
loaded_model1 = joblib.load(path.join(modelpath,model1))

def main(y_test):
    y=[]
    for i in y_test:
        i =  ','.join(str(i)) 
        i=i.split(",")
        for ix in i[1:3]:
            y.append(ix)

    y=np.array(y)
    y=y.reshape(int(len(y)/2),2)
    result = loaded_model1.predict(y)
    # sccore = loaded_model1.score(y,result)
    l=0
    p=0

    for i in result:
        if i==0:
            l=l+1   
        else:
            p=p+1
            
    sp=(p*100)/len(result)
    sl=(l*100)/len(result)
    horas=int(len(result))/2

    y2=[horas,sp,sl]

    y2=np.array(y2)
    y2=y2.reshape(int(len(y2)/3),3)

    loaded_model2 = joblib.load(path.join(modelpath,model2))
    result2= loaded_model2.predict(y2)
    return result2