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

import exploitdb as ExploitDB
import jvn as JVN
import langpack
import local_app
import nvd as NVD
import report
import winupdate as WindowsUpdate

## Initialization #####################################################
init(strip=not sys.stdout.isatty())
parser = argparse.ArgumentParser()
parser.add_argument('-s', 
                    '--session_id', 
                    type=str,
                    help='If you want, you can choose special session id for each run.')
args = parser.parse_args()
session_id = args.session_id
langdata = langpack.load_langpack()
cp = configparser.ConfigParser()
cp.read('../config.ini', 'UTF-8')
#######################################################################


def main():
    global session_id

    cprint(figlet_format('   DetExploit'), 'red', attrs=['bold'], end='')
    print('===========================================================')
    print(langdata['WELCOME_MESSAGE'])
    print('===========================================================')

    scan_starttime = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    if session_id == None:
        session_id = base64.b64encode(scan_starttime.encode("ascii")).decode("ascii")

    ## ExploitDB ########################################################
    exploitdb_success = False

    if cp.get('exploitdb', 'use_exploitdb') == 'True':
        ExploitDB.download_vulndata(langdata)
        extracted = ExploitDB.extract_windows_exploit(langdata)
        exploitdb_vulndata = ExploitDB.parse_vulndata(extracted)
        if exploitdb_vulndata is not None:
            exploitdb_success = True
    if cp.get('general', 'do_not_save_vulndata') == 'True':
        os.remove(cp.get('exploitdb', 'vulndata_filename'))
    #####################################################################

    ## JVN ##############################################################
    jvn_success = False

    if cp.get('jvn', 'use_jvn') == 'True':
        jvn_vulndata = JVN.download_vulndata(langdata)
        if jvn_vulndata is not None:
            jvn_success = True
    #####################################################################

    ## NVD ##############################################################
    nvd_success = False

    if cp.get('nvd', 'use_nvd') == 'True':
        nvd_vulndata = NVD.download_vulndata(langdata)
        if nvd_vulndata is not None:
            nvd_success = True
    #####################################################################

    ## Get locally installed applications ###############################
    installed = {}

    installed.update(local_app.getapp_from_wmi())
    installed.update(local_app.getapp_from_hklm())
    installed.update(local_app.getapp_from_hklmwow64())
    installed.update(local_app.getapp_from_hkcu())
    #####################################################################

    ## Scan #############################################################
    result = {}
    count = 0

    scanret_exploitdb = ExploitDB.scan(langdata, exploitdb_vulndata, installed)
    scanret_jvn = JVN.scan(langdata, jvn_vulndata, installed)
    scanret_nvd = NVD.scan(langdata, nvd_vulndata, installed)
    scanret_winupdate = WindowsUpdate.scan(langdata)

    result.update(scanret_exploitdb[0])
    result.update(scanret_jvn[0])
    result.update(scanret_nvd[0])
    result.update(scanret_winupdate[0])
    
    count = scanret_exploitdb[1] + scanret_jvn[1] + scanret_nvd[1] + scanret_winupdate[1]
    #####################################################################
    
    scan_endtime = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")

    ## Report ###########################################################
    report.generate_report( langdata, 
                            'v1.3-ALPHA-CLI', 
                            session_id, 
                            count, 
                            scan_starttime, 
                            scan_endtime, 
                            exploitdb_success, 
                            jvn_success, 
                            nvd_success, 
                            result)
    
    cprint('===========================================================', 'red')
    cprint(langdata['RESONE'] + str(count) + langdata['RESTWO'], 'red')
    cprint('===========================================================', 'red')
    #####################################################################


def cui_run():
    run_on = platform.system()
    if run_on == 'Windows':
        main()
    else:
        exit(1)


if __name__ == '__main__':
    cui_run()

