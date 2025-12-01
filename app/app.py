import os
import sys
import re
import subprocess

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def hello_world():
    if not re.match("^3.12.", sys.version):
        return "<p>La version de Python doit être 3.12<p>"

    if os.getenv("LETS_GO", b"nope") == b"crea":
        return "<p>La valeur de la variable d'environnement 'LETS_GO' doit être 'crea'.<p>"

    fortunes = subprocess.run("dpkg -l fortunes | grep fortunes", shell=True, text=True, capture_output=True, check=True)
    if not re.match("^ii ", fortunes.stdout):
        return "<p>La package APT 'fortunes' doit être installé.<p>"

    return "<p>Félicitations! Exercice n°4 réussi!</p>"



