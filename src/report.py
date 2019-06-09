###########################################################
# report.py
# File that contains code block related to scan report.
# DetExploit (https://github.com/moppoi5168/DetExploit)
# Licensed by GPL License
###########################################################

from bs4 import BeautifulSoup
from termcolor import cprint

import colorama
import configparser
import os
import requests
import socket
import webbrowser

LEVEL_DANGER = 'DANGER'
LEVEL_WARNING = 'WARNING'
LEVEL_CAUTION = 'CAUTION'

cp = configparser.ConfigParser()
cp.read('../config.ini', 'UTF-8')
REPORT_FORMAT = cp.get('general', 'report_format')


def determine_level(data_src, ext=None):
    if data_src == 'ExploitDB':
        return LEVEL_DANGER
    elif data_src == 'WinUpdate':
        if ext == None or 'KB' not in ext:
            return LEVEL_WARNING
        tmp = ext.find('KB')
        tmp = ext[tmp:]
        kb_code = tmp[:9]
        url = 'https://www.catalog.update.microsoft.com/Search.aspx?q=' + kb_code
        response = requests.get(url).text
        soup = BeautifulSoup(response, 'lxml')
        td = soup.find_all("td")
        for tag in td:
            try:
                tctn = tag.string
                if 'Feature Packs' in tctn:
                    return LEVEL_WARNING
                elif 'Security Updates' in tcin:
                    return LEVEL_DANGER
                elif 'Critical Updates' in tctn:
                    return LEVEL_DANGER
            except:
                pass
        return LEVEL_WARNING
    elif data_src == 'JVN':
        return LEVEL_CAUTION
    elif data_src == 'NVD':
        return LEVEL_CAUTION
    else:
        return 'Error'


def generate_report(langdata, platform, session_id, detect_num, starttime, endtime, exploitdb_success, jvn_success, nvd_success, resultdict):
    if REPORT_FORMAT == 'HTML':
        with open(file='../resources/report_template.html', encoding="utf-8") as base:
            BASE = base.read()
    elif REPORT_FORMAT == 'PlainText':
        with open(file='../resources/report_template.txt', encoding="utf-8") as base:
            BASE = base.read()
    elif REPORT_FORMAT == 'Markdown':
        with open(file='../resources/report_template.md', encoding="utf-8") as base:
            BASE = base.read()
    else:
        cprint(langdata['REPORT_FORMAT_READ_ERROR_ONE'], 'red')
        cprint(langdata['REPORT_FORMAT_READ_ERROR_TWO'], 'red')
        with open(file='../resources/report_template.html', encoding="utf-8") as base:
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
    if nvd_success == True:
        nvd = 'Success'
    else:
        nvd = 'Failed or not runned'
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
            detect_using_nvd = '〇'
        else:
            detect_using_nvd = '×'
        if tmp[4] is True:
            is_windows_update = '〇'
        else:
            is_windows_update = '×'
        if tmp[5] == 'DANGER':
            tdid = 'danger'
        elif tmp[5] == 'WARNING':
            tdid = 'danger'
        elif tmp[5] == 'CAUTION':
            tdid = 'caution'
        else:
            tdid = 'unknown'
        if REPORT_FORMAT == 'PlainText':
            ext = '.txt'
            row = row + '''
            [{} v{}] - {}
            Detected using ExploitDB: {}
            Detected using JVN: {}
            Detected using NVD: {}
            Is it Windows Update: {}
            Attack Code Existence: {} 
            '''.format(app_name, app_version, tmp[5], detect_using_exploitdb, detect_using_jvn, detect_using_nvd, is_windows_update, attack_code_exists)
        elif REPORT_FORMAT == 'Markdown':
            ext = '.md'
            row = row + '''

            ### {} v{}

            - Level: {}
            - Detected by ExploitDB: {}
            - Detected by JVN: {}
            - Detected by NVD: {}
            - Is it Windows Update: {}
            - Attack Code Existence: {}

            '''.format(app_name, app_version, tmp[5], detect_using_exploitdb, detect_using_jvn, detect_using_nvd, is_windows_update, attack_code_exists)
        else:
            ext = '.html'
            row = row + '''
            <tr>
                <td id="{}">{}</td>
                <td id="vulnapp_name">{}</td>
                <td id="vulnapp_version">{}</td>
                <td id="vulnapp_exploitdb">{}</td>
                <td id="vulnapp_jvn">{}</td>
                <td id="vulnapp_nvd">{}</td>
                <td id="vulnupdate">{}</td>
                <td id="vulnapp_attackcode">{}</td>
            </tr>
            '''.format(tdid, tmp[5], app_name, app_version, detect_using_exploitdb, detect_using_jvn, detect_using_nvd, is_windows_update, attack_code_exists)
    report = BASE.format(platform=platform,hostname=hostname, starttime=starttime, endtime=endtime, detect_num=str(detect_num), session_id=session_id, loaded_langdata=langdata['LANGPACK_SIGNATURE'], exploitdb=exploitdb, jvn=jvn, nvd=nvd, row=row)
    with open('../reports/detexploit_report_' + session_id + ext, mode='w', encoding="utf-8") as f:
        f.write(report)
    cprint(langdata['REPORT_OUTPUT_INFO_ONE'] + session_id + ext + langdata['REPORT_OUTPUT_INFO_TWO'], 'green')
    print('===========================================================')
    if REPORT_FORMAT == 'HTML':
        webbrowser.open_new('file://' + os.path.realpath('../reports/detexploit_report_' + session_id + '.html'))
    

if __name__ == '__main__':
    colorama.init()
    print('======================================================')
    cprint('   ERROR: Direct execution of report.py detected', 'red')
    cprint('   ERROR: Please run the following to run DetExploit.', 'red')
    cprint('   ERROR: -> main.py for CUI version', 'red')
    cprint('   ERROR: -> gui.py for GUI version', 'red')
    print('======================================================')
