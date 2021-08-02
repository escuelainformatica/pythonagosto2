# repo de repositorio
# las funciones de la base de datos que tienen que ver con libro.
import sqlite3

# si tengo una funcion, y tengo que leer una propiedad = no puede ser estatico.
# en caso contrario, la funcion puede ser estatica (y seria recomendado).
from modelo.Libro import Libro


class LibroRepo:
    # propiedad
    propiedad:int

    @staticmethod
    def conectar():
        con = sqlite3.connect('base.db')
        # crear un cursor (o tambien llamado comando)
        cursor = con.cursor()
        return con,cursor

    @staticmethod
    def desconectar(con,cursor):
        cursor.close()
        con.close()

    @staticmethod  # <-- eso es una anotacion.
    def listar_todo():
        con,cursor=LibroRepo.conectar()
        # ejecuta la siguiente operacion
        cursor.execute("select Id,Nombre,Precio,Categoria from Libros")
        # traer todos los datos
        libros_tuples = cursor.fetchall()
        LibroRepo.desconectar(con,cursor)
        return libros_tuples

    @staticmethod
    def insertar(libro:Libro)->int:
        con,cursor=LibroRepo.conectar()
        cursor.execute("insert into libros(nombre,precio,categoria)"
                       " values(?,?,?)"
                       ,[libro.Nombre,libro.Precio,libro.Categoria])
        con.commit()
        resultado=cursor.lastrowid # obtengo el ultimo id ingresado (si hay un auto numerico)
        LibroRepo.desconectar(con,cursor)
        return resultado


