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


def operation(log_text):
    log_text.config(state=tk.NORMAL)
    log_text.insert(tk.END, 'Starting operation ......\n\n')
    log_text.insert(tk.END, 'Downloading vulnerability data from ExploitDB GitHub Repo ......\n')
    log_text.insert(tk.END, '(Data file will be saved as exploitdb.detexploit)\n')
    log_text.config(state=tk.DISABLED)
    exploitdb_download = getdata.get_exploitdb()
    log_text.config(state=tk.NORMAL)
    if exploitdb_download is 0:
        log_text.insert(tk.END, 'File has been successfully downloaded!!!\n\n')
        log_text.insert(tk.END, 'Extracting windows exploit from data file ......\n')
        log_text.config(state=tk.DISABLED)
        extracted = getdata.get_windows_exploit()
        log_text.config(state=tk.NORMAL)
        log_text.insert(tk.END, 'Data has been extracted successfully.\n\n')
        log_text.insert(tk.END, 'Parsing the extracted data ......\n')
        log_text.config(state=tk.DISABLED)
        exploitdb_product_dict = parse.parse_exploitdb(extracted)
        log_text.config(state=tk.NORMAL)
        log_text.insert(tk.END, 'Successfully parsed the ExploitDB data!!!\n\n')
    else:
        log_text.insert(tk.END, 'Download failed!!! Please check internet connection of your PC.\n')
    log_text.config(state=tk.DISABLED)


def main():
    start_button = tk.Button(root, text='Start', width=25, command=root.destroy, font='Times 13 bold')
    log_text = tk.Text(root, height=16, width=100)
    app_info = tk.Label(root, text='DetExploit : Simple, but strong vulnerability scanner for Windows : MOPI (twitter: @naogramer)')
    log_text.pack(padx=5, pady=5)
    log_text.config(state=tk.DISABLED)
    start_button.pack(padx=5, pady=5, fill=tk.X)
    app_info.pack(padx=5, pady=5)
    log_text.config(state=tk.NORMAL)
    log_text.insert(tk.END, 'Welcome to DetExploit v0.5 (GRAPHICAL EDITION)!!!\n')
    log_text.config(state=tk.DISABLED)
    operation(log_text)
    log_text.config(state=tk.DISABLED)
    root.mainloop()


if __name__ == "__main__":
    main()