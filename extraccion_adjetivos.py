#-*- coding: utf-8 -*-
import requests
import json
import glob
from pathlib import Path
import os
# Get text files directories
currentDir = Path(os.getcwd())
dataDir = currentDir / 'Modernismo'
textFiles = glob.glob(str(dataDir)+'/*.json',recursive=True)
for textfile in textFiles:
    # Read text file
    f = open(textfile, "r")
    rawText = f.read()
    f.close()
#adjetives
for entry in data:
    for dict in entry: # cada entrada es un diccionario
        if dict['tag'].startswith('A'): # Si el tag empieza con A es un adjetivo
            adjective = dict['lemma']
            print(adjective)    