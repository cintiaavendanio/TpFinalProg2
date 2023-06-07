import sqlite3


class ProgramaPrincipal:
    def menu(self):
        while True:
            print("Menu de opciones Buscalibre")
            print("1 - Cargar Libros")
            print("2 - Modificar precio de un libro")
            print("3 - Borrar un libro")
            print("4 - Cargar Disponibilidad")
            print("5 - Listado de Libros")
            print("0- Salir del menú")
            nro = int(input("Por favor ingrese la opción mediante su número"))
            if nro == 1:
                ISBN = input("Por favor ingrese el ISBN del libro: ")
                titulo = input("Por favor ingrese el titulo del libro: ")
                autor = input("Por favor ingrese el autor del libro: ")
                genero = input("Por favor ingrese el genero del libro: ")
                precio = input("Por favor ingrese el precio del libro: ")
                fechaUltimoPrecio = input(
                    "Por favor ingrese la fecha de ultimo precio: "
                )
                cantDisponible = input(
                    "Por favor ingrese la cantidad de unidades disponibles: "
                )

                nuevo_libro = Libro(
                    ISBN,
                    titulo,
                    autor,
                    genero,
                    precio,
                    fechaUltimoPrecio,
                    cantDisponible,
                )

                nuevo_libro.cargar_libro()

            elif nro == 2:
                ID_ingresado = input("Por favor ingrese el ID del libro: ")
                precio = input("Por favor ingrese el nuevo precio: ")
                libro_a_modificar = Libro(ID_ingresado, precio)
                libro_a_modificar.modificar_libro(ID_ingresado)
            elif nro == 0:
                # conexion.cerrarConexion()
                break

    def crearTablas(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        conexion.miCursor.execute("DROP TABLE IF EXISTS LIBROS")
        conexion.miCursor.execute(
            "CREATE TABLE LIBROS (ID INTEGER identity(1, 2) PRIMARY KEY , ISBN INTEGER, titulo  VARCHAR(30) ,autor  VARCHAR(30), genero VARCHAR(30), precio FLOAT NOT NULL, cantidadDisponibles INTEGER NOT NULL, fechaUltimoPrecio INTEGER)"
        )
        conexion.miConexion.commit()
        conexion.cerrarConexion()


class Libro:
    def __init__(
        self,
        ISBN,
        titulo,
        autor,
        genero,
        precio,
        fechaUltimoPrecio,
        cantDisponible=None,
    ):
        self.ISBN = ISBN
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.precio = precio
        self.fechaUltimoPrecio = fechaUltimoPrecio
        self.cantDisponible = cantDisponible

    def cargar_libro(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute(
                "INSERT INTO LIBROS(ISBN, titulo, autor, genero, precio, fechaUltimoPrecio, cantDisponible) VALUES('{}','{}', '{}','{}','{}','{}','{}','{}')".format(
                    self.ISBN,
                    self.titulo,
                    self.autor,
                    self.genero,
                    self.precio,
                    self.fechaUltimoPrecio,
                    self.cantDisponible,
                )
            )
            conexion.miConexion.commit()
            print("Libro cargado exitosamente")
        except:
            print("Error al agregar un libro")
        finally:
            conexion.cerrarConexion()

    def modificar_libro(self, ID_ingresado):
        conexion = Conexiones()
        conexion.abrirConexion()

        try:
            conexion.miCursor.execute(
                "UPDATE LIBROS SET precio='{}' where ID='{}'".format(
                    self.precio, ID_ingresado
                )
            )
            conexion.miConexion.commit()
            print("Libro modificado correctamente")
        except:
            print("Error al actualizar el libro")
        finally:
            conexion.cerrarConexion()


class Conexiones:
    def abrirConexion(self):
        self.miConexion = sqlite3.connect("Libreria")
        self.miCursor = self.miConexion.cursor()

    def cerrarConexion(self):
        self.miConexion.close()


programa = ProgramaPrincipal()
programa.crearTablas()
programa.menu()
