import os
import sys
import shutil
from config import *

import logging

logging.basicConfig(filename="debug.log")
# sites
# tvmarkets, latam, tvglobal, tvforex

def remove(target_dir: str):
    if os.path.isdir(target_dir):
        shutil.rmtree(target_dir)
    else:
        os.remove(target_dir)

def main():
    print("ROOT: {}".format(ROOT))
    print("SITES: {}".format(SITES))
    try:
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
        logging.error("Error on removing directory: {}".format(e))


if __name__ == "__main__":
    main()