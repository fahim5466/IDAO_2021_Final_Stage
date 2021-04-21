import pathlib as path

import numpy as np
import pandas as pd

def make_map(col):

    values = col.unique()
    mp = {}
    for i, value in enumerate(values):
        mp[value] = i
    #print(mp)
    return mp

def mappify(df):
    df.replace(np.nan, 'nan')
    return df.map(make_map(df)).to_numpy()

def split(x):
    
    ind = int(len(x)*.75)

    train = x[:ind]
    val = x[ind:]
    
    return train, val