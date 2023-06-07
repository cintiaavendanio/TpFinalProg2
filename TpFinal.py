import sqlite3


class Libreria:
    def __init__(self):
        self.conexion = Conexiones()
        self.conexion.abrirConexion()
        self.conexion.miCursor.execute("DROP TABLE IF EXISTS LIBROS")
        self.conexion.miCursor.execute(
            "CREATE TABLE LIBROS (id_libro INTEGER PRIMARY KEY,ISBN INTEGER, titulo VARCHAR(30), autor VARCHAR(30), genero VARCHAR(30), precio FLOAT NOT NULL, fechaUltimoPrecio INTEGER, cantDisponibles INTEGER NOT NULL, UNIQUE(titulo, autor))"
        )
        self.conexion.miConexion.commit()

    def agregar_libro(self, titulo, autor, precio, cantidadDisponibles):
        try:
            self.conexion.miCursor.execute(
                "INSERT INTO LIBROS (ISBN, titulo, autor, genero, precio,fechaUltimoPrecio, cantDisponibles) VALUES (?, ?, ?, ?, ?, ?,?)",
                (titulo, autor, precio, cantidadDisponibles),
            )
            self.conexion.miConexion.commit()
            print("Libro agregado exitosamente")
        except:
            print("Error al agregar un libro")

    def modificar_libro(self, titulo, autor, precio):
        try:
            self.conexion.miCursor.execute(
                "UPDATE LIBROS SET precio = ? WHERE titulo = ? AND autor = ?",
                (precio, titulo, autor),
            )
            self.conexion.miConexion.commit()
            print("Libro modificado correctamente")
        except:
            print("Error al modificar un libro")

    def cerrar_libreria(self):
        self.conexion.cerrarConexion()


class Conexiones:
    def abrirConexion(self):
        self.miConexion = sqlite3.connect("Libreria.db")
        self.miCursor = self.miConexion.cursor()

    def cerrarConexion(self):
        self.miConexion.close()


libreria = Libreria()


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
        fechaUltimoPrecio = input("Por favor ingrese la fecha de ultimo precio: ")
        cantDisponible = input(
            "Por favor ingrese la cantidad de unidades disponibles: "
        )

        libreria.agregar_libro(
            ISBN, titulo, autor, genero, precio, fechaUltimoPrecio, cantDisponible
        )

        # elif nro == 2:
        # ID_ingresado = input("Por favor ingrese el ID del libro: ")
        # precio = input("Por favor ingrese el nuevo precio: ")
        # libro_a_modificar = Libro(ID_ingresado, precio)
        # libro_a_modificar.modificar_libro(ID_ingresado)
        # elif nro == 0:
        # conexion.cerrarConexion()
        break
