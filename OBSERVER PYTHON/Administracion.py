from ILibroMalEstado import ILibroMalEstado


class Administracion(ILibroMalEstado):
    def update(self, libro):
        if libro.estado == "MALO":
            print("Queja formal del libro " + libro.titulo + "por mal estado")
        else:
            print("El libro " + libro.titulo + "se encuentra en buen estado")
