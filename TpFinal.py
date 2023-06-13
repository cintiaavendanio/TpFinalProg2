import sqlite3
from datetime import datetime


class Conexiones:
    def abrirConexion(self):
        # se conecta con la base de datos:
        self.miConexion = sqlite3.connect("Libreria.db")
        # se crea el cursor:
        self.miCursor = self.miConexion.cursor()

    def cerrarConexion(self):
        self.miConexion.close()

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
            try:
                nro = int(input("Por favor ingrese la opción mediante su número: "))
            except ValueError:
                print("Por favor ingrese un número válido.")
                continue

            if nro == 1:
                try:
                    ISBN = int(input("Por favor ingrese el ISBN del libro: "))
                    titulo = input("Por favor ingrese el titulo del libro: ")
                    autor = input("Por favor ingrese el autor del libro: ")
                    genero = input("Por favor ingrese el genero del libro: ")
                    precio = float(input("Por favor ingrese el precio del libro: "))
                    fechaUltimoPrecio = datetime.now()
                    cantDisponibles = int(input("Por favor ingrese la cantidad de unidades disponibles: "))

                    libreria.agregar_libro(
                        ISBN,
                        titulo,
                        autor,
                        genero,
                        precio,
                        fechaUltimoPrecio,
                        cantDisponibles,
                    )
                
                except Exception as err:
                    print("Error al agregar un libro")
                    print(err)

            elif nro == 2:
                id = input("Por favor ingrese el id del libro: ")
                nuevo_precio = input("Por favor ingrese el nuevo precio: ")
                libreria.modificar_libro(id, nuevo_precio)

            elif nro == 3:
                id = input("Por favor ingrese el id del libro: ")
                libreria.borrar_libro(id)

            elif nro == 4:
                id = input("Por favor ingrese el id del libro: ")
                nueva_disponibilidad = input(
                    "Por favor ingrese la nueva disponibilidad: "
                )
                libreria.modificar_disponibilidad(id, nueva_disponibilidad)

            elif nro == 5:
                libreria.mostrar_libros()

            elif nro == 6:
                id_libro = input("ingrese id del libro vendido")
                cantVendidas = input("ingrese cantidades vendidas")
                fecha = datetime.now()

                libreria.registrar_venta(id_libro, cantVendidas, fecha)

            elif nro == 7:
                porcentajeDeAumento = int(
                    input("ingrese porcentaje de aumento (sin %)")
                )
                fechaActual = datetime.now()
                print("fecha actual:")
                print(fechaActual)
                libreria.actualizarPrecios(fechaActual, porcentajeDeAumento)
                
            elif nro == 8:
                fecha = input("ingrese fecha (AÑO-MES-DIA)")
                libreria.mostrarRegistro(fecha)

            elif nro == 99:
                self.crearTablas()

            elif nro == 0:
                break
            else:
                print("Opción inválida. Por favor ingrese un número válido.")

    def crearTablas(self):
        print("entro al crear tabla")
        conexion = Conexiones()
        conexion.abrirConexion()
        conexion.miCursor.execute("DROP TABLE IF EXISTS LIBROS")
        conexion.miCursor.execute(
            "CREATE TABLE LIBROS (id_libro INTEGER PRIMARY KEY, ISBN INTEGER, titulo VARCHAR(30), autor VARCHAR(30), genero VARCHAR(30), precio FLOAT NOT NULL, fechaUltimoPrecio DATETIME, cantDisponibles INTEGER NOT NULL, UNIQUE(ISBN), UNIQUE(titulo, autor))"
        )
        conexion.miCursor.execute("DROP TABLE IF EXISTS VENTAS")
        conexion.miCursor.execute(
            "CREATE TABLE VENTAS (id_venta INTEGER PRIMARY KEY,id_libro INTEGER, cantVendida INTEGER, fecha INTEGER)"
        )
        conexion.miCursor.execute("DROP TABLE IF EXISTS HISTORICO_LIBROS")
        conexion.miCursor.execute(
            "CREATE TABLE HISTORICO_LIBROS (id_historico INTEGER PRIMARY KEY, id_libro, ISBN INTEGER, titulo VARCHAR(30), autor VARCHAR(30), genero VARCHAR(30), precio FLOAT NOT NULL, fechaUltimoPrecio DATETIME, cantDisponibles INTEGER NOT NULL)"
        )
        conexion.miConexion.commit()
        conexion.cerrarConexion()
        print("Tablas creadas")