import json
import xmltodict
from mapp import mapping_xml
import pprint


def read_xml_file(filename):
    with open(filename, 'r') as file:
        obj = xmltodict.parse(file.read())
        # TODO: PROBLEMA CON LOS ACENTOS
        obj_str = json.dumps(obj)
        obj_json = json.loads(obj_str)['entry']
        file.close()
        return obj_json


def cac_mapping(map_status, json_from_file, cac):
    # WIP
    cac_extras_to_return = map_status
    cac_extras_to_return['cac:PartyName'], cac_extras_to_return['cac:PartyLocation'] = cac_located_contracting_party(
                                                        json_from_file[cac], 'cac-place-ext:LocatedContractingParty')
    return cac_extras_to_return


def cac_located_contracting_party(json_file, cac):
    return json_file[cac]['cac:Party']['cac:PartyName']['cbc:Name'], \
           json_file[cac]['cac-place-ext:ParentLocatedParty']['cac:PartyName']['cbc:Name']


def first_mapping_extract(json_extract):
    first_value_to_map = {}
    # TODO: TODOS LOS CAC TIENE MAS DENTRO
    for x in json_extract:
        if x == 'summary':
            first_value_to_map[x] = json_extract[x]['#text']
        elif x == 'link':
            first_value_to_map[x] = json_extract[x]['@href']
        elif x == 'cac-place-ext:ContractFolderStatus':
            first_value_to_map = cac_mapping(first_value_to_map, json_extract, x)
        else:
            first_value_to_map[x] = json_extract[x]

    for key, value in mapping_xml.items():
        first_value_to_map[value] = first_value_to_map.pop(key)
    return first_value_to_map


def extra_mapping_extract(prev_map):
    # FALTA VER SI VALE PARA TODO
    mapped_return = prev_map
    mapped_return['bidding'] = prev_map['short_description'].split(":")[1].split(";")[0]
    mapped_return['contracting_authority'] = prev_map['short_description'].split(":")[2].split(";")[0]
    mapped_return['cost'] = prev_map['short_description'].split(":")[3].split(";")[0]
    mapped_return['status'] = prev_map['short_description'].split(":")[4].split(";")[0]
    return mapped_return


xml_json = read_xml_file('xml-entry-sample.xml')
print("MAPPING...")
print("---------------------")
first_mapping = first_mapping_extract(xml_json)
extra_mapping = extra_mapping_extract(first_mapping)
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(extra_mapping)
print("---------------------")
