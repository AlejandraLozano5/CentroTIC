from django.shortcuts import render
import paho.mqtt.publish as publish
from .models import Temperatura
from django.http import JsonResponse


# Create your views here.
def index(request):
    respuesta = {}
    return render(request, "app_praes/index.html", respuesta)

def medicion_actual(request):
    respuesta = {}
    return render(request, "app_praes/medicion_actual.html", respuesta)

def monitoreo_lecturas(request):
    temp = Temperatura.objects.all()
    temperatura = temp.values("fecha", "valor")
    respuesta = {"temperatura": temperatura}
    return render(request, "app_praes/monitoreo_lecturas.html", respuesta)

def control_ESP32(request):
    topico = "UIS/LP/213"
    IP_broker = "34.73.25.149"
    usuario_broker = "pi"
    password_broker = "raspberry"
    publish.single(topico, "ESP32-LED", port=1883, hostname=IP_broker,
    auth={"username": usuario_broker, "password":password_broker})
    respuesta = {}
    return render(request, "app_praes/control_ESP32.html", respuesta)

def hora_local(request):
    import time
    tz = time.localtime()
    print(tz)
    resultado = {"GMT-5": tz}
    return JsonResponse(resultado)
