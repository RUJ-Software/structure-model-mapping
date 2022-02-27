import requests
from bs4 import BeautifulSoup

#url = ' https://contrataciondelestado.es/wps/poc?uri=deeplink:detalle_licitacion&idEvl=57p7Vz36p1KXQV0WE7lYPw%3D%3D'
#url = 'https://contrataciondelestado.es/wps/poc?uri=deeplink:detalle_licitacion&idEvl=5HKn3DhBJRV7h85%2Fpmmsfw%3D%3D'
url = 'https://contrataciondelestado.es/wps/poc?uri=deeplink%3Adetalle_licitacion&idEvl=%2BwQ9SIPFjUrnSoTX3z%2F7wA%3D%3D'

response = requests.get(url)
soup = BeautifulSoup(response.content.decode('utf-8'), "html.parser")
raw_data = soup.find_all('form', class_='form')
#print(raw_data[1])

def form_to_model(data):
    soup = BeautifulSoup(str(data), "html.parser")    
    elements = soup.find_all('ul')

    dictOfWords = {'exp': '', 'org_contratacion': '', 'estado': '', 'objeto': '', 'presupuesto_sin_impuestos': '', 'valor_estimado': '', 'tipo_contrato': '', 'cpv': '', 'lugar': '', 'procedimiento': '',
            'info': {}}

    for element in elements:
        if element.get('class') and ('ancho100' in element.get('class') or 'altoDetalleLicitacion' in element.get('class')):
            if element.get('id') == 'fila2':
                dictOfWords['org_contratacion'] = element.find('span', class_="outputText").text
            elif element.get('id') == 'fila3':
                dictOfWords['estado'] = element.find('span', class_="outputText").text
            elif element.get('id') == 'fila4':
                dictOfWords['objeto'] = element.find('span', class_="outputText").text
            elif element.get('id') == 'fila5':
                dictOfWords['presupuesto_sin_impuestos'] = float(element.find('span', class_="outputText").text.replace('.', '').replace(',', '.'))
            elif element.get('id') == 'fila6':
                dictOfWords['valor_estimado'] = float(element.find('span', class_="outputText").text.replace('.', '').replace(',', '.'))
            elif element.get('id') == 'fila7':
                dictOfWords['tipo_contrato'] = element.find('span', class_="outputText").text
            elif element.get('id') == 'fila8':
                dictOfWords['cpv'] = element.find('span', class_="outputText").text
            elif element.get('id') == 'fila9':
                dictOfWords['lugar'] = element.find('span', class_="outputText").text
            elif element.get('id') == 'fila10':
                dictOfWords['procedimiento'] = element.find('span', class_="outputText").text
            # Info
            if element.find('span', class_="tipo3"):
                if element.find('span', class_="tipo3").text == 'Fecha fin de presentación de oferta':
                    dictOfWords['info']['fecha_fin_presentacion_oferta'] = element.find('span', class_="outputText").text
                elif element.find('span', class_="tipo3").text == 'Resultado':
                    dictOfWords['info']['resultado'] = element.find('span', class_="outputText").text
                elif element.find('span', class_="tipo3").text == 'Adjudicatario':
                    dictOfWords['info']['adjudicatario'] = element.find('span', class_="outputText").text
                elif element.find('span', class_="tipo3").text == 'Nº de Licitadores Presentados':
                    dictOfWords['info']['num_licitadores'] = element.find('span', class_="outputText").text
                elif element.find('span', class_="tipo3").text == 'Importe de Adjudicación':
                    try:
                        dictOfWords['info']['importe_adjudicacion'] = float(element.find('span', class_="outputText").text.replace('.', '').replace(',', '.'))
                    except:
                        dictOfWords['info']['importe_adjudicacion'] = element.find('span', class_="outputText").text
                elif element.find('span', class_="tipo3").text == 'Fecha de Actualización del Expte.':
                    dictOfWords['info']['fecha_act_expediente'] = element.find('span', class_="outputText").text
                elif element.find('span', class_="tipo3").text == 'Fecha fin de presentación de solicitud':
                    dictOfWords['info']['fecha_presentacion_solicitud'] = element.find('span', class_="outputText").text
            #print(element.get('title', 'No title attribute'))


    print(dictOfWords)

form_to_model(raw_data[1])
