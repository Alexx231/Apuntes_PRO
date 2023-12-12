#El sistema importa todas las funciones y variables de los módulos ordenacionnumeros, bubble y shell.
from ordenacionnumeros import * 
from bubble import *
from shell import *

def menu(): #El sistema define la función menu con todos los mensajes de las opciones.
    print("BIENVENIDO AL PROGRAMA DE ORDENACIÓN DE NÚMEROS\n")
    print("1. Generar vector")
    print("2. Ordenación por el método Bubble Sort")
    print("3. Ordenación por el método Shell Sort")
    print("4. Salir")
    opcion = int(input("Introduce una opción: "))
    return opcion


while True: #El sistema entra en un bucle infinito.
    opcion = menu() #Llama a la función menu y guarda la opción seleccionada.
    
    if opcion == 1: #Si la opción es 1, realiza lo siguiente:
        vector = generarnumeros() #Genera un vector de números.
        listadesordenada(vector) #Guarda el vector desordenado en un archivo.
        print(f"\nVector generado: {vector}\n") #Imprime el vector generado.
    elif opcion == 2: #Si la opción es 2, realiza lo siguiente:
        vector = bubble_sort(vector) #Ordena el vector utilizando el método Bubble Sort.
        listaordenada_bubble(vector) #Guarda el vector ordenado en un archivo.
        print(f"\nVector después de la ordenación Bubble Sort: {vector}\n") #Imprime el vector después de la ordenación.
    elif opcion == 3: #Si la opción es 3, realiza lo siguiente:
        vector = shell_sort(vector) #Ordena el vector utilizando el método Shell Sort.
        listaordenada_shell(vector) #Guarda el vector ordenado en un archivo.
        print(f"\nVector después de la ordenación Shell Sort: {vector}\n") #Imprime el vector después de la ordenación.
    elif opcion == 4: #Si la opción es 4, realiza lo siguiente:
        print("\nGracias por usar el programa\n") #Imprime un mensaje de agradecimiento.
        break #Termina el bucle.
    else: #Si la opción no es ninguna de las anteriores, realiza lo siguiente:
        print("Opción incorrecta") #Imprime un mensaje de error.S