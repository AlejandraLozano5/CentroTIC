from rest_framework import generics 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from .models import Temperatura, Humedad, PresionAtmosferica, MaterialParticulado, NO2, \
      Polvo, O3, SO2, CO, CO2, MetanoPropanoCO, LuzUV, MaterialOrganico, CH4, Anemometro, Sensores
from .serializers import TemperaturaSerializer, HumedadSerializer, PresionAtmosfericaSerializer, \
      MaterialParticuladoSerializer, NO2Serializer, PolvoSerializer, O3Serializer, SO2Serializer, \
      COSerializer, CO2Serializer, MetanoPropanoCOSerializer, LuzUVSerializer,\
      MaterialOrganicoSerializer, CH4Serializer, AnemometroSerializer, UserSerializer, SensoresSerializer



# class SensoresAPI(APIView):
#     """ Provee la lista de todos los sensores usados para el monitoreo ambiental,
#     esto es util para programar la tarjeta de desarrollo o terminal IoT, 
#     solo el administrador tiene acceso a esta API
#     """
#     permission_classes = (permissions.IsAdminUser,)
#     def get(self, request, format=None):
#         datos = Sensores.objects.all()
#         sensores = datos.values("id", "nombre_sensor")
#         return Response(sensores)

# Clases para el administrador centroTIC
class LoginView(APIView):
    """ Esta API es para ver los usuarios registrados hasta el momento
    en la aplicacion del CENTROTIC
    """
    permission_classes = (permissions.IsAdminUser,)
    
    def get(self, request,):
        users = User.objects.all()
        usuarios = users.values("username", "email")
        return Response(usuarios)

class SensoresAPI(generics.ListCreateAPIView):
    """ Provee la lista de todos los sensores usados para el monitoreo ambiental,
    esto es util para programar la tarjeta de desarrollo o terminal IoT, 
    solo el administrador tiene acceso a esta API
    """
    permission_classes = (permissions.IsAdminUser,)
    queryset = Sensores.objects.all()
    serializer_class = SensoresSerializer

class CrearUsuarioAPI(generics.CreateAPIView):
    permission_classes = (permissions.IsAdminUser,)
    serializer_class = UserSerializer
###

## Variables ambientales 
class TemperaturaAPI(generics.CreateAPIView):
    queryset = Temperatura.objects.all()
    serializer_class = TemperaturaSerializer

class HumedadAPI(generics.CreateAPIView):
    queryset = Humedad.objects.all()
    serializer_class = HumedadSerializer

class PresionAtmosfericaAPI(generics.CreateAPIView):
    queryset = PresionAtmosferica.objects.all()
    serializer_class = PresionAtmosfericaSerializer

class MaterialParticuladoAPI(generics.CreateAPIView):
    queryset = MaterialParticulado.objects.all()
    serializer_class = MaterialParticuladoSerializer

class NO2API(generics.CreateAPIView):
    queryset = NO2.objects.all()
    serializer_class = NO2Serializer

class PolvoAPI(generics.CreateAPIView):
    queryset = Polvo.objects.all()
    serializer_class = PolvoSerializer

class O3API(generics.CreateAPIView):
    queryset = O3.objects.all()
    serializer_class = O3Serializer

class SO2API(generics.CreateAPIView):
    queryset = SO2.objects.all()
    serializer_class = SO2Serializer

class COAPI(generics.CreateAPIView):
    queryset = CO.objects.all()
    serializer_class = COSerializer

class CO2API(generics.CreateAPIView):
    queryset = CO2.objects.all()
    serializer_class = CO2Serializer

class MetanoPropanoCOAPI(generics.CreateAPIView):
    queryset = MetanoPropanoCO.objects.all()
    serializer_class = MetanoPropanoCOSerializer

class LuzUVAPI(generics.CreateAPIView):
    queryset = LuzUV.objects.all()
    serializer_class = LuzUVSerializer

class MaterialOrganicoAPI(generics.CreateAPIView):
    queryset = MaterialOrganico.objects.all()
    serializer_class = MaterialOrganicoSerializer

class CH4API(generics.CreateAPIView):
    queryset = CH4.objects.all()
    serializer_class = CH4Serializer

class AnemometroAPI(generics.CreateAPIView):
    queryset = Anemometro.objects.all()
    serializer_class = AnemometroSerializer