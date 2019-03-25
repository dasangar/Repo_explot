#
# core.py
# Core function script file of DetExploit
# Author: MOPI
# Licensed by MIT License
#

import subprocess
import winreg
import win32com.client
import wmi


from termcolor import cprint

HKEY_CLASSES_ROOT = 2147483648
HKEY_CURRENT_USER = 2147483649
HKEY_LOCAL_MACHINE = 2147483650
HKEY_USERS = 2147483651
HKEY_CURRENT_CONFIG = 2147483653

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

    # Get installed application via WMI
    for result in wins.Win32_Product():
        # p.Caption = Application Name
        # p.Version = Application Version
        data.append(result.Caption + '/' + result.Version)
    # Get installed application via Registry HKLM
    # Get installed application via Registry HKLM Wow64
    # Get installed application via Registry HKCU
    bat_result = subprocess.check_output(["get_registryvalue.bat"])
    tmp = bat_result.split('\n')
    for line in tmp:
        #

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
    a
    return count

if __name__ == '__main__':
    print('Error: Please run main.py!!!')

