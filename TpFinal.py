import sqlite3


class Conexiones:
    def abrirConexion(self):
        # se conecta con la base de datos:
        self.miConexion = sqlite3.connect("Libreria.db")
        # se crea el cursor:
        self.miCursor = self.miConexion.cursor()

    def cerrarConexion(self):
        self.miConexion.close()


class Libreria:
    def agregar_libro(
        self, ISBN, titulo, autor, genero, precio, fechaUltimoPrecio, cantDisponibles
    ):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute(
                "INSERT INTO LIBROS (ISBN, titulo, autor, genero, precio,fechaUltimoPrecio, cantDisponibles) VALUES (?, ?, ?, ?, ?, ?,?)",
                (
                    ISBN,
                    titulo,
                    autor,
                    genero,
                    precio,
                    fechaUltimoPrecio,
                    cantDisponibles,
                ),
            )
            conexion.miConexion.commit()
            print("Libro agregado exitosamente")
        except Exception as err:
            print("Error al agregar un libro")
            print(err)
        finally:
            conexion.cerrarConexion()

    def modificar_libro(self, ISBN_ingresado, nuevo_precio):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute(
                "UPDATE LIBROS SET precio = ? WHERE ISBN = ?",
                (nuevo_precio, ISBN_ingresado),
            )
            conexion.miConexion.commit()
            print("Libro modificado correctamente")
        except Exception as err:
            print("Error al modificar un libro")
            print(err)
        finally:
            conexion.cerrarConexion()

    def borrar_libro(self, ISBN_ingresado):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute(
                "DELETE FROM LIBROS WHERE ISBN = ?",
                (ISBN_ingresado,),
            )
            conexion.miConexion.commit()
            print("Libro borrado correctamente")
        except Exception as err:
            print("Error al borrar libro")
            print(err)
        finally:
            conexion.cerrarConexion()

    def modificar_disponibilidad(self, ISBN_ingresado, nueva_disponibilidad):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute(
                "UPDATE LIBROS SET cantDisponibles = ? WHERE ISBN = ?",
                (nueva_disponibilidad, ISBN_ingresado),
            )
            conexion.miConexion.commit()
            print("Cantidad modificada correctamente")
        except Exception as err:
            print("Error al modificar la cantidad de libros disponibles")
            print(err)
        finally:
            conexion.cerrarConexion()

    def mostrar_libros(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            cursor = conexion.miCursor.execute("SELECT ISBN, titulo, autor FROM LIBROS")
            for fila in cursor:
                print("ISBN:", fila[0])
                print("Título:", fila[1])
                print("Autor:", fila[2])
                print("---")
        except Exception as err:
            print("Error al mostrar libros")
            print(err)
        finally:
            conexion.cerrarConexion()


class ProgramaPrincipal:
    def menu(self):
        while True:
            print("Menu de opciones Buscalibre")
            print("1 - Cargar Libros")
            print("2 - Modificar precio de un libro")
            print("3 - Borrar un libro")
            print("4 - Cargar Disponibilidad")
            print("5 - Listado de Libros")
            print("6 - Vender un libro")
            print("7 - Actualizar precio")
            print("8 - Mostrar registro")
            print("99 - Crear tablas")
            print("0- Salir del menú")
            nro = int(input("Por favor ingrese la opción mediante su número "))

            if nro == 1:
                ISBN = input("Por favor ingrese el ISBN del libro: ")
                titulo = input("Por favor ingrese el titulo del libro: ")
                autor = input("Por favor ingrese el autor del libro: ")
                genero = input("Por favor ingrese el genero del libro: ")
                precio = input("Por favor ingrese el precio del libro: ")
                fechaUltimoPrecio = input(
                    "Por favor ingrese la fecha de ultimo precio: "
                )
                cantDisponibles = input(
                    "Por favor ingrese la cantidad de unidades disponibles: "
                )

                libreria.agregar_libro(
                    ISBN,
                    titulo,
                    autor,
                    genero,
                    precio,
                    fechaUltimoPrecio,
                    cantDisponibles,
                )

            elif nro == 2:
                ISBN_ingresado = input("Por favor ingrese el ISBN del libro: ")
                nuevo_precio = input("Por favor ingrese el nuevo precio: ")
                libreria.modificar_libro(ISBN_ingresado, nuevo_precio)

            elif nro == 3:
                ISBN_ingresado = input("Por favor ingrese el ISBN del libro: ")
                libreria.borrar_libro(ISBN_ingresado)

            elif nro == 4:
                ISBN_ingresado = input("Por favor ingrese el ISBN del libro: ")
                nueva_disponibilidad = input(
                    "Por favor ingrese la nueva disponibilidad: "
                )
                libreria.modificar_disponibilidad(ISBN_ingresado, nueva_disponibilidad)

            elif nro == 5:
                libreria.mostrar_libros()

            elif nro == 99:
                self.crearTablas()

            elif nro == 6:
                ISBN = input("ingrese ISBN del libro vendido")
                cantVendidas = input("ingrese cantidades vendidas")
                fecha = input("ingrese fecha de venta")

            elif nro == 0:
                break

    def crearTablas(self):
        print("entro al crear tabla")
        conexion = Conexiones()
        conexion.abrirConexion()
        conexion.miCursor.execute("DROP TABLE IF EXISTS LIBROS")
        conexion.miCursor.execute(
            "CREATE TABLE LIBROS (id_libro INTEGER PRIMARY KEY,ISBN INTEGER, titulo VARCHAR(30), autor VARCHAR(30), genero VARCHAR(30), precio FLOAT NOT NULL, fechaUltimoPrecio INTEGER, cantDisponibles INTEGER NOT NULL, UNIQUE(ISBN), UNIQUE(titulo, autor))"
        )

        conexion.miConexion.commit()
        conexion.cerrarConexion()
        print("Tablas creadas")


libreria = Libreria()
programa = ProgramaPrincipal()
programa.menu()
