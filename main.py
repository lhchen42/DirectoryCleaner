import os
import sys
import shutil
from config import *
from time import time
from datetime import datetime

import logging

logging.basicConfig(filename="debug.log")

def remove(target_dir: str):
    if os.path.isdir(target_dir):
        shutil.rmtree(target_dir)
    else:
        os.remove(target_dir)

def main():
    print("ROOT: {}".format(ROOT))
    print("SITES: {}".format(SITES))
    try:
        if not ROOT or not SITES:
            raise ValueError("ROOT and SITES is not configured")

        for site in SITES:
            site_path = os.path.join(ROOT, site)
            # loop through dir in the site directory        
            dirs = os.listdir(site_path)
            for dir in dirs:
                target_dir = os.path.join(site_path, dir)
                sys.stdout.write("Remove {}".format(target_dir))
                # remove directory or file
                remove(target_dir)
                sys.stdout.flush()
                sys.stdout.write("\r" + "Remove {} ........... Done!\n".format(target_dir))
    except Exception as e:
        now = datetime.now()
        logging.error("[{}]::Error on removing directory: {}".format(now.strftime("%m-%d-%y %H:%M:%S"), e))


if __name__ == "__main__":
    main()