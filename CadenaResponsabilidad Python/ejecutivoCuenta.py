from iAprobador import *

class EjecutivoCuenta(IAprobador):

    def __init__(self):
        self._next = None

    def set_next(self, next):
        self._next = next

    def solicitudPrestamo(self, monto):
        if monto <= 10000:
            print("Lo manejo yo, el ejecutivo de cuenta")
        else:
            self._next.solicitudPrestamo(monto)

