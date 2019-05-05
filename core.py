#
# core.py
# Core function script file of DetExploit
# Author: MOPI
# Licensed by GPL License
#

from termcolor import cprint

import colorama
import datetime
import subprocess
import winreg
import win32com.client
import wmi

import report

resultdict = {}

def windows(starttime, exploitdb_success, jvn_success, exploitdb_product_dict, jvn_product_dict):
    print('   Starting windows platform operation.')
    try:
        import wmi
    except ImportError:
        cprint('   Error: Failed to import WMI library.', 'red')
        cprint('   Error: Did you run pip install -r requirements.txt?', 'red')
        exit(3)
    wins = wmi.WMI()
    data = {}
    count = 0

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
    # Get installed application via Registry HKLM Wow64
    hkmlwow64_search_result = []
    tmp = subprocess.Popen(r'reg query "HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall" /s', stdout=subprocess.PIPE, shell=True).stdout.readlines()
    for obj in tmp:
        hkml_search_result.append(obj.decode('utf_8', 'ignore'))
    tmp = ''.join(hkml_search_result)
    tmp = tmp.split(r'HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall')
    for app in tmp:
        app_name = ''
        app_version = ''
        for info_line in app:
            if 'DisplayName' in info_line:
                app_name = info_line[30:]
            if 'DisplayVersion' in info_line:
                app_version = info_line[30:]
        data[app_name] = app_version
    # Get installed application via Registry HKCU
    hkcu_search_result = []
    tmp = subprocess.Popen(r'reg query "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Uninstall" /s', stdout=subprocess.PIPE, shell=True).stdout.readlines()
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

    # ExploitDB Check
    for key in exploitdb_product_dict:
        name = key
        version = exploitdb_product_dict[key]
        try:
            tmp = data[name]
        except KeyError:
            continue
        if data[name] == version:
            resultdict[name] = (version, True, False)
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
        version = jvn_product_dict[key]
        try:
            tmp = data[name]
        except KeyError:
            continue
        if data[name] == version:
            if resultdict[name] is not None:
                resultdict[name] = (version, True, True)
            else:
                resultdict[name] = (version, False, True)
            print('======================================================')
            cprint('<< ALERT :: VULNERABLE APPLICATION DETECTED >>', 'red')
            cprint('<< Application Name: ' + name, 'blue')
            cprint('<< Application Version: ' + version, 'blue')
            cprint('<< Used database: Japan Vulnerability Notes', 'blue')
            print('======================================================')
            count = count + 1
    endtime = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    report.gen_report('v0.6-CUI', count, starttime, endtime, exploitdb_success, jvn_success, resultdict)
    return count


if __name__ == '__main__':
    colorama.init()
    print('======================================================')
    cprint('   ERROR: Direct loading of core.py detected', 'red')
    cprint('   ERROR: Please run the following to run DetExploit.', 'red')
    cprint('   ERROR: -> main.py for CUI version', 'red')
    cprint('   ERROR: -> gui.py for GUI version', 'red')
    print('======================================================')

