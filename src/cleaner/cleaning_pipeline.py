# cleaning_pipeline.py

import os

# local imports
from config.extract_statics import get_statics
from .cleaner import (
    drop_duplicates,
    strip_columns,
    transform_dates,
    drop_column_if_too_many_nulls,
    handle_missing_values,
    delete_cleaned_file
)

archive_folder_path = get_statics("paths")["archive_folder"]

class DataCleaner:
    def __init__(self):
        self.self = self

    def clean(self, df):
        df = drop_duplicates(df)
        df = strip_columns(df)
        df = transform_dates(df)
        df = drop_column_if_too_many_nulls(df)
        df = handle_missing_values(df)
        return df
    
    def save_cleaned_file(self, df, path):
        file_name = os.path.splitext(os.path.basename(path))[0]
        df.to_csv(archive_folder_path + file_name + "_cleaned.csv")


    def delete_file(self, path):
        delete_cleaned_file(path)