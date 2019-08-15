import json
cuentas = ["@IESSec","@SRIoficialEc","@CPCCS"]
cuenta = cuentas[0]
principal = {}
principal["tweets"] = []
ids = []
fileName = "datos_" + cuenta[1:] + ".json"

contador = 0

f = open(fileName)
datos_json = json.load(f)
f.close()
for tweet in datos_json["tweets"]:
    contador += 1
    if(contador<6):
        principal["tweets"].append(tweet)

print("Datos del archivo: ", contador, "tweets")
print()
fileName = "datos_" + cuenta[1:] + "(500).json"
with open(fileName, 'w') as file:
    json.dump(principal, file, indent=4)