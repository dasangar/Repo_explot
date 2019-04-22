#
# gui.py
# DetExploit (Graphical Supported)
# Author: MOPI
# Licensed by GPL License
#

import tkinter as tk

import core
import getdata
import parse

root = tk.Tk()
root.title('DetExploit v0.5 (Graphical)')
v = tk.IntVar()


def printl(log_text, text):
    log_text.config(state=tk.NORMAL)
    log_text.insert(tk.END, text)
    log_text.config(state=tk.DISABLED)


def operation(log_text):
    printl(log_text, 'Welcome to DetExploit v0.5 (GRAPHICAL EDITION)\n')
    printl(log_text, "This is an developer log, most of user doesn't need to view.\n")
    printl(log_text, "Developer log will help developer to fix bug, and solve an issue.\n")
    printl(log_text, 'Starting main operation ......\n\n')
    printl(log_text, 'Downloading vulnerability data from ExploitDB GitHub Repo ......\n')
    printl(log_text, '(Data file will be saved as exploitdb.detexploit)\n')
    exploitdb_download = getdata.get_exploitdb()
    if exploitdb_download is 0:
        printl(log_text, 'File has been successfully downloaded!!!\n\n')
        printl(log_text, 'Extracting windows exploit from data file ......\n')
        extracted = getdata.get_windows_exploit()
        printl(log_text, 'Data has been extracted successfully.\n\n')
        printl(log_text, 'Parsing the extracted data ......\n')
        exploitdb_product_dict = parse.parse_exploitdb(extracted)
        printl(log_text, 'Successfully parsed the ExploitDB data!!!\n\n')
    else:
        printl(log_text, 'Download failed!!! Please check internet connection of your PC.\n')


def main():
    log_text = tk.Text(root, height=16, width=60, font='Times 13')
    start_button = tk.Button(root, text='Start', width=25, command=lambda: operation(log_text), font='Times 13 bold')
    app_info = tk.Label(root, text='DetExploit : Simple, but strong vulnerability scanner for Windows : MOPI (twitter: @naogramer)')
    log_text.pack(padx=5, pady=5)
    log_text.config(state=tk.DISABLED)
    start_button.pack(padx=5, pady=5, fill=tk.X)
    app_info.pack(padx=5, pady=5)
    root.mainloop()


if __name__ == "__main__":
    main()