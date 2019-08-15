import tweepy
import json

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
    twits = api.search(cuenta,count = 10)

    contador = 1
    for tweet in twits:
        d = json.dumps(tweet._json)
        diccionario = json.loads(d)
        if len(diccionario["entities"]["user_mentions"]) != 0:
            usuario = "@" + str(diccionario["entities"]["user_mentions"][0]["screen_name"])
            nombre = str(diccionario["entities"]["user_mentions"][0]["name"])
            id = diccionario["id"]
            fecha = diccionario["created_at"]
            l_hashtags = diccionario["entities"]["hashtags"]  # lista de diccionarios
            hashtags = []
            for elemento in l_hashtags:
                hashtags.append(elemento["text"])
            mensaje = diccionario["text"]
            if ("retweeted_status" in diccionario):
                mensaje = diccionario["retweeted_status"]["text"]

            if usuario != cuenta:  # No imprimir los tweets hechos por la misma cuenta
                print(str(contador) + ". Usuario:", nombre, "(", usuario, ")")
                print("\tid:", id)
                print("\tFecha:", fecha)
                print("\tMensaje:", mensaje)
                print("\tHahtags:", hashtags)
                contador += 1
                print()


cuentas = ["@IESSec","@SRIoficialEc","@CPCCS", "@Correos_Ecuador"]
for cuenta in cuentas:
    print("*" * 50, cuenta, "*" * 50)
    recolectarDatosTwitter(cuenta)
    print()