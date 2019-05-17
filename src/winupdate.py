# 
# winupdate.py
# Functions of DetExploit related to Windows Update
# Author: MOPI
# Licensed by GPL License
#

from colorama import init
from termcolor import cprint
from time import sleep
from pyfiglet import figlet_format

import os
import pywintypes
import re
import subprocess
import sys
import win32com.client
import win32con
import win32api

init(strip=not sys.stdout.isatty())

DETEXPLOIT_WINDOWSUPDATE_SEARCHER_VBSCRIPT = '''
Set updateSession = CreateObject("Microsoft.Update.Session")
updateSession.ClientApplicationID = "DetExploit Windows Update Searcher Script"
Set updateSearcher = updateSession.CreateUpdateSearcher()
Set searchResult = _
updateSearcher.Search("IsInstalled=0 and Type='Software' and IsHidden=0")

For I = 0 To searchResult.Updates.Count-1
    Set update = searchResult.Updates.Item(I)
    WScript.Echo update.Title
Next
WScript.Quit
'''

def get_available_update():
    print('===========================================================')
    print('   Running update searcher script to gather not-installed update.')
    with open('DetExploit_WinUpdateSearcher.vbs', mode='w') as f:
        f.write(DETEXPLOIT_WINDOWSUPDATE_SEARCHER_VBSCRIPT)
    tmp = subprocess.Popen(r'cscript DetExploit_WinUpdateSearcher.vbs', stdout=subprocess.PIPE, shell=True).stdout.readlines()
    os.remove('DetExploit_WinUpdateSearcher.vbs')
    tmp = tmp[3:]
    result = []
    for upd in tmp:
        result.append(upd.decode('cp932', 'ignore')[:-2])
    return result


if __name__ == '__main__':
    print('======================================================')
    cprint('   ERROR: Direct execution of winupdate.py detected', 'red')
    cprint('   ERROR: Please run the following to run DetExploit.', 'red')
    cprint('   ERROR: -> main.py for CUI version', 'red')
    cprint('   ERROR: -> gui.py for GUI version', 'red')
    print('======================================================')
