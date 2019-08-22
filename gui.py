###########################################################
# gui.py
# GUI script file of DetExploit.
# DetExploit (https://github.com/moppoi5168/DetExploit)
# Licensed by GPL License
###########################################################

import tkinter as tk
from tkinter import ttk
from html.parser import HTMLParser

import base64
import configparser
import datetime
import os
import platform
import pythoncom
import sys
import threading
import time
import urllib.request
import webbrowser

import exploitdb as ExploitDB
import jvn as JVN
import langpack
import local_app
import nvd as NVD
import report
import utils
import winupdate as WindowsUpdate

jvn_vulndata = {}


class html_parser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)


    def handle_starttag(self, tag, attrs):
        if tag == "sec:cpe":
            attrs = dict(attrs)
            if 'product' in attrs and 'version' in attrs:
                jvn_vulndata[attrs['product']] = attrs['version']


def proc_jvn():
    jvn_success = False
    if cp.get('jvn', 'use_jvn') == 'True':
        year_list = range(int(cp.get('jvn', 'data_from')), int(cp.get('jvn', 'data_to')) + 1)
        month_list = range(1, 13)
        for year in year_list:
            for month in month_list:
                progress_label.config(text=langdata['JVN_DOWNLOAD_INTRO'] + ' ... (' +  str(year) + '/' + str(month) + ')')
                url = 'https://jvndb.jvn.jp/myjvn?method=getVulnOverviewList&feed=hnd&rangeDatePublished=n&rangeDateFirstPublished=n&datePublicStartY=' + str(year) + '&datePublicStartM=' + str(month) + '&datePublicEmdY=' + str(year) + '&datePublicEmdM=' + str(month)
                mem = urllib.request.urlopen(url).read().decode()
                tmp = mem.split('\n')
                parser = html_parser()
                for line in tmp:
                    if '<sec:cpe' in line:
                        parser.feed(line)
        parser.close()
        if jvn_vulndata is not None:
            jvn_success = True
    return jvn_vulndata, jvn_success

def scan():
    pythoncom.CoInitialize()
    DETEXPLOIT_VERSION = 'v1.4-ALPHA-GUI'
    scan_starttime = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    session_id = base64.b64encode(scan_starttime.encode("ascii")).decode("ascii")
    utils.config_test()

    progress_label.config(text=langdata['EXPLOITDB_DOWNLOAD_INTRO'])
    ExploitDB_RetData = ExploitDB.proc_data(langdata)
    ExploitDB_VulnData = ExploitDB_RetData[0]
    ExploitDB_Success = ExploitDB_RetData[1]

    progress_label.config(text=langdata['JVN_DOWNLOAD_INTRO'])
    JVN_RetData = proc_jvn()
    JVN_VulnData = JVN_RetData[0]
    JVN_Success = JVN_RetData[1]

    progress_label.config(text=langdata['NVD_DOWNLOAD_INTRO'])
    NVD_RetData = NVD.proc_data(langdata)
    NVD_VulnData = NVD_RetData[0]
    NVD_Success = NVD_RetData[1]

    progress_label.config(text=langdata['GET_LOCAL_APP'])
    installed = local_app.get_all()

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
    #####################################################################

def open_github():
    webbrowser.open_new('https://github.com/moppoi5168/DetExploit')

def apply_settings():
    print('Apply clicked.')

