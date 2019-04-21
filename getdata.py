#
# data.py
# Data processing stage of DetExploit
# Author: MOPI
# Licensed by GPL License
#

import xml.etree.ElementTree as ET
import urllib.request
import os
from tqdm import tqdm

from html.parser import HTMLParser
from termcolor import cprint

EXPLOITDB_FILENAME = 'exploitdb.detexploit'

JVN_FILENAME = 'jvn.detexploit'
JVN_ALLPRODUCT_XML_FILENAME = 'jvn_products.xml'

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
    '''Download raw CSV files from ExploitDB GitHub repo.

    :param None
    :rtype Integer
    '''
    print('   Downloading data from ExploitDB GitHub repo.')
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
    print('   Downloading data from JVN.')
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
    '''Extract windows related exploit from data file.

    :param None
    :rtype ExtractedCSV
    '''
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
    print('Error: Please run main.py!!!')

