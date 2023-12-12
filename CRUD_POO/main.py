from conexion import Conectar
from libro import Libros
from lector import Lectores
from prestamo import Prestamos

def menu():
    print("\nBIENVENIDO A LA BIBLIOTECA\n")
    print("1. Añadir un libro")
    print("2. Ver los libros")
    print("3. Buscar un libro")
    print("4. Eliminar un libro")
    print("5. Modificar un libro")
    print("6. Prestar un libro")
    print("7. Devolver un libro")
    print("8. Añadir un lector")
    print("9. Ver los lectores")
    print("10. Buscar un lector")
    print("11. Eliminar un lector")
    print("12. Modificar un lector")
    print("13. Añadir un préstamo")
    print("14. Ver los préstamos")
    print("15. Buscar un préstamo")
    print("16. Eliminar un préstamo")
    print("17. Modificar un préstamo")
    print("18. Salir")
    opcion = int(input("\nSeleccione una opción: "))
    return opcion


conexion = Conectar().conexion_biblioteca()

while True:
    opcion = menu()

    if opcion == 1:
        libro = Libros(conexion)
        libro.anadirlibro()
    elif opcion == 2:
        libro = Libros(conexion)
        print(libro.verlibros())
    elif opcion == 3:
        libro = Libros(conexion)
        print(libro.buscarlibro())
    elif opcion == 4:
        libro = Libros(conexion)
        libro.eliminarlibro()
    elif opcion == 5:
        libro = Libros(conexion)
        libro.modificarlibro()
    elif opcion == 6:
        libro = Libros(conexion)
        libro.prestarlibro()
    elif opcion == 7:
        libro = Libros(conexion)
        libro.devolverlibro()
    elif opcion == 8:
        lector = Lectores(conexion)
        lector.anadirlector()
    elif opcion == 9:
        lector = Lectores(conexion)
        print(lector.verlectores())
    elif opcion == 10:
        lector = Lectores(conexion)
        lector.buscarlector()
    elif opcion == 11:
        lector = Lectores(conexion)
        lector.eliminarlector()
    elif opcion == 12:
        lector = Lectores(conexion)
        lector.modificarlector()
    elif opcion == 13:
        prestamo = Prestamos(conexion)
        prestamo.anadirprestamo()
    elif opcion == 14:
        prestamo = Prestamos(conexion)
        print(prestamo.verprestamos())
    elif opcion == 15:
        prestamo = Prestamos(conexion)
        prestamo.buscarprestamo()
    elif opcion == 16:
        prestamo = Prestamos(conexion)
        prestamo.eliminarprestamo()
    elif opcion == 17:
        prestamo = Prestamos(conexion)
        prestamo.modificarprestamo()
    elif opcion == 18:
        print("\nMuchas gracias por usar la biblioteca.\n")
        break
    else:
        print("Opción Incorrecta.")