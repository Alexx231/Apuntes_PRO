class Prestamos:
        
    def __init__(self, fecha_prestamo, libro, lector, fecha_devolucion, id_prestamo):
        self.fecha_prestamo = fecha_prestamo
        self.libro = libro
        self.lector = lector
        self.fecha_devolucion = fecha_devolucion
        self.id_prestamo = id_prestamo
        
    def anadirprestamo(self, conexion): #Esta función es la que se encarga de añadir un préstamo a la base de datos de la biblioteca y se le pide al usuario que ingrese los datos del préstamo que desea añadir.
        fecha_prestamo = input("Ingresa cuando se realizo el prestamo: ")
        libro = input("Cual es el nombre del libro: ")
        lector = input("Cual es el nombre del lector: ")
        fecha_devolucion = input("Ingresa cuando se realizo la devolución: ")
        if conexion:
            try:
                cursor = conexion.cursor()
                query = ("INSERT INTO prestamos (fecha_prestamo, libro, lector, fecha_devolucion) VALUES (%s, %s, %s, %s)")
                prestamo = fecha_prestamo, libro, lector, fecha_devolucion
                cursor.execute(query, prestamo)
                conexion.commit()
                cursor.close()
                print("Préstamo agregado con éxito.")
            except ValueError as e:
                print("Error al agregar el préstamo.", e)
        return prestamo

    def verprestamos(self, conexion): #Esta función es la que se encarga de mostrar los préstamos que se encuentran en la base de datos de la biblioteca.
        if conexion:
            try: 
                cursor = conexion.cursor()
                query = ("SELECT fecha_prestamo, libro, lector, fecha_devolucion FROM prestamos")
                cursor.execute(query)
                for (fecha_prestamo, libro, lector, fecha_devolucion) in cursor:
                    print(f"Fecha Préstamo: {fecha_prestamo}, Libro: {libro}, Lector: {lector}, Fecha Devolución: {fecha_devolucion}")
                conexion.commit()
                cursor.close()
            except ValueError as e:
                print("Error al mostrar los préstamos.", e)
                
    def buscarprestamo(self, conexion): #Esta función es la que se encarga de buscar un préstamo en la base de datos de la biblioteca.
        if conexion:
            try:
                libro = input("Ingresa el libro prestado que desea buscar: ")
                cursor = conexion.cursor()
                query = ("SELECT id_prestamo, fecha_prestamo, libro, lector, fecha_devolucion FROM prestamos WHERE id_prestamo = %s")
                valores = (libro, )
                cursor.execute(query, valores)
                for (fecha_prestamo, libro, lector, fecha_devolucion) in cursor:
                    print(f"Fecha Préstamo: {fecha_prestamo}, Libro: {libro}, Lector: {lector}, Fecha Devolución: {fecha_devolucion}")
                conexion.commit()
                cursor.close()
            except ValueError as e:
                print("Error al buscar el préstamo.", e)

    def eliminarprestamo(self, conexion): #Esta función es la que se encarga de eliminar un préstamo de la base de datos de la biblioteca.
        if conexion:
            try:
                id_prestamo = input("Ingresa el id del préstamo que desea eliminar: ")
                cursor = conexion.cursor()
                query = ("DELETE FROM prestamos WHERE id_prestamo = %s")
                prestamo = (id_prestamo, )
                cursor.execute(query, prestamo)
                conexion.commit()
                cursor.close()
                print("Préstamo eliminado correctamente.")
            except ValueError as e:
                print("Error al eliminar el préstamo.", e)
        return prestamo

    def modificarprestamo(self, conexion): #Esta función es la que se encarga de modificar un préstamo de la base de datos de la biblioteca.
        fecha_prestamo = input("Ingresa cuando se realizo el nuevo prestamo: ")
        libro = input("Cual es el nombre del nuevo libro: ")
        lector = input("Cual es el nombre del nuevo lector: ")
        fecha_devolucion = input("Ingresa cuando se realizo la devolución: ")
        if conexion:
            try:
                cursor = conexion.cursor()
                query = ("UPDATE prestamos SET fecha_prestamo = %s, libro = %s, lector = %s, fecha_devolucion = %s WHERE fecha_prestamo = %s")
                prestamo = fecha_prestamo, libro, lector, fecha_devolucion
                cursor.execute(query, prestamo)
                conexion.commit()
                cursor.close()
                print("Préstamo modificado correctamente.")
            except ValueError as e:
                print("Error al modificar el préstamo.", e)
        return prestamo