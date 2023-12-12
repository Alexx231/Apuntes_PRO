class Libros:

    def __init__(self, titulo, autor, editorial, genero, anio_publicacion, paginas, idioma, edicion, prestamos_realizados, ISBN, id_libro):
        self.titulo = titulo
        self.autor = autor
        self.editorial = editorial
        self.genero = genero
        self.ano_publicacion = anio_publicacion
        self.paginas = paginas
        self.idioma = idioma
        self.prestado = False
        self.edicion = edicion
        self.prestamos_realizados = prestamos_realizados
        self.isbn = ISBN
        self.id_libro = id_libro
        
    def cargar_tabla_libros(self, conexion):
        if conexion:
            try:
                cursor = conexion.cursor()
                query = ("SELECT * FROM libros")
                libro = self.titulo, self.autor, self.editorial, self.genero, self.ano_publicacion, self.paginas, self.idioma, self.prestado, self.edicion, self.prestamos_realizados, self.isbn, self.id_libro
                cursor.execute(query, libro)
                conexion.commit()
                cursor.close()
            except ValueError as e:
                print("Error al mostrar los libros.", e)
        return libro
    
    def anadirlibro(self, conexion):
        titulo = input("Dime cual es el titulo del libro:: ")
        autor = input("Quien es su autor: ")
        genero = input("Ingresa el genero del libro: ")
        paginas = int(input("Cuantas paginas tiene el libro: "))
        anio_publicacion = input("Ingresa el año de publicacion del libro: ")
        edicion = input("Cual edicion es: ")
        idioma = input("En que idioma esta escrito: ")
        ISBN = input("Ingrese el ISBN del libro: ")
        prestamos_realizados = int(input("Ingrese el número de préstamos realizados del libro: "))
        prestado = bool(input("El libro está prestado?(s/n): "))
        if conexion:
            try:
                cursor = conexion.cursor()
                query = ("INSERT INTO libros " "(titulo, autor, genero, paginas, anio_publicacion, edicion, idioma, ISBN, prestamos_realizados, prestado)" "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
                libro = titulo, autor, genero, paginas, anio_publicacion, edicion, idioma, ISBN, prestamos_realizados, prestado
                cursor.execute(query, libro)
                conexion.commit()
                cursor.close()
                print("Libro agregado con exito.")
            except ValueError as e:
                print("Error al agregar el libro.",e)
        return libro
    
    def verlibros(self, conexion):
        if conexion:
            try:
                cursor = conexion.cursor()
                query = ("SELECT titulo, autor, genero, paginas, anio_publicacion, edicion, idioma, ISBN, prestamos_realizados, prestado FROM libros")
                cursor.execute(query)
                for (titulo, autor, genero, paginas, anio_publicacion, edicion, idioma, ISBN, prestamos_realizados, prestado) in cursor:
                    print(f"Título: {titulo}, Autor: {autor}, Género: {genero}, Páginas: {paginas}, Año de publicación: {anio_publicacion}, Edición: {edicion}, Idioma: {idioma}, ISBN: {ISBN}, Préstamos realizados: {prestamos_realizados}, Prestado: {prestado}")
                conexion.commit()
                cursor.close()
            except ValueError as e:
                print("Error al mostrar los libros.",e)

    def buscarlibro(self, conexion):
        if conexion:
            try:
                titulo = input("Ingrese el titulo del libro que desea buscar: ")
                cursor = conexion.cursor()
                query = ("SELECT titulo, autor, genero, paginas, anio_publicacion, edicion, idioma, ISBN, prestamos_realizados, prestado FROM libros WHERE titulo = %s")
                cursor.execute(query, (titulo,))
                for (titulo, autor, genero, paginas, anio_publicacion, edicion, idioma, ISBN, prestamos_realizados, prestado) in cursor:
                        print(f"Título: {titulo}, Autor: {autor}, Género: {genero}, Páginas: {paginas}, Año de publicación: {anio_publicacion}, Edición: {edicion}, Idioma: {idioma}, ISBN: {ISBN}, Préstamos realizados: {prestamos_realizados}, Prestado: {prestado}")
                conexion.commit()
                cursor.close()
            except ValueError as e:
                print("Error al buscar el libro.",e)
    
    def eliminarlibro(self, conexion):
        if conexion:
            try:
                id_libro = input("Ingrese el id del libro que desea eliminar: ")
                cursor = conexion.cursor()
                query = ("DELETE FROM libros WHERE id_libro = %s")
                libro = id_libro, 
                cursor.execute(query, libro)
                conexion.commit()
                cursor.close()
                print("Libro ha sido eliminado correctamente.")
            except ValueError as e:
                print("Error al eliminar el libro.",e)
        return libro

    def modificarlibro(self, conexion):
        titulo = input("Dime cual es el título del libro que desea modificar: ")
        autor = input("Cual es el nuevo autor del libro: ")
        genero = input("El nuevo género del libro: ")
        paginas = input("Cuantas paginas tiene el nuevo libro: ")
        anio_publicacion = input("En que año se publico: ")
        edicion = input("Cual es la nueva edición del libro: ")
        idioma = input("En que idioma esta escrito el nuevo libro: ")
        ISBN = input("Ingresa el nuevo ISBN del libro: ")
        prestamos_realizados = input("Cual es el numero de prestamos realizados del nuevo libro: ")
        prestado = bool(input("El libro está prestado?(s/n): "))
        if conexion:
            try:
                cursor = conexion.cursor()
                query = ("UPDATE libros SET titulo = %s, autor = %s, genero = %s, paginas = %s, anio_publicacion = %s, edicion = %s, idioma = %s, ISBN = %s, prestamos_realizados = %s, prestado = %s WHERE titulo = %s")
                libro = titulo, autor, genero, paginas, anio_publicacion, edicion, idioma, ISBN, prestamos_realizados, prestado
                cursor.execute(query, libro)
                conexion.commit()
                cursor.close()
                print("Libro modificado de forma correcta")
            except ValueError as e:
                print("Error al modificar el libro.",e)
        return libro
                
    def prestarlibro(self, conexion):
        if conexion:
            try:
                id_libro = input("Ingrese el id del libro que desea prestar: ")
                cursor = conexion.cursor()
                query = ("UPDATE libros SET prestado = %s WHERE id_libro = %s")
                libro = (True, id_libro)
                cursor.execute(query, libro)
                conexion.commit()
                cursor.close()
                print("El libro fue prestado con exito.")
            except ValueError as e:
                print("Error al prestar el libro.",e)
        return libro
    
    
    def devolverlibro(self, conexion):
        if conexion:
            try:
                id_libro = input("Ingrese el id del libro que desea devolver: ")
                cursor = conexion.cursor()
                query = ("UPDATE libros SET prestado = %s WHERE id_libro = %s")
                libro = (False, id_libro)
                cursor.execute(query, libro)
                conexion.commit()
                cursor.close()
                print("El libro fue devuelto con exito.")
            except ValueError as e:
                print("Error al devolver el libro.",e)
        return libro
        
    
