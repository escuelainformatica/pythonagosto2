class Libro():
    """Id,Nombre,Precio,Categoria"""
    Id: int
    Nombre: str
    Precio: int
    Categoria: str

    # * en una funcion es para empaquetar, es decir, tomar todos los argumentos y crear un tuple
    def __init__(self, *tuple) -> None:
        self.Id, self.Nombre, self.Precio, self.Categoria =tuple
