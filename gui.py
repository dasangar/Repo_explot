#
# gui.py
# DetExploit (Graphical Supported)
# Author: MOPI
# Licensed by GPL License
#

import tkinter as tk
from tkinter import ttk
import urllib.request
import logging
import datetime

import core
import getdata
import parse

pbar_value = 0


def about():
    print('About is clicked!!')


def get_jvn_vulnerability(pbar):
    # Experimentary letting DetExploit to download data from 2010
    global pbar_value
    product_dict = {}
    year_list = range(2010, 2020)
    month_list = range(1, 13)
    for year in year_list:
        for month in month_list:
            url = 'https://jvndb.jvn.jp/myjvn?method=getVulnOverviewList&feed=hnd&rangeDatePublished=n&rangeDateFirstPublished=n&datePublicStartY=' + str(year) + '&datePublicStartM=' + str(month) + '&datePublicEmdY=' + str(year) + '&datePublicEmdM=' + str(month)
            mem = urllib.request.urlopen(url).read().decode()
            tmp = mem.split('\n')
            parser = getdata.html_parser()
            for line in tmp:
                if '<sec:cpe' in line:
                    parser.feed(line)
            pbar_value = pbar_value + 1
            pbar.configure(value=pbar_value)
    parser.close()
    return product_dict


def operation(pbar):
    global pbar_value
    logging.info('DetExploit v0.5 Developer Log\n')
    logging.info("This is an developer log, most of users doesn't need to view this.\n")
    logging.info("Developer log will help developers to fix bug, and solve an issue.\n")
    exploitdb_download = getdata.get_exploitdb()
    if exploitdb_download is 0:
        logging.info('[SUCCESS] ExploitDB Data Download\n')
        pbar_value = pbar_value + 1
        pbar.configure(value=pbar_value)
        extracted = getdata.get_windows_exploit()
        logging.info('[SUCCESS] ExploitDB Data Extraction\n')
        pbar_value = pbar_value + 1
        pbar.configure(value=pbar_value)
        exploitdb_product_dict = parse.parse_exploitdb(extracted)
        logging.info('[SUCCESS] ExploitDB Data Parse\n')
        pbar_value = pbar_value + 1
        pbar.configure(value=pbar_value)
    else:
        logging.info('[FAILED] ExploitDB Data Download\n\n')
        logging.info('[FAILED] Skipping three progress.\n\n')
        pbar_value = pbar_value + 3
        pbar.configure(value=pbar_value)
    jvn_product_dict = getdata.get_all_vulnerability()


def main():
    log_text = tk.Text(root, height=16, width=60, font='Times 13')
    start_button = tk.Button(root, text='Scan the vulnerable apps!!!', width=25, command=lambda: operation(pbar), font='Times 13')
    app_info = tk.Label(root, text='DetExploit : Simple, but strong vulnerability scanner for Windows : MOPI (twitter: @naogramer)')
    pbar = ttk.Progressbar(mode='determinate')
    pbar.configure(maximum=123, value=pbar_value)
    log_text.pack(padx=5, pady=5)
    log_text.config(state=tk.DISABLED)
    pbar.pack(padx=5, pady=5, fill=tk.X)
    start_button.pack(padx=5, pady=5, fill=tk.X)
    app_info.pack(padx=5, pady=5)
    root.mainloop()

formatter = '%(levelname)s : %(asctime)s : %(message)s'
date = datetime.datetime.today().strftime("%Y/%m/%d/%H/%M/%S")
logging.basicConfig(filename='DETEXPLOIT_' + date + '_GUI.log', level=logging.INFO, format=formatter)
root = tk.Tk()
root.title('DetExploit v0.5 (Graphical Edition)')
menu_root = tk.Menu(root)
root.configure(menu=menu_root)
menu_file = tk.Menu(menu_root, tearoff=False)
menu_help = tk.Menu(menu_root, tearoff=False)
menu_root.add_cascade(label='File', menu=menu_file)
menu_root.add_cascade(label='Help', menu=menu_help)
menu_file.add_command(label='Exit', command=root.destroy)
menu_help.add_command(label='About', command=about)


if __name__ == "__main__":
    main()