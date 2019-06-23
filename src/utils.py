###########################################################
# utils.py
# Utility script file of DetExploit.
# DetExploit (https://github.com/moppoi5168/DetExploit)
# Licensed by GPL License
###########################################################

import configparser
import os


def config_test():
    cp = configparser.ConfigParser()
    cp.read('../config.ini', 'UTF-8')
    exploitdb_filename = cp.get('exploitdb', 'vulndata_filename')
    try:
        with open(exploitdb_filename, 'w') as tf:
            tf.write('Hello, World.')
        os.path.isfile(exploitdb_filename)
        os.remove(exploitdb_filename)
    except:
        print('Error: Cannnot generate ExploitDB vulnerability data file.')
        print('Error: Check filename in config.ini')
        exit(1)
    
