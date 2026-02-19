#!/bin/ipython3

""" 
   Crear una lista de listas
   (lista  con 5 listas), cada
   una de esas sublistas, se 
   crean igual que el ej anterior
"""

class GestionarLista:


    def __init__(self):
        self.super_lista = []


    def order_li(self):
        val = int(input("Introduce el primer valor para la lista\n"))
        li_val = [val]
        while len(li_val) < 5:
            val = int(input("Introduce otro valor a la lista\n"))
            if val < li_val[-1]:
                print("\t\tERROR\nEse valor no puede ser introducido a la lista debido a que cada valor debe ser mayor que el anterior\n")
            else:
                li_val.append(val)
        return li_val


    def super_list(li):
        order_list = []
        principal_list = []
        for i in range(5):
            order_list = li()
            principal_list.append(order_list)
            print("\n")

        return principal_list

    super_list = super_list(order_li)

    def visualizar(super_list):
        for i in super_list:
            print(i)



