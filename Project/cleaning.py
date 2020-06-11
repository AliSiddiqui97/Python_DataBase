def print_col_name(df):
    cols = df.columns
    return cols

def print_col_name_type(df):
    dtype = df.dtypes
    return dtype
def print_shape(df):
    shape = df.shape
    return shape
def print_info(df):
    return df.info(verbose=True)
def print_describe(df):
    return df.describe()
def convert_type(df,name,typeToBe):
    try:
        df[name] = df[name].astype(typeToBe)
        

    except:
        print('Cant convert to given type')
def get_params(df, listOfCond):
    
    for i in listOfCond:
        print(i)

import pandas as pd
import pyodbc 
import numpy as np
import sys

df = pd.read_csv('csv.csv')
listOfCond=[]

listOfCond.append({'col_name':'TV' , 'cond': '>40'})

listOfCond.append({'col_name':'radio' , 'cond': '>3'})
get_params(df, listOfCond)

# print(df.dtypes)

# convert_type(df,'TV','int')
# print(df.dtypes)
# print(print_describe(df))
# print(print_col_name_type(df))
# print(print_shape(df))
# print(print_info(df))