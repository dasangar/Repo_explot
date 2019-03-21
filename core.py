#
# core.py
# Core function script file of DetExploit
# Author: MOPI
# Licensed by MIT License
#

import wmi

from termcolor import cprint


def windows(name_and_version):
    print('Starting windows platform operation.')
    try:
        import wmi
    except ImportError:
        cprint('Error: Failed to import WMI library.', 'red')
        cprint('Error: Did you run pip install -r requirements.txt?', 'red')
        exit(3)
    wins = wmi.WMI()
    data = []
    count = 0
    for result in wins.Win32_Product():
        # Get data of installed application using wmi module.
        # p.Caption = Application Name
        # p.Version = Application Version
        data.append(result.Caption + '/' + result.Version)
    for db_elem in name_and_version:
        for data_elem in data:
            if db_elem == data_elem:
                app_info = db_elem.split('/')
                cprint('======================================================')
                cprint('<< ALERT :: VULNERABLE APPLICATION DETECTED >>', 'red')
                cprint('<< Application Name: ' + app_info[0], 'blue')
                cprint('<< Application Version: ' + app_info[1], 'blue')
                cprint('======================================================')
                count = count + 1
    return count

