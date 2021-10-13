from iAprobador import *

class LiderEjecutivo(IAprobador):

    def __init__(self):
        self._next = None

    def set_next(self, next):
        self._next = next

    def solicitudPrestamo(self, monto):
        if monto > 10000 and monto <= 50000:
            print("Lo manejo yo, el lider")
        else:
            self._next.solicitudPrestamo(monto)