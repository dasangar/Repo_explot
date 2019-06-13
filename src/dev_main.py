###########################################################
# dev_main.py
# Main script file for development of DetExploit.
# DetExploit (https://github.com/moppoi5168/DetExploit)
# Licensed by GPL License
###########################################################

from colorama import init
from termcolor import cprint
from pyfiglet import figlet_format

import configparser
import sys

import main as MAIN
import gui as GUI

cp = configparser.ConfigParser()
cp.read('../config.ini', 'UTF-8')


def main():
    cprint(figlet_format('   DetExploit'), 'red', attrs=['bold'], end='')
    print('===========================================================')
    print('   Development (debug, test) Version')
    print('===========================================================\n\n')
    while True:
        cmd = input('DetExploit >> ')
        cmd_list = cmd.split(' ')
        if cmd_list[0] == 'run':
            print('\n')
            if cmd_list[1] == 'cui':
                MAIN.cui_run()
            elif cmd_list[1] == 'gui':
                GUI.gui_run()
            else:
                print('Usage: run [cui or gui]')
            print('\n')
        elif cmd_list[0] == 'config':
            print('\n')
            print('Listing up current settings in config.ini...\n')
            for section in cp.sections():
                print('[{}]'.format(section))
                for key in cp.options(section):
                    print('{} = {}'.format(key, cp.get(section, key)))
                print('\n')
        elif cmd_list[0] == 'exit':
            break
        elif cmd_list[0] == 'help':
            print('\n')
            print('DetExploit Development Version')
            print('Command List: ')
            print('run [cui or gui] : Execute specified version of DetExploit')
            print('config : List up current settings in config.ini')
            print('help : Help command. It will output entire command list.')
            print('\n')
        else:
            print('Unknown command. Run help for entire command list.')


if __name__ == "__main__":
    init(strip=not sys.stdout.isatty())
    main()
