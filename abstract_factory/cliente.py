from nike_fabrica import *
from adidas_fabrica import *

class Cliente():
    def cliente(self, fabrica):
        zapatillas = fabrica.crear_zapatillas()
        ropa = fabrica.crear_ropa_deportiva()

        print(zapatillas.funcion_zapatillas())
        print(ropa.funcion_ropa_deportiva())
