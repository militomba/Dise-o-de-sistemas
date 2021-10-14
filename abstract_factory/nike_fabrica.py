from fabrica import Fabrica
from nike_ropa_deportiva import *
from nike_zapatillas import *

class NikeFabica(Fabrica):
    def crear_ropa_deportiva(self):
        return RopaDeportiva()
    
    def crear_zapatillas(Self):
        return Zapatillas()
        