import random #El sistema importa el módulo random para poder generar números aleatorios.

def generarnumeros(): #El sistema define la función generar_vector.
    try:
        vector = [] #Inicializa una lista llamada vector vacía.
        while len(vector) < 10: #Mientras la longitud del vector sea menor que 10, realiza lo siguiente:
            numero = random.randint(1, 10) #Genera un número aleatorio entre 1 y 10.
            if numero not in vector: #Si el número no está en el vector, realiza lo siguiente:
                vector.append(numero) #Agrega el número al vector.
    except ValueError: #Si ocurre un error ValueError, realiza lo siguiente:
        print("No se pueden generar los numeros") #Imprime un mensaje de error.
    return vector #Devuelve el vector.

def listadesordenada(vector): #El sistema define la función listadesordenada con el parámetro vector.
    try: #Intenta hacer lo siguiente:
        with open("listadesordenada.txt", "w") as archivo: #Abre un archivo llamado "listadesordenada.txt" en modo de escritura.
                archivo.write(str(vector)) #Escribe el vector en el archivo.
    except FileNotFoundError: #Si no puede crear el archivo, realiza lo siguiente:
        print("No se ha podido crear el archivo") #Imprime un mensaje de error.
    return vector #Devuelve el vector.