# Clases para crear una lista doblemente ligada utilizando python.
# El codigo original en el cual se basa este proyecto se encuentra en: stackabuse.com
# Partes del codigo fueron tomadas del original con algunas modificaciones.
# Autor: Juan Ricardo Chalita Pérez.
# Autor original del codigo: Usman Malik.

# A continuacion crearemos pruebas para validar el funcionamiento de la lista doblemente ligada

from dList import doubleList

#Creamos una nueva lista doblemente ligada
nuevaListaD = doubleList()

#Pruebas de insersion de datos
nuevaListaD.insertar_lista_vacia(50)

#Si navegamos a travez de la lista deberiamos poder observar 50 como el unico elemento en la lista
print("Prueba 0 insertar el primer elemento")
nuevaListaD.navegar_lista() 


#Ahora agregaremos algunos elementos al inicio de la lista 
nuevaListaD.insertar_inicio(10)
nuevaListaD.insertar_inicio(5)
nuevaListaD.insertar_inicio(18)

print("Prueba 1 insertar elementos al inicio")
nuevaListaD.navegar_lista() 


#Agregramos elementos al final de la lista 
nuevaListaD.insertar_final(29)
nuevaListaD.insertar_final(39)
nuevaListaD.insertar_final(49)

print("Prueba 2 insertar elementos al final")
nuevaListaD.navegar_lista() 


#Agregamos un elemento despues del elemento 50 
nuevaListaD.insertar_despues_elemento(50, 65)

print("Prueba 3 insertar el elemento 65 despues del 50")
nuevaListaD.navegar_lista() 


#Agregamos un elemento antes del elemento 50 
nuevaListaD.insertar_antes_elemento(29, 100)

print("Prueba 4 insertar el elemento 100 antes del 29")
nuevaListaD.navegar_lista() 


#Pruebas de eliminacion de elementos 
#Eliminando elmentos al inicio de la lista 
nuevaListaD.eliminar_inicio()

print("Prueba 5 eliminar el primer elemento")
nuevaListaD.navegar_lista() 


#Eliminando elementos al final de la lista 
nuevaListaD.eliminar_final()

print("Prueba 6 eliminar el ultimo elemento")
nuevaListaD.navegar_lista() 


#Eliminando el elemento buscado 
nuevaListaD.eliminar_elemento(65)

print("Prueba 7 eliminar el elemento 65")
nuevaListaD.navegar_lista() 


#Prueba para invertir la lista
nuevaListaD.invertir()

print("Prueba 8 invertir el order de la lista")
nuevaListaD.navegar_lista() 

#Prueba para contar elementos de la lista
print("Prueba 9 contar elementos en la lista")
print(nuevaListaD.contar_elementos())