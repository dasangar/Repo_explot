#
# gui.py
# DetExploit (Graphical Supported)
# Author: MOPI
# Licensed by GPL License
#

from kivy.app import App
from kivy.config import Config
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.properties import StringProperty

import urllib.request
import logging
import datetime
import time
import webbrowser
import subprocess
import winreg
import win32com.client
import wmi

import core
import getdata
import parse
import report


class RootWidgets(Widget):
    status = StringProperty()
    expdb_download = True
    jvn_download = True

    def __init__(self, **kwargs):
        super(RootWidgets, self).__init__(**kwargs)
        self.update_status('Please click scan button to start.')


    def start_scan(self):
        starttime = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        self.update_status('Operation has been started.')
        self.update_status('Downloading vulnerability data from ExploitDB GitHub Repo.')
        exploitdb_success = getdata.get_exploitdb()
        if exploitdb_success is 0:
            self.update_status('Extracting Windows vulnerability from data.')
            extracted = getdata.get_windows_exploit()
            self.update_status('Parsing vulnerability data.')
            exploitdb_product_dict = parse.parse_exploitdb(extracted)
        self.update_status('Downloading data from JVN, this make take a while.')
        # GUI Version JVN Data Download (START)
        jvn_product_dict = {}
        year_list = range(2019, 2020)
        month_list = range(1, 13)
        for year in year_list:
            for month in month_list:
                print('JVNDL: ' + str(year) + '/' + str(month))
                url = 'https://jvndb.jvn.jp/myjvn?method=getVulnOverviewList&feed=hnd&rangeDatePublished=n&rangeDateFirstPublished=n&datePublicStartY=' + str(year) + '&datePublicStartM=' + str(month) + '&datePublicEmdY=' + str(year) + '&datePublicEmdM=' + str(month)
                mem = urllib.request.urlopen(url).read().decode()
                tmp = mem.split('\n')
                parser = getdata.html_parser()
                for line in tmp:
                    if '<sec:cpe' in line:
                        parser.feed(line)
        parser.close()
        # GUI Version JVN Data Download (END)
        if jvn_product_dict is not None:
            jvn_success = 0
        wins = wmi.WMI()
        data = {}
        count = 0
        self.update_status('Retrieving application data from WMI.')
        for result in wins.Win32_Product():
            data[result.Caption] = result.Version
        self.update_status('Retrieving application data from Windows Registry.')
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
        self.update_status('Comparing fetched data and installed application list.')
        count = 0
        resultdict = {}
        for key in exploitdb_product_dict:
            name = key
            version = exploitdb_product_dict[key]
            try:
                tmp = data[name]
            except KeyError:
                continue
            if data[name] == version:
                resultdict[name] = (version, True, False)
                count = count + 1
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
                count = count + 1
        self.update_status('Done.')
        endtime = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        report.gen_report('v0.6-GUI', count, starttime, endtime, exploitdb_success, jvn_success, resultdict)


    def update_status(self, info):
        self.status = '[color=#000000]' + info + '[/color]'
    
    
    def open_github(self):
        webbrowser.open('https://github.com/moppoi5168/DetExploit')


class detexploit(App):
    def build(self):
        return RootWidgets()


formatter = '%(levelname)s : %(asctime)s : %(message)s'
date = datetime.datetime.today().strftime("%Y%m%d%H%M%S")
logging.basicConfig(filename='DETEXPLOIT_' + date + '.log', level=logging.INFO, format=formatter)


if __name__ == "__main__":
    detexploit().run()
