"""
La cantidad de Tweets que se obtuvieron con Tweepy fue muy grande, los archivos datos_<CUENTA>(500) tienen a lo mucho 500 tweets de los archivos originales.
"""

import json
cuentas = ["@IESSec","@SRIoficialEc","@CPCCS"]
cuenta = cuentas[2]
principal = {}
principal["tweets"] = []

fileName = "datos_" + cuenta[1:] + ".json"

contador = 0
cantidad = 500       #cantidad de tweets que se desean

f = open(fileName)
datos_json = json.load(f)
f.close()
for tweet in datos_json["tweets"]:
    contador += 1
    principal["tweets"].append(tweet)
    if(contador==cantidad):
        break

print("Datos del archivo: ", contador, "tweets")
fileName = "datos_" + cuenta[1:] + "(500).json"
with open(fileName, 'w') as file:
    json.dump(principal, file, indent=4)