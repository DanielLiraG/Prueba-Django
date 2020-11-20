from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from Devices.models import Temperatura, Humedad
from .serializers import TemperaturaSerializer, HumedadSerializer
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def temperatura (request):

    if request.method == 'GET':

        temperatura = Temperatura.objects.all()
        serializer = TemperaturaSerializer(temperatura, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':

        data = JSONParser().parse(request)
        serializer = TemperaturaSerializer(data=data)

        if serializer.is_valid():
            print("serializer valido")
            serializer.save()
            return JsonResponse(serializer.data, status= 201)

        print("serializer no valido")
        return JsonResponse(serializer.errors, status= 400)


