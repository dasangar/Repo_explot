###########################################################
# gui.py
# GUI execution script file of DetExploit.
# DetExploit (https://github.com/moppoi5168/DetExploit)
# Licensed by GPL License
###########################################################

from html.parser import HTMLParser
from kivy.app import App
from kivy.config import Config
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.properties import StringProperty


import configparser
import datetime
import os
import platform
import pythoncom
import subprocess
import threading
import urllib.request
import webbrowser
import winreg
import win32com.client
import wmi

import exploitdb as ExploitDB
import jvn as JVN
import local_app
import report
import winupdate as WindowsUpdate

product_dict = {}


class html_parser(HTMLParser):
        def __init__(self):
            HTMLParser.__init__(self)


        def handle_starttag(self, tag, attrs):
            if tag == "sec:cpe":
                attrs = dict(attrs)
                if 'product' in attrs and 'version' in attrs:
                    product_dict[attrs['product']] = attrs['version']


class RootWidgets(Widget):
    status = StringProperty()


    def __init__(self, **kwargs):
        super(RootWidgets, self).__init__(**kwargs)
        self.update_status('Please click scan button to start.')


    def jvn_download_vulndata(self):
        product_dict = {}

        year_list = range(int(cp.get('jvn', 'data_from')), int(cp.get('jvn', 'data_to')) + 1)
        month_list = range(1, 13)
        for year in year_list:
            for month in month_list:
                self.update_status('Downloading data from JVN ... ' + str(year) + '/' + str(month))
                print('JVNDL: ' + str(year) + '/' + str(month))
                url = 'https://jvndb.jvn.jp/myjvn?method=getVulnOverviewList&feed=hnd&rangeDatePublished=n&rangeDateFirstPublished=n&datePublicStartY=' + str(year) + '&datePublicStartM=' + str(month) + '&datePublicEmdY=' + str(year) + '&datePublicEmdM=' + str(month)
                mem = urllib.request.urlopen(url).read().decode()
                tmp = mem.split('\n')
                parser = html_parser()
                for line in tmp:
                    if '<sec:cpe' in line:
                        parser.feed(line)
        parser.close()

    
    def start_scan(self):
        threading.Thread(target=self.scan_main).start()


    def scan_main(self):
        pythoncom.CoInitialize()
        scan_starttime = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        self.update_status('Operation has been started.')

        ## ExploitDB ########################################################
        exploitdb_success = False

        self.update_status('Downloading vulnerability data from ExploitDB GitHub Repo.')
        if cp.get('exploitdb', 'use_exploitdb') == 'True':
            ExploitDB.download_vulndata()
            self.update_status('Extracting Windows vulnerability from data.')
            extracted = ExploitDB.extract_windows_exploit()
            self.update_status('Parsing vulnerability data.')
            exploitdb_vulndata = ExploitDB.parse_vulndata(extracted)
            if exploitdb_vulndata is not None:
                exploitdb_success = True
        if cp.get('general', 'do_not_save_vulndata') == 'True':
            os.remove(cp.get('exploitdb', 'vulndata_filename'))
        #####################################################################

        ## JVN ##############################################################
        jvn_success = False

        self.update_status('Downloading data from JVN ...')
        if cp.get('jvn', 'use_jvn') == 'True':
            self.jvn_download_vulndata()
            jvn_vulndata = product_dict
            if jvn_vulndata is not None:
                jvn_success = True
        #####################################################################

        ## Get locally installed applications ###############################
        installed = {}

        self.update_status('Retrieving application data from WMI.')
        installed.update(local_app.getapp_from_wmi())
        self.update_status('Retrieving application data from Windows Registry.')
        installed.update(local_app.getapp_from_hklm())
        installed.update(local_app.getapp_from_hklmwow64())
        installed.update(local_app.getapp_from_hkcu())
        #####################################################################

        ## Scan #############################################################
        result = {}
        count = 0

        self.update_status('Comparing fetched data and installed application list.')
        scanret_exploitdb = ExploitDB.scan(exploitdb_vulndata, installed)
        scanret_jvn = JVN.scan(jvn_vulndata, installed)
        self.update_status('Checking available Windows Updates.')
        scanret_winupdate = WindowsUpdate.scan()

        result.update(scanret_exploitdb[0])
        result.update(scanret_jvn[0])
        result.update(scanret_winupdate[0])
    
        count = scanret_exploitdb[1] + scanret_jvn[1] + scanret_winupdate[1]
        #####################################################################

        scan_endtime = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")

        ## Report ###########################################################
        report.generate_report('v1.0-ALPHA-GUI', 
                                count, 
                                scan_starttime, 
                                scan_endtime, 
                                exploitdb_success, 
                                jvn_success, 
                                result)
        #####################################################################

        self.update_status('Done.')


    def update_status(self, info):
        self.status = '[color=#000000]' + info + '[/color]'
    
    
    def open_github(self):
        webbrowser.open('https://github.com/moppoi5168/DetExploit')


class detexploit(App):
    def build(self):
        self.title = 'DetExploit v1.0α'
        return RootWidgets()


if __name__ == "__main__":
    cp = configparser.ConfigParser()
    cp.read('./config.ini', 'UTF-8')
    run_on = platform.system()
    if run_on == 'Windows':
        detexploit().run()
    else:
        exit(1)
