#Abstarct Factory
from abc import ABC, abstractmethod

class Fabrica(ABC):
    @abstractmethod
    def crear_zapatillas(self):
        pass

class Fabrica(ABC):
    @abstractmethod
    def crear_ropa_deportiva(self):
        pass