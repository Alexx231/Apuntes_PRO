import mysql.connector

class Conectar:
    
    def __init__(self, host, user, password, database): #Esta función es la que se encarga de inicializar la conexión a la base de datos de la biblioteca.
        self.host = host 
        self.user = user
        self.password = password
        self.database = database
        self.conexion = None

    def conexion_biblioteca(self): #Esta función es la que se encarga de conectar a la base de datos de la biblioteca.
        try:    
            self.conexion = mysql.connector.connect(
                host= self.host,
                user= self.user,
                password= self.password,
                database= self.database
            )
            print("Conexión exitosa.")
            return self.conexion
        
        except mysql.connector.Error as e:
            print("Error al conectar a la base de datos: ", e)

    def close_connection(self,conexion): #Esta función es la que se encarga de cerrar la conexión a la base de datos de la biblioteca.
        if conexion:
            self.conexion.close()
            print("Conexión cerrada.")
            
conexion = Conectar(host='localhost', user='root', password='', database='biblioteca').conexion_biblioteca()