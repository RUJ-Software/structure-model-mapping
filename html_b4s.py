import json
import sys
import pprint
from bs4 import BeautifulSoup

sys.setrecursionlimit(1500000000)


def divided_data(data):
    data_split = data.split(",")
    data_dict = {}
    for info in data_split:
        number, definition = info.split("-")
        data_dict[number] = definition
    return data_dict


def get_values_b4s(bs4_extract):
    soup = BeautifulSoup(bs4_extract)
    spans = soup.find_all('span')
    final_values = {}
    tipo3 = ""
    cont = 0
    for span in spans:
        if span.has_attr('class') and span['class'][0] == 'tipo3':
            tipo3 = span.get("title").replace(":", "").strip()
        if span.has_attr('class') and span['class'][0] == 'outputText':
            if tipo3 != "":
                if tipo3 == 'CÃ³digo CPV':
                    final_values[tipo3] = divided_data(span.get("title"))
                else:
                    final_values[tipo3] = span.get("title")
            else:
                final_values[cont] = span.get("title")
                tipo3 = ""
                cont += 1
    return final_values


def read_xml_file(filename):
    with open(filename, 'r') as file:
        print("GET VALUES...")
        b4s_extracts = get_values_b4s(file)
        return b4s_extracts


html_file = read_xml_file('form_example.html')
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(html_file)
