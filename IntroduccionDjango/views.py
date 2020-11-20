from django.shortcuts import HttpResponse, render
from IntroduccionDjango.DHT11 import DHT11, ErrorChecksum, ErrorTimeOut
from django.http import JsonResponse


#Vista para la lectura del sensor con toda la logica. 
def sensores(request):

    sensorDHT11 = DHT11(19)    #Objeto de la clase DHT11
    sensorDHT11.inicio()     #Inicio del pin asociado al 
    try:
        data = sensorDHT11.leer()    #lectura del sensor
    except ErrorTimeOut:

        return HttpResponse("""Error 01""")   #Respuesta Http en caso de error por TimeOut
    except ErrorChecksum:

        return HttpResponse('''Error 02''')   #Respuesta Http en caso de error por Checksum

    sensorDHT11.final()     #Finalizacion del pin asociado
 
    return JsonResponse(data)    #respuesta en formato Json con toda la data extraida


def index(request):

    return render(request, 'index.html')