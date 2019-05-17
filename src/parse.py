#
# parse.py
# Data parsing stage of DetExploit
# Author: MOPI
# Licensed by GPL License
#

from termcolor import cprint

import colorama

def parse_exploitdb(data_list):
    product_dict = {}
    for data in data_list:
        splitted = data.split(',')
        title = splitted[2]
        base = title.split(' - ')[0][1:]
        baselist = base.split(' ')
        name = ' '.join(baselist[:-1])
        version = baselist[-1]
        product_dict[name] = version
    return product_dict

if __name__ == '__main__':
    colorama.init()
    print('======================================================')
    cprint('   ERROR: Direct execution of parse.py detected', 'red')
    cprint('   ERROR: Please run the following to run DetExploit.', 'red')
    cprint('   ERROR: -> main.py for CUI version', 'red')
    cprint('   ERROR: -> gui.py for GUI version', 'red')
    print('======================================================')
