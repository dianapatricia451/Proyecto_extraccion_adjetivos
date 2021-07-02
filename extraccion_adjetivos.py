#-*- coding: utf-8 -*-
import json
import glob
from pathlib import Path
import os
# Get text files directories
currentDir = Path(os.getcwd())
dataDir = currentDir / 'Modernismo'
jsonfiles = glob.glob(str(dataDir)+'/*.json',recursive=True)

adjectives = []

for file in jsonfiles:
    # Read json file
    f = open(file, "r")
    data = json.load(f)
    f.close()
    for entry in data:
        for dict in entry: # cada entrada es un diccionario
            if dict['tag'].startswith('A'): # Si el tag empieza con A es un adjetivo
                adjective = dict['lemma']
                adjectives.append(adjective)

print(adjectives)    