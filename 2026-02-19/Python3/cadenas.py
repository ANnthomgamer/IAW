#!/bin/python3

""" 
    Dada una frase u oración, reemplazar 
    cada vocal por la siguiente como el 
    cifrado Cesar solo en vocales
"""


def cifrado_cesar_vocales(cadena):
    cadena_cifrada = ""
    vocales = ["a", "e", "i", "o", "u"]
    for letra in cadena:
        if letra in vocales:
            posicion = vocales.index(letra)
            nueva_posicion = (posicion + 1) % 5
            cadena_cifrada += vocales[nueva_posicion]
        else:
            cadena_cifrada += letra
        
    return [cadena, cadena_cifrada]

cadena = "Hola mundo"
print(cifrado_cesar_vocales(cadena))
