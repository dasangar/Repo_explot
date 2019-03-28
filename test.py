#
# test.py
# Test script of DetExploit (not needed to run)
# Author: MOPI
# Licensed by MIT License
#

import urllib.request
import os

from html.parser import HTMLParser

product_dict = {}


class html_parser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)


    def handle_starttag(self, tag, attrs):
        if tag == "sec:cpe":
            attrs = dict(attrs)
            if 'product' in attrs and 'version' in attrs:
                product_dict[attrs['product']] = attrs['version']


def main():
    get_all_vulnerability()


def get_all_vulnerability():
    year_list = range(1998, 2020)
    month_list = range(1, 13)
    for year in year_list:
        for month in month_list:
            url = 'https://jvndb.jvn.jp/myjvn?method=getVulnOverviewList&feed=hnd&rangeDatePublished=n&rangeDateFirstPublished=n&datePublicStartY=' + str(year) + '&datePublicStartM=' + str(month) + '&datePublicEmdY=' + str(year) + '&datePublicEmdM=' + str(month)
            mem = urllib.request.urlopen(url).read().decode()
            tmp = mem.split('\n')
            parser = html_parser()
            for line in tmp:
                if '<sec:cpe' in line:
                    parser.feed(line)
    parser.close()
    return product_dict

main()

