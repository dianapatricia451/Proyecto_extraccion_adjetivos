#-*- coding: utf-8 -*-
import requests
import json
import glob
from pathlib import Path
import os

# Get text files directories
currentDir = Path(os.getcwd())
dataDir = currentDir / 'Modernismo'
textFiles = glob.glob(str(dataDir)+'/*.txt',recursive=True)

# Freeling parameters
params = {'outf': 'tagged', 'format': 'json'}
url = "http://www.corpus.unam.mx/servicio-freeling/analyze.php"

for textfile in textFiles:
    # Set filename for json file
    filepath = Path(textfile)
    author=filepath.parts[-1].split('.')[0]
    json_filename = author+'.json'

    # Read text file
    f = open(textfile, "r")
    rawText = f.read()
    f.close()

    # Send request to server
    text = {'file': rawText}
    freeling_request = requests.post(url, files=text, params=params)
    data = freeling_request.json()

    # Save server responce as json file
    with open(json_filename, 'w') as f:
        json.dump(data, f, indent=2) 