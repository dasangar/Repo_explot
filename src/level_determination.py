#
# level_determination.py
# Script file of DetExploit that determines how that vulnerability is dangerous
# Author: MOPI
# Licensed by GPL License
#

from termcolor import cprint

import colorama

LEVEL_DANGER = 'DANGER'
LEVEL_WARNING = 'WARNING'
LEVEL_CAUTION = 'CAUTION'


def level_determination(data_src):
    if data_src == 'ExploitDB':
        return LEVEL_DANGER
    elif data_src == 'WinUpdate':
        return LEVEL_WARNING
    elif data_src == 'JVN':
        return LEVEL_CAUTION
    else:
        return 'Error'


if __name__ == '__main__':
    colorama.init()
    print('======================================================')
    cprint('   ERROR: Direct execution of parse.py detected', 'red')
    cprint('   ERROR: Please run the following to run DetExploit.', 'red')
    cprint('   ERROR: -> main.py for CUI version', 'red')
    cprint('   ERROR: -> gui.py for GUI version', 'red')
    print('======================================================')
