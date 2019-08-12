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
            l_hashtags = tweet["entities"]["hashtags"] #lista de diccionarios
            hashtags = []
            for elemento in l_hashtags:
                hashtags.append(elemento["text"])

            print(str(contador)+". Usuario:",nombre,"(",usuario,")")
            print("\tFecha:",tweet["created_at"])
            print("\tMensaje:",end="")
            if ("retweeted_status" in tweet):
                print(tweet["retweeted_status"]["text"])
            else:
                print(tweet["text"])
            print("\tHahtags:",hashtags)
            contador+=1
            print()


cuentas = ["@IESSec","@SRIoficialEc","@CPCCS"]
cuenta = cuentas[0]
print("*"*50,cuenta,"*"*50)
cargarInfoArchivo(cuenta)