#-*- coding: utf-8 -*-
import requests
import io
#Archivo a ser enviado
files = {'file': open("Modernismo/efren-rebolledo.txt")}
#Parámetros
params = {'outf': 'tagged', 'format': 'json'}
#Enviar petición
url = "http://www.corpus.unam.mx/servicio-freeling/analyze.php"
r = requests.post(url, files=files, params=params)
#Convertir de formato json
obj = r.json()
print(obj[0][0])
# #Ejemplo, obtener todos los lemas
# for sentence in obj:
#     for word in sentence:
#         print(word["lemma"])
with open(r"Modernismo/efren-rebolledo.txt") as archivo:
    texto_raw = archivo.read()
print(texto_raw)
adjetivos = [w for sent in obj for w in sent if w["tag"].startswith("A")]
print(adjetivos)