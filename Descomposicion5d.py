# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 17:53:37 2019

@author:
"""

import sys
if len(sys.argv) == 2:
    numero = int(sys.argv[1])
    if numero < 0 or numero > 99999:
        print("Introduzca un número entero")
        print("Debe introducir: Ejercicio3_8.py del 0 al 99999")
    else: # Esto es la parte importante
        cadena = str(numero) # Convertimos el número en cadena para saber su longitud
        longitud = len (cadena)
        
        for i in range(longitud):
            print(" {:05d} ".format( int(cadena[longitud-1-i])*10**i))





else:
    print("Introduzca un número entero")
    print("Debe introducir: Ejercicio3_8.py del 0 al 99999")
