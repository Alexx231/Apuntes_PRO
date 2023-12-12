class Lectores:

    def __init__(self, nombre, apellidos, fecha_alta, fecha_baja, id_lector):
        self.nombre = nombre
        self.apellidos = apellidos
        self.fecha_alta = fecha_alta
        self.fecha_baja = fecha_baja
        self.id_lector = id_lector
        
        
    def cargar_tabla_lectores(self, conexion): #Esta función es la que se encarga de cargar la tabla de lectores de la base de datos de la biblioteca.
        if conexion:
            try:
                cursor = conexion.cursor()
                query = ("SELECT * FROM lectores")
                lector = self.nombre, self.apellidos, self.fecha_alta, self.fecha_baja, self.id_lector
                cursor.execute(query, lector)
                conexion.commit()
                cursor.close()
            except ValueError as e:
                print("Error al mostrar los lectores.", e)
        return lector

    def anadirlector(self, conexion): #Esta función es la que se encarga de añadir un lector a la base de datos de la biblioteca y se le pide al usuario que ingrese los datos del lector que desea añadir.
        nombre = input("Cual es el nombre del lector: ")
        apellidos = input("Cuales son los apellidos del lector: ")
        fecha_alta = input("Cuando se dio de alta el lector: ")
        fecha_baja = input("Cuando se dio de baja el lector: ")
        if conexion:
            try:
                cursor = conexion.cursor()
                query = ("INSERT INTO lectores (nombre, apellidos, fecha_alta, fecha_baja) VALUES (%s, %s, %s, %s)")
                lector = nombre, apellidos, fecha_alta, fecha_baja
                cursor.execute(query, lector)
                conexion.commit()
                cursor.close()
                print("Lector agregado con éxito.")
            except ValueError as e:
                print("Error al agregar el lector.", e)
        return lector

    def verlectores(self, conexion): #Esta función es la que se encarga de mostrar los lectores que se encuentran en la base de datos de la biblioteca.
        if conexion:
            try:
                cursor = conexion.cursor()
                query = ("SELECT nombre, apellidos, fecha_alta, fecha_baja FROM lectores")
                cursor.execute(query)
                for (nombre, apellidos, fecha_alta, fecha_baja) in cursor:
                    print(f"Nombre: {nombre}, Apellidos: {apellidos}, Fecha de alta: {fecha_alta}, Fecha de baja: {fecha_baja}")
                conexion.commit()
                cursor.close()
            except ValueError as e:
                print("Error al mostrar los lectores.", e)

    def buscarlector(self, conexion): #Esta función es la que se encarga de buscar un lector en la base de datos de la biblioteca.
        if conexion:
            try:
                nombre = input("Ingresa el nombre del lector que desea buscar: ")
                cursor = conexion.cursor()
                query = ("SELECT nombre, apellidos, fecha_alta, fecha_baja FROM lectores WHERE nombre = %s")
                valores = nombre,
                cursor.execute(query, valores)
                for (nombre, apellidos, fecha_alta, fecha_baja) in cursor:
                    print(f"Nombre: {nombre}, Apellidos: {apellidos}, Fecha de alta: {fecha_alta}, Fecha de baja: {fecha_baja}")
                conexion.commit()
                cursor.close()
            except ValueError as e:
                print("Error al buscar el lector.", e)

    def eliminarlector(self, conexion): #Esta función es la que se encarga de eliminar un lector de la base de datos de la biblioteca.
        if conexion:
            try:
                id_lector = input("Ingresa el id del lector que desea eliminar: ")
                cursor = conexion.cursor()
                query = ("DELETE FROM lectores WHERE id_lector = %s")
                lector = id_lector, 
                cursor.execute(query, lector)
                conexion.commit()
                cursor.close()
                print("Lector eliminado correctamente.")
            except ValueError as e:
                print("Error al eliminar el lector.", e)
        return lector

    def modificarlector(self, conexion): #Esta función es la que se encarga de modificar un lector de la base de datos de la biblioteca.
        nombre = input("Cual es el nombre del lector: ")
        apellidos = input("Cuales son los apellidos del  nuevo lector: ")
        fecha_alta = input("Cuando se dio de alta el nuevo lector: ")
        fecha_baja = input("Cuando se dio de baja el nuevo lector: ")
        if conexion:
            try:
                cursor = conexion.cursor()
                query = ("UPDATE lectores SET nombre = %s, apellidos = %s, fecha_alta = %s, fecha_baja = %s WHERE nombre = %s")
                lector = nombre, apellidos, fecha_alta, fecha_baja
                cursor.execute(query, lector)
                conexion.commit()
                cursor.close()
                print("Lector modificado correctamente.")
            except ValueError as e:
                print("Error al modificar el lector.", e)
        return lector