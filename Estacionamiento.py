# -*- Coding utf8 -*-
#Programa: Estacionamiento.py
#Objetivo: Crear un servicio de estacionamiento de Vehiculos para clientes Particulares
#Autor: Karol Castellanos
#Fecha: 13 de Marzo 2020

import platform
import sys
import os
from datetime import datetime, timedelta

class VehiculoCliente():
    """
    Se ingresan los datos de los vehiculos de los clientes que usan el estacionamiento 

    """

    def Limpiar_Pantalla(self):
        """
        Función encargada de limpiar la pantalla
        """
        if platform.system == "Windows":
            os.system("cls")
        elif platform.system == "Darwin" or platform.system == "Linux":
            os.system("Clear")
        else:
            print("Plataforma no valida")
    
    def enter(self):
        """Hace una pausa mientras espera que se precione una tecla"""
        input("\nPresione una tecla para continuar")
    
    def Menu(self):
        """
        Se encarga de mostrar las opciones validas del menu
        """

        print("""---------------Genesys Inc----------------
                 -- 1. Ingreso de vehiculo               --
                 -- 2. Salida Vehiculo                   --
                 -- 3. Buscar                            --
                 -- 4. Reporte Diario                    --
                 -- 5. Salir                             --
                 ------------------------------------------
                 """)
    def __init__(self):
        """Procesa la opcion elegida por el usuario """
        self.vehiculo = list()
        self.marca = list()
        self.modelo = list()
        self.tipo_vehiculo = list()
        self.hora_entrada = list()
        self.estado = list()
        self.opcion = {"1": self.ingreso_vehiculo(),
                     "2": self.salida_vehiculo(),
                     "3": self.buscar(),
                     "4": self.reporte_diario(),
                     "5": self.salir()}
        
    def ingreso_vehiculo(self):
        """Agrega un nuevo vehiculo al momento de ingresar al estacionamiento"""
        print("------------------Ingreso de vehiculo------------------")
        self.vehiculo.append(input("\nNumero de Placa: "))
        self.marca.append(input("\nMarca: "))
        self.modelo.append(input("\nModelo: "))
        self.tipo_vehiculo.append(input("\nTipo de vehiculo: "))
        self.hora_entrada.append(datetime.now)
        self.estado.append('True')
        self.enter()
    
    def salida_vehiculo(self):
        """Ingresa la salida de un vehiculo y muestra los datos correspondientes del ticket"""


    def buscar(self):
        """Busca un vehiculo por el numero de placa"""


    def reporte_diario(self):
        """Muestra el reporte diario de los vehiculos que ingresaron al estacionamiento"""


    def salir(self):
        """Finaliza el programa"""
        print("Gracias por utilizar nuestro sistema")
        sys.exit


    def Run(self):
        """ """
        while True:
            self.Menu()
            choice = input("\nIngrese una opcion: ")
            action = self.opcion.get(choice)
            if action: 
                action()
            else:
                print("\nOpcion no valida")
                self.enter


if __name__ == "__main__":
    vehiculo = VehiculoCliente()
    vehiculo.Run()