import sqlite3
from modelo.Libro import Libro
from servicio.LibroRepo import LibroRepo

numero=20
texto="hola"

print("numero="+str(numero)+" texto="+texto)
print("numero=%s texto=%s" % (numero,texto))
print("numero={0} texto={1} {0}".format(numero,texto))
print("numero=$numero texto=$texto")



while True:
    print("libros---------------")
    print("1) insertar")
    print("2) modificar")
    print("3) eliminar")
    print("4) listar")
    opcion=input("seleccione su opcion:")
    if(opcion=="4"):
        libros=LibroRepo.listar_todo()
        for libro in libros:
            print(libro.Id,libro.Nombre,libro.Precio)
    elif(opcion=="1"):
        libro=Libro(0
                    ,input("Ingrese nombre:")
                    ,input("Ingrese precio:")
                    ,input("Ingrese categoria:"))
        id=LibroRepo.insertar(libro)
        print("El id ingresado es",id)
    elif(opcion=="2"):
        # modificar
        id=int(input("Ingrese id:"))
        libro_base=LibroRepo.obtener(id)
        nombre=input("Ingrese nombre: [%s]" % (libro_base.Nombre))
        precio=input("Ingrese precio: [%s]" % (libro_base.Precio))
        categoria=input("Ingrese categoria: [%s]" % (libro_base.Categoria))

        libro=Libro(id,nombre,precio,categoria)

        LibroRepo.modificar(libro)
    elif(opcion=="3"):
        id=int(input("Ingrese id:"))
        LibroRepo.eliminar(id)




# libro=Libro(0,"libro5",123,"categoria")
# print("el valor ingresado es :",LibroRepo.insertar(libro))

# lrepo=LibroRepo() # estoy creando una memoria y dentro de ella la funcion
# libros_tuples=lrepo.listar_todo()
# una funcion estatica se puede llamar sin crear una variable

# libros_objetos=[]
# libros_diccionario=[]

#  ojb=Libro(2,"libro3",5555,"novela")

# for libro in libros_tuples:
    # * es para desempaquetar, tenemos un tuple y lo convertimos en 4 argumentos.
#    obj=Libro(*libro) # libro[0],libro[1],libro[2],libro[3]
#    libros_objetos.append(obj)
    # {} indica un set o diccionario
#    dic={"Id":libro[0],"Nombre":libro[1]
#        ,"Precio":libro[2],"Categoria":libro[3]}
#    libros_diccionario.append(dic)

# tuples
# for libro in libros_tuples:
#    print(libro[1])

# diccionario
# for libro in libros_diccionario:
#    print(libro.get('Nombre')) # None (ningun valor)


# listado de objetos


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





