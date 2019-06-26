###########################################################
# commands/config.py
# Script file for commands related to config file.
# DetExploit (https://github.com/moppoi5168/DetExploit)
# Licensed by GPL License
###########################################################

import configparser


def cmd_current_config(val=None):
    cp = configparser.ConfigParser()
    cp.read('config.ini', 'UTF-8')
    for section in cp.sections():
        print('#####\n\n[{}]\n'.format(section))
        for key in cp.options(section):
            print('{} = {}'.format(key, cp.get(section, key)))
            print('\n')
    exit(0)


def cmd_default_config():
    dp = configparser.ConfigParser(val=None)
    dp.read('resources/default.ini', 'UTF-8')
    for section in dp.sections():
        print('#####\n\n[{}]\n'.format(section))
        for key in dp.options(section):
            print('{} = {}'.format(key, dp.get(section, key)))
            print('\n')
    exit(0)
