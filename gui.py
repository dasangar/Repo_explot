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
root.title('DetExploit v0.5')


def main():
    tk.Label(root, text='DetExploit will detect malicious app installed on the system.').pack()
    root.mainloop()


if __name__ == "__main__":
    main()