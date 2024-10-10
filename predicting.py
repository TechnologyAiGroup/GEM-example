import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV,cross_validate
from sklearn import metrics
from sklearn.metrics import f1_score
import joblib
import os,time


begin = 1
end = 1+500
chip_num = end-begin
name = "boom_div"
fault_type = "msl7"
common_path = f'../test2/{name}/{fault_type}/train_and_test/'
model = "hgb"
val = 74

rf0 = joblib.load(f'{name}/{model}.model')

real=0
cand=0

start_time = time.time()

for i in range(begin,end) :
    csv_path=common_path+str(i)+".csv"
    if os.path.exists(csv_path) : 
        test = pd.read_csv(csv_path)
        
        target='y'
        fault_col = 'fault'
        x_columns = [x for x in test.columns if x not in [target, fault_col]]
        X = test[x_columns]
        y = test['y']
        faults = test[fault_col]

        poss=[]
        poss=rf0.predict_proba(X)
        y_pred=[]

        for j in poss : 
            if j[1]*100>=val :
                y_pred.append(1)
            else :
                y_pred.append(0)

        res = []
        for k in range(0,len(y_pred)) :
            if y_pred[k]==1 :
                res.append(faults[k])
                cand+=1
            if y_pred[k]==1 and y[k]==1 :
                real+=1
            
        
        pred_res=common_path+str(i)+".res"
        print(pred_res)
        
        with open(pred_res,'w') as out :
            for s in res :
                out.write(s+"\n")

print(real/chip_num,cand/chip_num)

end_time = time.time()
print("avg time : ",end_time-start_time,"s")