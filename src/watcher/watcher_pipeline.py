# watcher.py


import watchdog.events 
import time
import os
import logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# local imports
from config.extract_statics import get_statics
from cleaner.cleaning_pipeline import DataCleaner

paths_subtree = get_statics("paths")
input_folder_path = paths_subtree["input_folder"]
archive_folder_path = paths_subtree["archive_folder"]
cleaner = DataCleaner()


# this is an inherited class:
class Handler(watchdog.events.PatternMatchingEventHandler):
    def __init__(self):
        watchdog.events.PatternMatchingEventHandler.__init__(
                                    self, patterns=['*.csv'], 
                                    ignore_directories= True,
                                    ignore_patterns= None,
                                    case_sensitive= True
                                    )
    def _on_created(self, event):
        file_path = event.src_path
        logging.info(f"New file detected: {file_path}")
        try:
            cleaned_df = cleaner.clean(file_path)
            cleaner.save_cleaned_file(cleaned_df, file_path)
            logging.info(f"File cleaned and saved in {self.archive_path}")
        except Exception as e:
            logging.error(f"Failed to clean file {event.src_path}: {e}")
        return 0
    
    def _on_deleted(self, event):
        file_path = event.src_path
        try:
            cleaner.delete_file(file_path)
            logging.info(f"File deleted: {file_path}")
        except Exception as e:
            logging.error(f"Failed to delete file {event.src_path}: {e}")

    
    def start_watching(self):
        event_handler = Handler()
        observer = watchdog.observers.Observer()
        observer.schedule(event_handler, input_folder_path, recursive= False)
        observer.start()
        logging.info(f"Started the watcher on the folder{input_folder_path}")

        # The program stops when ctrl+c is pressed in the keyboard
        try:
            while True:
                time.sleep(60)    
        except KeyboardInterrupt:
            observer.stop()
            logging.info("The watcher is stopped")
        observer.join()

    
