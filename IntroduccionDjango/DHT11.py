# -*- coding: iso-8859-15 -*-
# ===================================================================
#   Ejemplo #08: Sensor de humedad y temperatura DHT11
# ===================================================================
# Librerias necesarias ----------------------------------------------
import RPi.GPIO as GPIO
from time import sleep
# Definición de terminales ------------------------------------------

# Definiciones para retardos ----------------------------------------

# Mensajes y depuración ---------------------------------------------

# Clases para errores en este programa ------------------------------


class Errores(Exception):
    pass


class ErrorTimeOut(Errores):
    pass


class ErrorChecksum(Errores):
    pass
# Clases y Métodos para el DHT11 ------------------------------------


class DHT11:

    def __init__(self, gpio):
        self.msRetardo = lambda x: sleep(x/1000)
        self.Retardo = lambda x: sleep(x)
        self.pinDHT = gpio
        self.dhtOK = 0

    def inicio(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pinDHT, GPIO.OUT)

    def final(self):
        GPIO.cleanup()

    def Verificar(self, espera, valor, tiempo):
        for i in range(espera):
            if GPIO.input(self.pinDHT) == valor and tiempo == False:
                return self.dhtOK
            if GPIO.input(self.pinDHT) == valor and tiempo == True:
                return i
        raise ErrorTimeOut('Se excede el contador establecido')

    def datos(self):
        resultado = 0
        for i in range(8):
            ValorA = self.Verificar(100, True, True)
            ValorB = self.Verificar(100, False, True)
            resultado = resultado | (ValorA < ValorB) << (7 - i)
        return resultado

    def leer(self):
        # Secuencia de inicio de comunicación ---
        GPIO.setup(self.pinDHT, GPIO.OUT)
        GPIO.output(self.pinDHT, True)
        GPIO.output(self.pinDHT, False)
        self.msRetardo(20)
        GPIO.output(self.pinDHT, True)
        GPIO.setup(self.pinDHT, GPIO.IN)
        # Se espera un lapso de hasta 40 us por una respuesta ---
        self.Verificar(100, False, False)
        # Cuando se da False, se espera hasta 90 us por True ---
        self.Verificar(100, True, False)

        # Cuando se da el True se espera por el inicio de datos ---
        self.Verificar(100, False, False)
        humedad = self.datos()
        humedad_dec = self.datos()
        temperatura_int = self.datos()
        temperatura_dec = self.datos()
        Checksum = self.datos()
        VerificarCheck = humedad+humedad_dec+temperatura_int+temperatura_dec
        if VerificarCheck != Checksum:
            raise ErrorChecksum('No coincide el CHECKSUM')
        GPIO.setup(self.pinDHT, GPIO.OUT)
        GPIO.output(self.pinDHT, True)
        sensorDHT = {'Humedad': humedad, 'HumedadDec': humedad_dec,
                     'Temp': temperatura_int, 'TempDec': temperatura_dec, 'Checksum': Checksum}
        print("""Humedad:{},{}
        \rTemperatura: {},{} Celsius\n\r""".format(sensorDHT['Humedad'],
                                                   sensorDHT['HumedadDec'], sensorDHT['Temp'], sensorDHT['TempDec']))
        return sensorDHT
# Ejecutando métodos de la clase DHT11 ------------------------------
# =================== FIN DEL PROGRAMA ==============================
