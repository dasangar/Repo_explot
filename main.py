#
# main.py
# Main script file of DetExploit
# Author: MOPI
# Licensed by MIT License
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

BYPASS_PLATFORM_CHK = True


def main():
    cprint(figlet_format('DetExploit'), 'red', attrs=['bold'], end='')
    print('==============================================')
    print('Hello, W0rld!! Welcome to DetExploit v0.1 :)')
    print('==============================================')
    getdata.get_whole_csv()
    extracted = getdata.extract_windows_exploit()
    name_and_version = parse.parse_name_and_version(extracted)
    run_on = platform.system()
    if run_on == 'Windows':
        print('Winodws platform detected.')
        num = core.windows(name_and_version)
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
        if BYPASS_PLATFORM_CHK:
            cprint('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~', 'red')
            cprint('DANGER: BYPASS_PLATFORM_CHK IS ENABLED!!!', 'red')
            cprint('>> It may corrupt your system.', 'red')
            cprint('>> If you are not developer, press Ctrl+C to exit and disable right now.', 'red')
            cprint('>> DetExploit will run normally as windows machine after 10 seconds.', 'red')
            cprint('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~', 'red')
            sleep(10)
            core.windows(name_and_version)
    print('==============================================')

if __name__ == '__main__':
    main()

