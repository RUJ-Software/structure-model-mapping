import json
import xmltodict
from mapp import mapping_xml
import pprint
import html_to_json
import sys
sys.setrecursionlimit(1500000000)


def read_xml_file(filename):
    with open(filename, 'r') as file:
        html = file.read()
        obj_json = html_to_json.convert(html)
        return obj_json


def recursive_get_values(list_val):
    if type(list_val) == dict:
        recursive_get_values(list_val.values())
    for value in list_val:
        if value != 'fin':
            if value == '_value':
                values_html_from.append(list_val[value])
                return recursive_get_values(value)
            elif type(value) != str:
                return recursive_get_values(value)
        else:
            print("fin")

    return None


def recursive_get_values_test(items):
    return None


def first_mapping_extract(json_extract):
    recursive_get_values(json_extract)


html_json = read_xml_file('form_example.html')
print("GET VALUES...")
html_json['fin'] = 'fin'
values_html_from = []
first_mapping_extract(html_json)
print(values_html_from)
# pp = pprint.PrettyPrinter(indent=4)
# pp.pprint(xml_json.values())
# print(xml_json)
# print("---------------------")
