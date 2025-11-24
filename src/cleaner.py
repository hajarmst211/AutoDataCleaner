#cleaner.py

import pandas as pd 
import datetime
import numpy as np

threshold = 0.8

def load_data(path):
    return pd.read_csv(path)

def drop_duplicated(df):
    df_copy = df.copy
    return df_copy.drop_duplicates(inplace = True)

def strip_columns(df):
    df_copy = df.copy()
    for column in df_copy.select_dtypes(include = ["object"]).columns():
        df_copy[column] = df_copy[column].astype(str).str.strip()
    return df_copy

def transform_dates(df):
    df_copy = df.copy
    for column in df_copy.columns():
        if isinstance(column, datetime):
            df_copy[column] = pd.to_datetime(column, errors="coerce")
    return df_copy

def drop_column(df_copy, column):
        number_of_nulls = sum(column.isnan())
        length_of_column = np.len(np.array(column)) 
        nulls_ratio = number_of_nulls / length_of_column
        if nulls_ratio > threshold:
            df_copy = df_copy.drop_columns(column)
        
        return df_copy
    
def handle_missing_values(df):
    df_copy = df.copy
    
    for column in df_copy.columns():
        df_copy = drop_column(df_copy, column)
        bool_series = pd.isnull(df_copy[column])
        if column.isdigit():
            mean = np.mean(np.array(column))
            df_copy[column].fillna(mean, inplace = True) 
        else: 
            df_copy[column].fillna(df_copy[column].mode().iloc[0], inplace = True) 
    return df_copy

def main_cleaner(path):
    df= load_data(path)
    df= drop_duplicated(df)
    df= strip_columns(df)
    df= transform_dates(df)
    df= drop_column(df)
    df= handle_missing_values(df)
    
    return df