from Administracion import Administracion
from Compras import Compras
from Stock import Stock
from AlarmaLibro import Alarmalibro

class Biblioteca:
    @staticmethod
    def devuelve_libro(libro):
        print("Devolucion del libro: " + libro.titulo)
        attach_array = [Administracion(), Compras(), Stock()]
        Alarmalibro.multi_attach(attach_array)
        Alarmalibro.notifyObservers(libro)
