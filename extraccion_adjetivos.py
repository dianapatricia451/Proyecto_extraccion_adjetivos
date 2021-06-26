#-*- coding: utf-8 -*-
import requests
import json
import glob
from pathlib import Path
import os

#Read the text files
currentDir = Path(os.getcwd())
dataDir = currentDir / 'Modernismo'

textFiles = glob.glob(str(dataDir)+'/*.txt',recursive=True)

print(textFiles)
#Archivo a ser enviado
files = {'file': open("Modernismo/efren-rebolledo.txt")}


#Parámetros
params = {'outf': 'tagged', 'format': 'json'}
#Enviar petición
url = "http://www.corpus.unam.mx/servicio-freeling/analyze.php"
r = requests.post(url, files=files, params=params)
#Convertir de formato json
data = r.json() # lista

with open('efren_rebolledo.json', 'w') as f:
    json.dump(data, f, indent=2)

# Obtener todos los adjetivos
for entry in data:
    for dict in entry: # cada entrada es un diccionario
        if dict['tag'].startswith('A'): # Si el tag empiza con A es un adjetivo
            adjective = dict['lemma']
            print(adjective)

#with open(r"Modernismo/efren-rebolledo.txt") as archivo:
#    texto_raw = archivo.read()
#print(texto_raw)
#adjetivos = [w for sent in obj for w in sent if w["tag"].startswith("A")]
#print(adjetivos)