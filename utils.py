import os
import glob
import json


def get_result_files(root_dir):
    if os.path.isdir(root_dir) == False:
        print("[ERROR] Directory '{}' does NOT exist".format(root_dir))
        exit(1)

    # match number only
    files = glob.glob(root_dir + "/*.txt")

    return files


def load_json(file):
    data = None

    with open(file, "r") as fin:
        data = json.load(fin)
    
    return data