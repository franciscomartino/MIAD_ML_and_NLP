#!/usr/bin/python

import pandas as pd
import joblib
import sys
import os
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import RidgeClassifier

def predict_genres(plot):
    
    clf = joblib.load(os.path.dirname(__file__) + '/movies_clf.pkl') 
    
    vect = CountVectorizer()
    d = {'plot': [plot]}
    df = pd.DataFrame(data=d)
    XTest = vect.fit_transform(df)
    

    #cols = ['p_Action', 'p_Adventure', 'p_Animation', 'p_Biography', 'p_Comedy', 'p_Crime', 'p_Documentary', 'p_Drama', 'p_Family',
    #    'p_Fantasy', 'p_Film-Noir', 'p_History', 'p_Horror', 'p_Music', 'p_Musical', 'p_Mystery', 'p_News', 'p_Romance',
    #    'p_Sci-Fi', 'p_Short', 'p_Sport', 'p_Thriller', 'p_War', 'p_Western']

    # Make prediction
    p1 = clf.predict(XTest)
    
    #res = pd.DataFrame(p1, columns=cols)

    return p1


if __name__ == "__main__":
    
    if len(sys.argv) == 1:
        print('Por favor ingrese la sinopsis de la película')
        
    else:

        plot = sys.argv[1]
 

        p1 = predict_genres(plot)
        
        print('Géneros de la película: ', p1)