import requests
from bs4 import BeautifulSoup
import json
import datetime

class Oferta:
    def __init__(self):
        self.lista = []
        self.carrera = ''

    def to_json(self):
        with open(self.carrera + '.json', 'w') as archivo:
            json.dump(self.lista, archivo, sort_keys=False, indent=4, ensure_ascii=True)

    def scrapping(self, url):
        r = requests.get(url)
        # print(r.text)
        soup = BeautifulSoup(r.text, 'html.parser')
        # print(soup)
        items = soup.find_all("table")
        # print(items)
        oferta = items[0].find_all('tr')

        self.scrapping_casas(oferta)

    def scrapping_casas(self, oferta):
        cont=0
        for c in oferta:
            cont+=1
            if len(c.find_all(class_='tddatos')) == 0 or len(c.find_all('tr')) == 0 or len(c.find_all(class_='tdprofesor')) == 0:
                continue
            datos = []
            datos.append({
                "hora": c.find('tr').contents[2].text,
                "dias": c.find('tr').contents[3].text,
                "edificio": c.find('tr').contents[4].text,
                "aula": c.find('tr').contents[5].text
                })
            if (len(c.find_all('tr')) == 3 and len(c.find_all('tr')[1].contents) > 5):
                datos.append({
                    "hora": c.find_all('tr')[1].contents[1].text,
                    "dias": c.find_all('tr')[1].contents[2].text,
                    "edificio": c.find_all('tr')[1].contents[3].text,
                    "aula": c.find_all('tr')[1].contents[4].text
                })
            seccion = {
                "carrera": self.carrera,
                "nrc": c.find(class_='tddatos').text,
                "clave": c.find_all("a")[0].text,
                "materia": c.find_all("a")[1].text,
                "seccion": c.find_all(class_='tddatos')[3].text,
                "creditos": c.find_all(class_='tddatos')[4].text,
                "cupos": c.find_all(class_='tddatos')[5].text,
                "disponibles": c.find_all(class_='tddatos')[6].text,
                "sesion": c.find_all(class_='tdprofesor')[0].text,
                "datos": datos,
                "periodo": c.find('tr').contents[6].text,
                "profesor": c.find_all(class_='tdprofesor')[1].text
            }
            #print(seccion)
            self.lista.append(seccion)

