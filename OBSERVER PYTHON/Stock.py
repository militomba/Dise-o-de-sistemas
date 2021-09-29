from ILibroMalEstado import ILibroMalEstado
class Stock(ILibroMalEstado):
    def update(self, libro):
        if libro.estado == "MALO":
            print("Le doy de baja al libro: " + libro.titulo)
        print("el libro ", + libro.titulo, "sigue en stock")