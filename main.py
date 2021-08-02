import sqlite3
from modelo.Libro import Libro
# libreria SqlAlchemy, Django

# crear una conexion
from servicio.LibroRepo import LibroRepo

libro=Libro(0,"libro5",123,"categoria")
print("el valor ingresado es :",LibroRepo.insertar(libro))

# lrepo=LibroRepo() # estoy creando una memoria y dentro de ella la funcion
# libros_tuples=lrepo.listar_todo()
libros_tuples=LibroRepo.listar_todo() # una funcion estatica se puede llamar sin crear una variable

libros_objetos=[]
libros_diccionario=[]

#  ojb=Libro(2,"libro3",5555,"novela")

for libro in libros_tuples:
    # * es para desempaquetar, tenemos un tuple y lo convertimos en 4 argumentos.
    obj=Libro(*libro) # libro[0],libro[1],libro[2],libro[3]
    libros_objetos.append(obj)
    # {} indica un set o diccionario
    dic={"Id":libro[0],"Nombre":libro[1]
        ,"Precio":libro[2],"Categoria":libro[3]}
    libros_diccionario.append(dic)

# tuples
for libro in libros_tuples:
    print(libro[1])

# diccionario
for libro in libros_diccionario:
    print(libro.get('Nombre')) # None (ningun valor)


# listado de objetos
for libro in libros_objetos:
    print(libro.Nombre)

# clases, herencia, base de datos.

# para que nos sirven las herencias?
# principalmente para objetos visuales.

# cual es el problema de la herencia?
# crea dependencia.

# peluqueria canina



class Animal():
    Nombre:str
    Dueno:str
    Peso:str

    def mostrar(self):
        print(self.Nombre," ",self.Dueno)

# Gato hereda de la clase Animal
# Gato depende de la clase Animal
class Gato(Animal):
    Especie:str
    def mostrar(self):
        print("el nombre del gato ",self.Nombre," ",self.Dueno)


# Perro hereda de Animal
class Perro(Animal):
    Muerde:bool





snoopy=Perro()
snoopy.Nombre="Snoopy"
snoopy.Peso=3
snoopy.Dueno="Charlie"
snoopy.Muerde=False
snoopy.mostrar()

garfield=Gato()
garfield.Nombre="Garfield"
garfield.Dueno="Jhon B."
garfield.Peso=5
garfield.mostrar()

# python se puede crear una funcion y con un argumento con diferentes tipos de datos.
# Interface

def calcular_tarifa(animal)->int:
    if(type(animal) is int):
        return "el valor es un entero"
    else:
        return animal.Peso*2000


print("la tarifa es: ", calcular_tarifa(snoopy))
print("la tarifa es: ", calcular_tarifa(garfield))
print("la tarifa es: ", calcular_tarifa(200))

# python no tiene interface.
# programacion moderna, se usa las interfaces por sobre las herencias.

def sumar(arg1,arg2):
    if(type(arg1) is int and type(arg2) is int):
        print(arg1+arg2)
    else:
        print("no se puede sumar ya que no son enteros")

sumar(20,40)
sumar("hola","mundo")





