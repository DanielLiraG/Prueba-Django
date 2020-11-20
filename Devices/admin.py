from django.contrib import admin
from .models import Temperatura, Humedad

# Register your models here.

class TemperaturaAdmin (admin.ModelAdmin):
    list_display = ('fecha', 'valor')
    list_filter = ('fecha', 'valor')


class HumedadAdmin (admin.ModelAdmin):
    list_display = ('fecha' , 'valor')
    list_filter = ('fecha', 'valor')

admin.site.register(Temperatura, TemperaturaAdmin)
admin.site.register(Humedad, HumedadAdmin)

