# extract_statics.py

import yaml


# this function will return a dictionary-like element, you can access the information you want then
def get_statics(subtree):
    with open("src/config/statics.yaml") as f:
        cfg = yaml.safe_load(f)

    section = cfg[subtree]
    return section
