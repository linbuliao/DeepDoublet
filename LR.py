import os
import random
import statsmodels.api as sm
import pylab as pl
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV, cross_validate
from sklearn.ensemble import GradientBoostingClassifier, GradientBoostingRegressor, RandomForestClassifier
from sklearn import metrics, svm, preprocessing
from pandas import DataFrame
import sklearn
from sklearn.model_selection import train_test_split, KFold
from IPython.display import SVG
import time
from sklearn.linear_model import LogisticRegression
import gc
import pickle
import joblib

def load_data(root = '', MetaFile = 'ADoub_meta.csv', ADoubFile = 'ADoub.npy'):

    ADoub_meta = pd.read_csv(root + MetaFile)
    X = np.load(root + ADoubFile)
    
    return X, ADoub_meta

def gen_label(Y_raw):
    
    Y_raw = Y_raw.astype(int)
    Y = np.zeros((Y_raw.shape[0], Y_raw.max() + 1))
    for i, idx in enumerate(Y_raw):
        Y[i, idx] = 1
        
    return Y

#################################
############Load Data############
#################################
file_root = 'ADoub_new/'
save_root = 'DecompModel/'

if not os.path.exists(save_root):
    os.makedirs(save_root)
    
X, ADoub_meta = load_data(file_root, 'ADoub_meta.csv', 'ADoub.npy')

Y1_raw = ADoub_meta.iloc[:, 0].values.squeeze().astype(int)
Y2_raw = ADoub_meta.iloc[:, 2].values.squeeze().astype(int)

print(Y1_raw.shape)
print(Y2_raw.shape)
print(X.shape)
print(X.sum(axis = 1))

kf = KFold(n_splits=5, random_state = 0, shuffle = True)
cv_index = kf.split(X)

Accuracy = []

i = 0

for cv_train, cv_test in cv_index:
    
    i += 1
    print(i)
    print('c1:')

    sta = time.time()    

    clf = LogisticRegression(n_jobs = 16).fit(X = X[cv_train, :],
                                              y = Y1_raw[cv_train])
    
    end = time.time()
    dura = (end - sta)/3600
    print(dura, 'h(s)')
    
    joblib.dump(clf, save_root + 'LR_hep_' + str(i) + '.sav')

    test_pred_c1 = clf.predict(X[cv_test, :])

    t1 = test_pred_c1 == Y1_raw[cv_test]
    c1_accuracy = t1.sum() / test_pred_c1.shape[0]
    
    print('c2:')

    sta = time.time()

    clf = LogisticRegression(n_jobs = 16).fit(X = X[cv_train, :],
                                              y = Y2_raw[cv_train])
    
    end = time.time()
    dura = (end - sta)/3600
    print(dura, 'h(s)')

    joblib.dump(clf, save_root + 'LR_LEC_' + str(i) + '.sav')

    test_pred_c2 = clf.predict(X[cv_test, :])

    t2 = test_pred_c2 == Y2_raw[cv_test]
    c2_accuracy = t2.sum() / test_pred_c2.shape[0]
    
    c12_accuracy = np.sum(t1&t2) / test_pred_c2.shape[0]
    
    print([c1_accuracy, c2_accuracy, c12_accuracy])
    Accuracy.append([c1_accuracy, c2_accuracy, c12_accuracy])

print(np.mean(Accuracy, axis = 0))

