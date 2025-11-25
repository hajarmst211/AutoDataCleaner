# watcher.py

from cleaner import main_cleaner
from watchdog.observers import Observer 
import watchdog.events 
import time
import os

input_folder_path = "../input_folder/"
archive_folder_path = "../archive_folder/"

def delete_cleaned_file(file_path):
    raw_file_name = os.path.splitext(os.path.basename(file_path))[0]
    cleaned_file_path = archive_folder_path + raw_file_name + "_cleaned.csv"
    try:
        os.remove(cleaned_file_path)
    except OSError as error:
        print(error)
        print("File path can not be removed")
        
    return 0

# this is an inherited class:
class Handler(watchdog.events.PatternMatchingEventHandler):
    def __init__(self):
        watchdog.events.PatternMatchingEventHandler.__init__(
                                    self, patterns=['*.csv'], 
                                    ignore_directories= True,
                                    ignore_patterns= None,
                                    case_sensitive= True
                                    )
    def on_created(self, event):
        file_path = event.src_path
        main_cleaner(file_path)
        print(f"A new file is appended to {input_folder_path}\n")
        print(f"The file {file_path} is cleaned and the cleaned version is saved in {archive_folder_path}\n")
        return 0
    
    def on_deleted(self, event):
        file_path = event.src_path
        delete_cleaned_file(file_path)
        print(f"File '{file_path}' located at '{event.src_path}' was deleted and archived to '{archive_folder_path}'\n")

        return 0

def watch_input_folder():
    event_handler = Handler()
    observer = watchdog.observers.Observer()
    observer.schedule(event_handler, input_folder_path, recursive= False)
    observer.start()
    # throwing an exception to stop the program when ctrl+c is pressed in the keyboard
    try:
        while True:
            time.sleep(60)    
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
    return 0

if __name__ == "__main__":
    watch_input_folder()