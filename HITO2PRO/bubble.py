from ordenacionnumeros import * #El sistema importa todas las funciones y variables del módulo ordenacionnumeros.

def bubble_sort(vector): #El sistema define la función bubble_sort con el parámetro vector.
    try:
        n = len(vector) #Obtiene la longitud del vector.
        paso = 1 #Inicializa la variable paso con el valor 1.
        for i in range(n): #Para cada elemento en el vector:
            for j in range(0, n - i - 1): #Para cada elemento restante en el vector, excluyendo el último elemento ya ordenado:
                if vector[j] > vector[j + 1]: #Si el elemento actual es mayor que el siguiente, realiza lo siguiente:
                    vector[j], vector[j + 1] = vector[j + 1], vector[j] #Intercambia los elementos.
                    print(f"Paso {paso} de la ordenación por Bubble: {vector}") #Imprime el paso actual de la ordenación y el estado actual del vector.
                    paso += 1 #Incrementa la variable paso en 1.
    except ValueError: #Si ocurre un error ValueError, realiza lo siguiente:
        print("El vector no puede ser ordenado por el metodo de Bubble Sort") #Imprime un mensaje de error.
    return vector #Devuelve el vector ordenado.

def listaordenada_bubble(vector): #El sistema define la función listaordenada_bubble con el parámetro vector.
    try: #Intenta hacer lo siguiente:
        with open("listaordenada_bubble.txt", "w") as archivo: #Abre un archivo llamado "listaordenada_bubble.txt" en modo de escritura.
                archivo.write(str(vector)) #Escribe el vector en el archivo.
    except FileNotFoundError: #Si no puede crear el archivo, realiza lo siguiente:
        print("No se ha podido crear el archivo") #Imprime un mensaje de error.
    return vector #Devuelve el vector.