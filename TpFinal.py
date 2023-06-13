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
        
    class Libreria:
    def agregar_libro(
        self, ISBN, titulo, autor, genero, precio, fechaUltimoPrecio, cantDisponibles
    ):
        if (
            not ISBN
            or not titulo
            or not autor
            or not genero
            or not precio
            or not cantDisponibles
        ):
            print("Por favor ingrese todos los campos requeridos.")
            return
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

    def modificar_libro(self, id, nuevo_precio):
        conexion = Conexiones()
        conexion.abrirConexion()
        consulta = "SELECT id_libro FROM LIBROS WHERE id_libro = ?"
        cursor = conexion.miCursor.execute(consulta, (id,))
        if not cursor.fetchone():
            print("El libro con el ID especificado no existe.")
            return

        try:
            conexion.miCursor.execute(
                "UPDATE LIBROS SET precio = ? WHERE id_libro = ?",
                (nuevo_precio, id),
            )
            conexion.miConexion.commit()
            print("Libro modificado correctamente")
        except Exception as err:
            print("Error al modificar un libro")
            print(err)
        finally:
            conexion.cerrarConexion()

    def borrar_libro(self, id):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute(
                "DELETE FROM LIBROS WHERE id_libro = ?",
                (id,),
            )
            conexion.miConexion.commit()
            print("Libro borrado correctamente")
        except Exception as err:
            print("Error al borrar libro")
            print(err)
        finally:
            conexion.cerrarConexion()

    def modificar_disponibilidad(self, id, nueva_disponibilidad):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute(
                "UPDATE LIBROS SET cantDisponibles = ? WHERE id_libro = ?",
                (nueva_disponibilidad, id),
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
            cursor = conexion.miCursor.execute(
                "SELECT id_libro, titulo, autor FROM LIBROS ORDER BY id_libro, autor, titulo"
            )
            for fila in cursor:
                print("id:", fila[0])
                print("Título:", fila[1])
                print("Autor:", fila[2])
                print("---")
        except Exception as err:
            print("Error al mostrar libros")
            print(err)
        finally:
            conexion.cerrarConexion()

    def registrar_venta(self, id_libro, cantVendidas, fecha):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute(
                "INSERT INTO VENTAS (id_libro, cantVendida,fecha) VALUES (?, ?, ?)",
                (id_libro, cantVendidas, fecha),
            )

            cursor = conexion.miCursor.execute(
                "SELECT cantDisponibles FROM LIBROS WHERE id_libro = ?",
                (id_libro),
            )
            for fila in cursor:
                cantDisponibles = fila[0] - int(cantVendidas)

            conexion.miCursor.execute(
                "UPDATE LIBROS SET cantDisponibles = ? WHERE id_libro = ?",
                (cantDisponibles, id_libro),
            )

            print("Venta agregada exitosamente")

            conexion.miConexion.commit()
        except Exception as err:
            print("Error al agregar la venta")
            print(err)
        finally:
            conexion.cerrarConexion()

    def actualizarPrecios(self, fechaActual, porcentajeDeAumento):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute(
                "INSERT INTO HISTORICO_LIBROS (id_libro, ISBN, titulo, autor, genero, precio, fechaUltimoPrecio, cantDisponibles) SELECT id_libro, ISBN, titulo, autor, genero, precio, fechaUltimoPrecio, cantDisponibles FROM LIBROS"
            )
            print("Libros agregados a la tabla historico exitosamente")
            aumento = float((porcentajeDeAumento / 100) + 1)
            conexion.miCursor.execute(
                "UPDATE LIBROS SET precio = precio*?, fechaUltimoPrecio = ?",
                (aumento, fechaActual),
            )

            conexion.miConexion.commit()
        except Exception as err:
            print("Error al agregar a historicos")
            print(err)
        finally:
            conexion.cerrarConexion()

    def mostrarRegistro(self, fecha):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            consulta = "SELECT id_libro, ISBN, titulo, fechaUltimoPrecio FROM LIBROS WHERE fechaUltimoPrecio < ?"
            cursor = conexion.miCursor.execute(consulta, (fecha,))
            for fila in cursor:
                print("id:", fila[0])
                print("ISBN:", fila[1])
                print("titulo:", fila[2])
                print("fechaUltimoPrecio:", fila[3])
                print("---")

            conexion.miConexion.commit()
        except Exception as err:
            print("Error al mostrar registros")
            print(err)
        finally:
            conexion.cerrarConexion()




libreria = Libreria()
programa = ProgramaPrincipal()
programa.menu()