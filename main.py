#
# main.py
# Main script file of DetExploit
# Author: MOPI
# Licensed by GPL License
#

import platform
import sys

try:
    from colorama import init
    init(strip=not sys.stdout.isatty())
    from termcolor import cprint
    from time import sleep
    from pyfiglet import figlet_format
except ModuleNotFoundError:
    print('Error: Required modules not found on your system.')
    print('Error: Did you run pip install -r requirements.txt ?')
    exit(5)

import core
import getdata
import parse


def main():
    cprint(figlet_format('DetExploit'), 'red', attrs=['bold'], end='')
    print('==============================================')
    print('Hello, W0rld!! Welcome to DetExploit v0.2 :)')
    print('==============================================')
    getdata.get_exploitdb()
    extracted = getdata.get_windows_exploit()
    exploitdb_product_dict = parse.parse_exploitdb(extracted)
    jvn_product_dict = getdata.get_all_vulnerability()
    run_on = platform.system()
    if run_on == 'Windows':
        print('Winodws platform detected.')
        num = core.windows(exploitdb_product_dict, jvn_product_dict)
        cprint('==============================================', 'red')
        cprint('RESULT: ' + str(num) + ' vulnerable application found!!', 'red')
        cprint('==============================================', 'red')
    else:
        if run_on == 'Darwin':
            print('macOS platform detected.')
            print("Sorry, DetExploit doesn't support macOS environment.")
        elif run_on == 'Linux':
            print('Linux platform detected.')
            print("Sorry, DetExploit doesn't support linux environment.")
            print('But it may support in future, keep your eyes on GitHub Repo!!')
            print('GitHub Repo: https://github.com/moppoi5168/DetExploit')
        elif run_on == 'Java':
            print('Java platform detected.')
            print("Sorry, DetExploit doesn't support Java environment.")
        else:
            print('Platform determination failed.')
            print("This platform doesn't support DetExploit")
    print('==============================================')

if __name__ == '__main__':
    main()

