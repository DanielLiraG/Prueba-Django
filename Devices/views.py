from django.shortcuts import HttpResponse, render
from Devices.DHT11 import DHT11, ErrorChecksum, ErrorTimeOut
from django.http import JsonResponse
from Devices.models import Temperatura, Humedad

#Vista para la lectura del sensor con toda la logica. 
def sensores(request):

    sensorDHT11 = DHT11(19)    #Objeto de la clase DHT11
    sensorDHT11.inicio()     #Inicio del pin asociado al 
    try:
        data = sensorDHT11.leer()    #lectura del sensor
        temperatura = float(str(data['Temp'])+'.'+str(data['TempDec']))
        humedad = float(str(data['Humedad'])+'.'+str(data['HumedadDec']))

        temperatura_db = Temperatura(valor= temperatura)
        humedad_db = Humedad(valor= humedad)

        temperatura_db.save()
        humedad_db.save()

        data = {'Temperatura':temperatura, 'Humedad':humedad, 'Hora':temperatura_db.fecha.strftime("%X")}

    except ErrorTimeOut:

        return HttpResponse("""Error 01""")   #Respuesta Http en caso de error por TimeOut
    except ErrorChecksum:

        return HttpResponse('''Error 02''')   #Respuesta Http en caso de error por Checksum

    sensorDHT11.final()     #Finalizacion del pin asociado
 
    return JsonResponse(data)    #respuesta en formato Json con toda la data extraida


def index(request):

    return render(request, 'index.html')


def data (request):

    valor_temperatura = []
    fecha_temperatura = []
    valor_humedad = []
    fecha_humedad = []

    temperaturaValor = Temperatura.objects.values('valor')
    for diccionario in temperaturaValor:
        valor_temperatura.append(diccionario['valor'])

    temperaturaFecha = Temperatura.objects.values('fecha')
    for diccionario in temperaturaFecha:
        fecha_temperatura.append(diccionario['fecha'].strftime("%X"))

    humedadValor = Humedad.objects.values('valor')
    for diccionario in humedadValor:
        valor_humedad.append(diccionario['valor'])

    humedadFecha = Humedad.objects.values('fecha')
    for diccionario in humedadFecha:
        fecha_humedad.append(diccionario['fecha'].strftime("%X"))

    respuesta = {'valor_temperatura':valor_temperatura,'fecha_temperatura':fecha_temperatura, 'valor_humedad':valor_humedad, 'fecha_humedad':fecha_humedad}

    return JsonResponse(respuesta)