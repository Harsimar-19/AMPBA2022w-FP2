from joblib import load
import pandas as pd
import pickle

def FetchModel():
    b = ''
    with open('./InputData.pickle', 'rb') as handle:
        b = pickle.load(handle)
    #return load("C:\\Users\\harsi\\OneDrive - Indian School of Business\\AMPBA\\Term5\\FP-2\\AMPBA2022w-FP2\\InputData.pkl")
    return b