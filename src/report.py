###########################################################
# report.py
# File that contains code block related to scan report.
# DetExploit (https://github.com/moppoi5168/DetExploit)
# Licensed by GPL License
###########################################################

from termcolor import cprint

import colorama
import os
import socket
import webbrowser

LEVEL_DANGER = 'DANGER'
LEVEL_WARNING = 'WARNING'
LEVEL_CAUTION = 'CAUTION'


def determine_level(data_src):
    if data_src == 'ExploitDB':
        return LEVEL_DANGER
    elif data_src == 'WinUpdate':
        return LEVEL_WARNING
    elif data_src == 'JVN':
        return LEVEL_CAUTION
    else:
        return 'Error'


def generate_report(platform, detect_num, starttime, endtime, exploitdb_success, jvn_success, resultdict):
    with open(file='../resources/template.html', encoding="utf-8") as base:
        BASE = base.read()
    hostname = socket.gethostname() 
    if exploitdb_success == True:
        exploitdb = 'Success'
    else:
        exploitdb = 'Failed or not runned'
    if jvn_success == True:
        jvn = 'Success'
    else:
        jvn = 'Failed or not runned'
    row = ''
    for detected in resultdict:
        tmp = resultdict[detected]
        app_name = detected
        app_version = tmp[0]
        if tmp[1] is True:
            detect_using_exploitdb = '〇'
            attack_code_exists = '〇'
        else:
            detect_using_exploitdb = '×'
            attack_code_exists = 'Unknown'
        if tmp[2] is True:
            detect_using_jvn = '〇'
        else:
            detect_using_jvn = '×'
        if tmp[3] is True:
            is_windows_update = '〇'
        else:
            is_windows_update = '×'
        if tmp[4] == 'DANGER':
            tdid = 'danger'
        elif tmp[4] == 'WARNING':
            tdid = 'danger'
        elif tmp[4] == 'CAUTION':
            tdid = 'caution'
        else:
            tdid = 'unknown'
        row = row + '''
        <tr>
            <td id="{}">{}</td>
            <td id="vulnapp_name">{}</td>
            <td id="vulnapp_version">{}</td>
            <td id="vulnapp_exploitdb">{}</td>
            <td id="vulnapp_jvn">{}</td>
            <td id="vulnupdate">{}</td>
            <td id="vulnapp_attackcode">{}</td>
        </tr>
        '''.format(tdid, tmp[4], app_name, app_version, detect_using_exploitdb, detect_using_jvn, is_windows_update, attack_code_exists)
    report = BASE.format(platform=platform,hostname=hostname, starttime=starttime, endtime=endtime, detect_num=str(detect_num), exploitdb=exploitdb, jvn=jvn, row=row)
    with open('../reports/detexploit_report.html', mode='w', encoding="utf-8") as f:
        f.write(report)
    webbrowser.open_new('file://' + os.path.realpath('../reports/detexploit_report.html'))
    

if __name__ == '__main__':
    colorama.init()
    print('======================================================')
    cprint('   ERROR: Direct execution of report.py detected', 'red')
    cprint('   ERROR: Please run the following to run DetExploit.', 'red')
    cprint('   ERROR: -> main.py for CUI version', 'red')
    cprint('   ERROR: -> gui.py for GUI version', 'red')
    print('======================================================')
