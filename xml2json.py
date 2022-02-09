import json
import xmltodict
from mapp import mapping_xml


def read_xml_file(filename):
    with open(filename, 'r') as file:
        obj = xmltodict.parse(file.read())
        # TODO: PROBLEMA CON LOS ACENTOS
        obj_str = json.dumps(obj)
        obj_json = json.loads(obj_str)['entry']
        file.close()
        return obj_json


def first_mapping_extract(json_extract):
    first_value_to_map = {}
    # cac_value_to_map = []
    # TODO: TODOS LOS CAC TIENE MAS DENTRO
    for x in json_extract:
        if x == 'summary':
            first_value_to_map[x] = json_extract[x]['#text']
        elif x == 'link':
            first_value_to_map[x] = json_extract[x]['@href']
        elif x == 'cac-place-ext:ContractFolderStatus':
            print('\n')
        else:
            first_value_to_map[x] = json_extract[x]

    for key, value in mapping_xml.items():
        first_value_to_map[value] = first_value_to_map.pop(key)
    return first_value_to_map


def extra_mapping_extract(first_mapp):
    mapp_return = first_mapp
    mapp_return['bidding'] = first_mapp['short_description'].split(":")[1].split(";")[0]
    mapp_return['contracting_authority'] = first_mapp['short_description'].split(":")[2].split(";")[0]
    mapp_return['cost'] = first_mapp['short_description'].split(":")[3].split(";")[0]
    mapp_return['status'] = first_mapp['short_description'].split(":")[4].split(";")[0]
    return mapp_return


xml_json = read_xml_file('xml-entry-sample.xml')
print("MAPPING...")
first_mapping = first_mapping_extract(xml_json)
extra_mapping = extra_mapping_extract(first_mapping)
print(extra_mapping)
print("---------------------")