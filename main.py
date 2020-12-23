# A clash subscribe with modify script
# Writing by Pan Xiao 2020-12-19
# Version 0.1
# Please use
# pip3 install ruamel.yaml requests
# First
from ruamel import yaml
import requests


def add_key_value(key_name: str, locate: int, list_name: list, dict_name: dict, value: object):
    if key_name in dict_name:
        dict_name[key_name] = value
    else:
        list_name.insert(locate, key_name)
        dict_name[key_name] = value


# Get origin sub file
url = input()
clash_sub_origin = requests.get(url)
clash_sub_origin.raise_for_status()

if clash_sub_origin.status_code == requests.codes.ok:
    # load yaml data
    clash_sub_data = yaml.load(clash_sub_origin.text, Loader=yaml.RoundTripLoader)
    # 维护一个列表，使字典有序
    clash_sub_key = list(clash_sub_data.keys())

    # Add keys and value
    # clash_sub_key.insert(clash_sub_key.index('mixed-port') + 1, 'socks-port')
    # clash_sub_data['socks-port'] = 7891
    add_key_value('socks-port', clash_sub_key.index('mixed-port') + 1, clash_sub_key, clash_sub_data, 7891)

    # add redir port
    # clash_sub_key.insert(clash_sub_key.index('socks-port') + 1, 'redir-port')
    # clash_sub_data['redir-port'] = 7892
    add_key_value('redir-port', clash_sub_key.index('socks-port') + 1, clash_sub_key, clash_sub_data, 7892)

    # rebuild dict
    clash_sub_output = {}
    for i in clash_sub_key:
        clash_sub_output[i] = clash_sub_data[i]

    # print(clash_sub_output)
    print(yaml.round_trip_dump(clash_sub_output, allow_unicode=True))
