import json
import xmltodict
from mapp import mapping_xml

with open('xml-entry-sample.xml', 'r') as file:
    obj = xmltodict.parse(file.read())
    # TODO: PROBLEMA CON LOS ACENTOS
    obj_str = json.dumps(obj)
    obj_json = json.loads(obj_str)['entry']
    file.close()

print("FUTURE MAPPING:")
first_value_to_map = {}
cac_value_to_map = []
# TODO: TODOS LOS CAC TIENE MAS DENTRO
for x in obj_json:
    # print(x)
    if x == 'summary':
        first_value_to_map[x] = obj_json[x]['#text']
    elif x == 'link':
        first_value_to_map[x] = obj_json[x]['@href']
    elif x == 'cac-place-ext:ContractFolderStatus':
        # first_value_to_map[x] = obj_json[x]
        print('\n')
    else:
        first_value_to_map[x] = obj_json[x]

for key, value in mapping_xml.items():
    first_value_to_map[value] = first_value_to_map.pop(key)

print(first_value_to_map)
