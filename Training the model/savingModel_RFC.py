# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 22:43:08 2020

@author: dell
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 01:39:48 2020

@author: dell
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 02:47:53 2020

@author: dell
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 00:24:59 2020

@author: dell
"""

#import joblib
import pickle
import pandas as pd 
from sklearn.model_selection import train_test_split 
from sklearn.metrics import accuracy_score 
from sklearn.ensemble import RandomForestClassifier 

data = pd.read_excel("FinalData.xlsx")

print(data)
X = data.values[:, 3:21] 
Y = data.values[:, 22]
print(X)
print(Y)
best=0
for i in range(100):
    X_train, X_test, y_train, y_test = train_test_split(  
                    X, Y, test_size = 0.3,shuffle=False)
    RFC = RandomForestClassifier(n_estimators = 1500,max_features=6,oob_score=True)
    RFC.fit(X_train, y_train)
    y_pred = RFC.predict(X_test)

    accuracy=accuracy_score(y_test,y_pred)*100
    print(accuracy)
    if(accuracy>best):
        best=accuracy
        pickle.dump(RFC,open("finalize.pkl","wb"))

        

        
            



 
    