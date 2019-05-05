#
# data.py
# Data processing stage of DetExploit
# Author: MOPI
# Licensed by GPL License
#

from tqdm import tqdm
from html.parser import HTMLParser
from termcolor import cprint

import colorama
import os
import urllib.request
import xml.etree.ElementTree as ET

EXPLOITDB_FILENAME = 'exploitdb.detexploit'

product_dict = {}


class html_parser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)


    def handle_starttag(self, tag, attrs):
        if tag == "sec:cpe":
            attrs = dict(attrs)
            if 'product' in attrs and 'version' in attrs:
                product_dict[attrs['product']] = attrs['version']


def get_exploitdb():
    print('   Downloading vulnerability data from ExploitDB GitHub repo.')
    print('   (Saved as: ' + EXPLOITDB_FILENAME + ')')
    url = 'https://github.com/offensive-security/exploitdb/raw/master/files_exploits.csv'
    mem = urllib.request.urlopen(url).read()
    with open(EXPLOITDB_FILENAME, mode='wb') as f:
        f.write(mem)
    if os.path.isfile(EXPLOITDB_FILENAME):
        cprint('   Download complete.', 'green')
        print('===========================================================')
        return 0
    else:
        cprint('   Error: Download failed.', 'red')
        exit(1)


def get_all_vulnerability():
    # Experimentary letting DetExploit to download data from 2010
    year_list = range(2010, 2020)
    month_list = range(1, 13)
    print('   Downloading vulnerability data from JVN.')
    print('   This may need a long time to process.')
    print('   Do not exit the program.\n')
    for year in year_list:
        for month in tqdm(month_list, desc=str(year)):
            url = 'https://jvndb.jvn.jp/myjvn?method=getVulnOverviewList&feed=hnd&rangeDatePublished=n&rangeDateFirstPublished=n&datePublicStartY=' + str(year) + '&datePublicStartM=' + str(month) + '&datePublicEmdY=' + str(year) + '&datePublicEmdM=' + str(month)
            mem = urllib.request.urlopen(url).read().decode()
            tmp = mem.split('\n')
            parser = html_parser()
            for line in tmp:
                if '<sec:cpe' in line:
                    parser.feed(line)
    cprint('\n   Download complete.', 'green')
    print('===========================================================')
    parser.close()
    return product_dict


def get_windows_exploit():
    print('   Extracting Windows platform exploit from ' + EXPLOITDB_FILENAME + '......')
    tmp = []
    with open(EXPLOITDB_FILENAME, encoding="utf-8_sig") as wc:
        line = wc.readline()
        while line:
            if 'windows' in line:
                tmp.append(line)
            line = wc.readline()
    cprint('   Extracted successfully.', 'green')
    print('===========================================================')
    return tmp


if __name__ == '__main__':
    colorama.init()
    print('======================================================')
    cprint('   ERROR: Direct execution of getdata.py detected', 'red')
    cprint('   ERROR: Please run the following to run DetExploit.', 'red')
    cprint('   ERROR: -> main.py for CUI version', 'red')
    cprint('   ERROR: -> gui.py for GUI version', 'red')
    print('======================================================')
