# repo de repositorio
# las funciones de la base de datos que tienen que ver con libro.
import sqlite3

# si tengo una funcion, y tengo que leer una propiedad = no puede ser estatico.
# en caso contrario, la funcion puede ser estatica (y seria recomendado).
from modelo.Libro import Libro


class LibroRepo:
    @staticmethod
    def conectar():
        con = sqlite3.connect('base.db')
        # crear un cursor (o tambien llamado comando)
        cursor = con.cursor()
        return con, cursor

    @staticmethod
    def desconectar(con, cursor):
        cursor.close()
        con.close()

    @staticmethod
    def listar_todo():
        con, cursor = LibroRepo.conectar()
        # ejecuta la siguiente operacion
        cursor.execute("select Id,Nombre,Precio,Categoria from Libros")
        # traer todos los datos
        libros_tuples = cursor.fetchall()
        LibroRepo.desconectar(con, cursor)
        libro_arreglo = []
        # libros_tuples es un listado de tuples.
        for tuple in libros_tuples:
            libro = Libro(*tuple)  # transformar tuple en un objeto libro.
            libro_arreglo.append(libro)  # el objeto libro, lo voy a agregar al listaod
        return libro_arreglo

    @staticmethod
    def obtener(id: int) -> Libro:
        con, cursor = LibroRepo.conectar()
        # ejecuta la siguiente operacion
        cursor.execute("select Id,Nombre,Precio,Categoria from Libros where id=?", [id])
        # traer todos los datos
        libro_tuples = cursor.fetchone()
        LibroRepo.desconectar(con, cursor)
        libro = Libro(*libro_tuples)
        return libro

    @staticmethod
    def insertar(libro: Libro) -> int:
        con, cursor = LibroRepo.conectar()
        cursor.execute("insert into libros(nombre,precio,categoria)"
                       " values(?,?,?)"
                       , [libro.Nombre, libro.Precio, libro.Categoria])
        con.commit()
        resultado = cursor.lastrowid  # obtengo el ultimo id ingresado (si hay un auto numerico)
        LibroRepo.desconectar(con, cursor)
        return resultado

    @staticmethod
    def modificar(libro: Libro):
        con, cursor = LibroRepo.conectar()
        cursor.execute("update libros set nombre=?,precio=?,categoria=? where id=?"
                       , [libro.Nombre, libro.Precio, libro.Categoria, libro.Id])
        con.commit()
        LibroRepo.desconectar(con, cursor)

    @staticmethod
    def eliminar(id: int):
        con, cursor = LibroRepo.conectar()
        cursor.execute("delete from libros where id=?"
                       , [id])
        con.commit()
        LibroRepo.desconectar(con, cursor)
