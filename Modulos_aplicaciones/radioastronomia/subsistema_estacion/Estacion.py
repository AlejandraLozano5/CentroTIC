import requests
import random
import json
from Davis import Davis_6162C
import time
class Estacion():

    def __init__(self,direccionIP, APIusername, APIpassword):
        self.direccionIP = direccionIP
        self.APIusername = APIusername
        self.APIpassword = APIpassword

    def serialRS232(self):
        """ la salida de los datos debe ser un diccionario
        valores = {"temperatura": 100,
                "humedad_relativa": 20,
                "presion_atomosferica": 30,
                "radiacion_solar": 30,
                "vel_viento": 90,
                "dir_viento": "N-S",
                "precipitacion": 50}
                """
        

        values = Davis_6162C.read()
        return values 

    #comunicacion con la API
    def getToken(self):
        """Esta funcion se encarga de consultar el token de acuerdo al usuario
        y contrasena para la API """
        data = {
        "username": self.APIusername,
        "password": self.APIpassword}
        URL = "http://"+self.direccionIP+"/app_praes/token/"
        r = requests.post(URL, data=data)
        #print("HTTP status token {}".format(r.status_code))
        token = json.loads(r.content)
        # print(token["token"])
        return token["token"]

    def estacionAPI(self, valores, region):
        """ este metodo es para iniciar la comunicacion donde la base de datos
        y registrar las mediciones, las entradas son:
        * URL: es la direccion de la API sin colocar la IP, por ejemplo: /radioastronomia/estacion-monitoreo
        * valores: es un json que contiene las lecturas
        * region: es el id de la region donde se registra la medicion
        """
        data = {"temperatura": valores["temperatura"],
                "humedad_relativa": valores["humedad_relativa"],
                "presion_atomosferica": valores["presion_atomosferica"],
                "radiacion_solar": valores["radiacion_solar"],
                "vel_viento": valores["vel_viento"],
                "dir_viento": valores["dir_viento"],
                "precipitacion": valores["precipitacion"],
                "region": region}
        
        token = self.getToken()
        headers={"Authorization":"Token "+token}
        URL = "http://"+self.direccionIP+"/radioastronomia/estacion-monitoreo"
        r = requests.post(URL, data=data, headers=headers)

        if r.status_code==200:
            print("HTTP status ok. {}".format(r.status_code))
            r.close()
        else:
            print("HTTP status {}".format(r.status_code))
            pass
    
    def comunicacionAPI(self, region):
        """ las funciones a ejecuar son:
        valores = self.serialRS232()
        self.estacionAPI(valores, region)
        """
        pass


if __name__ == "__main__":
    direccionIP = "35.243.199.245"
    APIusername = "mario"
    APIpassword = "mario"
    valores = {"temperatura": random.random(),
                "humedad_relativa": random.random(),
                "presion_atomosferica": random.random(),
                "radiacion_solar": random.random(),
                "vel_viento": random.random(),
                "dir_viento": "N-S",
                "precipitacion": random.random()}

    region = 6

    estacion = Estacion(direccionIP, APIusername, APIpassword)
    def updater():
 
        for k, v in estacion.serialRS232().items():

            if k in valores:
                valores[k] = v
            else:
                pass

        estacion.estacionAPI(valores, region)

    for i in range(100):
        time.sleep(3)
        updater()
        print(estacion.serialRS232())


