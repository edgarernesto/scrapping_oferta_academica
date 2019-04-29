import json

with open('prueba.txt', 'w') as archivo:
    s = ('MUÑOZ')
    json.dump(s, archivo, sort_keys=False, indent=4, ensure_ascii=True)

with open('prueba.txt', 'rb') as archivo:
    aux = json.load(archivo)
    print(aux)