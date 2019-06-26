###########################################################
# commands/cmd_base.py
# Script file for parsing, and executing commands.
# DetExploit (https://github.com/moppoi5168/DetExploit)
# Licensed by GPL License
###########################################################

from commands import config
from commands import history
from commands import scan_schedule


def proc_cmd(cmd, value):
    for command in CMD_LIST:
        if CMD_LIST[0] == cmd:
            CMD_LIST[2](val=value)


def cmd_list(val=None):
    print('DetExploit Built-In Command List :)')
    for command in CMD_LIST:
        print('> ' + command[0] + ' : ' + command[1])
    exit(0)

# CMD_LIST Sample ('TestCommand', 'Description of TestCommand', test_command_function())
CMD_LIST = [('current_config', 'This command will show the current config settings.', config.cmd_current_config), 
            ('default_config', 'This command will show the default config settings.', config.cmd_default_config), 
            ('view_history', 'This command will show the scan history.', history.cmd_view_history), 
            ('delete_history', 'This command will delete entire scan history.', history.cmd_delete_history), 
            ('setup_new_schedule', 'This command will start setup of scheduled scan.', scan_schedule.cmd_setup_new_schedule), 
            ('list', 'This is the command that shows command list which you are looking right now.'), cmd_list]
