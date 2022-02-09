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
    if x == 'summary':
        first_value_to_map[x] = obj_json[x]['#text']
    elif x == 'link':
        first_value_to_map[x] = obj_json[x]['@href']
    elif x == 'cac-place-ext:ContractFolderStatus':
        print('\n')
    else:
        first_value_to_map[x] = obj_json[x]

for key, value in mapping_xml.items():
    first_value_to_map[value] = first_value_to_map.pop(key)

# EXTRAS
first_value_to_map['bidding'] = first_value_to_map['short_description'].split(":")[1].split(";")[0]
first_value_to_map['contracting_authority'] = first_value_to_map['short_description'].split(":")[2].split(";")[0]
first_value_to_map['cost'] = first_value_to_map['short_description'].split(":")[3].split(";")[0]
first_value_to_map['status'] = first_value_to_map['short_description'].split(":")[4].split(";")[0]

print(first_value_to_map)
print("---------------------")
