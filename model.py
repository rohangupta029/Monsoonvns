#%matplotlib inline
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import pickle 
names=["Temp[C]","PH","pH[mV]","ORP[mV]","EC[muS per cm]","EC Abs.[muS per cm]","RES[Ohm-cm]","TDS[ppm]","Sal.[psu]","Sigma T","Press[psi]","D.O.[percent]","D.O.[ppm]","Turb[FNU]","GPS Lat.","GPS Long."
]
Monsoondata=pd.read_csv("Monsoonvns.csv",names=names)
x = Monsoondata.iloc[:,[1,7,12]].values
y = Monsoondata.iloc[:, 0].values
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.30,random_state=0)
from sklearn.linear_model import LinearRegression 
regr = LinearRegression() 
  
regr.fit(x_train, y_train) 
# Saving model to disk
pickle.dump(regr, open('model.pkl','wb'))

# Loading model to compare the results
model = pickle.load(open('model.pkl','rb'))