import os
from cleaner import main_cleaner
import time

input_folder_path = "../input_folder/"
seen = set()

def is_new():
    global seen 
    input_files = os.listdir(input_folder_path)# returns a list of the files in that folder
    for file in input_files:
        if file not in seen:
            seen.add(file)
            main_cleaner(file)
    return 0

def watcher():
    while(1):
        is_new()
        time.sleep(10*60)
    return 0

if __name__=="__main__":
    watcher()    
