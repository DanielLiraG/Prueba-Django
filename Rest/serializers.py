from rest_framework import serializers
from Devices.models import Temperatura, Humedad


class TemperaturaSerializer (serializers.Serializer):

    fecha = serializers.DateTimeField()
    valor = serializers.FloatField()

    def create (self, validated_data):
        return Temperatura.objects.create(valor=validated_data.get('valor'))

    def update(self, instance, validated_data):
        instance.fecha = validated_data.get('fecha', instance.fecha)
        instance.valor = validated_data.get('valor', instance.valor)
        instance.save()
        return instance

        #comentario depues del checkout
        #comentario

        #comentario
        

class HumedadSerializer (serializers.Serializer):

    fecha = serializers.DateTimeField()
    valor = serializers.FloatField()

    def create (self, validated_data):
        return Humedad.objects.create(valor=validated_data.get('valor'))

    def update(self, instance, validated_data):
        instance.fecha = validated_data.get('fecha', instance.fecha)
        instance.valor = validated_data.get('valor', instance.valor)
        instance.save()
        return instance


