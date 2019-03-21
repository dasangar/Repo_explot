#
# data.py
# Data processing stage of DetExploit
# Author: MOPI
# Licensed by MIT License
#

import urllib.request
import os

from termcolor import cprint

WHOLE_CSV_FILENAME = 'whole.csv'


def get_whole_csv():
    '''Download raw CSV files from ExploitDB GitHub repo.

    :param None
    :rtype Integer
    '''
    print('Downloading whole CSV from ExploitDB GitHub repo.')
    print('(Saved as: ' + WHOLE_CSV_FILENAME + ')')
    url = 'https://github.com/offensive-security/exploitdb/raw/master/files_exploits.csv'
    filename = WHOLE_CSV_FILENAME
    mem = urllib.request.urlopen(url).read()
    with open(filename, mode='wb') as f:
        f.write(mem)
    if os.path.isfile(filename):
        cprint('Download complete.', 'green')
        print('==============================================')
        return 0
    else:
        cprint('Error: Download failed.', 'red')
        exit(1)


def extract_windows_exploit():
    '''Extract windows related exploit from raw CSV.

    :param None
    :rtype ExtractedCSV
    '''
    print('Extracting Windows platform exploit from whole CSV......')
    tmp = []
    with open(WHOLE_CSV_FILENAME, encoding="utf-8_sig") as wc:
        line = wc.readline()
        while line:
            if 'windows' in line:
                tmp.append(line)
            line = wc.readline()
    cprint('Extracted successfully.', 'green')
    print('==============================================')
    return tmp


def parse_title(line):
    tmp = ' '.split(title)


if __name__ == '__main__':
    print('ERROR: Please run main.py!!!')