def open_settings():
    setting = tk.Tk()
    val = tk.IntVar()
    val.set(0)
    setting.iconbitmap(r'DetExploit.jpg')
    setting.title('DetExploit ' + langdata['SETTINGS_TITLE'])
    frame = tk.Frame(setting, padx=10)
    frame.grid()
    t_label = tk.Label(frame, text=langdata['SETTINGS_TITLE'], fg='black', font="メイリオ 15")
    t_label.grid(row=0)
    language = tk.StringVar()
    l_label = ttk.Labelframe(
              frame, 
              text=langdata['LANGUAGE'],
              padding=5)
    l_label.grid(row=1, column=0, pady=5, sticky='w')
    lrb1 = ttk.Radiobutton(
           l_label,
           text='日本語 (Japanese)',
           value='ja',
           variable=language)
    lrb1.grid(row=1, sticky='w')
    lrb2 = ttk.Radiobutton(
           l_label,
           text='English',
           value='en',
           variable=language)
    lrb2.grid(row=2, sticky='w')
    save_vulndata = tk.BooleanVar()
    s_label = ttk.Labelframe(
              frame, 
              text=langdata['SVD_LOCAL'],
              padding=5)
    s_label.grid(row=4, column=0, pady=5, sticky='w')
    srb1 = ttk.Radiobutton(
           s_label,
           text=langdata['YES'],
           value=True,
           variable=save_vulndata)
    srb1.grid(row=4, sticky='w')
    srb2 = ttk.Radiobutton(
           s_label,
           text=langdata['NO'],
           value=False,
           variable=save_vulndata)
    srb2.grid(row=5, sticky='w')
    report_format = tk.StringVar()
    r_label = ttk.Labelframe(
              frame, 
              text=langdata['REPORT_FORMAT'],
              padding=5)
    r_label.grid(row=5, column=0, pady=5, sticky='w')
    rrb1 = ttk.Radiobutton(
           r_label,
           text='HTML',
           value='HTML',
           variable=report_format)
    rrb1.grid(row=5, sticky='w')
    rrb2 = ttk.Radiobutton(
           r_label,
           text='Markdown',
           value='Markdown',
           variable=report_format)
    rrb2.grid(row=6, sticky='w')
    rrb3 = ttk.Radiobutton(
           r_label,
           text='Plaintext',
           value='Plaintext',
           variable=report_format)
    rrb3.grid(row=7, sticky='w')
    apply_button = tk.Button(frame, text=langdata['APPLY'], command=apply_settings, font='メイリオ 10')
    apply_button.grid(row=8, pady=5)



## Initialization ####################################################
run_on = platform.system()
langdata = langpack.load_langpack()
cp = configparser.ConfigParser()
cp.read('config.ini', 'UTF-8')

if __name__ == '__main__':
    if run_on == 'Windows':
        root = tk.Tk()
        root.iconbitmap(r'DetExploit.jpg')
        root.title('DetExploit')
        frame = tk.Frame(root)
        frame.pack()
        appname_label = tk.Label(frame, text='DetExploit', fg='black', font="メイリオ 30")
        appname_label.pack(pady=(10,0))
        description_label = tk.Label(frame, text=langdata['DESCRIPTION'], fg='black', font="メイリオ 9")
        description_label.pack(padx=20)
        progress_label = tk.Label(frame, text=langdata['FIRST_MSG'], fg='black', font="メイリオ 12")
        progress_label.pack(padx=20)
        progress_bar = ttk.Progressbar(frame)
        progress_bar.configure(value=0, mode='indeterminate', maximum=100)
        progress_bar.pack(fill=tk.X, padx=10, pady=3)
        start_button = tk.Button(frame, text=langdata['START'], command=threading.Thread(target=scan).start, font="メイリオ 12")
        start_button.pack(fill=tk.X, padx=10, pady=3)
        githubrepo_button = tk.Button(frame, text=langdata['GITHUB'], command=open_github, font="メイリオ 12")
        githubrepo_button.pack(fill=tk.X, padx=10, pady=3)
        settings_button = tk.Button(frame, text=langdata['SETTINGS'], command=open_settings, font="メイリオ 12")
        settings_button.pack(fill=tk.X, padx=10, pady=3)      
        exit_button = tk.Button(frame, text=langdata['EXIT'], command=root.destroy, font="メイリオ 12")
        exit_button.pack(fill=tk.X, padx=10, pady=3)
        root.mainloop()
    else:
        root = tk.Tk()
        root.iconbitmap(default='DetExploit.ico')
        root.title('DetExploit')
        frame = tk.Frame(root)
        failed_label = tk.Label(frame, text='Sorry. This program supports only Windows.', fg='black', font = "メイリオ 40")
        failed_label.pack()
        start_button = tk.Button(frame, text='Exit', command=root.destroy)
        start_button.pack(fill=tk.X, padx=10, pady=3)
#######################################################################    
