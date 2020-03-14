# -*- Coding utf8 -*-
# Objetivo: Calcular el tiempo de un vehiculo
from datetime import datetime, timedelta

class Tiempo():
    """
    Clase encargada de calcular el tiempo que un vehiculo pasa en el estacionamiento,
    cual sera su monto a pagar y el descuento por hora
    """

    def aleatorio(self):
        """Generara la hora de salida de manera aleatoria para cada vehiculo"""
        hora = datetime.now + timedelta(hora=5)
    
    def ticket(self):
        """
        Muestra el ticket correspondiente al cliente por su estadia 
        en el estacionamiento y el total a pagar
        """
        if self.horas > 1:
            if self.tipo_vehiculo == "Automovil":
                self.subtotal = 20 * 0.20 - 20
                self.pagar = (horas - 1) * self.subtotal +20
            elif self.tipo_vehiculo == "Motocicleta":
                self.subtotal = 10 * 0.10 - 10
                self.pagar = (horas - 1 ) * self.subtotal + 10 
            else:
                print("Tipo de vehiculo no valido")
    
    def Hora_Salida(self):
        hora_salida = datetime.now + timedelta(hora=5)