import tweepy
import json
import os.path as path

def recolectarDatosTwitter(cuenta):
    #Autenticación
    CONSUMER_KEY = 'YpYcmiKHtGxOXheTDW4HIc3zc'
    CONSUMER_SECRET = 'Pb7whiggvDJnISGwTEugSJP4Pn6CCUbei0fObTtlfhHyxfQ2zU'
    ACCESS_KEY = '738112788942495745-QQnjiJfb54za9XVICrLRLyMjRYZbiD2'
    ACCESS_SECRET = 'TwNe0LYo0c5P1S7jDI6lhULX2UMBPAVtV97uwPDYkIZXH'
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)

    #Realizar la búsqueda
    twits = api.search(cuenta,count = 100)

    principal = {}
    principal["tweets"] = []
    ids = []
    fileName = "datos_"+cuenta[1:]+".json"

    contador = 0
    if path.exists(fileName):
        f = open(fileName)
        datos_json = json.load(f)
        f.close()
        for tweet in datos_json["tweets"]:
            contador+=1
            principal["tweets"].append(tweet)
            ids.append(tweet["id"])
    print("Datos del archivo: ",contador,"tweets")
    print()

    contador = 0
    for tweet in twits:
        d = json.dumps(tweet._json)
        diccionario = json.loads(d)
        id = diccionario["id"]
        if id not in ids:
            contador+=1
            principal["tweets"].append(diccionario)
    print("Datos nuevos, obtenidos de twitter:",contador)
    #Crear/actualizar archivo json
    with open(fileName, 'w') as file:
        json.dump(principal, file, indent=4)


cuentas = ["@IESSec","@SRIoficialEc","@CPCCS"]
for cuenta in cuentas:
    print("*" * 50, cuenta, "*" * 50)
    recolectarDatosTwitter(cuenta)
    print()