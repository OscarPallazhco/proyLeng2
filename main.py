import json
import os.path as path

def cargarInfoArchivo(cuenta):
    fileName = "datos_" + cuenta[1:] + ".json"
    if not  path.exists(fileName):
        print("No existe el archivo, ejecute primero el archivo recoleccion.py")
        exit()
    f = open(fileName)
    datos_json = json.load(f)
    f.close()

    contador = 1
    for tweet in datos_json["tweets"]:
        if len(tweet["entities"]["user_mentions"]) !=0:
            usuario = "@" + str(tweet["entities"]["user_mentions"][0]["screen_name"])
            nombre = str(tweet["entities"]["user_mentions"][0]["name"])
            id = tweet["id"]
            fecha = tweet["created_at"]
            l_hashtags = tweet["entities"]["hashtags"] #lista de diccionarios
            hashtags = []
            for elemento in l_hashtags:
                hashtags.append(elemento["text"])
            mensaje = tweet["text"]
            if ("retweeted_status" in tweet):
                mensaje = tweet["retweeted_status"]["text"]

            if usuario != "@IESSec" and usuario != "@SRIoficialEc" and usuario != "@CPCCS":        #No imprimir los tweets hechos por la misma cuenta
                print(str(contador) + ". Usuario:", nombre, "(", usuario, ")")
                print("\tid:", id)
                print("\tFecha:", fecha)
                print("\tMensaje:", mensaje)
                print("\tHahtags:", hashtags)
                contador += 1
                print()


cuentas = ["@IESSec","@SRIoficialEc","@CPCCS"]
for cuenta in cuentas:
    print("*"*50,cuenta,"*"*50)
    cargarInfoArchivo(cuenta)
    print()