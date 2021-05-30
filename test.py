import sklearn
from sklearn.ensemble import RandomForestClassifier
import pickle
import os
import pandas as pd
import time

#model_path = '/cnvrg/output/frt_model_random_forest.sav'
#model_path = '/output/frt_model_random_forest.sav'
os.sleep(10000)
model_path = '/cnvrg/output/frt_model_random_forest.sav'
model = pickle.load(open(model_path, 'rb'))

def predict(created_hr,day_of_week,epoch,category,other = None):
    
    data = [[created_hr,day_of_week,epoch,category]]
    df = pd.DataFrame(data, columns = ['created_hr','day_of_week','epoch','category'])
    rfc_predict = model.predict(df)
    out = 'Your ticket is on its way. We will be in touch with you within ' + re.findall(r'\d+', rfc_predict[0])[-1] + ' hours.'
#    print(out)
    return out  
