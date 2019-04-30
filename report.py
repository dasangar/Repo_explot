#
# report.py
# Functions around report for DetExploit
# Author: MOPI
# Licensed by GPL License
#

import socket
import webbrowser


def gen_report(platform, detect_num, starttime, endtime, exploitdb_getdata, jvn_getdata, resultdict):
    # resultdict['HogeTalk'] = ('1.00', True, True)
    # resultdict[APPNAME] = (VERSION, DETECT_USING_EXPLOITDB, DETECT_USING_JVN)
    with open(file='template.html', encoding="utf-8") as base:
        BASE = base.read()
    hostname = socket.gethostname() 
    if exploitdb_getdata is 0:
        exploitdb = 'Success'
    if jvn_getdata is 0:
        jvn = 'Success'
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
        row = row + '''
        <tr>
            <td id="danger">DANGER</td>
            <td id="vulnapp_name">{}</td>
            <td id="vulnapp_version">{}</td>
            <td id="vulnapp_exploitdb">{}</td>
            <td id="vulnapp_jvn">{}</td>
            <td id="vulnapp_attackcode">{}</td>
        </tr>
        '''.format(app_name, app_version, detect_using_exploitdb, detect_using_jvn, attack_code_exists)
    report = BASE.format(platform=platform,hostname=hostname, starttime=starttime, endtime=endtime, detect_num=str(detect_num), exploitdb=exploitdb, jvn=jvn, row=row)
    with open('detexploit_report.html', mode='w', encoding="utf-8") as f:
        f.write(report)
    webbrowser.open('detexploit_report.html')
    