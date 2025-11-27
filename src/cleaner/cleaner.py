# cleaner.py

import pandas as pd
import os
from datetime import date
from pandas.api.types import is_numeric_dtype
from config.extract_statics import get_statics

threshold = get_statics("thresholds")["date_threshold"]
archive_folder_path = get_statics("paths")["archive_folder"]


def load_data(path):
    return pd.read_csv(path)


def drop_duplicated(df):
    df_copy = df.copy()
    return df_copy.drop_duplicates()


def strip_columns(df):
    df_copy = df.copy()
    df_copy.columns = df_copy.columns.str.strip()
    return df_copy


def transform_dates(df):
    df_copy = df.copy()
    for column in df_copy.columns:
        if df_copy[column].dtype == "object":
            converted = pd.to_datetime(df_copy[column], errors="coerce")
            valid_ratio = converted.notna().mean()
            if valid_ratio >= threshold:
                df_copy[column] = converted

    return df_copy


def drop_column_if_too_many_nulls(df, threshold=0.6):
    df_copy = df.copy()
    columns = df_copy.columns
    for column in columns:
        column_series = df_copy[column]
        number_of_nulls = column_series.isna().sum()
        length = len(column_series)
        nulls_ratio = number_of_nulls / length
        if nulls_ratio > threshold:
            df_copy = df_copy.drop(columns=[column])

    return df_copy


def handle_missing_values(df):
    df_copy = df.copy()
    columns = list(df_copy.columns)
    for column in columns:

        if is_numeric_dtype(df_copy[column]):
            mean = df_copy[column].mean()
            df_copy[column].fillna(mean, inplace=True)
        else:
            mode_series = df_copy[column].mode()
            if not mode_series.empty:
                df_copy[column].fillna(mode_series.iloc[0], inplace=True)
            else:
                df_copy[column].fillna("Unknown", inplace=True)

    return df_copy


def delete_cleaned_file(file_path):
    raw_file_name = os.path.splitext(os.path.basename(file_path))[0]
    cleaned_file_path = archive_folder_path + raw_file_name + "_cleaned.csv"
    os.remove(cleaned_file_path)

    return 0


def main_cleaner(path):
    df = load_data(path)
    df = drop_duplicated(df)
    df = strip_columns(df)
    df = transform_dates(df)
    df = drop_column_if_too_many_nulls(df)
    df = handle_missing_values(df)
    file_name = os.path.splitext(os.path.basename(path))[0]
    df.to_csv(archive_folder_path + file_name + "_cleaned.csv")
    return 0

