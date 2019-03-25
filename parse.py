#
# parse.py
# Data parsing stage of DetExploit
# Author: MOPI
# Licensed by MIT License
#

def parse_exploitdb(data_list):
    # 46527,exploits/windows/webapps/46527.sh,"PRTG Network Monitor 18.2.38 - (Authenticated) Remote Code Execution",2019-03-11,M4LV0,webapps,windows,80\n
    name_and_version = []
    for data in data_list:
        splitted = data.split(',')
        title = splitted[2]
        base = title.split(' - ')[0][1:]
        baselist = base.split(' ')
        name = ' '.join(baselist[:-1])
        version = baselist[-1]
        name_and_version.append(name + '/' + version)
    return name_and_version

if __name__ == '__main__':
    print('Error: Please run main.py!!!')

