from ILibroMalEstado import ILibroMalEstado

class Compras(ILibroMalEstado):
    def update(self, libro):
        if libro.estado == "MALO":
            print("compras: ")
        print("Se solciita una nueva cotizacion del libro " + libro.titulo)