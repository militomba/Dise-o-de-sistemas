from iAprobador import *

class Director(IAprobador):

    def __init__(self):
        self._next = None

    def set_next(self, next):
        self._next = next

    def solicitudPrestamo(self, monto):
        if monto > 100000:
            print("Lo manejo yo, el director")
        else:
            self._next.solicitudPrestamo(monto)