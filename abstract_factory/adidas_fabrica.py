from fabrica import Fabrica
from adidas_ropa_deportiva import *
from adidas_zapatillas import *

class AdidasFabica(Fabrica):
    def crear_ropa_deportiva(self):
        return RopaDeportiva()
    
    def crear_zapatillas(Self):
        return Zapatillas()