###########################################################
# jvn.py
# File that contains code block related to JVN.
# DetExploit (https://github.com/moppoi5168/DetExploit)
# Licensed by GPL License
###########################################################

from tqdm import tqdm
from html.parser import HTMLParser
from termcolor import cprint

import colorama
import configparser
import urllib.request
import xml.etree.ElementTree as ET

import report

product_dict = {}

cp = configparser.ConfigParser()
cp.read('./config.ini', 'UTF-8')


class html_parser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)


    def handle_starttag(self, tag, attrs):
        if tag == "sec:cpe":
            attrs = dict(attrs)
            if 'product' in attrs and 'version' in attrs:
                product_dict[attrs['product']] = attrs['version']


def download_vulndata():
    year_list = range(int(cp.get('jvn', 'data_from')), int(cp.get('jvn', 'data_to')) + 1)
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


def scan(jvn_product_dict, data):
    count = 0
    resultdict = {}
    for key in jvn_product_dict:
        name = key
        version = jvn_product_dict[key]
        try:
            tmp = data[name]
        except KeyError:
            continue
        if data[name] == version:
            level = report.determine_level('JVN')
            if resultdict[name] is not None:
                resultdict[name] = (version, True, True, False, resultdict[name][4])
            else:
                resultdict[name] = (version, False, True, False, level)
            print('======================================================')
            cprint('   << ALERT :: VULNERABLE APPLICATION DETECTED >>', 'red')
            cprint('   << Application Name: ' + name + ' >>', 'blue')
            cprint('   << Application Version: ' + version + ' >>', 'blue')
            cprint('   << Used database: Japan Vulnerability Notes >>', 'blue')
            cprint('   << Level: ' + level + ' >>', 'blue')
            print('======================================================')
            count = count + 1
    return resultdict, count


if __name__ == '__main__':
    colorama.init()
    print('======================================================')
    cprint('   ERROR: Direct execution of jvn.py detected', 'red')
    cprint('   ERROR: Please run the following to run DetExploit.', 'red')
    cprint('   ERROR: -> main.py for CUI version', 'red')
    cprint('   ERROR: -> gui.py for GUI version', 'red')
    print('======================================================')
