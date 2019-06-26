###########################################################
# main.py
# Main script file of DetExploit.
# DetExploit (https://github.com/moppoi5168/DetExploit)
# Licensed by GPL License
###########################################################

from colorama import init
from termcolor import cprint
from pyfiglet import figlet_format

import argparse
import base64
import configparser
import datetime
import os
import platform
import sys
import threading

from commands import cmd_base
import exploitdb as ExploitDB
import jvn as JVN
import langpack
import local_app
import nvd as NVD
import report
import utils
import winupdate as WindowsUpdate


def main():
    global session_id
    DETEXPLOIT_VERSION = 'v1.4-ALPHA-CLI'

    scan_starttime = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    if session_id == None:
        session_id = base64.b64encode(scan_starttime.encode("ascii")).decode("ascii")
    utils.config_test()

    ExploitDB_RetData = ExploitDB.proc_data(langdata)
    ExploitDB_VulnData = ExploitDB_RetData[0]
    ExploitDB_Success = ExploitDB_RetData[1]

    JVN_RetData = JVN.proc_data(langdata)
    JVN_VulnData = JVN_RetData[0]
    JVN_Success = JVN_RetData[1]

    NVD_RetData = NVD.proc_data(langdata)
    NVD_VulnData = NVD_RetData[0]
    NVD_Success = NVD_RetData[1]

    installed = local_app.get_all()
    #####################################################################

    ## Scan #############################################################
    result = {}
    count = 0

    scanret_exploitdb = ExploitDB.scan(langdata, ExploitDB_VulnData, installed)
    scanret_jvn = JVN.scan(langdata, JVN_VulnData, installed)
    scanret_nvd = NVD.scan(langdata, NVD_VulnData, installed)
    scanret_winupdate = WindowsUpdate.scan(langdata)

    result.update(scanret_exploitdb[0])
    result.update(scanret_jvn[0])
    result.update(scanret_nvd[0])
    result.update(scanret_winupdate[0])
    
    count = scanret_exploitdb[1] + scanret_jvn[1] + scanret_nvd[1] + scanret_winupdate[1]
    #####################################################################
    
    scan_endtime = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    history = '''
    Session ID: {}
    Scan started at: {}
    Scan ended at: {}
    Found vulnerable application and available update: {}
    DetExploit Version: {}

    #####################################################################

    '''.format(session_id, scan_starttime, scan_endtime, count, DETEXPLOIT_VERSION)
    with open('../history.detexploit', 'w') as wh:
        wh.write(history)

    ## Report ###########################################################
    report.generate_report( langdata, 
                            DETEXPLOIT_VERSION, 
                            session_id, 
                            count, 
                            scan_starttime, 
                            scan_endtime, 
                            ExploitDB_Success, 
                            JVN_Success, 
                            NVD_Success, 
                            result)
    
    cprint('===========================================================', 'red')
    cprint(langdata['RESONE'] + str(count) + langdata['RESTWO'], 'red')
    cprint('===========================================================', 'red')
    #####################################################################


## Initialization ####################################################
init(strip=not sys.stdout.isatty())

run_on = platform.system()
langdata = langpack.load_langpack()
cp = configparser.ConfigParser()
cp.read('config.ini', 'UTF-8')

cprint(figlet_format('   DetExploit'), 'red', attrs=['bold'], end='')
print('===========================================================')
print(langdata['WELCOME_MESSAGE'])
print('===========================================================')
try:
    tmp = sys.argv[1]
    tmp = sys.argv[2]
except IndexError:
    if __name__ == '__main__':
        if run_on == 'Windows':
            session_id = ''
            main()
            exit(0)
        else:
            print('Currently, this platform is not supported.')
            exit(1)

if sys.argv[1] == 'session_id':
    if run_on == 'Windows':
        session_id = sys.argv[2]
        main()

cmd_base.proc_cmd(sys.argv[1], sys.argv[2])
#######################################################################