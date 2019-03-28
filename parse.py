#
# parse.py
# Data parsing stage of DetExploit
# Author: MOPI
# Licensed by GPL License
#

def parse_exploitdb(data_list):
    product_dict = {}
    for data in data_list:
        splitted = data.split(',')
        title = splitted[2]
        base = title.split(' - ')[0][1:]
        baselist = base.split(' ')
        name = ' '.join(baselist[:-1])
        version = baselist[-1]
        product_dict[name] = version
    return product_dict

if __name__ == '__main__':
    print('Error: Please run main.py!!!')

