# watcher_test.py

from watcher.watcher_pipeline import Handler
from cleaner.cleaning_pipeline import DataCleaner
from data_handling.data_generator import generate_data
import pandas as pd
import logging
import threading
from config.extract_statics import get_statics


paths_subtree = get_statics("paths")
input_folder_path = paths_subtree["input_folder"]


def main_cleaning_test(df_path):
    try:
        df = pd.read_csv(df_path)
        cleaner = DataCleaner()
        cleaned_df = cleaner.clean(df)
        # cleaner.save_cleaned_file(cleaned_df, df_path)
        logging.info("Data cleaned and saved")
    except Exception as e:
        logging.error(f"the error is {e}")
    return 0 


def main_watcher_test():
    try:
        watcher = Handler()
        watcher.start_watcher()
        watcher_thread = threading.Thread(target=watcher.start_watcher, args=(input_folder_path,), daemon=True)
        watcher_thread.start()
        generate_data() #simulating a new data in the input folder
        watcher_thread.join()
    except Exception as e:
        logging.error(f"The error is {e}")
    return 0


if __name__ == "__main__":
    main_watcher_test()