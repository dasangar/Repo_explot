#
# test.py
# Test script of DetExploit (not needed to run)
# Author: MOPI
# Licensed by GPL License
#

import subprocess
import win32com.client
import winreg
import wmi


def main():
    wins = wmi.WMI()
    data = {}
    # Get installed application via WMI
    for result in wins.Win32_Product():
        data[result.Caption] = result.Version
    # Get installed application via Registry HKLM
    hkml_search_result = []
    tmp = subprocess.Popen(r'reg query "HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Uninstall" /s', stdout=subprocess.PIPE, shell=True).stdout.readlines()
    for obj in tmp:
        hkml_search_result.append(obj.decode('utf_8', 'ignore'))
    tmp = ''.join(hkml_search_result)
    tmp = tmp.split(r'HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Uninstall')
    for app in tmp:
        app_name = ''
        app_version = ''
        for info_line in app:
            if 'DisplayName' in info_line:
                app_name = info_line[30:]
            if 'DisplayVersion' in info_line:
                app_version = info_line[30:]
        data[app_name] = app_version
    print(data)


main()

