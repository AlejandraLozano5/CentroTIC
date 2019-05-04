from urequests import urequests
import utime 
import dht
import machine


def enviar_API(url, fecha, valor, sensor):
    """ esta funcion se encarga de enviar los datos a la API"""
    date = str(fecha[0])+"-"+str(fecha[1])+"-"+str(fecha[2])+" "+str(fecha[3])+":"+str(fecha[4])+":"+str(fecha[5])
    pyload = {
        "fecha": date,
        "valor": valor,
        "sensor": sensor
    }
    r = urequests.post(url, json=pyload, headers={"Authorization": " Token d2865cc229825bd3b05d765f11f21b6b80c0fff6"})
    print(r.content)
    print(r.status_code)
    r.close()


fecha = utime.localtime()
url = "http://34.73.25.149/app_praes/temperatura/"
sensor = 2
valor = 1000
enviar_API(url, fecha, valor, sensor)
