#!/bin/python3


""" 

   Introducir valores numericos en una lista, 
   maximo 5 valores, de forma ascendente, si 
   el valor es menor que el anterior, no se guarda

"""
 
def order_li():
    val = int(input("Introduce el primer valor para la lista\n"))
    li_val = [val]
    while len(li_val) < 5:
        val = int(input("Introduce otro valor a la lista\n"))
        if val < li_val[-1]:
            print("\t\tERROR\nEse valor no puede ser introducido a la lista debido a que cada valor debe ser mayor que el anterior\n")
        else:
            li_val.append(val)
    return li_val


print(order_li())
