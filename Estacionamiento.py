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
            
        


        

    