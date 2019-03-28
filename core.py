#
# core.py
# Core function script file of DetExploit
# Author: MOPI
# Licensed by GPL License
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

def windows(exploitdb_product_dict, jvn_product_dict):
    print('Starting windows platform operation.')
    try:
        import wmi
    except ImportError:
        cprint('Error: Failed to import WMI library.', 'red')
        cprint('Error: Did you run pip install -r requirements.txt?', 'red')
        exit(3)
    wins = wmi.WMI()
    data = {}
    count = 0

    # Get installed application via WMI
    for result in wins.Win32_Product():
        # p.Caption = Application Name
        # p.Version = Application Version
        data[result.Caption] = result.Version
    # Get installed application via Registry HKLM
    # Get installed application via Registry HKLM Wow64
    # Get installed application via Registry HKCU
    bat_result = subprocess.check_output(["get_registryvalue.bat"])
    tmp = bat_result.split('\n')
#    for line in tmp:
#TODO Finish up batch processing function


    # ExploitDB Check
    for key in exploitdb_product_dict:
        name = key
        version = exploitdb_product_dict[key]
        if data[name] == version:
            print('======================================================')
            cprint('<< ALERT :: VULNERABLE APPLICATION DETECTED >>', 'red')
            cprint('<< Application Name: ' + name, 'blue')
            cprint('<< Application Version: ' + version, 'blue')
            cprint('<< Used database: ExploitDB', 'blue')
            print('======================================================')
            count = count + 1
    # JVN Check
    for key in jvn_product_dict:
        name = key
        version = exploitdb_product_dict[key]
        if data[name] == version:
            print('======================================================')
            cprint('<< ALERT :: VULNERABLE APPLICATION DETECTED >>', 'red')
            cprint('<< Application Name: ' + name, 'blue')
            cprint('<< Application Version: ' + version, 'blue')
            cprint('<< Used database: Japan Vulnerability Notes', 'blue')
            print('======================================================')
            count = count + 1
    return count

if __name__ == '__main__':
    print('Error: Please run main.py!!!')

